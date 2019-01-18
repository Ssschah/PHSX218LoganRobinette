
# coding: utf-8

# In[33]:


import numpy as np
def rule3(errA,errB):
    errQ = np.sqrt(errA**2 + errB**2)
    return errQ
errT_i = 0.3 #C
errT_f = 0.1 #C

err_Delta_T = rule3(errT_i, errT_f)
#print (err_Delta_T)
def rule4(Q,m,errA,A,n,errB,B,p,errC,C):
    errQ = Q*np.sqrt((m*(errA/A))**2 +(n*(errB/B))**2 +(p*(errC/C))**2)
    return errQ
alpha = 0.00125*(1.05**(-1))*((92.5-23.4)**(-1))
print ("alpha",alpha)
L=1.05 #m
delta_L=0.001 #m
err_Delta_L=0.00001 #m
Delta_L=0.00125 #m
T_i=23.4 #C
T_f=92.5 #C
delta_T=0.2 #C
T=69.1 #C
m=1
n=-1
p=-1


err_alpha = rule4(alpha,m,err_Delta_L,Delta_L,n,delta_L,L,p,delta_T,T)
print ("err_Alpha",err_alpha)


# Logan Robinette, Jan 17, 2019, Synthetic Data Thermal Expansion: Week 1 Lab

# $ \alpha = \Delta L  L^{-1}  \Delta T^{-1} $

# $ \delta \alpha = \alpha \sqrt{\frac{err\Delta L}{\Delta L}^{2} + \frac{-errL}{L}^{2} + \frac{-err \Delta T}{T}^{2}}$
