import math
import random

def calculate_entropy(data, target_col):
    total = len(data)
    counts = {}
    for row in data:
        label = row[target_col]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    entropy = 0
    for count in counts.values():
        prob = count / total
        entropy += -prob * math.log2(prob)
    return entropy

def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    values = set(row[attribute] for row in data)
    weighted_entropy = 0
    for value in values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * calculate_entropy(subset, target_col)
    return total_entropy - weighted_entropy

import pandas as pd

def build_tree(data, attributes, target_col):
    df = pd.DataFrame(data)
    if len(df[target_col].unique()) == 1:
        return df[target_col].iloc[0]
    if not attributes:
        return df[target_col].mode()[0]
    best_attr = None
    max_gain = -1
    for attr in attributes:
        gain = calculate_information_gain(data, attr, target_col)
        if gain > max_gain:
            max_gain = gain
            best_attr = attr
    tree = {best_attr: {}}
    for value in df[best_attr].unique():
        subset = df[df[best_attr] == value].to_dict(orient='records')
        remaining_attributes = [attr for attr in attributes if attr != best_attr]
        tree[best_attr][value] = build_tree(subset, remaining_attributes, target_col)
    return tree


def predict(tree, data_point):
    if isinstance(tree, dict):
        attribute = list(tree.keys())[0]
        value = data_point[attribute]
        return predict(tree[attribute][value], data_point)
    else:
        return tree

def build_random_forest(data, attributes, target_col, n_trees=2):
    forest = []
    for _ in range(n_trees):
        sampled_data = random.choices(data, k=len(data))
        tree = build_tree(sampled_data, attributes, target_col)
        print(f"Tree {_ + 1}:")
        print(tree) 
        forest.append(tree)
    return forest

data = [
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Sunny', 'Temperature': 'Mild', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Hot', 'Play?': 'No'}
]

tree = build_tree(data, ['Weather', 'Temperature'], 'Play?')
print("Decision Tree:")
print(tree)

new_data_point = {'Weather': 'Sunny', 'Temperature': 'Mild'}
predicted_class = predict(tree, new_data_point)
print(f"Predicted class for {new_data_point}: {predicted_class}")

random_forest = build_random_forest(data, ['Weather', 'Temperature'], 'Play?', 2)
predictions = [predict(tree, new_data_point) for tree in random_forest]
print(f"Predictions from Random Forest for {new_data_point}: {predictions}")

