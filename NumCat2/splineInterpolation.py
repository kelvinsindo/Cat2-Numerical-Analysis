import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Sample data
x_data = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_data = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Create the cubic spline
cs = CubicSpline(x_data, y_data)

# Evaluate the spline at some points
x_new = np.linspace(2, 10.6, 100)
y_new = cs(x_new)

# Plot the data and the spline
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_new, y_new, label='Cubic Spline', color='red')
plt.legend()
plt.show()
