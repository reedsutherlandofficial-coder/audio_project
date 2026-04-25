import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt 
from pathlib import Path



class Audioprocess():
    def __init__(self, file_path):
        self.file_paths = file_path
        counter = 0
        for i in range(2 , len(self.file_paths)):
            audio = self.file_paths[i]
            y, sr = librosa.load(audio)
            plt.figure()
            M_highres = librosa.feature.melspectrogram(y=y, hop_length=512)

            f = librosa.display.specshow(librosa.power_to_db(M_highres, ref=np.max),y_axis='mel', x_axis='time')
            plt.savefig(f"chroma{counter}.png")
            counter += 1




    #def fft(self):
        #Data.outpath.append(librosa.fft_frequencies.self.file_paths)
    
#y, sr = librosa.load("/Users/barnmac/Downloads/Audio/bonus_ui_close_RS_Recreation.wav", sr=None, mono=False,)

#plt.figure()
#f = librosa.feature.tonnetz(y=y, sr=sr)
#plt.savefig('chroma.png')

#plt.figure()
#librosa.display.specshow(y , sr=44100, x_axis='time', y_axis='log', cmap='magma')
#plt.savefig('waveform.png')



