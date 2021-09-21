import numpy as np
np.random.seed(1)


def relu(x):
    return (x > 0) * x


def relu2deriv(output):
    return output > 0


streetlights = np.array( [[ 1, 0, 1 ], [ 0, 1, 1 ], [ 0, 0, 1 ], [ 1, 1, 1 ] ] )
walk_vs_stop = np.array([[ 1, 1, 0, 0]]).T


alpha = 0.2
hidden_size = 4
hidden_size_layer_3 = 6


weights_0_1 = 2 * np.random.random((3,hidden_size)) - 1
weights_1_2 = 2 * np.random.random((hidden_size,1)) - 1
weights_2_3 = 2 * np.random.random((1,hidden_size_layer_3)) - 1


for iteration in range(1024):

    layer_2_error = 0
    layer_3_error = 0

    for i in range(len(streetlights)):

        layer_0 = streetlights[i:i+1]
        layer_1 = relu(np.dot(layer_0,weights_0_1))
        layer_2 = relu(np.dot(layer_1,weights_1_2))
        layer_3 = np.dot(layer_2,weights_2_3)

        layer_2_error += np.sum((layer_2 - walk_vs_stop[i:i+1]) ** 2)
        layer_2_delta = (layer_2 - walk_vs_stop[i:i+1])

        layer_3_error += np.sum((layer_3 - walk_vs_stop[i:i+1]) ** 2)
        layer_3_delta = (layer_3 - walk_vs_stop[i:i+1])

        layer_1_delta = layer_2_delta.dot(weights_1_2.T)*relu2deriv(layer_1)

        weights_2_3 -= alpha * layer_2.T.dot(layer_3_delta)
        weights_1_2 -= alpha * layer_1.T.dot(layer_2_delta)
        weights_0_1 -= alpha * layer_0.T.dot(layer_1_delta)

    if(iteration % 10 == 9):
        print("Error:" + str(layer_3_error))
