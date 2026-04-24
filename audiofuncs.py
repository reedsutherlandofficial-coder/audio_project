import librosa
import soundfile as sf
import matplotlib.pyplot as plt 
from pathlib import Path
class Audioprocess():
    def __init__(self, file_path):
        self.file_paths = file_path

    def visuals(self):
        for i in self.file_paths:
            if i == "~":
                pass
            y, sr = librosa.load(i)
            plt.figure()
            f = librosa.display.specshow(librosa.feature.chroma_stft(y=y, sr=sr), y_axis='chroma', x_axis='time')
            plt.savefig('chroma.png')




    #def fft(self):
        #Data.outpath.append(librosa.fft_frequencies.self.file_paths)
    
#y, sr = librosa.load("/Users/barnmac/Downloads/Audio/bonus_ui_close_RS_Recreation.wav", sr=None, mono=False,)

#plt.figure()
#f = librosa.feature.tonnetz(y=y, sr=sr)
#plt.savefig('chroma.png')

#plt.figure()
#librosa.display.specshow(y , sr=44100, x_axis='time', y_axis='log', cmap='magma')
#plt.savefig('waveform.png')



