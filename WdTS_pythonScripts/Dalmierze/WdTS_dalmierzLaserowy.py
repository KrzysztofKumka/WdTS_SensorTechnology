#VL53L0X
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
read1 = []
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
 val = matrix[i][2]
 int_val = int(val)
 read1.append(int_val)
for i in range(20):
 val = matrix[i][4]
 int_val = int(val)
 temp.append(int_val)
distance_m = (distance * 100)
time_s = (time * 100)
acc_tab = []
for i in range(20):
 v = abs(read1[i] - distance[i])
 acc_tab.append(v)
accuracy = max(acc_tab) #DOKLADNOSC
#print(accuracy)
plt.xlim(0, 1200)
plt.ylim(0, 1200)
plt.plot(distance, read1, 'o', color='b')
plt.title('Dalmierz laserowy')
plt.xlabel('Dystans przeszkody')
plt.ylabel('Odczyt VL53L1X')
plt.show()