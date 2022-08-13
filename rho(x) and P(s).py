#!/usr/bin/env python
# coding: utf-8

# In[117]:


import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg as spalin
from scipy.optimize import curve_fit
from scipy import linalg
from scipy.special import factorial
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', size=16) 


# # GOE: Sample lots of $2 \times 2$ matrices

# # 1) $\rho(x)$ for a single large $N \times N$ matrix

# In[103]:


np.random.seed(1)
N= 1000 # size of matrix
niter = 1 # number of samples
evals = np.zeros((niter,N))
delta = np.zeros((niter,N-1))
for n in range(niter):
    M_temp = np.random.randn(N,N)
    M = (M_temp + M_temp.T)/2
    M = M/np.sqrt(N)
    evals[n,:] = linalg.eigvalsh(M)
    delta[n] = evals[n,1:]-evals[n,:-1]


# In[104]:


plt.figure(figsize=(10,8))
plt.hist(np.ravel(evals), bins=100, density=True)
plt.xlabel('Eigenvalues')
plt.title(r'$\rho(x)$ GOE, niter=$%d$, $%d \times %d$ matrices' %(niter,N,N))
plt.show()


# # 2A) $P(s)$ for many $2\times 2$ matrices [PLEASE ANIMATE]

# In[105]:


np.random.seed(1)
N= 2 # size of matrix
niter = 5000 # number of samples
evals = np.zeros((niter,N))
delta = np.zeros((niter,N-1))
for n in range(niter):
    M_temp = np.random.randn(N,N)
    M = (M_temp + M_temp.T)/2
    M = M/np.sqrt(N)
    evals[n,:] = linalg.eigvalsh(M)
    delta[n,:] = evals[n,1:]-evals[n,:-1]


# In[106]:


plt.figure(figsize=(8,8))
plt.hist(delta/np.mean(delta), bins=100, density=True) #The distribution is normalized so that the average level spacing is unity; Hence we are dividing by delta. This gets rid of any overall scales in the problem
s = np.linspace(0, 5,100)
GOE = 0.5*np.pi*s*np.exp(-0.25*np.pi*s*s)
plt.plot(s,GOE, 'r', lw=3)
plt.xlabel('s')
plt.title(r'$P(s)$ GOE, niter=$%d$, $%d \times %d$ matrices' %(niter,N,N))
plt.show()

# # 2B) $P(s)$ for single large $N\times N$ matrix [PLEASE ANIMATE]

# In[107]:


np.random.seed(1)
N= 5000 # size of matrix
niter = 1 # number of samples
evals = np.zeros((niter,N))
delta = np.zeros((niter,N-1))
for n in range(niter):
    M_temp = np.random.randn(N,N)
    M = (M_temp + M_temp.T)/2
    M = M/np.sqrt(N)
    evals[n,:] = linalg.eigvalsh(M)
    delta[n,:] = evals[n,1:]-evals[n,:-1]


# In[108]:


plt.figure(figsize=(8,8))
plt.hist(np.ravel(delta)/np.mean(delta), bins=100, density=True) #The distribution is normalized so that the average level spacing is unity; Hence we are dividing by delta. This gets rid of any overall scales in the problem
s = np.linspace(0, 5,100)
GOE = 0.5*np.pi*s*np.exp(-0.25*np.pi*s*s)
plt.plot(s,GOE, 'r', lw=3)
plt.xlabel('s')
plt.title(r'$P(s)$ GOE, niter=$%d$, $%d \times %d$ matrices' %(niter,N,N))
plt.show()

# # Poissonian (uncorrelated) eigenvalues

# # 1) $\rho(x)$ Poisson

# In[138]:


np.random.seed(1)
N=5000
niter = 100
evals = np.zeros((niter,N))
delta = np.zeros((niter,N-1))
for n in range(niter):
    evals[n,:]=np.sort(np.random.uniform(-N/2,N/2,N))
    delta[n,:] = evals[n,1:]-evals[n,0:-1]


# In[139]:


plt.figure(figsize=(10,8))
plt.hist(np.ravel(evals), bins=100, density=True)
plt.xlabel('Eigenvalues')
plt.title(r'$\rho(x)$ Poisson, niter=$%d$, $%d \times %d$ matrices' %(niter,N,N))


# # 2) $P(s)$ Poisson  [PLEASE ANIMATE]

# In[141]:


plt.figure(figsize=(8,8))
entries, bin_edges, patches=plt.hist(delta.ravel(), bins=100, density=True) #The distribution is normalized so that the average level spacing is unity; Hence we are dividing by delta. This gets rid of any overall scales in the problem
plt.xlabel('s')
plt.title(r'$P(s)$ Poissson, niter=$%d$ $N \times N$ matrix, $N=%d$' %(niter,N))
s = np.linspace(0, 5,100)
Ps = np.exp(-s)
plt.plot(s,Ps, 'r', lw=3)
plt.show()


# In[ ]:




