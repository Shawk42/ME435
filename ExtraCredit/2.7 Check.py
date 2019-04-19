#Present value required at start of retirement [at age 65 this should be the present value of the account]
n = 30*12

i = 0.04


AtoP = ((1+i)**n-1)/(i*(1+i)**n)

P_retire = AtoP*2000

print(2000*n)
print(P_retire)


