import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


B = np.array([])
G = np.array([])
R = np.array([])
im = cv2.imread(fi)

b = im[:,:,0]
b = b.reshape(b.shape[0]*b.shape[1])
g = im[:,:,1]
g = g.reshape(g.shape[0]*g.shape[1])
r = im[:,:,2]
r = r.reshape(r.shape[0]*r.shape[1])
B = np.append(B,b)
G = np.append(G,g)
R = np.append(R,r)

nbins = 10
plt.hist2d(B, G, bins=nbins, norm=LogNorm())
plt.xlabel('B')
plt.ylabel('G')
plt.xlim([0,255])
plt.ylim([0,255])


