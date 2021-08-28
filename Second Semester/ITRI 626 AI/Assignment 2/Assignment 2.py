weight = 0.5
goal_pred = 0.8
input = 0.5
minimum_error = 0.000001
error = 1
weight_delta = 0
delta = 0
count = 0

# old for loop:
# for iteration in range(20):

# used a while instead:
while error >= minimum_error:
    pred = input * weight
    error = (pred - goal_pred) ** 2

    # direction_and_amount = (pred - goal_pred) * input
    # weight = weight - direction_and_amount

    delta = pred - goal_pred
    
    #this is the derivative
    weight_delta = delta * input

    weight = weight - weight_delta
    count += 1

    print("Iteration:" + str(count) + " Error:" + str(error) + " Prediction:" + str(pred))

