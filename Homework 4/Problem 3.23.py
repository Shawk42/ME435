import numpy as np
from CoolProp.CoolProp import PropsSI

n_c = 0.83   #Efficenry of each compressor
Vdot_air = 3500/2118.88    #Vdot of air in m^3 per second

'''Initial State Tables'''
#Everything is in base SI units (K,Pa,J,etc.)
points = np.array(["POINT",int(1),int(2),int(3),int(4),int(5),int(6)])
fluid = np.array(["FLUID",'Air','Air','Air','Air','Water','Water'])
temp = np.array(["TEMP[K]",25+273.15,"unknown","T_5+10R","unknown",25+273.15,75+273.15])
pressure = np.array(["PRES[Pa]",101325,500000,500000,1*(10**6),101325,101325])

'''CALCULATED STATE VARIABLES'''
#Finding T_3
T_3 = float(temp.item(6))+ 5.55556     #Finding temperature at exit at HX via pinch point

#Finding T_2
h_1 = PropsSI('H','T',float(temp.item(1)),'P',float(pressure.item(1)),fluid.item(1))   #Enthalpy at compressor entrance
s_1 = PropsSI('S','T',float(temp.item(1)),'P',float(pressure.item(1)),fluid.item(1))   #Entropy at compressor entrance
h_2_s = PropsSI('H','S',s_1,'P',float(pressure.item(2)),fluid.item(2))                 #Isentropic
h_2 = ((h_2_s-h_1)/n_c)+h_1                                                            #Enthalpy at state 2
T_2 = PropsSI('T','P',float(pressure.item(2)),'H',h_2,fluid.item(2))                   #Tempearture at state 2

#Determining C_p's
Tavg_water = (float(temp.item(5))+float(temp.item(6)))/2
Tavg_air = (T_2+T_3)/2

Cp_water = PropsSI('C','T',float(temp.item(5)),'P',float(pressure.item(5)),fluid.item(5))      #C_p for water assuming average temp and atm pressure
Cp_air = PropsSI('C','T',Tavg_air,'P',float(pressure.item(3)),fluid.item(3))          #C_p for air assuming average temp

#Determining density
rho_air = PropsSI('D','T',float(temp.item(1)),'P',float(pressure.item(1)),fluid.item(1))

#Enthalpies for part 2
h_5 = PropsSI('H','T',float(temp.item(5)),'P',float(pressure.item(5)),fluid.item(5))
h_6 = PropsSI('H','T',float(temp.item(6)),'P',float(pressure.item(6)),fluid.item(6))
h_3 = PropsSI('H','T',T_3,'P',float(pressure.item(3)),fluid.item(3))
s_3 = PropsSI('S','T',T_3,'P',float(pressure.item(3)),fluid.item(3))
h_4_s = PropsSI('H','P',float(pressure.item(4)),'S',s_3,fluid.item(4))
h_4 = ((h_4_s-h_3)/n_c)+h_3                                                     #Enthalpy at state 4
T_4 = PropsSI('T','H',h_4,'P',float(pressure.item(4)),fluid.item(4))

"""STATE TABLE ADDITIONS"""
h = np.array(["ENTHALPY",h_1,h_2,h_3,h_4,h_5,h_6])
temp = np.array(["TEMP[K]",25+273.15,T_2,T_3,T_4,25+273.15,75+273.15])

"""SOLUTION A"""
mdot_air = Vdot_air*rho_air
Cdot_air = mdot_air*Cp_air
num = Cdot_air*(float(temp.item(2))-float(temp.item(3)))
dem = float(temp.item(5))-float(temp.item(6))
Cdot_water = num/dem
mdot_water = abs(Cdot_water/Cp_water)
rho_water_5 = PropsSI('D','T',float(temp.item(5)),'P',float(pressure.item(5)),fluid.item(5))
vdot_water = mdot_air/rho_water_5
vdot_water = vdot_water*15850.372483753                                                     #Vdot water in GPM

"""SOLUTION B"""

in_terms = (mdot_air*float(h.item(1)))+(mdot_water*float(h.item(5)))
out_terms = (mdot_air*float(h.item(4)))+(mdot_water*float(h.item(6)))
Wdot_C = out_terms-in_terms
Wdot_C = Wdot_C*(1/1000)

"""SOLUTION PRINTING"""
print("Solution A - v_dot_water =",vdot_water,"[gpm]")
print("Solution B - Wdot_C = ",Wdot_C,"kW")

"""STATE TABLE"""
master_table = np.vstack((points,fluid,temp,pressure,h))
print("STATE TABLE")
print(master_table)

"""TROUBLEHSOOTING"""
print(" ")
print("Troubleshooting")
print("Mdot Air",mdot_air)
print("Rho Air",rho_air)
print("Isentripic enthalpy",h_2_s)
print("Enthalpy at 2",h_2)
print("Mdot Water",mdot_water,"[kg/s]")