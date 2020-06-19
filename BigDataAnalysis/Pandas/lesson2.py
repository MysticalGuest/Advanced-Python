# 2.DataFrame的创建
import pandas as pd
import numpy as np


# 设置显示文本对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


# 2-1  方式1：用数组创建
df_v1 = pd.DataFrame(np.random.randint(10, 100, size=(10, 3)),
                     index=np.arange(0, 10, 1),
                     columns=['语文', '数学', "英语"])
print("df_v1的原始数据".ljust(30, "="), "\n")
print(df_v1)

# 2-2  方式2：用字典创建
df_dict = {"熟食": list(np.random.randint(10, 100, size=15)),
           "化妆品": list(np.random.randint(100, 200, size=15)),
           "日用品": list(np.random.randint(10, 100, size=15))}

df_v2 = pd.DataFrame(df_dict, index=pd.date_range(start="20200615",
                                                  end="20200629",
                                                  freq="D"))
print("df_v2的原始数据".ljust(30, "="), "\n")
print(df_v2)

