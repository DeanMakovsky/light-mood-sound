import pyaudio
import wave
import threading
import signal
import sys
import os

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2048
INTERVAL = 1
WINDOW = 30

FILENAME = "output.wav"

updating = False
aok = True

def export(audio, frameSet):
	# start writing
	f = wave.open(FILENAME, 'wb')
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

def update(audio, frameSet):	
	export(audio,frameSet)
	# do GraceNote and Lightbulb stuff

	# play audio for testing
	playAudio(FILENAME)
	
	global updating
	updating = False

def doInExternalThread(f, a):
	t = threading.Thread(target = f, args = a)
	t.daemon = True
	t.start()

def main():
	def sigintHandler(signal, frame):
		global aok
		aok = False
	signal.signal(signal.SIGINT, sigintHandler)

	audio = pyaudio.PyAudio()
	frameSet = []

	# print out input devices and corresponding indeces
	for i in range(audio.get_device_count()):
		dev = audio.get_device_info_by_index(i)
		print((i,dev['name'],dev['maxInputChannels']))
	
	# start Recording
	stream = audio.open(format=FORMAT, rate=RATE, input=True,
			channels=CHANNELS, 
	                frames_per_buffer=CHUNK)
	
	while aok:
		frames = []
		for i in range(0, int(RATE / CHUNK * INTERVAL)):
			data = stream.read(CHUNK)
			frames.append(data)
		frameSet.append(frames)
		deleteOldFrames(frameSet)
		global updating
		if not updating:
			updating = True
			doInExternalThread(update,(audio,frameSet[:]))
	
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
