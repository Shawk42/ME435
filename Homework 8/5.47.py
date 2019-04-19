print("Problem 5.47")
import numpy as np
from CoolProp.CoolProp import PropsSI

"""GIVENS"""
#Hot Fluid Properties
t_i = 80+273.15             #Hot inlet temp [K]
m_doth = 1                  #[kg/s]

#Cold Fluid Properties
T_i = 50+237.15             #Cold intlet temp [K]
m_dotc = 0.9                #[kg/s]

"""PART A"""
#Incomplete