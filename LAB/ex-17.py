"""Feed-forward neural network with one hidden layer and sigmoid units."""
from math import exp

def sigmoid(value):
    return 1 / (1 + exp(-value))

def feed_forward(inputs, hidden_weights, hidden_bias, output_weights, output_bias):
    hidden = [sigmoid(sum(x*w for x,w in zip(inputs,row)) + bias)
              for row,bias in zip(hidden_weights, hidden_bias)]
    outputs = [sigmoid(sum(h*w for h,w in zip(hidden,row)) + bias)
               for row,bias in zip(output_weights, output_bias)]
    return hidden, outputs

if __name__ == "__main__":
    x = [1.0, 0.0]
    w_hidden = [[0.5, -0.4], [0.3, 0.8]]
    b_hidden = [0.1, -0.2]
    w_output = [[0.7, -1.2], [1.1, 0.4]]
    b_output = [0.2, -0.1]
    hidden, output = feed_forward(x, w_hidden, b_hidden, w_output, b_output)
    print("Hidden activations:", [round(v, 4) for v in hidden])
    print("Output activations:", [round(v, 4) for v in output])
