import numpy as np
from prettytable import PrettyTable

# ' GIVENS
p = 3.2 * 0.001  # Plate Pitch [m]
t = 0.6 * 0.001  # Plate Thickness [m]
phi = 1.25  # Enlargement Factor [dim]
L_h = 248 * 0.001  # Plate Width [m]
D_p = 55 * 0.001  # Inlet Diameter [m]
m_dot = np.array([10.3,9.8])  # Mass Flow Rate of Fluids
N_t = 116  # Number of Plates in HX
N_p = 1  # Assumption from book
A_e = 0.32  # Effective Heat Transfer Area [m^2]

# ' Material Properties
eth = 0  # Index for ethanol
wat = 1  # Index for water
mu = np.array([1.04*(10**-5),0.00114])
rho = np.array([1.642,999.1])

# ' Pressure Drop in plates
L_w = L_h + D_p
b = p - t
D_hyd = (4 * b * L_w) /(2 *(b + phi * L_w))

N_cp = (N_t-1) / (2*N_p)
G_ch = m_dot / (N_cp * b * L_w)
Re = (G_ch * D_hyd) / mu

K_p = 3.008
m = 0.161
f = K_p / (Re ** m)

L_p = (phi * A_e) / L_w
L_v = L_p - D_p
PDelta_plate = f * ((L_v * N_p) / D_hyd) * ((G_ch ** 2) / (2 * rho))

# ' Table
table = PrettyTable()

table.field_names = ["Variable","Ethanol","Water","Units"]
table.add_row(["D_hyd",round(D_hyd,5),round(D_hyd,5),"m"])
table.add_row(["G_ch",G_ch.item(eth),G_ch.item(wat),"kg/m^2-s"])
table.add_row(["Reynolds Number",Re.item(eth),Re.item(wat),"dim"])
table.add_row(["f",f.item(eth),f.item(wat),"dim"])
table.add_row(["L_v",L_v,L_v,"m"])
table.add_row(["Plate Pressure Drop",PDelta_plate.item(eth)/1000,PDelta_plate.item(wat)/1000,"kPa"])

print(table)