import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf

audio_file = 'C:/Users/ashis/Downloads/voicerecording.mp3'
audio_dampedcosinefn, sampling_rate = librosa.load(audio_file, sr=None)

fft_size = 512
hop = 256
stft_dampedcosinefn = librosa.stft(audio_dampedcosinefn, n_fft = fft_size, hop_length = hop)
stftmag = np.abs(stft_dampedcosinefn)

noisecancel = 0.1 * np.max(stftmag)  
stftmag[stftmag < noisecancel] = 0  # comment to remove noise reduction filter

plt.figure(figsize = (10, 5))
db_change = librosa.amplitude_to_db(stftmag, ref = np.max)
librosa.display.specshow(db_change, sr = sampling_rate, hop_length = hop, x_axis = 'time', y_axis = 'log')
plt.title('STFT of an audio recording') # with or without noise reduction
plt.colorbar(format = '%+2.0f dB')
plt.show()


