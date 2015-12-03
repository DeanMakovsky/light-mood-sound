import pyaudio
import wave
import threading
import signal
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
INTERVAL = 5
WINDOW = 30

updating = False

def export(audio, frameSet, filename = 'file.wav'):
	# start writing
	f = wave.open(filename, 'wb')
	f.setnchannels(CHANNELS)
	f.setsampwidth(audio.get_sample_size(FORMAT))
	f.setframerate(RATE)
	# write data to wave file
	for frames in frameSet:
		f.writeframes(b''.join(frames))
	# finish writing
	f.close()

def deleteOldFrames(frameSet):
	if len(frameSet) > WINDOW/INTERVAL:
		del frameSet[:len(frameSet)-WINDOW/INTERVAL]

def update(audio, frameSet):	
	export(audio,frameSet)
	# do GraceNote and Lightbulb stuff

	global updating
	updating = False

def doInExternalThread(f, a):
	t = threading.Thread(target = f, args = a)
	t.daemon = True
	t.start()

def main():
	aok = True
	def sigintHandler(signal, frame):
		aok = False
	signal.signal(signal.SIGINT, sigintHandler)

	audio = pyaudio.PyAudio()
	frameSet = []

	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	
	while aok:
		frames = []
		for i in range(0, int(RATE / CHUNK * INTERVAL)):
			data = stream.read(CHUNK)
			frames.append(data)
		frameSet.append(frames)
		deleteOldFrames(frameSet)
		if not updating:
			global updating
			updating = True
			doInExternalThread(update,(audio,frameSet[:]))
	
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	# exit
	sys.exit(0)

if __name__ == "__main__":
	main()
