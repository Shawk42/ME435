import numpy as np
import matplotlib.pyplot as plt

"""PROBLEM 4.32"""

C_2 = 0.09  #$/kW-hr
t = 260*12   #Op time in hours


rho = 48.541
D = 0.05
mu = 2.2741
ep = 0.00015
dev = 10000000
V_dot = 2.228009
b = 0.02
s = 1.14
C_1 = 22.50
i = 0.20
n = 50
crf = (i*(1+i)**n)/(((1+i)**n)-1)
F = 6.9
yr = 2012
n_p = 0.68

while dev >= 0.00001:
    Area = np.pi*(D/2)**2
    V = V_dot/Area
    Re = (rho*V*D)/mu
    if Re <= 2300:
        #print("Laminar")
        f = 64/Re
    elif Re > 2300:
        #print("Turblent")
        q = ((ep/D)/3.7)+(5.74/(Re**0.9))
        f = 0.25/np.log10(q)**2
    m_dot = rho*V_dot
    num = 40*C_2*t*f*(m_dot**3)
    dem = s*(crf+b)*(1+F)*((1+0.015)**(yr-1980))*C_1*n_p*np.pi**2*rho**2
    D_econ = num/dem
    dev = abs(D_econ-D)
    D = D+0.00001
    print(D,"|",D_econ)
    if D> 1:
            break

print("No solution found")
print("C_2",C_2)
print("t",t)
print("f",f)
print("m_dot",m_dot)
print("s",s)
print("crf",crf)
print("b",b)
print("F",F)
print("C_1",C_1)
print("n_p",n_p)
print("rho",rho)
