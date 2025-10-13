import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_openml

anscombe = sns.load_dataset('anscombe')

# Lọc dữ liệu theo từng nhóm
group1 = anscombe[anscombe['dataset'] == 'I']
group2 = anscombe[anscombe['dataset'] == 'II']
group3 = anscombe[anscombe['dataset'] == 'III']
group4 = anscombe[anscombe['dataset'] == 'IV']

# Tạo lưới đồ thị 2x2
plt.figure(figsize=(10, 8))

# Đồ thị 1
plt.subplot(2, 2, 1)
plt.scatter(group1['x'], group1['y'], color='blue')
plt.title('Dataset I')
plt.xlabel('x1')
plt.ylabel('y1')

# Đồ thị 2
plt.subplot(2, 2, 2)
plt.scatter(group2['x'], group2['y'], color='green')
plt.title('Dataset II')
plt.xlabel('x2')
plt.ylabel('y2')

# Đồ thị 3
plt.subplot(2, 2, 3)
plt.scatter(group3['x'], group3['y'], color='red')
plt.title('Dataset III')
plt.xlabel('x3')
plt.ylabel('y3')

# Đồ thị 4
plt.subplot(2, 2, 4)
plt.scatter(group4['x'], group4['y'], color='purple')
plt.title('Dataset IV')
plt.xlabel('x4')
plt.ylabel('y4')

# Hiển thị đồ thị
plt.tight_layout()
plt.show()