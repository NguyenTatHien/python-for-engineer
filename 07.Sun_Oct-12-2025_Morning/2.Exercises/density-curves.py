import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde 
# Tạo dữ liệu x
np.random.seed(42)
x = np.random.normal(size=500) 
# Tạo dữ liệu y
np.random.seed(2)
y = np.random.normal(size=500) + 1
 
# Tính mật độ cho x
density_x = gaussian_kde(x) 
# Tính mật độ cho y
density_y = gaussian_kde(y) 
# Tạo lưới giá trị x để vẽ mật độ
x_grid = np.linspace(min(min(x), min(y)), max(max(x), max(y)), 1000) 
# Vẽ đồ thị
plt.figure(figsize=(8, 6))
plt.plot(x_grid, density_x(x_grid), color='red', linewidth=2, label='Density of x')
plt.plot(x_grid, density_y(x_grid), color='blue', linewidth=2, label='Density of y')
plt.title("Multiple curves", fontsize=16)
plt.xlabel("", fontsize=12)
plt.legend()
plt.show()