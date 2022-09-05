# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
ip.editing_mode ='vi'
help(np.greater)
def hat(x):
    if isinstance(x, float):
        r = np.empty(1)
    else: 
        r = np.empty(x.shape)
    
lambda g 

def hat(x):
    if isinstance(x, float):
        r = np.empty(1)
    else: 
        r = np.empty(x.shape)
        for i in range(len(x)):
            if x
help(lambda)
get_ipython().run_line_magic('pinfo', 'lambda')
lambda
lambda g 

def hat(x):
    r = np.empty(x.shape)
def hat(x):
    r = np.empty(x.shape)
    for i in range(x.size):
        if x[i] <= -np.pi / 2 and x[i] > 0:
            r[i] = 1 + 2 * x[i] / np.pi
        elif x[i] >= 0 and x[i] < np.pi / 2:
            r[i] = 1 - 2 * x[i] / np.pi
        else:
            r[i] = 0
            
data = np.arange(0, np.pi + 0.0001, 0.0001)
dx = 0.0001
def hat(x):
    r = np.empty(x.shape)
    for i in range(x.size):
        if x[i] <= -np.pi / 2 and x[i] > 0:
            r[i] = 1 + 2 * x[i] / np.pi
        elif x[i] >= 0 and x[i] < np.pi / 2:
            r[i] = 1 - 2 * x[i] / np.pi
        else:
            r[i] = 0
    return r
    
plt.figure()
plt.plot(data, hat(data))
plt.show()
def hat(x):
    r = np.empty(x.shape)
    for i in range(x.size):
        if x[i] >= -np.pi / 2 and x[i] > 0:
            r[i] = 1 + 2 * x[i] / np.pi
        elif x[i] >= 0 and x[i] < np.pi / 2:
            r[i] = 1 - 2 * x[i] / np.pi
        else:
            r[i] = 0
    return r
    
plt.figure()
plt.plot(data, hat(data))
plt.show()
help(np.arange)
data = np.arange(-np.pi, np.pi + 0.0001, 0.0001)
plt.plot(data, hat(data))
plt.show()
len(data)
plt.show()
plt.plot(data, hat(data))
plt.show()
def hat(x):
    r = np.empty(x.shape)
    for i in range(x.size):
        if x[i] >= -np.pi / 2 and x[i] > 0:
            r[i] = 1 + 2 * x[i] / np.pi
        elif x[i] >= 0 and x[i] < np.pi / 2:
            r[i] = 1 - 2 * x[i] / np.pi
        else:
            r[i] = 0
    return r
    
plt.plot(data, hat(data))
plt.show()
def hat(x):
    r = np.empty(x.shape)
    for i in range(x.size):
        if x[i] >= -np.pi / 2 and x[i] < 0:
            r[i] = 1 + 2 * x[i] / np.pi
        elif x[i] >= 0 and x[i] < np.pi / 2:
            r[i] = 1 - 2 * x[i] / np.pi
        else:
            r[i] = 0
    return r
    
plt.plot(data, hat(data))
plt.show()
def hat(x):
    r = np.empty(x.shape)
    for i in range(x.size):
        if x[i] >= -np.pi / 2 and x[i] < 0:
            r[i] = 1 + 2 * x[i] ** 2/ np.pi
        elif x[i] >= 0 and x[i] < np.pi / 2:
            r[i] = 1 - 2 * x[i] ** 2 / np.pi
        else:
            r[i] = 0
    return r
    
plt.plot(data, hat(data))
plt.show()
a_0 = np.sum(hat(data)) * dx
ffs = a_0 / 2
ip = get_ipython()
ip.editing_mode ='vi'
