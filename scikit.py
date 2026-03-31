from sklearn.linear_model import LinearRegression

# Hardcoded training data
# Features: [size in square feet]
X = [
    [500],
    [800],
    [1000],
    [1200],
]

# Target: price in thousands
y = [100, 150, 180, 200]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict price of a 900 sq ft house
test = [[900]]
prediction = model.predict(test)

print("Predicted price:", prediction[0])