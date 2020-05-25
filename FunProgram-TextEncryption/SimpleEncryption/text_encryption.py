"""***************************************************************************

                                 text_encryption.py


***************************************************************************"""

# To run this program, start python and then type:
# from text_encryption import *
# code_message('flower.bmp', 'flower_out.bmp', 'secret.txt', 1, 2)
# decode_message('flower_out.bmp', 'secret_out.txt', 1, 2)


import sys


"""----------------------------------------------------------------------------

调用时，此函数以bmp格式接收图像文件。该函数以二进制格式打开文件用于只读。
bytearray（）函数转换read（）函数返回的整个文件放入字节数组。
该函数返回这个字节数组。
When called, this function receives the image file in bmp format.
The function opens the file in binary format for read-only. 
The bytearray() function converts the entire file returned by the read() function
into a byte array.
This function returns the byte array. """


def read_image_file(bmp_file):
    file = open(bmp_file, 'rb')
    by_image = bytearray(file.read())
    file.close()
    return by_image


"""----------------------------------------------------------------------------

调用时，此函数接受txt格式的文本文件，函数中遍历文件中每个字符，
将每个字符的ASCII编码存入code_list列表，此函数返回这个编码列表。
When called, this function accepts a text file in txt format. 
The function traverses each character in the file and stores
the ASCII code of each character in the code_list list.
This function returns the code list."""


def read_message_file(message_file):
    code_list = []
    file = open(message_file, 'r')
    text = file.read()
    flag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for letter in text:
        bin_list = []
        w = ord(letter)
        for i in range(8):
            bit = w & 0b00000001
            bin_list.append(bit)
            w = w >> 1
        bin_list.reverse()
        code_list.extend(bin_list)
    # 当记录信息编码存完了之后，加上终止标志
    # When the encoding of the value of the recorded information length is completed,
    # the termination flag is added
    code_list.extend(flag)
    return code_list


"""----------------------------------------------------------------------------

调用时，此函数接受一个存有ASCII编码信息的列表，一个存有bmp文件信息的字节数组，
p和q两个整型参数。函数将以add_text_bits(secret_code, by_image, p, q)的方式接受参数
把文本文件的信息以特定的形式存入字节数组。此函数返回这个字节数组。
When called, this function accepts a list of ASCII-encoded information,
a byte array containing bmp file information, and p and q integer parameters.
The function accepts the arguments in the form of
add_text_bits(secret_code, by_image, p, q) and
stores the text file information in a specific form into the byte array.
This function returns this byte array."""


def add_text_bits(code_list, by_image, p, q):
    for letter in code_list:
        by_image[54+p] = by_image[54+p] & 0b11111110
        by_image[54+p] = by_image[54+p] | letter
        p = p + q
    return by_image


"""----------------------------------------------------------------------------

调用时，此函数接受一个存有bmp文件信息的字节数组，和一个bmp格式的文件。
函数中以二进制格式打开这个文件用于读写，然后把字节数组中的信息写入bmp格式的文件并保存
它不返回值。
When called, this function accepts a byte array containing bmp file information,
and a bmp file. The function opens the file in binary format for reading and writing,
and then writes the information in the byte array to a file in bmp format and saves it.
It does not return a value."""


def save_image_file(by_image, bmp_outfile):
    file = open(bmp_outfile, 'wb')
    file.write(by_image)
    file.close()


"""----------------------------------------------------------------------------

调用时，此函数接受一个存有bmp文件信息的字节数组，p和q两个整型参数。
函数中将之前存在bmp文件中的ASCII编码信息提取出来，存在一个text_code列表中，
此函数返回这个text_code列表。
When called, this function accepts a byte array containing bmp file information,
p and q integer parameters. The function extracts the ASCII encoding information
from the bmp file that existed before, and there is a text_code list.
This function returns the text_code list."""


def extract_text_bits(by_image, p, q):
    flag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    text_code = []
    for i in range(16):
        bit = by_image[54 + p] & 0b00000001
        text_code.append(bit)
        p = p + q
    start = 0
    end = 16
    while text_code[start:end] != flag:
        bit = by_image[54+p] & 0b00000001
        text_code.append(bit)
        p = p+q
        start += 1
        end += 1
    text_code = text_code[0:-16]
    return text_code


"""----------------------------------------------------------------------------

调用时，此函数接受一个存有ASCII编码信息的列表。
函数按照规则将编码信息解码转化为文本信息存入text，此函数返回这个text。
When called, this function accepts a list of ASCII encoded information.
The function decodes the encoded information into text information according to the rules,
and the function returns the text."""


def assemble_text_bits(text_code):
    m = 0
    message = []
    for i in range(int(len(text_code)/8)):
        code_list = text_code[0+m:8+m]
        # text_code中的元素是int，join服务于字符串数组，所以我要把int型元素转为char
        # The elements in text_code are int, and the join serves arrays of strings,
        # so I want to convert int-type elements to char
        letter = " ".join('%s' % i for i in code_list)
        # 去掉字符串中的空格
        # Remove spaces in strings
        letter = letter.replace(" ", "")
        m += 8
        message.append(letter)
    text = bytes([int(x, 2) for x in message]).decode("utf-8")
    return text


"""----------------------------------------------------------------------------

调用时，此函数接受一个txt格式的文本文件，一个之前解码好的文本信息。
函数中以二进制格式打开这个文件用于读写，然后把文本信息写入txt格式的文件并保存
它不返回值。
When called, this function accepts a text file in txt format,
a previously decoded text message. Open this file in binary format for reading and writing,
then write the text information to a file in txt format and save it.
It does not return a value."""


def save_message_file(message_outfile, text):
    file = open(message_outfile, 'w', encoding='UTF-8')
    if file.write(text):
        print("Success!")
    file.close()


"""----------------------------------------------------------------------------

调用时，此函数接受一个bmp格式的图像文件，一个将作为存入文本信息的bmp格式的文件，
一个txt格式的文本文件，p和q两个整型参数。函数会调用之前定义好的四个方法，分别是：
read_image_file(bmp_infile)方法，
read_message_file(message_file)方法，
add_text_bits(secret_code, by_image, p, q)方法， 
save_image_file(after_encode_image, bmp_outfile)方法，
将文本信息编码存入bmp格式的图像文件中。
它不返回值。
When called, this function accepts an image file in bmp format,
a file in bmp format that stores text information, a text file in txt format,
and two integer parameters p and q. 
The function will call the four methods defined before:
read_image_file(bmp_infile) method,
read_message_file(message_file) method,
add_text_bits(secret_code, by_image, p, q) method,
save_image_file(after_encode_image, bmp_outfile) method,
encoding text information. Save it in an image file in bmp format.
It does not return a value."""


def code_message(bmp_infile, bmp_outfile, message_file, p, q):
    by_image = read_image_file(bmp_infile)
    secret_code = read_message_file(message_file)
    after_encode_image = add_text_bits(secret_code, by_image, p, q)
    save_image_file(after_encode_image, bmp_outfile)


"""----------------------------------------------------------------------------

调用时，此函数接受一个已经存入文本信息的bmp格式的图像文件，一个将作为写入文本的txt格式的文件，
p和q两个整型参数。函数会调用之前定义好的四个方法，分别是：
read_image_file(bmp_infile)方法，
extract_text_bits(by_image, p, q)方法，
assemble_text_bits(text_code)方法，
save_message_file(message_outfile, 
after_decode_text)方法，
将存入文本信息的bmp格式的图像文件解码写入txt格式的文本文件中。
它不返回值。
When called, this function accepts an image file in bmp format that has
been saved with text information, a file in txt format that will be written as text,
and two integer parameters p and q. The function will call the four methods defined before:
read_image_file(bmp_infile) method,
extract_text_bits(by_image, p, q) method,
assemble_text_bits(text_code) method,
save_message_file(message_outfile, after_decode_text) method,
which will store the text information.
The image file in bmp format is decoded and written into a text file in txt format.
It does not return a value."""


def decode_message(bmp_infile, message_outfile, p, q):
    by_image = read_image_file(bmp_infile)
    text_code = extract_text_bits(by_image, p, q)
    after_decode_text = assemble_text_bits(text_code)
    save_message_file(message_outfile, after_decode_text)


# code_message('flower.bmp', 'flower_out.bmp', 'secret.txt', 1, 2)
# decode_message('flower_out.bmp', 'secret_out.txt', 1, 2)

"""----------------------------------------------------------------------------

Allow the program to be run from the command line. Assuming your filename is
text_encryption.py:

To CODE message in a .bmp:
python text_encryption.py code flower.bmp flower_out.bmp secret.txt 1 2

To DECODE message in a .bmp, call it like this:
python text_encryption.py decode flower_out.bmp secret_out.txt 1 2

"""


if __name__ == '__main__':

    try:

        if len(sys.argv) == 7 and sys.argv[1] == 'code':
            # code
            code_message(sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6]))

        elif len(sys.argv) == 6 and sys.argv[1] == 'decode':
            # decode
            decode_message(sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]))

        else:
            print('Usage:')
            print('python a1234567890.py code flower.bmp ', end='')
            print('flower2.bmp msg.txt 1 2')
            print('python a1234567890.py decode flower2.bmp msg2.txt 1 2')
    except():
        print('Usage:')
        print('python a1234567890.py code flower.bmp ', end='')
        print('flower2.bmp msg.txt 1 2')
        print('python a1234567890.py decode flower2.bmp msg2.txt 1 2')
