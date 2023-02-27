#learning about machine learning
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
    
def activate(inputs, weights):
    result = 0
    for input, weight in zip(inputs, weights):
        result += input * weight

    return sigmoid(result)

if __name__ == "__main__":
    inputs = [.5, .4, .2]
    weights = [.6, .7, .2]
    output = activate(inputs, weights)
    print(output)
    






quit()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import soundfile as sf
import sounddevice as sd
from glob import glob
import librosa
import librosa.display
import os
from itertools import cycle
sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])

os.system("cls")

audios_files= glob("audios/*/*.wav")

def audio_info(audio_file, index=0):
    audio_infos , sr= librosa.load(audio_file[index]) #sr = sample rate
    
    print(pd.Series(audio_infos))
    print(f"Sample rate: {sr}")
    print(f"Duration: {len(audio_infos)/sr} seconds")
    print(f"Number of samples: {len(audio_infos)}")
    print(f"value of the first sample: {audio_infos[0]}")

    values=[]
    total=0
    for i in range(0, len(audio_infos)):
        print(f"index: {i} value: {audio_infos[i]}")
        total += audio_infos[i]
        if audio_infos[i] not in values:
            values.append(audio_infos[i])       
    
    print(pd.Series(values))
    print("min value: {:.6f}".format(np.min(audio_infos)))
    print("max value: {:.6f}".format(np.max(audio_infos)))
    print("mean value: {:.6f}".format(np.mean(audio_infos)))    

    pd.Series(audio_infos).plot()
    plt.show()   


 
audio_info(audios_files)

