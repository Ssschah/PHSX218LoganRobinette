
# coding: utf-8

# In[3]:


#Copper#
#Length 
cu_length_i = 0.70000 #m
cu_length_f = 0.70083 #m
cu_dial_i = 0.00 #mm
cu_dial_f = 0.830 #mm

#Resistance 
cu_r_i = 124.2 #kohm
# error = 124.0 - 124.4 kohm
cu_r_f = 8.24 #kohm
# error = 8.24 - 8.50 #kohm

#Temperature
cu_temp_i = 24.50 #C
cu_temp_f = 87.84 #C
#error range = 87.84 - 86.91 #C


#Aluminum#
#Length 
al_length_i = 0.70000 #m
al_length_f = 0.70170 #m
al_dial_i = 0.00 #mm
al_dial_f = 1.17 #mm

#Resistance 
al_r_i = 124.2 #kohm
#124.1 - 124.3 #kohm
#al_r_f = 8.16 #kohm
#error range = 8.16 - 8.44 #kohm

#Temperature
al_temp_i = 24.32 #C
al_temp_f = 88.13 #C
#error_range_i = 24.32 - 24.50 #C
#error_range_f = 88.13 - 87.48 #C

def d_l(length_i, length_f):
    d_l = length_f - length_i
    return d_l

def d_t(temp_f, temp_i):
    d_t = temp_f - temp_i
    return d_t

Cu_dl = d_l(cu_length_i, cu_length_f)
Cu_dt = d_t(cu_temp_f, cu_temp_i)
Al_dl = d_l(al_length_i, al_length_f)
Al_dt = d_t(al_temp_f, al_temp_i)

def linear_expansion(d_L, L, d_T):
    coefficient = d_L / (L*d_T)
    return coefficient

    
Copper = linear_expansion(Cu_dl, cu_length_f, Cu_dt)
print("Alpha Copper =", Copper)

Aluminum = linear_expansion(Al_dl, al_length_f, Al_dt)
print("Alpha Aluminum =", Aluminum)


# In[23]:


import numpy as np
errT_iAL = 0.65 #C
errT_fAL = 0.65 #C
errT_iCu = 0.93 #C
errT_fCu = 0.93 #C
def rule3(errA,errB):
    errQ=np.sqrt(errA**2 + errB**2)
    return errQ
errAl = rule3(errT_iAL, errT_fAL)
errCu = rule3(errT_iCu, errT_fCu)
print ("Error in Delta_T, Aluminum =", errAl, "deg C")
print ("Error in Delta_T, Copper =", errCu, "deg C")


# In[22]:


def rule4(errA,errB,errC,A,B,C,a,b,c,Q):
    errQ= Q* np.sqrt(((a*errA)/A)**2 +((b*errB)/B)**2 +((c*errC)/C)**2)
    return errQ

D_L = 0.00117 #m
errD_L = 4e-5 #m
L = 0.7 #m
errL = 0.005 #m
D_T = 88.13-21.66 #C
errD_T = 0.919 #C

def alpha(A,B,C):
    a = A*B**(-1)*C**(-1)
    return a
alpha = alpha(D_L,L,D_T)
print("Alpha, Aluminum =", alpha)

err_alpha= rule4(errD_L,errL,errD_T,D_L,L,D_T,1,-1,-1,alpha)
print ("Error in Alpha, Aluminum =", err_alpha)


# In[21]:


def rule4(errA,errB,errC,A,B,C,a,b,c,Q):
    errQ= Q* np.sqrt(((a*errA)/A)**2 +((b*errB)/B)**2 +((c*errC)/C)**2)
    return errQ

D_L = 8.3e-4 #m
errD_L = 1e-5 #m
L = 0.7 #m
errL = 0.005 #m
D_T = 87.84-21.66 #C
errD_T = 1.32 #C

def alpha(A,B,C):
    a = A*B**(-1)*C**(-1)
    return a
alpha = alpha(D_L,L,D_T)
print("Alpha, Copper =", alpha)

err_alpha= rule4(errD_L,errL,errD_T,D_L,L,D_T,1,-1,-1,alpha)
print ("Error in Alpha, Copper =", err_alpha)

