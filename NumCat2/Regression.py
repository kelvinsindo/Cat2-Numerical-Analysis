import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data 
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 3, 5, 7, 11])

# Reshape the data to fit the model 
x_data = x_data.reshape(-1, 1)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x_data, y_data)

# Get the slope (coefficient) and intercept of the fitted line
slope = model.coef_[0]
intercept = model.intercept_

print(f'Slope (coefficient): {slope}')
print(f'Intercept: {intercept}')

# Predict y values based on the model
y_pred = model.predict(x_data)

# Plot the original data points
plt.scatter(x_data, y_data, color='blue', label='Data points')

# Plot the fitted line
plt.plot(x_data, y_pred, color='red', label='Fitted line')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
