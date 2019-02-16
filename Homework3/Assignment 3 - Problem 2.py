"""
ASSIGNMENT 3 - PROBLEM 2 [Design 1]
OBJECTIVE: SOLVE A-H
FLUID - VARIOUS
"""



'''MODULE IMPORTATION'''
import numpy as np
import matplotlib.pyplot as plt

"""STATE 1"""   #Water coming in
T_1 = 50    #Temperature [Rankine]
P_1 = 50            #Pressure [psia]
h_1 = 18.222

"""STATE_2"""    #WAter coming out
T_2 = 325   #Tempearture [Rankine]
P_2 = P_1
h_2 = 1198
rho_2 = 60.77
Vdot_2 = 100   #Volumetric flow rate
mdot_2 = Vdot_2*0.133681*rho_2*(1/60)

"""STATE 3"""    #Steam coming in
T_3 = 180
P_3 = P_1
h_3 = 148.27



"""PART A"""
#Solving for mdot1 Water coming in
num = (mdot_2*h_2)-(h_3*mdot_2)
dem = (h_1-h_3)
mdot_1 = num/dem

#Checking
a = (mdot_1*h_1)+h_3*(mdot_2-mdot_1)
b = mdot_2*h_2
print(a,"a")
print(b,"b")

print(mdot_1,"mdot")




"""MATRIX printing"""
Mdots = np.array([mdot_1,mdot_2])
print(Mdots)


