import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0.1, 0.6],
              [0.15, 0.71],
              [0.25, 0.8],
              [0.35, 0.45],
              [0.5, 0.5],
              [0.6, 0.2],
              [0.65, 0.3],
              [0.8, 0.35]])
y = np.array([[1], [1], [1], [1], [0], [0], [0], [0]])

def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(1)
    W1 = np.random.randn(input_size, hidden_size) * 0.01
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size) * 0.01
    b2 = np.zeros((1, output_size))
    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}
    return parameters

def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))

def forward_propagation(X, parameters):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    
    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache

def compute_loss(y_true, y_pred):
    m = y_true.shape[0]
    loss = -(1/m) * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

def backward_propagation(X, y, parameters, cache):
    m = X.shape[0]
    W1 = parameters["W1"]
    W2 = parameters["W2"]
    A1 = cache["A1"]
    A2 = cache["A2"]
    
    dZ2 = A2 - y
    dW2 = (1/m) * np.dot(A1.T, dZ2)
    db2 = (1/m) * np.sum(dZ2, axis=0, keepdims=True)
    
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * (1 - np.tanh(cache["Z1"])**2)
    dW1 = (1/m) * np.dot(X.T, dZ1)
    db1 = (1/m) * np.sum(dZ1, axis=0, keepdims=True)
    
    gradients = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return gradients

def update_parameters(parameters, gradients, learning_rate):
    W1 = parameters["W1"] - learning_rate * gradients["dW1"]
    b1 = parameters["b1"] - learning_rate * gradients["db1"]
    W2 = parameters["W2"] - learning_rate * gradients["dW2"]
    b2 = parameters["b2"] - learning_rate * gradients["db2"]
    
    updated_parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}
    return updated_parameters

def train_network(X, y, hidden_size, learning_rate, epochs):
    input_size = X.shape[1]
    output_size = 1
    parameters = initialize_parameters(input_size, hidden_size, output_size)
    loss_values = []
    
    for epoch in range(epochs):
        A2, cache = forward_propagation(X, parameters)
        loss = compute_loss(y, A2)
        loss_values.append(loss)
        
        gradients = backward_propagation(X, y, parameters, cache)
        parameters = update_parameters(parameters, gradients, learning_rate)
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss}")
    
    return parameters, loss_values

def plot_decision_boundary(X, y, parameters):
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    Z, _ = forward_propagation(np.c_[xx.ravel(), yy.ravel()], parameters)
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, levels=[0, 0.5, 1], alpha=0.8, cmap=plt.cm.RdYlBu)
    plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), cmap=plt.cm.RdYlBu, edgecolors='k', s=50)
    plt.title("Decision Boundary")
    plt.show()

hidden_size = 4
learning_rate = 0.1
epochs = 1000
parameters, loss_values = train_network(X, y, hidden_size, learning_rate, epochs)

plt.plot(loss_values)
plt.title("Loss over Epochs")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()

plot_decision_boundary(X, y, parameters)
