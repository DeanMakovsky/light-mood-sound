import requests
import time
import json

class MoodEvent(object):
	submit_url = 'http://devapi.gracenote.com/timeline/api/1.0/audio/extract/'
	get_url = 'http://devapi.gracenote.com/timeline/api/1.0/audio/features/'

	def __init__(self, filename):
		self.filename = filename
		self.results = None
		self.latest_mood = None
		self.bpm = None

	def submit(self):
		req = requests.post(MoodEvent.submit_url, files={
			"audio_file": open(self.filename, 'rb')
			}
		)
		raw_data = req.content.decode('UTF-8')
		# print raw_data
		data = json.loads(raw_data)
		self.audio_id = data['audio_id']

	def _get_gracenote(self):
		# audio_id = '8319d59ad511a4ef1b4485a51b17d6b9'
		# audio_id = '07824e902981936fbcb9a12cbc41bb48'
		req = requests.get(MoodEvent.get_url + self.audio_id)

		# print req.status_code
		if req.status_code != 200:
			return False

		data = req.json()
		# print data
		if data['job_status'] == '1':
			# features = data['features']
			# print features['meta']['bpm']
			self.results = data
			return True
		elif data['job_status'] == '2':
			raise ValueError("External Gracenote API error.")
		return False

	def retrieve_results(self):
		# time and get response
		t_submit = time.time()
		while not self._get_gracenote():
			# print "another one"
			time.sleep(1)
		t_done = time.time()
		self.features = eval(self.results['features'])  # because they messed up their json
		if len(self.features['timeline']['mood']) == 0:
			raise ValueError("No mood data in response.")
		# print self.results
		# print "Took " + str(t_done - t_submit) + " seconds"

	def get_mood(self):
		if self.latest_mood is not None:
			return self.latest_mood
		# extract information
		moods = self.features['timeline']['mood']
		self.bpm = self.features['meta']['bpm']  # float
		# [ { 'values' : list, 'start', 'end' } , {}, ... ]

		# find the latest mood that is longer than 1.5 seconds
		for a_mood in moods:
			if (a_mood['end'] - a_mood['start']) >= 1.5:
				if self.latest_mood is None:
					self.latest_mood = a_mood
				elif a_mood['end'] > self.latest_mood['end']:
					self.latest_mood = a_mood
		
		return self.latest_mood

	def get_mood_label(self):
		return self.get_mood()['values'][0]['label']

	def get_bpm(self):
		if self.bpm is None:
			self.get_mood()
		return self.bpm

if __name__ == "__main__":
	me = MoodEvent('sound-short.wav')
	me.submit()
	try :
		me.retrieve_results()
	except ValueError as e:
		print e, 'with', me.filename
		import sys
		sys.exit(1)
	print me.get_bpm(), me.get_mood_label()
