import numpy as np
import librosa
import matplotlib.pyplot as plt 

class Audioprocess():
    def __init__(self, file_path):
        self.file_paths = file_path
        counter = 0
        for i in range(2 , len(self.file_paths)):
            audio = self.file_paths[i]
            y, sr = librosa.load(audio)
            plt.figure()
            M_highres = librosa.feature.melspectrogram(y=y, hop_length=128)

            f = librosa.display.specshow(librosa.power_to_db(M_highres, ref=np.max),y_axis='mel', x_axis='time')
            plt.savefig(f"Spectragraph{counter}.png")
            counter += 1


