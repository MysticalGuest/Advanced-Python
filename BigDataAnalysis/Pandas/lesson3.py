# 3.导入来自本地磁盘的数据
# 3-1  导入csv和txt文件
import pandas as pd


df_v3 = pd.read_csv("meal_order_detail1.csv", sep=",", encoding="utf-8")
print("df_v3的原始数据".ljust(30, "="), "\n")
print(df_v3)

df_v4 = pd.read_csv("meal_order_detail1.csv", sep=",", encoding="utf-8")
print("df_v4的原始数据".ljust(30, "="), "\n")
print(df_v4)
# 3-2  导入excel文件
print("df_v5的原始数据".ljust(30, "="), "\n")
df_v5 = pd.read_excel("超市营业额.xlsx", sheet_name=1)
print(df_v5)

