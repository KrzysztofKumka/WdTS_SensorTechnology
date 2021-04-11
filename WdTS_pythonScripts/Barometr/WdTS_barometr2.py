def function1(x, a, c, b):
 return a * np.exp(-b*x) + c
def function2(x, a, b):
 return a*x + b
def data_read():
 time = []
 pressure = []
 temperature = []
 with open('cisnienie_temperatura.csv') as file:
 read_csv = csv.reader(file, delimiter=',')
 next(read_csv)
 for row in read_csv:
 time.append(float(row[0]))
 pressure.append(float(row[1]))
 temperature.append(float(row[2]))
 return time, pressure, temperature
time, pressure, temperature = data_read()
temp_dec = []
time_dec = []
temp_inc = []
time_inc = []
for i in range(0, 4330):
 temp_dec.append(temperature[i])
 time_dec.append(time[i])
for i in range(4330, 8087):
 temp_inc.append(temperature[i])
 time_inc.append(time[i])
fit_params_dec, covariance_matrix_d = curve_fit(function1, time_dec, temp_dec)
fit_params_inc, covariance_matrix_i = curve_fit(function1, time_inc, temp_inc, p0=(-50,
0, 0))
x_dec = np.asarray(time_dec)
x_inc = np.asarray(time_inc)
V = 0.0005 #CONST - Sloik pol litra
R = 8.134
n = []
for i in range(len(pressure)):
 n.append((pressure[i]*V)/(R*temperature[i]))
pv = []
nrt = []
for i in range(len(pressure)):
 pv.append(pressure[i]*V)
 nrt.append(n[i]*R*temperature[i])
fit_params_lin, covariance_matrix_lin = curve_fit(function2, pv, nrt)
x_pv = np.asarray(pv)
plt.subplot(131)
plt.title('Malejaca temperatura')
plt.xlabel('Czas [s]')
plt.ylabel('Temperatura [C]')
plt.plot(time_dec, temp_dec, 'or', markersize='2')
plt.plot(x_dec, function1(x_dec, *fit_params_dec), 'b')
plt.grid(True)
plt.subplot(132)
plt.title('Rosnaca temperatura')
plt.xlabel('Czas [s]')
plt.ylabel('Temperatura [C]')
plt.plot(time_inc, temp_inc, 'ob', markersize='2')
plt.plot(x_inc, function1(x_inc, *fit_params_inc), 'r')
plt.grid(True)
plt.show()
plt.title('Zaleznosc p * V = n * R * T')
plt.xlabel('p * V')
plt.ylabel('n * R * T')
plt.plot(pv, nrt, 'og', markersize='2')
plt.plot(x_pv, function2(x_pv, *fit_params_lin), 'r')
plt.grid(True)
plt.show()