import numpy as np

"""GIVENS"""
#Global Properties
L = 6               #Length of DPHX [ft]
g = 32.2

#Outer Properties - Cold Fluid
Vdot_cold = 75*0.133681      #[ft^3/min]
Tavg_cold = 50      #[F]

#Inner Properties - Hot Fluid
Vdot_hot = 80      #[gpm]
Tavg_hot = 120      #[F]
n = 0

"""PART A-DeltaP clean and fouled inner [hard water]"""
ID_clean = 0.016742

kf_i = 1.70         #Btu/hr-ft-F
Rf_pp_i = 0.002     #hr-ft^2/Btu
ID_fouled = ID_clean*(np.exp(-(2*kf_i*Rf_pp_i)/(ID_clean)))

ID = np.array([ID_clean,ID_fouled])

Area_clean = ID.item(0)**2*(np.pi()/4)
V_hotclean = Vdot_cold*Area_clean
V_hotfouled = V_hotclean*(1-0.025)
V_hot = np.array([V_hotclean,V_hotfouled])
gamma_hot = 1
f_hot = np.array([1,1])
DeltaP_hot = (f_hot*(L/ID)*((V_hot**2)/(2*g)))*gamma_hot

"""PART B - Delta P clean and fouled outer [city water]"""
D_hyd = 1 #Diameter does change with fouling
V_cold = np.array([1,1*0.75])
gamma_cold = 500
f_cold = np.array([1,1])
DeltaP_cold = (f_cold*(L/D_hyd)+n)*(V_cold**2/(2*g))*gamma_cold


"""SOLUTION PRINTING"""
print("")
print("SOLUTIONS")
print("-"*50)
print("Part A")
print("Pressure Drop clean",round(DeltaP_hot.item(0),2),"psf")
print("Pressure Drop fouled",round(DeltaP_hot.item(1),2),'psf')
print("Part B")
print("Pressure Drop clean",round(DeltaP_cold.item(0),2),"psf")
print("Pressure Drop fouled",round(DeltaP_cold.item(1),2),'psf')


