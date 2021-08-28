import numpy as np
import matplotlib.pyplot as plt

stepX = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Full\stepX.csv', delimiter=',')
iterY = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Full\iterY.csv', delimiter=',')
errorZ = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Full\errorZ.csv', delimiter=',')

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.scatter(stepX, iterY, errorZ, c = errorZ)
ax.set_title('Full Filter (0.3) 1e-6 to 1e-1 (75), 1 to 100 000 (75)')
plt.show()
