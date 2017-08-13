"""
Question B6
Plots the results of compute_reach stored in logfile.
You can customize the generation of the bins
"""

import time

import numpy as np
import matplotlib.pyplot as plt

####################
logfile = '/Users/louisabraham/Dropbox/Cours X/INF421/project/results/reach.log'
title = 'Repartition of the reaches across random vertices of france.in'
####################

# data input in seconds, we ignore the vertices
reach = np.genfromtxt(logfile, delimiter=',', dtype=int).transpose()[1] / 1000

# generation of the bins
bins = [reach.min(), 5, 10, 15, 30]
bins += [i * 60 for i in [1, 2, 3, 5, 10, 15]]
while bins[-1] < reach.max():
    bins.append(bins[-1] * 2)
Nbins = len(bins)

# generation of the labels (a bit hackish)
labels = [time.strftime('%H:%M:%S', time.gmtime(t))
          for t in bins]

# generation of the histogram
heights, bins = np.histogram(reach, bins)

####################
# First figure
####################
plt.title(title)
plt.ylabel('Number of vertices')
plt.xlabel('reach (hh:mm:ss)')

width = 0.4
ind = np.arange(Nbins - 1) + 0.5 - width / 2

bars = plt.bar(ind, heights, width, color='rg')

# we modify the x axis
plt.xticks(np.arange(Nbins), labels, rotation=45,
           rotation_mode="anchor", ha="right")
# we add some boxes
textbox = dict(facecolor='w')
for bar in bars:
    x = bar.get_x() + bar.get_width() / 2
    height = bar.get_height()
    percent = '%u\n%.00f%%' % (height, 100 * height / len(reach))
    plt.text(x, height / 2, percent, fontsize=10, ha='center', bbox=textbox)
# we adjust the bottom
plt.subplots_adjust(bottom=0.2)
plt.show()

####################
# Second figure
####################
plt.title(title)
plt.ylabel('Number of vertices')
plt.xlabel('reach (hh:mm:ss), log scale')

plt.hist(np.log2(reach + 1), bins='auto', color='wheat')

plt.xticks(np.log2(bins + 1), labels, rotation=45,
           rotation_mode="anchor", ha="right")
plt.subplots_adjust(bottom=0.2)
plt.show()
