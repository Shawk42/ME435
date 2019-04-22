import numpy as np
import matplotlib.pyplot as plt

"""COMMON NUMBERS"""
#Cold Fluid
t_o = 80
t_i = 30
#Hot Fluid
T_i = 98
T_o = np.linspace(30,T_i-0.000001,1000)


"""SOLUTION"""
R = (T_i-T_o)/(t_o-t_i)
P = (t_o-t_i)/(T_i-t_i)

F_num = np.sqrt(R**2+1)*np.log((1-P)/(1-P*R))
F_lognum = 2-P*(R+1-np.sqrt(R**2+1))
F_logdem = 2-P*(R+1+np.sqrt(R**2+1))
F_log = F_lognum/F_logdem
F_dem = (R-1)*np.log(F_log)

F = F_num/F_dem

"""PLOTTING"""
T_i_delta = T_i-T_o

plt.subplot(2,1,1)
plt.plot(T_i_delta,F)
plt.grid()
plt.xlabel("Delta T Hot Fluid [C]")
plt.ylabel("F")
plt.title("Evaporator F curve - Deryk Ahner - Quiz 9")

plt.subplot(2,1,2)
plt.text(-0.125,0.125,"As shown in the above graph F approaches 1 in a evaporator or condenser. In both of these devices"
               " the inlet and outlet temperatures of the working fluid are relatively constant (due to the phase change)"
               " To determine the behavior of F, the outlet temperature was varied (in a linear spaced array) from"
               " the cold fluid inlet temperature to the hot fluid inlet temperature. To better show the F and temperature"
               " relationship the x-axis is the difference between the hot fluid inlet and outlet temperature. Therefore"
               " according the graph F approaches 1 in a phase change head exhanger, as the difference between inlet and "
               " outlet temperature goes to zero. The relationship also holds true for a condensor, however the graph "
                " has a positive second derivative (upward facing) ", wrap=True)
plt.axis('off')

plt.subplots_adjust(hspace = 0.5)
plt.show()