def data_read():
 t = []
 p = []
 with open('cisnienie_wysokosc.csv') as file:
 read_csv = csv.reader(file, delimiter=',')
 next(read_csv)
 for row in read_csv:
 t.append(float(row[0]))
 p.append(float(row[1]))
 return t, p
time, pressure = data_read()
temp = (85-32)*(5/9) + 273.15
p0 = 101000
ro = []
for i in range(len(pressure)):
 ro.append((pressure[i])/(temp*287.05))
h = []
for i in range(len(pressure)):
 val = (( p0 - pressure[i]) / (ro[i]*9.81))
 h.append(val)
floors = (max(h) - min(h)) / 3
plt.plot(time, pressure, 'og', markersize='2')
plt.title('Cisnienie w zaleznosci od czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Cisnienie [Pa]')
plt.grid(True)
plt.show()
plt.plot(time, h, 'or', markersize='2')
plt.title('Polozenie w zaleznosci od czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Wysokosc [m]')
plt.grid(True)
plt.show() 