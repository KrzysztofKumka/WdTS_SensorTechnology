#Cross-talk
def main():
 #mag_x = np.loadtxt(open("magneto_data_X.csv", "rb"), delimiter=",")
 mag_y = np.loadtxt(open("magneto_data_Yc.csv", "rb"), delimiter=",")
 #mag_z = np.loadtxt(open("magneto_data_Zc.csv", "rb"), delimiter=",")
 msrmt = mag_y
 ox = []
 oy = []
 oz = []
 for i in range(25):
 val = msrmt[i][1]
 ox.append(val)
 for i in range(25):
 val = msrmt[i][2]
 oy.append(val)
 for i in range(25):
 val = msrmt[i][3]
 oz.append(val)
 ext = oy
 fit_params0, covariance_matrix0 = curve_fit(func, ext, ox)
 fit_params1, covariance_matrix1 = curve_fit(func, ext, oz)
 ext = np.asarray(ext)
 ##### CROSS-TALK ########################
 cross_talk = fit_params0[0]/fit_params1[0]
 print(cross_talk)
 print(fit_params0)
 print(fit_params1)
 #########################################
 plt.subplot(121)
 plt.plot(ext, func(ext, *fit_params0), 'b--')
 plt.plot(oy, ox, 'o', color='b')
 plt.xlabel('Pomiar na osi Y [G]')
 plt.ylabel('Pomiar na osi X [G]')
 plt.subplot(122)
 plt.plot(ext, func(ext, *fit_params1), 'r--')
 plt.plot(oy, oz, 'o', color='r')
 plt.xlabel('Pomiar na osi Y [G]')
 plt.ylabel('Pomiar na osi Z [G]')
 plt.show()
def func(x, a, b):
 return a*x+b