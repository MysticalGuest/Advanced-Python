# 3.导入来自本地磁盘的数据
# 3-1  导入csv和txt文件
import pandas as pd
import numpy as np


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

# 4.写数据到本地磁盘文件
# 4-1写数据到csv中
df_dict = {"熟食": list(np.random.randint(10, 100, size=15)),
           "化妆品": list(np.random.randint(100, 200, size=15)),
           "日用品": list(np.random.randint(10, 100, size=15))}

df_v2 = pd.DataFrame(df_dict, index=pd.date_range(start="20200615",
                                                  end="20200629",
                                                  freq="D"))

df_v2.to_csv("market_data.csv", sep=",", encoding="gbk")

# 4-2写数据到excel中
df_v2.to_excel("excel_data.xlsx")