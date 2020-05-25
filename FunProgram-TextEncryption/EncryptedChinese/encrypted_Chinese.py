import re

flag = '011110'


# 将文件放入图像中
def code_message( bmp_infile, bmp_outfile, message_file, p, q):
    img_list = read_image_file(bmp_infile)
    message = process_message(read_message_file(message_file))
    message_str = ''.join(message)
    start = 1000 + p

    for i in message_str:
        img_list[start] = img_list[start] ^ int(i)
        start += q
    with open('out.bmp', 'wb') as f:
        f.write(img_list)
    return len(message_str)
    pass


# 将文字从图像中解码出来
def decode_message( bmp_infile, message_outfile, p, q):
    img_inmsg = read_image_file('it_building.bmp')
    msg_length = (code_message('it_building.bmp', '', 'start.txt', 1, 8))
    img_outmsg = read_image_file(bmp_infile)
    message_lists = []
    start = 1000 + p
    for i in range(msg_length):
        s = img_inmsg[start] ^ img_outmsg[start]
        start += q
        message_lists.append(s)
    # print(message_lists)
    # a = ''.join(message_lists)
    # a = list(map(str, a))
    # a = ''.join(a)
    # print(message_lists)
    a = message_lists
    a = list(map(str, a))
    a = ''.join(a)
    b = re.sub(flag, '0b', a)
    c = re.sub("1110", '111', b)
    print(c)
    m = c.split('0b')[1:]
    print(m)
    results = [int(x,2) for x in m]
    results = [chr(x) for x in results]
    print(results)
    with open(message_outfile ,'w',encoding='utf-8') as f:
        f.write(''.join(results))
    pass


# 读取图像
def read_image_file(bmp_infile):
    with open(bmp_infile, 'rb') as f:
        a = bytearray(f.read())
    return a


# 读取文字信息
def read_message_file(message_file):
    with open(message_file, 'r', encoding='utf-8') as f:
        s = f.read()
    return list(s)


# 让文字变成二进制，然后进行透明处理,返回一个数组
def process_message(message_list):
    pro_lists = []
    for i in message_list:
        # print(type(i))
        # s = re.sub('0b', flag, (bin(i)))
        if not isinstance(i,str):
            i = str(i)
        print(i)
        s = re.sub('0b', flag, pro_number(bin(ord(i))))
        # print(s)
        # s = list(s)
        # print(s)
        # s = list(map(int , s))
        pro_lists.append(s)
    # pro_lists = ''.join(pro_lists)
    # print(pro_lists)
    # pro_lists = list(map(int , list(pro_lists)))
    # print(pro_lists)
    return pro_lists
    pass


# 透明处理
def pro_number(s):
    num = 0
    s = list(s)
    for i, j in enumerate(s):
        if j == '1':
            num += 1
            if num == 3:
                s.insert(i+1, '0')
                num = 0
        if j == '0':
            num = 0
    return ''.join(s)
# pro_number('11101000')


# process_message(read_image_file('start.txt'))
# print(process_message(read_message_file('start.txt')))
# (code_message('it_building.bmp', '' ,message_file= 'start.txt' ,p=1 , q=8))
decode_message('out.bmp', 'result.txt', 1, 8)

