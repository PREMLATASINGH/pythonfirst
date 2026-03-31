from sklearn.tree import DecisionTreeClassifier

# Features: [weight, smoothness, color_code]
# smoothness: 1 = smooth, 0 = bumpy
# color_code: 0=green, 1=yellow, 2=orange, 3=red, 4=purple

X = [
    # Apples
    [150, 1, 3],   # apple
    [160, 1, 3],   # apple
    [170, 1, 3],   # apple

    # Oranges
    [130, 0, 2],   # orange
    [140, 0, 2],   # orange
    [150, 0, 2],   # orange

    # Bananas
    [120, 1, 1],   # banana
    [110, 1, 1],   # banana
    [100, 1, 1],   # banana

    # Grapes
    [5, 1, 4],     # grape
    [6, 1, 4],     # grape
    [7, 1, 4],     # grape
]

# Labels:
# 0 = Apple, 1 = Orange, 2 = Banana, 3 = Grape
y = [
    0, 0, 0,   # apples
    1, 1, 1,   # oranges
    2, 2, 2,   # bananas
    3, 3, 3    # grapes
]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Test fruit example
test = [[145, 0, 2]]  # weight=145, bumpy, orange color
prediction = model.predict(test)[0]

fruit_names = ["Apple", "Orange", "Banana", "Grape"]
print("Prediction:", fruit_names[prediction])