#2、绘制雷达图，来表示商场中，每个月各商品的销售情况！
import  matplotlib.pyplot  as plt
import  numpy as np
np.random.seed(12)
# 男装：30-60
arr_nan = np.random.randint(30,60,size=(12,))
# 女装：20-85
arr_nv = np.random.randint(20,85,size=(12,))
# 餐饮：30-75
arr_can = np.random.randint(30,75,size=(12,))
# 化妆品：80-140
arr_hua = np.random.randint(80,140,size=(12,))
# 首饰：70-150
arr_shou = np.random.randint(70,150,size=(12,))
# 月份：1-12
arr_month = np.arange(1,13,1)

#画布
plt.figure(figsize=(12,6),dpi=80)

plt.rcParams['font.sans-serif'] = 'SimHei'    #正常显示汉字
plt.rcParams['axes.unicode_minus'] = False    #正常显示符号
#  .  ,  o   v  ^  s  *  D  d  x  <  >  h  H  1  2  3  4  _  |

data_len = len(list(arr_nan))
print("data_len: ", data_len)
# #将圆分成n等份
arr1_len = np.linspace(0,     #第1个数据
                       2*np.pi,    #最后1个数据
                       data_len,    #数据个数
                       endpoint=False)   #不包含终点


plt.polar(arr_month,arr_nan,'r-v')

#         arr_month,arr_nv,'b-.*',
#         arr_month,arr_can,'y--o',
plt.title("某商场各部门销售情况折线图")
plt.thetagrids(arr1_len*180/np.pi,[str(x)+"月" for x in list(arr_month)])

# 图例：

plt.legend(['男装',"女装","餐饮"])
# 显示数据
for i in range(12):
    plt.annotate(xy = (arr_month[i],arr_nan[i]+2),s=arr_nan[i])

plt.show()

