print("Problem 5.51")
import numpy as np


"""GIVENS"""
#All units of temperature is F
T_i = 96
T_o = 82
t_i = 49
t_o = 83

"""PART A Solution"""

Delt_out =abs(T_o-t_o)
DelT_in = T_i-t_i
#print(DelT_in)
#print(Delt_out)
LMTD_num = Delt_out-DelT_in
LMTD_dem = np.log(Delt_out/DelT_in)
LMTD = LMTD_num/LMTD_dem


"""PART B Solution"""
R = (T_i-T_o)/(t_o-t_i)
P = (t_o-t_i)/(T_i-t_i)


F_num = np.sqrt(R**2+1)*np.log((1-P)/(1-P*R))

F_lognum = 2-P*(R+1-np.sqrt(R**2+1))
F_logdem = 2-P*(R+1+np.sqrt(R**2+1))
F_log = F_lognum/F_logdem

F_dem = (R-1)*np.log(F_log)

F = F_num/F_dem

print(""*50)
print("Comments on HX preformance")
print("-"*50)
if F > 1:
    print("F is greater than 1")
elif F == 1:
    print("HX is at max preformance")
elif F <= 0.75:
    print("HX is operating poorly and may be unprofitable")
else:
    print("HX is within normal parameters")

"""SOLUTION PRINTING"""
print("")
print("Solution")
print(""*50)
print("Part A - LMTD = ",round(LMTD,2),"F")
print("Part A - F =",round(F,3))
print("See above for comment on HX preformance")

print("-"*50)
print("Further comments on HX preformacne")
print("With a F value of",round(F,3),"being relatively close to the mininum cutoff of 0.75, the HX is economical but not by much")