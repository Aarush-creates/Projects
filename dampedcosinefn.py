import numpy as np
import matplotlib.pyplot as plt
import math

decayrate = 1  
f0 = 3      
time = 8    
range = 20   

t = np.linspace(0, time, 1000)
dampedcosinefn = np.exp(-decayrate * t) * np.cos(2 * np.pi * f0 * t)

normalization = 0.5 * (math.sqrt(2) * math.pi)
frequencies = np.linspace(-range, range, 1000)
FFT = normalization * (1 / (decayrate + 2j * np.pi * (frequencies - f0)) + 1 / (decayrate + 2j * np.pi * (frequencies + f0)))
FFTmag = np.abs(FFT)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t, dampedcosinefn, color = 'black')
plt.title("Time Domain: Damped Cosine Function")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(frequencies, FFTmag, color = 'black')
plt.title("Frequency Domain: Damped Cosine Function")
plt.xlabel("Frequency (f)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()
