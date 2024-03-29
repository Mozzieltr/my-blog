import wave
import numpy as np
import matplotlib.pyplot as plt
filepath = "C:/Users/AJS/Desktop/p/0_01.wav"
f = wave.open(filepath, 'rb')
num = filepath[-5]
params = f.getparams()
nchannels, samplewidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
f.close()
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 1
if nchannels == 2:
    wave_data.shape = -1, 2
else:
    pass
wave_data = wave_data.T
time = np.arange(0, nframes)*(1.0/framerate)
plt.subplot(211)
plt.plot(time, wave_data[0], 'r-')
plt.xlabel('Time/s')
plt.ylabel('Ampltitude')
plt.title('Num '+num+' time/ampltitude')
plt.show()
