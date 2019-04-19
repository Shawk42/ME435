'''
The intention of this function is to solve pressure drop problems easily. The function uses the SI unit system.
'''
import numpy as np

#Fluid properties
rho = 678.093592
mu = 0.000529637547516
#Pipe Props
L = 804.672
D = 0.182550816
z_1 = 0
z_2 = 0
epsilon = 4.6*(10**-5)
#Flow Props
V_dot = 0.03122955

#Velocity of fluid
Internal_Area = np.pi*(D/2)**2
Vel = V_dot/Internal_Area

#Constants
g = 9.81
Re_thrs = 2300

#Reynolds Number
Re_d = (rho*Vel*D)/mu

#Friction factor
if Re_d <= Re_thrs:
    flow_type = "Laminar"
    f = 64/Re_d
elif Re_d > Re_thrs:
    flow_type = "Turbulent"
    f = 0.25/((np.log(((epsilon/D)/3.7))+(5.74/(Re_d**0.9)))**2)
else:
    print("ERROR IN COMPUTING FRICTION FACTOR")

#Negative Pressure Drop
rho_vel = (rho*Vel**2)/2   #Common factor
P_delta = rho_vel+(rho*g*z_2)+(f*(L/D)*rho_vel)-rho_vel-(rho*g*z_1)


#Printing
print("-"*50)
print("OUTPUT OF PRESSURE DROP FUNCTION")
print("Delta P",P_delta,"[Pa]")
print("Flow Type",flow_type," - Reynolds Number",Re_d)
givens = np.array(["rho [kg/m^3]","mu [kg/m-s]","L [m]","D [m]","z_1 [m]","z_2 [m]","epsilon [dim]","Velocity [m/s]"])
given_inputs = np.array([rho,mu,L,D,z_1,z_2,epsilon,Vel])
checks = np.vstack((givens,given_inputs))
print(checks)

