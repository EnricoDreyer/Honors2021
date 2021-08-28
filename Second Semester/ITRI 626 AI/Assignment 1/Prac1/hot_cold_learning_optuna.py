import optuna

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

def objective(trial):
    step = trial.suggest_float("step", 1e-6, 1e-1)
    iter = trial.suggest_int("iter", 1, 100000)
    return hot_and_cold_learning(step, iter)

study = optuna.create_study()
study.optimize(objective, n_trials=100)

print(study.best_params)

#[I 2021-08-19 11:13:38,754] Trial 999 finished with value: 0.00010062703022151176 and parameters: {'step': 0.004552384465155281, 'iter': 47503}. Best is trial 404 with value: 2.4485952976327496e-07.        
#{'step': 3.308899388555665e-05, 'iter': 92375}