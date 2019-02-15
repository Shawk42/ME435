"""
ASSIGNMENT 3 - PROBLEM 1
OBJECTIVE: Determine is a tank will overflow and drain
FLUID - Water [assuming incompressible]
"""

'''MODULE IMPORTATION'''
import numpy as np
import matplotlib.pyplot as plt

'''GIVENS'''
#Conversions
m = 0.01     #Converts cm to m

#Common properties
H_t = 2.5       #Overall height of tank [m]
H_o = 1.5       #Initial height of water in tank [m]
D_t = 1.5       #Diameter of tank [m]
rho = 998       #Density of water [kg/m^3]

#Inlet Properties
Dia_i = 10*m        #Diameter of inlet pipe [m]
V_i = 3             #Inlet Veloctiy [m/s]

#Outlet Properties
Dia_o = 5.25*m      #Diameter of outlet pipe [m]
V_o = 6             #Outlet Velocity [m/s]

'''SOLUTION'''
#Finding M_dot of the system
A_i = (np.pi/4)*Dia_i**2
Mdot_i = rho*A_i*V_i            #Mdot coming into the tank [kg/s]

A_o = (np.pi/4)*Dia_o**2
Mdot_o = rho*A_o*V_i            #Mdot coming out of the tank [kg/s]

Mdot_sys = Mdot_i-Mdot_o        #Mdot of the system [kg/s]

if Mdot_sys > 0:                        #Logic to determine system state
    print("The tank level is rising")
elif Mdot_sys < 0:
    print("The tank level is lowering")
else:
    print("The tank level constant")

#Determing when tank will fill or drain
Vol_tot = ((np.pi/4)*D_t**2)*H_t         #Finding the total volume of the tank [m^3]
Vol_i = ((np.pi/4)*D_t**2)*H_t           #Finding the total volume of the tank [m^3]
