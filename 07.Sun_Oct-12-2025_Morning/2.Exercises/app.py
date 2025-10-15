import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2.Đọc file mtcars.csv
df = pd.read_csv("mtcars.csv")
# Hiển thị 5 dòng đầu tiên
print(df.head())

## 3.Phân tích dữ liệu
## - Mô tả dữ liệu:
print(df.describe())

## - Lọc dữ liệu:
filtered_df = df[df['mpg'] > 20]
print(filtered_df)

sns.scatterplot(data=df, x='mpg', y='hp')
plt.title("MPG vs Horsepower")
plt.show()