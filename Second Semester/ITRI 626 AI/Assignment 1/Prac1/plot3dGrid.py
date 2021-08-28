import numpy as np
import matplotlib.pyplot as plt

stepX = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\stepX.csv', delimiter=',')
iterY = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\iterY.csv', delimiter=',')
errorZ = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\errorZ.csv', delimiter=',')

fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.set_zlim([0,0.3])
# surf = ax.plot_trisurf(stepX, iterY, errorZ, linewidth=0, antialiased=False)
surf = ax.scatter(stepX, iterY, errorZ, c = errorZ)
ax.set_title('Surface plot')
plt.show()