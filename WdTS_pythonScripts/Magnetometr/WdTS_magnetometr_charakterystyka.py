#Wyznaczanie charakterystyk sensora, punkt 1
def main():
 mag_x = np.loadtxt(open("magneto_data_X.csv", "rb"), delimiter=",")
 mag_y = np.loadtxt(open("magneto_data_Yc.csv", "rb"), delimiter=",")
 mag_z = np.loadtxt(open("magneto_data_Zc.csv", "rb"), delimiter=",")
 current = []
 ox = []
 oy = []
 oz = []
 H_teor = []
 coil_const = 31.9
 for i in range(75):
 val = mag_x[i][0]
 current.append(val)
 for i in range(75):
 val = mag_x[i][1]
 ox.append(val)
 for i in range(75):
 val = mag_y[i][2]
 oy.append(val)
 for i in range(75):
 val = mag_z[i][3]
 oz.append(val)
 for i in range(75):
 val = coil_const * current[i]
 H_teor.append(val)
 plt.subplot(131)
 plt.plot(H_teor, ox, 'o', color='b')
 plt.title('OX')
 plt.xlabel('Zadane pole [G]')
 plt.ylabel('Pomiar na osi X [G]')
 plt.subplot(132)
 plt.plot(H_teor, oy, 'o', color='r')
 plt.title('OY')
 plt.xlabel('Zadane pole [G]')
 plt.ylabel('Pomiar na osi Y [G]')
 plt.subplot(133)
 plt.plot(H_teor, oz, 'o', color='g')
 plt.title('OZ')
 plt.xlabel('Zadane pole [G]')
 plt.ylabel('Po