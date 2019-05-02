import numpy as np

"""
GIVENS:
A 15% Magnesium chloride solution is being pumped through a 5 nom sch 40 commercial steel pipe.
It has the additional properties listed under givens.

FIND:
Convective heat transfer coefficient in the pipe
"""

# ' GIVENS
m_dot = 3250  # [lbm/hr]
T_avg = 10  # [F]

# ' TABLE VALUES
mu = 13.614  # [lbm/ft-hr]
rho = 70.951  # [lbm/ft^3]
D = 0.42058  # [ft]
Pr = 32.492  # [dim]
k = 0.29514  # [Btu/hr-ft-R]

# ' SOLUTION
V_dot = m_dot / rho
Area = np.pi*(D/2)**2
V = V_dot / Area
Re = (rho * V * D) / mu

if Re >= 2300:
    print("Flow is Turbulent")
    f = "null"
else:
    print("Flow is laminar")
    f = Re/64

Nu = ((f / 8) * (Re - 100) * Pr)  \
     / (1 + 12.7 * ((f / 8) ** 0.5) * ((Pr ** (2 / 3)) - 1))

h = (k * Nu) / D

print("Heat Transfer Coeff",round(h,2),"[Btu/hr-R]")


