import numpy as np
import matplotlib.pyplot as plt

stepX = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Bottom\stepX.csv', delimiter=',')
iterY = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Bottom\iterY.csv', delimiter=',')
errorZ = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\Bottom\errorZ.csv', delimiter=',')

fig = plt.figure()
ax = plt.axes(projection='3d')

surf = ax.scatter(stepX, iterY, errorZ, c = errorZ)
ax.set_title('Bottom End 1e-6 to 1e-4 (25), 1 000 to 100 000 (40)')
plt.show()
