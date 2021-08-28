from time import time
import random
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def hot_and_cold_learning(step_amount, number_of_iterations): # Do not modify the function name

    # step_amount = 1.2245760262582417e-05 # Choose a step_amount here between 1e-6 and 1e-1
    # number_of_iterations = 99998 # Choose the number of iterations between 1 and 100000

    ### Do not modify the code from here ###

    weight = 0.25
    input = 0.75
    goal_prediction = 1.0

    for iteration in range(number_of_iterations):

        prediction = input * weight
        error = (prediction - goal_prediction) ** 2
        #print("Error:" + str(error) + " Prediction:" + str(prediction))
        up_prediction = input * (weight + step_amount)
        up_error = (goal_prediction - up_prediction) ** 2
        down_prediction = input * (weight - step_amount)
        down_error = (goal_prediction - down_prediction) ** 2

        if(down_error < up_error):
            weight = weight - step_amount
        if(down_error > up_error):
            weight = weight + step_amount

    return abs(prediction - goal_prediction)

    ### Do not modify the code to here ###

#print(hot_and_cold_learning())

# set the starting time and the number of seconds it will optimize for
startTime = time()
endTime = startTime + 600
# set hyper paramater search space
stepTop = 1e-3
stepBottom = 1e-6
iterationsTop = 100000
iterationsBottom = 1
bestError = 1
bestStep = 0
bestIter = 0
# logging the attempts for plotting
stepX = np.array([])
iterY = np.array([])
errorZ = np.array([])
# pick a random set of hyperparameters
# perform hot_and_cold_learning and record the error
# keep doing this randomly till you run out of time
while (time() < endTime):
    print(time() - startTime)
    step = random.uniform(stepBottom, stepTop)
    iterations = random.randint(iterationsBottom, iterationsTop)
    error = hot_and_cold_learning(step, iterations)
    if error < 0.005:
        stepX = np.append(stepX,step)
        iterY = np.append(iterY,iterations)
        errorZ = np.append(errorZ,error)
    if error < bestError:
        bestStep = step
        bestIter = iterations
        bestError = error

# output the best hyperParameters found
print("Results - Step")
print(bestStep)
print("Results - Iterations")
print(bestIter)
print("Results - Error")
print(bestError)

# save to csv file
np.savetxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\RandomSearch\stepX.csv', stepX, delimiter=',')
np.savetxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\RandomSearch\iterY.csv', iterY, delimiter=',')
np.savetxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\RandomSearch\errorZ.csv', errorZ, delimiter=',')


#fig = plt.figure()
#ax = plt.axes(projection='3d')

#surf = ax.plot_trisurf(stepX, iterY, errorZ, linewidth=0, antialiased=False)
#ax.plot_surface(stepX, iterY, errorZ,cmap='viridis', edgecolor='none')
#ax.set_title('Surface plot')
#plt.show()
