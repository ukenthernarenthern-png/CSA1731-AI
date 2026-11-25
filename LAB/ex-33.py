"""Fit a simple linear regression model with gradient descent."""

def fit_line(x_values, y_values, learning_rate=0.01, epochs=10000):
    slope = 0.0
    intercept = 0.0
    n = len(x_values)
    for _ in range(epochs):
        slope_gradient = sum(2 * x * (slope * x + intercept - y)
                             for x, y in zip(x_values, y_values)) / n
        intercept_gradient = sum(2 * (slope * x + intercept - y)
                                 for x, y in zip(x_values, y_values)) / n
        slope -= learning_rate * slope_gradient
        intercept -= learning_rate * intercept_gradient
    return slope, intercept

if __name__ == "__main__":
    x = [1, 2, 3, 4]
    y = [3, 5, 7, 9]
    slope, intercept = fit_line(x, y)
    prediction = slope * 5 + intercept
    print(f"Model: y = {slope:.2f}x + {intercept:.2f}")
    print(f"Prediction for x=5: {prediction:.2f}")
