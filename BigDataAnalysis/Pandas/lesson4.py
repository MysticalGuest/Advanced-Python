# 4.写数据到本地磁盘文件
import pandas as pd
import numpy as np

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

