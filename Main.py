#import audioop
#import wave
#import random
#import struct
#import numpy as np
#import time
from WavSteg import hide_data
from WavSteg import recover_data
from WavSteg import usage

#sam = wave.open("Alice.wav", mode=None)
#framerate = sam.getframerate()
#nFrames = sam.getnframes()
#width = sam.getsampwidth()
#channels = sam.getnchannels()
#leng = nFrames/framerate
#data = sam.readframes(nFrames)
#l = len(data) / 1024.0 / 1024.0

#print ("Sampling rate:"), framerate
#print ("nFrame count: "), nFrames
#print ("Sample width: "), width
#print ("Channels: "), channels
#print ("Song length in seconds: "), leng
#print l, ("MB")

#ar = np.frombuffer(data, dtype = 'B')
#print (ar)
#ar = np.frombuffer(data, dtype = '<i2').reshape(-1,channels)
#ar_str = np.array_str(ar)
#print len(ar_str)


#noise_output = wave.open('noise2.wav', 'w')
#noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

#values = []

#for i in range(0, sp):
        #value = random.randint(-32767, 32767)
        #value = sam.readframes(i)
        #packed_value = struct.pack('i', value)
        #values.append(packed_value)
        #values.append(packed_value)

#value_str = ''.join(ar_str)

#noise_output.writeframes(ar)
#noise_output.close()

hide_data("Alice.wav", "Test.txt", "Hidden.wav", 1)
recover_data("Alice.wav", "Recovered.txt", 1, 4)

print ("Done")
