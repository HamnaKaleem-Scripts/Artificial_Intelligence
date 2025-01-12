def calculate_mean(values):
    return sum(values) / len(values)

def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = 0
    denominator = 0
    for i in range(len(X)):
        diff_X = X[i] - mean_X
        diff_Y = Y[i] - mean_Y
        numerator += diff_X * diff_Y
        denominator += diff_X ** 2
    return numerator / denominator

def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X

def predict(X, intercept, slope):
    predictions = []
    for x in X:
        y_pred = intercept + slope * x
        predictions.append(y_pred)
    return predictions

def calculate_mse(Y, Y_pred):
    total_error = 0
    for i in range(len(Y)):
        error = (Y[i] - Y_pred[i]) ** 2
        total_error += error
    mse = total_error / len(Y)
    return mse

def fit_linear_regression(X, Y):
    avg_X = sum(X) / len(X)
    avg_Y = sum(Y) / len(Y)
    top = 0
    bottom = 0
    for i in range(len(X)):
        top += (X[i] - avg_X) * (Y[i] - avg_Y)
        bottom += (X[i] - avg_X) ** 2
    slope = top / bottom
    intercept = avg_Y - slope * avg_X
    return intercept, slope

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 7, 8]
mean_X = calculate_mean(X)
mean_Y = calculate_mean(Y)
slope = calculate_slope(X, Y, mean_X, mean_Y)
intercept = calculate_intercept(mean_X, mean_Y, slope)
Y_pred = predict(X, intercept, slope)
mse = calculate_mse(Y, Y_pred)
# Y_pred = predict(X, intercept, slope)
# print(f"Predicted values: {Y_pred}")
print(f"Slope: {slope}, Intercept: {intercept}, MSE: {mse}")
X2 = [10, 20, 30, 40, 50]
Y2 = [12, 24, 30, 40, 48]

Y_pred1 = predict(X, intercept, slope)
mse1 = calculate_mse(Y, Y_pred1)

Y_pred2 = predict(X2, intercept, slope)
mse2 = calculate_mse(Y2, Y_pred2)

print(f"MSE for Dataset 1: {mse1}")
print(f"MSE for Dataset 2: {mse2}")
