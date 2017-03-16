from WavSteg import hide_data
from WavSteg import recover_data
from WavSteg import usage

hide_data("Alice.wav", "Test.txt", "Hidden.wav", 1)
recover_data("Hidden.wav", "Recovered.txt", 1, 31)

print ("Done")
