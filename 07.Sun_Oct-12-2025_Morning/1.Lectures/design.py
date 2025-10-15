import numpy as np
import matplotlib.pyplot as plt
# Average monthly temperatures in London
T1 = np.array([5.6, 5.8, 7.9, 10.5, 13.7, 16.8, 19.1, 18.7, 15.9, 12.3, 8.4, 5.9], dtype=float)
T2 = np.array([19.7, 20.6, 21.6, 23.7, 25.7, 27.4, 28.3, 28.4, 27.8, 26.1, 23.2, 21.3], dtype=float)
T3 = np.array([-8.4, -5.9, -3.4, 3.1, 8.9, 13.3, 15.3, 14.2, 9.6, 2.4, -4.7, -7.1], dtype=float)
# Diagram title
plt.title('Average Monthly Temperatures in London')
# Add months on the X axis
plt.xticks((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# Add label to Y axis
plt.ylabel('Temperature')
# Plot the temperatures
plt.plot(T, marker='s')
# Display values on the diagram
for i in range(0, 6):
    plt.text(i-0.3, T[i]+0.3, str(T[i]))
for i in range(6, 12):
    plt.text(i, T[i]+0.2, str(T[i]))
# Visualise the chart
plt.show()