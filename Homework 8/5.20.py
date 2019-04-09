import numpy as np
from numpy import genfromtxt

print("Problem 5.20")

"""GIVENS"""
#Common
U = 1280      #[W/m^2-K]
Q_dot = 700   #[kW]

#Cold Fluid [20% Magnesium Chloride]
t_i = 0+273.15     #[K] Inlet Tempeature
V_dotc = 26*0.001        #[m^3/s]

#Hot Fluid [20% Magnesium Chloride]
T_i = 26+273.15     #[K] Inlet Tempeature
V_doth = 30*0.001        #[m^3/s]


"""STATE TABLES"""
Hexane_Master = genfromtxt('HexaneProps.csv',delimiter=',')
Hex_T = Hexane_Master[:,0]
Hex_T = np.delete(Hex_T,0)    #Tempereture of fluid in K
Hex_rho = Hexane_Master[:,1]
Hex_rho = np.delete(Hex_rho,0)    #Density of fluid in kg/m^3
Hex_Cp = Hexane_Master[:,2]
Hex_Cp = np.delete(Hex_Cp,0)    #Cp of fluid in kJ/kg-K

Mag_Master = genfromtxt('TwentyMCW.csv',delimiter=',')
Mag_T = Mag_Master[:,0]
Mag_T = Mag_T+273.15
Mag_rho = Mag_Master[:,1]
Mag_Cp = Mag_Master[:,2]


"""Part [A]"""

dev = 10

T_o = T_i
while abs(dev) >= 0.01:
    T_avg = (T_o+T_i)/2
    rho_h = np.interp(T_avg,Hex_T,Hex_rho)
    C_ph = np.interp(T_avg,Hex_T,Hex_Cp)
    m_doth = rho_h*V_doth
    Q_dotC = m_doth*C_ph*(T_i-T_o)
    dev = Q_dotC-Q_dot
    T_o = T_o - 0.0001

    if T_o < t_i:
        print("No solution Found")
        break



"""PART [B]"""
dev = 10

t_o = t_i
while abs(dev) >= 0.01:
    t_avg = (t_o+t_i)/2
    rho_c = np.interp(t_avg,Mag_T,Mag_rho)
    C_pc = np.interp(t_avg,Mag_T,Mag_Cp)
    m_doth = rho_c*V_dotc
    Q_dotC = m_doth*C_pc*(t_o-t_i)
    dev = Q_dotC-Q_dot
    t_o = t_o + 0.0001

    if t_o > T_i:
        print("No solution Found")
        break


"""PART [C]"""
DeltaT_out = T_i-t_o
DeltaT_in = T_o-t_i

TempDiff = (DeltaT_out-DeltaT_in)/np.log(DeltaT_out/DeltaT_in)
Area = Q_dot/(U*TempDiff)



"""SOLUTION"""

print("PART A - Solution")
#print("Outlet Temperature Found")
print("T_o = ",T_o-273.15," [C]")

print("")

print("PART B - Solution")
#print("Outlet Temperature Found")
print("t_o = ",t_o-273.15," [C]")

print("PART C - Solution")
#print("Outlet Temperature Found")
print("Area",Area," [m^2]")

"""Verifications"""
#Checking if Hot fluid gets warmer
if T_i < T_o:
    print("Error - Hot Fluid has gotten warmer")
#Checking of Cold Fluid has gotten colder
if t_o < t_i:
    print("Error - Cold Fluid has gotten colder")