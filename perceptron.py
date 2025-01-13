import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

def perceptron(X, y, learning_rate=0.1, epochs=100):
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0

    for _ in range(epochs):
        for i in range(n_samples):
            linear_output = np.dot(X[i], weights) + bias
            predicted = 1 if linear_output >= 0 else -1
            if predicted != y[i]:
                weights += learning_rate * y[i] * X[i]
                bias += learning_rate * y[i]

    return weights, bias

def plot_perceptron_boundary(X, y, weights, bias):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', s=100)  # Data points with color map
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = np.dot(np.c_[xx.ravel(), yy.ravel()], weights) + bias
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='black')  # Decision boundary color
    plt.title('Perceptron Decision Boundary', fontsize=14)
    plt.xlabel('Feature 1', fontsize=12)
    plt.ylabel('Feature 2', fontsize=12)
    plt.show()

def train_xor_nn(X, y):
    model = MLPClassifier(hidden_layer_sizes=(2,), max_iter=10000, activation='relu', solver='adam')
    model.fit(X, y)
    return model

def visualize_xor_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', s=100)  # Data points with color map
    plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='black')  # Decision boundary color
    plt.title('XOR Problem Decision Boundary', fontsize=14)
    plt.xlabel('Feature 1', fontsize=12)
    plt.ylabel('Feature 2', fontsize=12)
    plt.show()

# Example for Perceptron with AND gate
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([-1, -1, -1, 1])

weights, bias = perceptron(X_and, y_and, learning_rate=0.1, epochs=100)
plot_perceptron_boundary(X_and, y_and, weights, bias)

# Example for XOR with XOR dataset
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

xor_model = train_xor_nn(X_xor, y_xor)
visualize_xor_boundary(xor_model, X_xor, y_xor)
