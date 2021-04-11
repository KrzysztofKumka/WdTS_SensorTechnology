import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.optimize import curve_fit
plt.style.use('seaborn-whitegrid')
csv = np.loadtxt(open("dane_sprezyna.csv", "rb"), delimiter = ",", skiprows = 1)
time = []
z_acc = []
for i in range(4999):
 v = csv[i][0]
 time.append(v)
for i in range(4999):
 v = csv[i][1]
 z_acc.append(v)
def function(x, a, f, ph, aa, b):
 return a * np.sin(2 * np.pi * f * x + ph) * np.exp(-aa * x) + b
####### calka ########
def integral(x, t):
 v = []
 v.append(0)
 for i in range(1, 4999):
 dt = t[i] - t[i-1]
 v.append(v[i-1]+x[i]*dt)
 return v
###### Zaleznosc przyszpieszenia od czasu #######
z_mean = np.mean(z_acc)
z_acc = z_acc - z_mean
plt.plot(time, z_acc, 'bo', markersize = 2)
plt.title("Przyspieszenie w zaleznosci od czasu")
plt.xlabel("Czas [s]")
plt.ylabel("Przyspieszenie [m/s^2]")
plt.show()
###### predkosc ######
v_ = integral(z_acc, time)
fs = 1/(time[1]-time[0])
v = [i*9.81 for i in v_]
sos = signal.butter(2, 0.9, 'highpass', output='sos', fs=fs)
vfilt = signal.sosfilt(sos, v)
plt.plot(time, v, 'or', markersize = 2)
plt.title("Predkosc w zaleznosci od czasu - DRYFT")
plt.xlabel("Czas [s]")
plt.ylabel("Prędkość [m/s]")
plt.show()
plt.plot(time, vfilt, 'og', markersize = 2)
plt.title("Predkosc w zaleznosci od czasu - FILTRACJA")
plt.xlabel("Czas [s]")
plt.ylabel("Predkosc [m/s]")
plt.show()
##### polozenie #####
s = integral(vfilt, time)
sfilt = signal.sosfilt(sos, s)
plt.plot(time, s, 'or', markersize=2)
plt.title("Polozenie w zaleznosci od czasu - DRYFT")
plt.xlabel("Czas [s]")
plt.ylabel("Polozenie [m]")
plt.show()
plt.plot(time, sfilt, 'ob', markersize=2)
plt.title("Polozenie w zaleznosci - FILTRACJA")
plt.xlabel("Czas [s]")
plt.ylabel("Polozenie [m]")
plt.show()
##### fitowanie ######
x = np.array(time)
y = np.array(sfilt)
fit_params, covariance_matrix = curve_fit(function, x, y)
plt.plot(x, y, 'ob')
plt.plot(x, function(x, *fit_params), '-r')
plt.title("Fitowanie przebiegu")
plt.xlabel("Czas [s]")
plt.ylabel("P