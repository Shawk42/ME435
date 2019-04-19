import numpy as np
import matplotlib.pyplot as plt

R = (T_i-T_o)/(t_o-t_i)
P = (t_o-t_i)/(T_i-t_i)


F_num = np.sqrt(R**2+1)*np.log((1-P)/(1-P*R))

F_lognum = 2-P*(R+1-np.sqrt(R**2+1))
F_logdem = 2-P*(R+1+np.sqrt(R**2+1))
F_log = F_lognum/F_logdem

F_dem = (R-1)*np.log(F_log)

F = F_num/F_dem