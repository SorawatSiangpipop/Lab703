# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:23:41 2019

@author: Omen
"""

#from scipy import *
import matplotlib.pyplot as plt
import numpy as np
#import math
# if using a Jupyter notebook, includes:
#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'
#%plt.rcParams['figure.fisize']=(6,3)
#%plt.rcParams['figure.dpi']=150

#from ipywidgets import interact, interactive, fixed, interact_manual
#import ipywidgets as widgets

def hw1(f, a):
    
    t = np.arange(0, 2, 0.01)
    y1 = np.cos(2*np.pi*f*t)
    y2 = np.exp(-a*t)
    y3 = y1*y2
    
    fig, ax = plt.subplots(1,3)
    fig.set_size_inches(15,3)
    
    plt.sca(ax[0])
    plt.plot(t, y1)
    
    plt.sca(ax[1])
    plt.plot(t, y2)
    
    plt.sca(ax[2])
    plt.plot(t, y3)
    
"""
#interactive
interact(hw1, f=(1,10), a=(0,10))
"""    