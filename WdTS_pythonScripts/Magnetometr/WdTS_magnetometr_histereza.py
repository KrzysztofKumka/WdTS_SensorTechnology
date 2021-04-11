#Histereza
def main():
 histereza = np.loadtxt(open("magneto_data_histereza.csv", "rb"), delimiter=",")
 c1 = []
 c2 = []
 c3 = []
 c4 = []
 H_teor = []
 coil_const = 31.9
 for i in range(300):
 val = histereza[i][0]
 c1.append(val)
 for i in range(300):
 val = histereza[i][1]
 c2.append(val)
 for i in range(300):
 val = histereza[i][2]
 c3.append(val)
 for i in range(300):
 val = histereza[i][3]
 c4.append(val)
 for i in range(300):
 val = coil_const * c1[i]
 H_teor.append(val)
 axis = c2
 ############### Fitowanie histerezy ####################
 fit_line_1 = []
 fit_line_2 = []
 H_his = []
 for i in range(276, 300):
 val = axis[i]
 fit_line_1.append(val)
 for i in range(0, 26):
 val = axis[i]
 fit_line_1.append(val)
 for i in range(176, 126, -1):
 val = axis[i]
 fit_line_2.append(val)
 for i in range(176, 126, -1):
 val = coil_const*c1[i]
 H_his.append(val)
 xx = np.linspace(-8, 8, 50)
 fit_params1, covariance_matrix1 = curve_fit(func, xx, fit_line_1)
 fit_params2, covariance_matrix2 = curve_fit(func, xx, fit_line_2)
 #print(fit_line_1)
 #print(fit_line_2)
 hist_list = []
 for i in range(50):
 val = func(xx[i], *fit_params1) - func(xx[i], *fit_params2)
 hist_list.append(val)
 hist_result = max(hist_list)
 print(hist_result)
 print(hist_list)
 ########################################################
 plt.xlim(-10, 10)
 plt.plot(H_teor, axis, 'o', color='b')
 plt.plot(xx, func(xx, *fit_params1), '--', color = 'g')
 plt.plot(xx, func(xx, *fit_params2), '--', color = 'r')
 plt.title('Pomiar petli histerezy: OX')
 plt.xlabel('Zadane pole [G]')
 plt.ylabel('Pomiar na osi X [G]')
 plt.show()
def func(x, a, b):
 return a*x+b