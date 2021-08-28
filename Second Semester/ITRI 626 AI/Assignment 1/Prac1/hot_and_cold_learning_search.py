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

# set hyper paramater search space
# step size
start = 1e-6
stop = 1e-1
numberOfSteps = 75
increment = (stop - start)/numberOfSteps
steps = np.arange(start, stop, increment)
# iterations
start = 1
stop = 100000
numberOfSteps = 75
increment = round((stop - start)/numberOfSteps)
iterations = np.arange(start, stop, increment)

# variables to track the best and worst performing parameters
bestError = 1
bestStep = 0
bestIter = 0
maxError = 0
maxStep = 0
maxIter = 0

# logging the attempts for plotting
stepX = np.array([])
iterY = np.array([])
errorZ = np.array([])

# loop over both lists to try each point in a grid search
for step in steps:
    print(step)
    for iter in iterations:
        error = hot_and_cold_learning(step, iter)
        # filter to only plot results below 0.05 error
        if error < 0.3:
            stepX = np.append(stepX,step)
            iterY = np.append(iterY,iter)
            errorZ = np.append(errorZ,error)
        if error < bestError:
            bestStep = step
            bestIter = iter
            bestError = error
        if error > maxError:
            maxStep = step
            maxIter = iter
            maxError = error

# output the best hyperParameters found
print("Results - Step")
print(bestStep)
print("Results - Iterations")
print(bestIter)
print("Results - Error")
print(bestError)

print("Results - MaxStep")
print(maxStep)
print("Results - MaxIterations")
print(maxIter)
print("Results - MaxError")
print(maxError)

# save to csv file
np.savetxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\stepX.csv', stepX, delimiter=',')
np.savetxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\iterY.csv', iterY, delimiter=',')
np.savetxt(r'C:\Users\29892287\Dropbox\Projects\StateMachinePrac\spikes\ITRI626\GridSearch\errorZ.csv', errorZ, delimiter=',')
