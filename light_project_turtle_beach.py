import pyaudio
import wave
import threading
import signal
import sys
import os
import collections

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
CHUNK = 2048
INTERVAL = 1
WINDOW = 30
CONSECUTIVE_ERROR_LIMIT = 150

FILENAME = "output.wav"

aok = True
audio = pyaudio.PyAudio()
NUM_FRAMES = RATE / CHUNK * WINDOW
frames = collections.deque(NUM_FRAMES*[''],NUM_FRAMES)

def export(dataList):
	# start writing
	f = wave.open(FILENAME, 'wb')
	f.setnchannels(CHANNELS)
	f.setsampwidth(audio.get_sample_size(FORMAT))
	f.setframerate(RATE)
	# write data to wave file
	f.writeframes(b''.join(dataList))
	# finish writing
	f.close()

def playAudio(fn):
	#open a wav format music  
	f = wave.open(fn,"rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(CHUNK)  
	
	#paly stream  
	while data != '':  
	    stream.write(data)  
	    data = f.readframes(CHUNK)
	
	#stop stream  
	stream.stop_stream()  
	stream.close()  
	
	#close PyAudio  
	p.terminate()  

def update():
	while aok:
		dataList = list(frames)
		export(dataList)
		# do GraceNote and Lightbulb stuff

		# play audio for testing
		playAudio(FILENAME)

def doInExternalThread(func):
	t = threading.Thread(target = func)
	t.daemon = True
	t.start()

def main():
	def sigintHandler(signal, frame):
		global aok
		aok = False
	signal.signal(signal.SIGINT, sigintHandler)

	# print out input devices and corresponding indeces
	for i in range(audio.get_device_count()):
		dev = audio.get_device_info_by_index(i)
		print((i,dev['name'],dev['maxInputChannels']))
	
	# start Recording
	stream = audio.open(format=FORMAT, input=True,
			channels=CHANNELS, rate=RATE,
	        frames_per_buffer=CHUNK)

	doInExternalThread(update)

	consecutiveErrors = 0
	while aok:
		try:
			for i in range(0, int(RATE / CHUNK * INTERVAL)):
				data = stream.read(CHUNK)
				frames.append(data)
			consecutiveErrors = 0
		except IOError:
			consecutiveErrors += 1
			if consecutiveErrors > CONSECUTIVE_ERROR_LIMIT:
				print 'Too many consecutive errors. Exiting program.'
				break
			print 'Encountered error while recording. Moving on and trying again.'
			continue
	
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	# remove file we were working with
	os.remove(FILENAME)

	# exit
	sys.exit(0)

if __name__ == "__main__":
	main()
