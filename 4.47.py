import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

#Givens
Sp = 45
Hp_1 = 15.5
Hp_2 = 52
Del_z = 20
V_dot_org = 240


#Part A
b = (Sp-Del_z)/(V_dot_org**2)
V_dot = np.linspace(0,350,1001)
H_p = Del_z+b*V_dot**2

b_1 = (Hp_1-Del_z)/(V_dot_org**2)
H_p1 = Del_z+b_1*V_dot**2

b_2 = (Hp_2-Del_z)/(V_dot_org**2)
H_p2 = Del_z+b_2*V_dot**2

#Part B
PC_25 = genfromtxt('2.5BB.csv',delimiter=',')
Hp25 = PC_25[:,1]
V25 = PC_25[:,0]

PC_4AD = genfromtxt('4AD.csv',delimiter=',')
Hp4AD = PC_4AD[:,1]
V4AD = PC_4AD[:,0]


plt.plot(V_dot,H_p)
plt.plot(V_dot,H_p1)
plt.plot(V_dot,H_p2)
plt.legend(("System","4AD Pump Sys. Curve","2.5BB Pump Sys. Curve"))
plt.title("System and Pump Head [PART A]")
plt.grid()
plt.show()

#Part B
plt.plot(V_dot,H_p)
plt.plot(V_dot,H_p1,linestyle = '--')
plt.plot(V_dot,H_p2,linestyle = '--')
plt.plot(V4AD,Hp4AD)
plt.plot(V25,Hp25)
plt.vlines(V_dot_org,0,np.max(H_p))
plt.plot(240,45,'*')
plt.legend(("System","4AD Pump Sys. Curve","2.5BB Pump Sys. Curve","4AD Pump Curve","2.5BB Pump Curve","Operating Point"))
plt.grid()
plt.ylabel("Head [ft]")
plt.xlabel("Capacity [gpm]")
plt.title("System and Pump Head [PART B]")
plt.show()

#Part C - 4AD Fails
plt.plot(V_dot,H_p,linestyle = '--')
plt.plot(V_dot,H_p1,linestyle = '--')
plt.plot(V_dot,H_p2)
plt.plot(V4AD,Hp4AD)
plt.plot(V25,Hp25)
plt.vlines(V_dot_org,0,np.max(H_p))
plt.plot(240,52,'*')
plt.legend(("System","4AD Pump","2.5BB Pump Sys. Curve","4AD Pump Curve","2.5BB Pump Curve","Operating Point"))
plt.grid()
plt.ylabel("Head [ft]")
plt.xlabel("Capacity [gpm]")
plt.title("System and Pump Head [PART C]")
plt.show()

#Part D - 2.5BB Fails
plt.plot(V_dot,H_p,linestyle = '--')
plt.plot(V_dot,H_p1)
plt.plot(V_dot,H_p2,linestyle = '--')
plt.plot(V4AD,Hp4AD)
plt.plot(V25,Hp25)
plt.vlines(V_dot_org,0,np.max(H_p))
plt.plot(240,16,'*')
plt.legend(("System","4AD Pump","2.5BB Pump Sys. Curve","4AD Pump Curve","2.5BB Pump Curve","Operating Point"))
plt.grid()
plt.ylabel("Head [ft]")
plt.xlabel("Capacity [gpm]")
plt.title("System and Pump Head [PART D]")
plt.show()
