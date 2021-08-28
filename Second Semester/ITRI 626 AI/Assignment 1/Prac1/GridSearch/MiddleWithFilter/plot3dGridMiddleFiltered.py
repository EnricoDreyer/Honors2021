import numpy as np
import matplotlib.pyplot as plt

stepX = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\MiddleWithFilter\stepX.csv', delimiter=',')
iterY = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\MiddleWithFilter\iterY.csv', delimiter=',')
errorZ = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\MiddleWithFilter\errorZ.csv', delimiter=',')

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.scatter(stepX, iterY, errorZ, c = errorZ)
ax.set_title('Middle Filtered (0.05) 1e-4 to 1e-2 (25), 1 000 to 20 000 (19)')
plt.show()


