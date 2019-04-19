print("Problem - 5.56")
import numpy as np

"""GIVENS"""
OD = 0.75     #Outside Diameter of Tube
Pt = 1          #Pitch [in]
mdot = 240000   #Mass Flow Rate [lbm/hr]
D_s = 17.25     #Diamter of shell [in]
B = 1           #Baffle Spacing [in]
C = Pt-OD       #Tube Clearance
Nb = 10

"""MATERIAL PROPERTIES"""
k = 0.33            #Btu/hr-ft-F
rho = 62.4          #lbm/ft^3
Pr = 9.4            #dim
mu = 3.15           #lb,/ft-hr
gamma = 0.99        #dim
g = 32.2

"""PART A SOLUTION"""
X = 2*np.sqrt(3)
D_e = (X*Pt**2)/(np.pi*(OD))
As = (D_s*C*B)/Pr

V = (mdot)/(rho*As)
Re = (rho*V*D_e)/mu
Nu = (0.36*Re**0.55)*(Pr**(1/3))

h = (k/D_e)*Nu

"""PART B SOLUTION"""
f = np.exp(0.576-0.19*np.log(Re))


DeltaP = gamma*(f*(Nb+1)*(D_s/D_e)*(V**2/(2*g)))
DeltaP = DeltaP*((1/3600)*(1/3600)*(1/32.174))
DeltaP = DeltaP*(1/144)

if DeltaP >= 10:
    print("ERROR - Delta P is larger than 10 psi")

"""SOLUTION PRINTING"""
print("")
print("SOLUTION")
print("-"*50)
print("Part A")
print( "h =",round(h,2),"Btu/hr-ft-F")
print("")
print("Part B")
print("Delta P",DeltaP,"psi")