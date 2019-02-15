"""
ASSIGNMENT 3 - PROBLEM 1
OBJECTIVE: Determine if (and when) a tank will overflow or drain
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

#Determing when tank will fill or drain
Vol_tot = ((np.pi/4)*D_t**2)*H_t         #Finding the total volume of the tank [m^3]
Vol_i = ((np.pi/4)*D_t**2)*H_o           #Finding the total volume of the tank [m^3]
m_tot = rho*Vol_tot                      #Finding the total mass of a filled tank [kg]
m_i = rho*Vol_i                          #Finding the initial mass of the water in the tank [kg]

if Mdot_sys > 0:                        #Logic to determine system state and time determination
    print("The tank level is rising")
    mass = m_tot-m_i
    t = mass/Mdot_sys
    print(t,"seconds")
elif Mdot_sys < 0:
    print("The tank level is lowering")
    mass = m_i
    t = abs(mass/Mdot_sys)
    #This needs verification for a system that is lowering
else:
    print("The tank level constant")

'''TIME BASED VERIFICATION'''
time = np.linspace(0,t+50,1001)     #Linear space array for time
m_cur = m_i+(Mdot_sys*time)         #Current mass of tank [kg]
vol_cur = m_cur/rho                 #Current volume of water [m^3]

plt.plot(time,vol_cur)              #Plotting current volume of tank
plt.plot([0,t+50],[Vol_tot,Vol_tot])#Plotting line of max volume
plt.plot(t,Vol_tot,'*')             #Plotting point of fill
plt.xlabel("Time [seconds]")
plt.ylabel("Volume [m^3]")
plt.title("Volume of tank vs. time")
plt.grid()
plt.legend(('Current Tank Volume','Max Tank Volume','Calculated Fill Point'))
plt.show()