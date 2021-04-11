#Fitowanie liniowych zakresów charakterystyk, punkt 2
def main():
 mag_x = np.loadtxt(open("magneto_data_X.csv", "rb"), delimiter=",")
 mag_y = np.loadtxt(open("magneto_data_Yc.csv", "rb"), delimiter=",")
 mag_z = np.loadtxt(open("magneto_data_Zc.csv", "rb"), delimiter=",")
 oi = []
 ox = []
 oy = []
 oz = []
 H_teor = []
 coil_const = 31.9
 for i in range(25):
 val = mag_x[i][0]
 oi.append(val)
 for i in range(25):
 val = mag_x[i][1]
 ox.append(val)
 for i in range(25):
 val = mag_x[i][2]
 oy.append(val)
 for i in range(25):
 val = mag_x[i][3]
 oz.append(val)
 for i in range(25):
 val = coil_const * oi[i]
 H_teor.append(val)
 x = H_teor
 y1 = ox
 y2 = oy
 y3 = oz
 ############## Fitowanie funkcji ######################
 fit_paramsX, covariance_matrixX = curve_fit(func, x, y1)
 fit_paramsY, covariance_matrixY = curve_fit(func, x, y2)
 fit_paramsZ, covariance_matrixZ = curve_fit(func, x, y3)
 x = np.asarray(x)
 print("OX ", fit_paramsX)
 print("OZ ", fit_paramsY)
 print("OY ", fit_paramsZ)
 #######################################################
 plt.subplot(131)
 plt.plot(x, func(x, *fit_paramsX), 'b--')
 plt.plot(H_teor, ox, 'o', color='b')
 plt.title('OX')
 plt.xlabel('Zadane pole [G]')
 plt.ylabel('Pomiar na osi X [G]')
 plt.subplot(132)
 plt.plot(x, func(x, *fit_paramsY), 'r--')
 plt.plot(H_teor, oy, 'o', color='r')
 plt.title('OY')
 plt.xlabel('Zadane pole [G]')
 plt.ylabel('Pomiar na osi Y [G]')
 plt.subplot(133)
 plt.plot(x, func(x, *fit_paramsZ), 'g--')
 plt.plot(H_teor, oz, 'o', color='g')
 plt.title('OZ')
 plt.xlabel('Zadane pole [G]')
 plt.ylabel('Pomiar na osi Z [G]')
 plt.show()
def func(x, a, b):
 return a*x+b