# -*- coding: utf-8 -*-
"""
Simple program that creates a high resolution photon picture
for use in publications


@author: Levi Smith - June 2015
"""
import math
import numpy as np
import matplotlib.pyplot as plt

## User-specifiec parameters
N_osc = 4                # Number of non-decaying oscillations
N_decay = 3              # Number of decaying oscillations
alpha_decay = np.pi/6    # Rate of decay for oscillations
photon_color = 'black'   # Photon color
transparent_fig = True   # Figure background transparency?
arrow_thickness = 6      # Line thickness

### ARROW SECTIONS ###
t_end = (N_osc+N_decay)*2*np.pi

# Decaying start section
t_decay_start = np.linspace(0,N_decay*2*np.pi,1000)
y_decay_start = np.exp(-alpha_decay*t_decay_start)*(-1*np.sin(t_decay_start))

# Oscilatting section
t_osc = np.linspace(0,N_osc*2*math.pi,1000)
y_osc = (np.sin(t_osc))

# Decaying end section
t_decay_end = np.linspace(0,N_decay*2*np.pi,1000)
y_decay_end = np.exp(-alpha_decay*t_decay_end)*(np.sin(t_decay_end))

### Time shifts ###
t_decay_end_plot = t_decay_end+N_osc*2*math.pi
t_decay_start_plot = -1*t_decay_start

# Plotting
plt.plot(t_decay_start_plot,y_decay_start,color=photon_color,linewidth=arrow_thickness)
plt.plot(t_osc,y_osc,color=photon_color,linewidth=arrow_thickness)
plt.plot(t_decay_end_plot,y_decay_end,color=photon_color,linewidth=arrow_thickness)
plt.axis('off')
plt.ylim(-1.1, 1.1)
plt.xlim(-N_decay*2*np.pi, t_end*1.05)

# Arrow head
plt.annotate("",
            xy=(t_end*1.05, 0), xycoords='data',
            xytext=(t_end*0.9, 0), textcoords='data',
            arrowprops=dict(color=photon_color,width=arrow_thickness,frac=1,headwidth=25)
            )

# Save the figure
plt.savefig(photon_color + '_photon.png', format='png', dpi=800, transparent=transparent_fig)