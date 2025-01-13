
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def cross_entropy_loss(y_true, y_pred):

    y_pred = np.clip(y_pred, 1e-10, 1 - 1e-10)
    loss = 0
    for i in range(len(y_true)):
        if y_true[i] == 1:
            loss -= np.log(y_pred[i])
        else:
            loss -= np.log(1 - y_pred[i])
    return loss / len(y_true)


def gradient_descent(X, y, weights, learning_rate, iterations):

    for i in range(iterations):
        predictions = sigmoid(np.dot(X, weights))
        error = predictions - y
        gradient = np.dot(X.T, error) / len(y)
        weights -= learning_rate * gradient 

    return weights


def predict(X, weights):
    probabilities = sigmoid(np.dot(X, weights))
    return (probabilities >= 0.5).astype(int)

def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    X = np.c_[np.ones(X.shape[0]), X] 
    weights = np.zeros(X.shape[1])
    weights = gradient_descent(X, y, weights, learning_rate, iterations)
    return weights

def evaluate(y_true, y_pred):
    return np.mean(y_true == y_pred)

def plot_decision_boundary(X, y, weights):
    x1 = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    x2 = -(weights[0] + weights[1] * x1) / weights[2]
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.plot(x1, x2, color='red')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Decision Boundary')
    plt.show()

data = np.array([
    [0.1, 1.1, 0],
    [1.2, 0.9, 0],
    [1.5, 1.6, 1],
    [2.0, 1.8, 1],
    [2.5, 2.1, 1],
    [0.5, 1.5, 0],
    [1.8, 2.3, 1],
    [0.2, 0.7, 0],
    [1.9, 1.4, 1],
    [0.8, 0.6, 0]
])
X, y = data[:, :2], data[:, 2]

X = (X - X.mean(axis=0)) / X.std(axis=0)

weights = logistic_regression(X, y, learning_rate=0.01, iterations=1000)

predictions = predict(np.c_[np.ones(X.shape[0]), X], weights)
accuracy = evaluate(y, predictions)
loss = cross_entropy_loss(y, sigmoid(np.dot(np.c_[np.ones(X.shape[0]), X], weights)))

print("Accuracy:", accuracy)
print("Loss:", loss)

plot_decision_boundary(X, y, weights)


