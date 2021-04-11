import numpy as np
import matplotlib.pyplot as plt from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
fig = plt.figure() ax = fig.add_subplot(111, projection='3d') csv = np.loadtxt(open("dane_animacja_v3.csv", "rb"), delimiter=",", skiprows=1)
csv_2 = np.loadtxt(open("dane_animacja_v2.csv", "rb"), delimiter=",", skiprows=1)
time_data = []
Gx = []
Gy = []
Gz = []
time_v2 = []
roll_v2 = []
pitch_v2 = []
for i in range(0, 999):
 v = csv[i][0]
 time_data.append(v)
for i in range(0, 999): v = csv[i][1]
 Gx.append(v)
for i in range(0, 999): v = csv[i][2]
 Gy.append(v)
for i in range(0, 999): v = csv[i][3]
 Gz.append(v)
############ DANE Z PLIKU ANIMACJA_V2 ####################
for i in range(0, 999): v = csv_2[i][0]
 time_v2.append(v)
for i in range(0, 999): v = csv_2[i][1]
 roll_v2.append(v)
for i in range(0, 999): v = csv_2[i][2]
 pitch_v2.append(v)
##########################################################
def get_params(time): t = int(time - 1)
 Yaw_deg = 0 Pitch_deg = np.arctan2(Gx[t], np.sqrt((Gy[t])**2 + (Gz[t])**2)) * 180/np.pi Roll_deg = np.arctan2(Gy[t], Gz[t])*180/np.pi
 X = 0 Y = 0 Z = 0 return Yaw_deg, Pitch_deg, Roll_deg, X, Y, Z def plot_IMU(time): Yaw_deg, Pitch_deg, Roll_deg, X, Y, Z = get_params(time)
 Yaw=Yaw_deg*np.pi/180 Pitch=Pitch_deg*np.pi/180 Roll=Roll_deg*np.pi/180 fig.clf()
 ax = fig.add_subplot(111, projection='3d')
 euler_Rx=np.array([[1,0,0],[0,np.cos(Roll),-np.sin(Roll)],[0,np.sin(Roll),np.cos(Roll)]])
 euler_Ry=np.array([[np.cos(Pitch),0,np.sin(Pitch)], [0,1,0], [-np.sin(Pitch),0,np.cos(Pitch)]])
 euler_Rz=np.array([[np.cos(Yaw),-np.sin(Yaw),0],[np.sin(Yaw),np.cos(Yaw),0], [0,0,1]])
 euler_Rzyx=np.dot(np.dot(euler_Rz,euler_Ry),euler_Rx)
 x_s=np.dot(euler_Rzyx,np.array([[1,0,0]]).T)
 y_s=np.dot(euler_Rzyx,np.array([[0,1,0]]).T)
 z_s=np.dot(euler_Rzyx,np.array([[0,0,1]]).T) #################### WYKRES ######################### ax.quiver(X,Y,Z,x_s[0],x_s[1],x_s[2],pivot='tail', color = 'b') ax.text(float(x_s[0]), float(x_s[1]), float(x_s[2]), "Xs", color = 'b') ax.quiver(X,Y,Z,y_s[0],y_s[1],y_s[2],pivot='tail', color = 'r') ax.text(float(y_s[0]), float(y_s[1]), float(y_s[2]), "Ys", color='r')
 ax.quiver(X,Y,Z,z_s[0],z_s[1],z_s[2],pivot='tail', color = 'g') ax.text(float(z_s[0]), float(z_s[1]), float(z_s[2]), "Zs", color='g')
 ############## UKLAD ODNIESIENIA #################### ax.quiver(-2, -2, -2, 1, 0, 0, pivot='tail', color='b') ax.text(-1, -2, -2, "Xo", color='b') ax.quiver(-2, -2, -2, 0, 1, 0, pivot='tail', color='r') ax.text(-2, -1, -2, "Yo", color='r') ax.quiver(-2, -2, -2, 0, 0, 1, pivot='tail', color='g') ax.text(-2, -2, -1, "Zo", color='g')
 plt.title("Krzysztof Kumka\nPitch: " + str(Pitch) + "\nRoll: " + str(Roll) + "\nTime: " + str(time_data[int(time-1)])) #todo ax.set_xlim([-2, 2]) ax.set_ylim([-2, 2]) ax.set_zlim([-2, 2]) ax.set_xlabel('X') ax.set_ylabel('Y') ax.set_zlabel('Z')
 plt.xticks(np.linspace(-2,2,num=5))
 plt.yticks(np.linspace(-2,2,num=5)) ax.set_zticks(np.linspace(-1,1,num=5)) ax.view_init(30,-115)
ani = FuncAnimation(fig, plot_IMU, frames=np.linspace(1,len(time_data),100), interval = 1)
ani.save('/path.gif', writer='imagemagick', fps=15)
plt.show()