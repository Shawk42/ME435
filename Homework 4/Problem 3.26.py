import numpy as np
from CoolProp.CoolProp import PropsSI

"""ASSUMPTIONS"""
print("The water entering the boiler (state 1) is assumed to be single phase water")

n_t = 0.86
n_g = 0.94
mdot_water = 400 #[kg/s]

"""INITIAL STATE TABLE SETUP"""
temp = np.array(["Temp[K]",100+273,650+273,"Temp 3 Unknown"])
press = np.array(["P [Pa]",5*(10**6),5*(10**6),10*(10**3)])
points = np.array(["Points",1,2,3])

"""CALCULATED STATE VARIABLES"""
h_1 = PropsSI('H','T',float(temp.item(1)),'P',float(press.item(1)),'Water')  #Cofirmed with Appendix 8.2
h_2 = PropsSI('H','T',float(temp.item(2)),'P',float(press.item(2)),'Water')
s_2 = ((7.2605+7.5136)/2)*(1000)      #Entropy found in table
h_3_s = PropsSI('H','S',s_2,'P',float(press.item(3)),'Water')
h_3 = (((h_2-h_3_s)*n_t)-h_2)*-1
T_3 = PropsSI('T','H',h_3,'P',float(press.item(3)),'Water')


"""AMENDED STATE TABLLES"""
temp = np.array(["Temp[K]",100+273,650+273,T_3])
h = np.array(["Enthalpy",h_1,h_2,h_3])


"""SOLUTIONS"""
#Part A
Wdot_turbine = mdot_water*(float(h.item(2))-float(h.item(3)))
Wdot_generator = n_g*Wdot_turbine
Wdot_generator = Wdot_generator*(1/(1*10**6))

#Part B
h_c = 21000*1000   #enthalpy of coal [K/kg]
AF = (h_c-float(h.item(1)))/(float(h.item(2))-float(h.item(1)))

#Part C
Qdot_boiler = mdot_water*abs(float(h.item(2))-float(h.item(1)))
mdot_coal = Qdot_boiler/h_c     #Mdot of coal in kg/s
mdot_coal = mdot_coal*(3.154*(10**7))  #Mdot of coal in kg/year
mdot_coal = mdot_coal*(1/1000)         #Mdot of coal in metric tons/year

#Part D
coal_rate = 48.52      #$/ton of coal
cost = mdot_coal*coal_rate

#Part E
gen_rate = 0.10       #$/kW-h
gen_output = (Wdot_generator*(1*(10**3)))*8760   #kW
income = gen_output*gen_rate

#Part F
revenue = income-cost

"""SOLUTIONS"""
print("Part A =",Wdot_generator,"[MW]")
print("Part B =",AF,"[dim]")
print("Part C =",mdot_coal,"[Metric Tons/year]")
print("Part D = $",cost)
print("Part E = $",income)
print("Part F = $",revenue)

"""STATE TABLE PRINTING"""
print(" ")
print("STATE TABLE")
master_table = np.vstack((points,temp,press,h))
print(master_table)

"""TROUBLESHOTTING"""
print(" ")
print("TROUBLESHOOTING")
print("Entropy at State 2 = ",s_2)
print("Tempearture at state 2 = ",float(temp.item(2))-273.15)
print("Pressure at state 2 = ",float(press.item(2))*(1/(1*10**6)),"[MPa]")
n_t_check = (float(h.item(2))-float(h.item(3)))/(float(h.item(2))-h_3_s)
print(n_t_check,"Expect",n_t)
n_g_check = (Wdot_generator*(1*(10**6)))/Wdot_turbine
print(n_g_check, "Expect",n_g)
print("Wdot Turbine",Wdot_turbine*(1/(1*10**6)),"[MW]")