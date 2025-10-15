import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde 
# Đọc dữ liệu mtcars từ file
mtcars = pd.read_csv('mtcars.csv') 
# Tạo dữ liệu ngẫu nhiên giống R
np.random.seed(0)
x = np.random.normal(size=500) 
# Tạo layout 1 hàng, 2 cột
fig, axes = plt.subplots(1, 2, figsize=(12, 6)) 
# Đồ thị 1: Bandwidth lớn
density_big_bw = gaussian_kde(x, bw_method=20 / np.std(x))  # bw = 20
x_vals = np.linspace(min(x) - 50, max(x) + 50, 1000)
axes[0].plot(x_vals, density_big_bw(x_vals), color='red', linewidth=2)
axes[0].set_title("Too big bandwidth", fontsize=14, fontweight='bold', pad=20)
axes[0].set_xlabel("x", fontsize=12)
axes[0].set_ylabel("Density", fontsize=12)
axes[0].set_xlim(-60, 60)
axes[0].set_ylim(0, 0.02)
axes[0].text(0.5, -0.15, "N = 500    Bandwidth = 20", ha='center', fontsize=10, transform=axes[0].transAxes) 
# Đồ thị 2: Bandwidth nhỏ
density_small_bw = gaussian_kde(x, bw_method=0.05 / np.std(x))  # bw = 0.05
axes[1].plot(x_vals, density_small_bw(x_vals), color='red', linewidth=2)
axes[1].set_title("Too small bandwidth", fontsize=14, fontweight='bold', pad=20)
axes[1].set_xlabel("x", fontsize=12)
axes[1].set_ylabel("Density", fontsize=12)
axes[1].set_xlim(-3, 3)
axes[1].set_ylim(0, 0.5)
axes[1].text(0.5, -0.15, "N = 500    Bandwidth = 0.05", ha='center', fontsize=10, transform=axes[1].transAxes)
# Hiển thị đồ thị
plt.tight_layout()
plt.show()