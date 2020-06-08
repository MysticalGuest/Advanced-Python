# 异常处理1 ：常用的异常结构
while True:
    try:
        age = int(input("请输入年龄"))
        break
    except ValueError:
        print("请输入数值")
        continue


# 异常处理2：只能捕获给出的异常（完整的异常结构)
while True:
    try:
        height = float(input("请输入身高(M)"))
        weight = float(input("请输入体重(kg)"))
        if height == 0.1:
            break
        bmi = round((weight/(height*height)),2)
    except ValueError:
        print("请输入数值")
        continue
    except ZeroDivisionError:
        print("除数不能为0")
        continue
    else:
        print("您的bmi指标是：", bmi)
        break
    finally:
        print("再来一次！")


# 异常处理3：except后面没有错误名称，也就是什么异常都可以捕获
while True:
    try:
        height = float(input("请输入身高(M)"))
        weight = float(input("请输入体重(kg)"))
        if height == 0.1:
            break
        bmi = round((weight/(height*height)), 2)
    except:
        print("您输入的有误！")
        continue
    else:
        print("您的bmi指标是：", bmi)
        break
    finally:
        print("再来一次！")

