import numpy as np
import matplotlib.pyplot as plt

stepX = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\RandomSearch\stepX.csv', delimiter=',')
iterY = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\RandomSearch\iterY.csv', delimiter=',')
errorZ = np.loadtxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\RandomSearch\errorZ.csv', delimiter=',')

fig = plt.figure()
ax = plt.axes(projection='3d')
#surf = ax.plot_trisurf(stepX, iterY, errorZ, linewidth=0, antialiased=False)
surf = ax.scatter(stepX, iterY, errorZ)
ax.set_title('Random (600) Filter (0.005) 1e-6 to 1e-3, 1 to 100 000')
plt.show()



#endTime = startTime + 600
#stepTop = 1e-1
#stepBottom = 1e-3
#iterationsTop = 50000
#iterationsBottom = 1
#Results - Step
#0.009420287539460722
#Results - Iterations
#41158
#Results - Error
#1.9972151599212395e-07



#startTime = time()
#endTime = startTime + 600
# set hyper paramater search space
#stepTop = 1e-3
#stepBottom = 1e-6
#iterationsTop = 100000
#iterationsBottom = 1
#Results - Step
#0.0002165800476936186
#Results - Iterations
#36829
#Results - Error
#4.892267457812238e-08
