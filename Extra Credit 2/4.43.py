print("Problem 4.43")
import numpy as np
import matplotlib.pyplot as plt

"""GIVENS"""
#V_dot = 400     #[gpm] 400 gpm required
V_dot = np.linspace(400,600,1001)
Delta_Z = 30    #[ft]
L = 85          #[ft]

"""TABLE VALUES"""
T = 55                  #[F]
D = 0.42058             #[ft]
rho = 0.3611            #[lbm/in^3]
mu = 6.768*(10**-5)     #[lbm/in-s]
epsilon = 0.00015       #[ft]
g = 32.2                #[ft/s^2]


"""REYNOLDS NUMBER"""
D_in = D*12                 #[in] Diamter of pipe                   - Correct Conversion
V_dot_ft = V_dot*0.002228   #[ft^3/s] flow rate of water            - Correct Conversion
V_dot_in = V_dot_ft*1728    #[in^3/s] flow rate of water
Area_in = np.pi*(D_in/2)**2 #[in^2] cross sectional area of pipe
V_in = V_dot_in/Area_in     #[in/s] velocity of water
V = V_in*(1/12)             #[ft/s] velocity of water

Re = (rho*V_in*D_in)/mu

#Section Troubleshooting
print("Pipe Diamter",D_in,"in")
print("V_dot_ft",V_dot_ft,"ft^3/s")
print("V_dot_in",V_dot_in,"in^3/s")
print("Area",Area_in,"in^2")
print("Velocity inches",V_in,"in/s")
print("Velcoity feet",V,"ft/s")


"""FRICTION FACTOR"""
#Fluid is always turbulent

epD = epsilon/D  #epsilon/D
logdem = (epD/3.7)+(5.74/(Re**0.9))
dem = np.log10(logdem)**2

f = 0.25/dem

"""K Losses"""
#Entrance Losses
K_1 = 1000
K_inf = 0.5
K_ent = (K_1/Re)+K_inf*(1+(1/D))
#Elbow Losses - assuming threaded
K_1 = 800
K_inf = 0.4
K_e = (K_1/Re)+K_inf*(1+(1/D))
K_e = 3*K_e
#Exit Losses
K_1 = 800
K_inf = 0.4
K_ext = (K_1/Re)+K_inf*(1+(1/D))



Hp = Delta_Z+(f*(L/D)+K_ent+3*K_e+K_ext)*(V**2/(2*g))



plt.plot(V_dot,Hp)
plt.xlabel("Flow [gpm]")
plt.ylabel("Head of System")
plt.show()

print("Find sheet and complete problem")