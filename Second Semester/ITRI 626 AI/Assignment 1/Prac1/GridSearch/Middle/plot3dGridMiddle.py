import numpy as np
import matplotlib.pyplot as plt

stepX = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Middle\stepX.csv', delimiter=',')
iterY = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Middle\iterY.csv', delimiter=',')
errorZ = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Middle\errorZ.csv', delimiter=',')

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.scatter(stepX, iterY, errorZ, c = errorZ)
ax.set_title('Middle 1e-4 to 1e-2 (50), 20 000 to 100 000 (8)')
plt.show()

