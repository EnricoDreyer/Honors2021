import numpy as np 

def hot_and_cold_learning(): # Do not modify the function name

    step_amount = 0.15555 # Choose a step_amount here between 1e-6 and 1e-1
    number_of_iterations = 8 # Choose the number of iterations between 1 and 100000

    ### Do not modify the code from here ###

    weight = 0.25
    input = 0.75
    goal_prediction = 1.0

    for iteration in range(number_of_iterations):

        prediction = input * weight
        error = (prediction - goal_prediction) ** 2
        # derivative = 2 * (prediction - goal_prediction)
        # print(derivative)
        print("Error:" + str(error) + " Prediction:" + str(prediction))
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

print(hot_and_cold_learning())