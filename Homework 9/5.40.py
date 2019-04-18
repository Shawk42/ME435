import numpy as np

"""GIVENS"""
#Global Properties
L = 6               #Length of DPHX [ft]
g = 32.2

#Outer Properties - Cold Fluid
Vdot_cold = 75      #[gpm]
Tavg_cold = 50      #[F]

#Inner Properties - Hot Fluid
Vdot_hot = 80      #[gpm]
Tavg_hot = 120      #[F]
n = 0

"""PART A-DeltaP clean and fouled inner"""
ID = 1 #Diameter does change with fouling
V_hot = np.array([1,1*0.75])
gamma_hot = 500
f_hot = np.array([1,1])
DeltaP_hot = (f_hot*(L/ID)*((V_hot**2)/(2*g)))*gamma_hot

"""PART B - Delta P clean and fouled outer """
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


