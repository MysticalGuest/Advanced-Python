import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


chipo = pd.read_csv("Chipotle.tsv", sep="\t")

chipo_df1 = chipo.loc[:, ['quantity', 'item_name']].groupby("item_name").agg(sum)
chipo_df2 = chipo_df1.sort_values('quantity', ascending=False).head(15)

# 7.在item_name这一列中，一共有多少种商品被下单？
kind = chipo.loc[:, ['quantity', 'item_name']].groupby("item_name").count().index.shape  # 分组的方法
print("kind: ", kind)

arr1 = np.array(list(set(chipo.loc[:, 'item_name'])))   # 集合的方法
print("arr1.shape: \n", arr1.shape)

chipo.loc[:, 'item_name'].drop_duplicates().count()    # 去重的方法
# 8.一共有多少个商品被下单？
print("chipo.loc[:, 'quantity'].sum(): ", chipo.loc[:, 'quantity'].sum())

# 9.将item_price转换为浮点数
np1 = np.float16("$12345"[1:])
print("np1: ", np1)
np2 = np.float16("$45.365"[1:]).round(2)
print("np2: ", np2)
# chipo['item_price'] = np.float16(chipo['item_price'].str[1:])
# print("chipo['item_price']: \n", chipo['item_price'])

chipo['item_price'] = chipo['item_price'].str[1:].astype(float)   # 转换类型的方法
print("chipo['item_price']: \n", chipo['item_price'])

# print("np.float16(chipo['item_price'].str[1:]): \n", np.float16(chipo['item_price'].str[1:]))

# 10.在该数据集对应的时期内，收入(revenue)是多少？
chipo['total'] = chipo['item_price']*chipo['quantity']
print("chipo['total'].sum(): ", chipo['total'].sum())

# 11.在该数据集对应的时期内，一共有多少订单？
chipo.loc[:, 'order_id'].drop_duplicates().count()    # 去重的方法

print("chipo.loc[:, 'order_id'].unique().shape:\n", chipo.loc[:, 'order_id'].unique().shape)    # 去重方法4

# 12.每一单(order)对应的平均总价是多少？
chipo_df3 = chipo.loc[:, ['order_id', 'total']].groupby('order_id')['total'].mean()

# chipo.loc[chipo['order_id'] == 1,:]

# 13.将最多的前20个平均总价，进行绘图（折线图），并显示数据值。
chipo_df3.nsmallest(10)
chipo_df4 = chipo_df3.nlargest(15).sort_index()

x1 = chipo_df4.index
y1 = chipo_df4.values

print("x1[range(0,15,1)]: \n", x1[range(0, 15, 1)])

plt.rcParams['font.sans-serif'] = 'SimHei'
fig = plt.figure(figsize=(13, 6), dpi=80)

# 第2个图绘图开始
ax2 = fig.add_subplot(212)     # 声明第2个图的位置
p2, = ax2.plot(x1, y1, 'b--H')
plt.xticks([x for x in range(x1.min(), x1.max()+100, 150)])
for i in (range(len(x1))):
    if i % 2 == 0:
        ax2.annotate(xy=(x1[i]-3, y1[i]+2), s="单号:%d\n均值:%.2f" % (x1[i], y1[i]), fontsize=8, color='red')
    else:
        ax2.annotate(xy=(x1[i]-3, y1[i]+2), s="单号:%d\n均值:%.2f" % (x1[i], y1[i]), fontsize=8, color='green')

p1, = ax2.plot(chipo_df2.index, chipo_df2.values, 'r-.D')

# 对整个图形的处理
plt.legend([p1, p2], ['下单最多的前15个产品', '均值最大的前15个订单'], loc="upper right",
           bbox_to_anchor=(1, 2.2))     # 图例
plt.savefig('快餐数据图.png')    # 保存
plt.show()

