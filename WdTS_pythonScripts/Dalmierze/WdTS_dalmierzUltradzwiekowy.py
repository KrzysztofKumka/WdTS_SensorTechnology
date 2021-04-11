#HC-SR04
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

plt.style.use('seaborn-whitegrid')
with open("dane1.txt", "r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    matrix = []

for line in content:
    s = line.split()
    if s[0].isdigit() and len(s) == 5:
        matrix.append(s)

distance = []
time = []
read2 = []
temp = []

for i in range(20):
 val = matrix[i][0]
 int_val = int(val)
 distance.append(int_val)
for i in range(20):
 val = matrix[i][1]
 int_val = float(val)
 time.append(int_val)
for i in range(20):
 val = matrix[i][3]
 int_val = int(val)
 read2.append(int_val)
for i in range(20):
 val = matrix[i][4]
 int_val = int(val)
 temp.append(int_val)
distance_m = (distance * 100)
time_s = (time * 100)
sound_speed = []
for i in range(4):
 res = 2*(distance_m[i]/time_s[i])
 sound_speed.append(res)
speed = np.mean(sound_speed) #PREDKOSC DZWIEKU
######################################## REGRESJA WG. SKRYPTU NA WYKLADZIE
x = np.array(read2).reshape((-1, 1))
y = np.array(time)
model = LinearRegression()
model.fit(x, y)
slope = float(model.coef_)
intercept = float(model.intercept_)
abline_values = [model.coef_ * i + model.intercept_ for i in x]
####################################### PARAMETRY REGRESJI && NIEPEWNOSC CZULOSCI
sum_x_tab = read2
sum_y_tab = time
sum_x2_tab = []
sum_y2_tab = []
sum_xy_tab = []
n = 20
for i in range(20):
 v1 = np.power(read2[i], 2)
 v2 = read2[i]*time[i]
 v3 = np.power(time[i], 2)
 sum_x2_tab.append(v1)
 sum_xy_tab.append(v2)
 sum_y2_tab.append(v3)
sum_x = np.sum(sum_x_tab)
sum_y = np.sum(sum_y_tab)
sum_x2 = np.sum(sum_x2_tab)
sum_y2 = np.sum(sum_y2_tab)
sum_xy = np.sum(sum_xy_tab)
a = (n*sum_xy - (sum_x*sum_y))/(n*sum_x2 - np.power(sum_x, 2))
b = (1/n)*(sum_y - a*sum_x)
s_a = np.sqrt((n*(sum_y2 - a*sum_xy - b*sum_y))/((n-2)*(n*sum_x2 - np.power(sum_x, 2))))
print(a,b,s_a)
######################################## DOKLADNOSC
acc_tab = []
for i in range(20):
 v = abs(read2[i] - distance[i])
 acc_tab.append(v)
accuracy = max(acc_tab) #DOKLADNOSC
#print(intercept) #OFFSET
#print(slope) #CZULOSC
#print(accuracy)
plt.scatter(x, y, s = 8, color='r')
plt.plot(x, abline_values, '-', label='y={:.2e}x+{:.2e}'.format(slope, intercept))
plt.title('Dalmierz ultradźwiękowy')
plt.xlabel('Odczyt HC-SR04 [mm]')
plt.ylabel('Czas odczytu [ms]')
plt.show()