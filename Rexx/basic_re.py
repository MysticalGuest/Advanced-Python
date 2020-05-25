import re

a = 'xy1x23'
# .的使用举例
b = re.findall('x..', a)
print(b)
# *的使用举例
c = re.findall('x*', a)
print(c)
# ?的使用举例
d = re.findall('x?', a)
print(d)
# .*的使用举例，贪心算法
secret_code = 'sdfejcakxxIxxasndfnfi124xxlovexx4956wewjxxyouxx6fyr'
e = re.findall('xx.*xx', secret_code)
print(e)
# .*?的使用举例
f = re.findall('xx.*?xx', secret_code)
print(f)

# 使用括号与不使用括号的区别
g = re.findall('xx(.*?)xx', secret_code)
print(g)
for each in g:
    print(each)

secret_hello = '''afijdsxxhello
xxdsfdfxxworldxxdsfdg'''

h = re.findall('xx(.*?)xx', secret_hello, re.S)
h1 = re.findall('xx(.*?)xx', secret_hello)
print(h)
# .好可以匹配任意字符，换行符除外
print(h1)

# findall和search的区别
s1 = 'sdksxxIxx123xxlovexxdir'
i = re.search('xx(.*?)xx123xx(.*?)xx', s1).group(1)
# group匹配括号
i1 = re.search('xx(.*?)xx123xx(.*?)xx', s1).group(2)
print(i, i1)
j = re.findall('xx(.*?)xx123xx(.*?)xx', s1)
print(j, j[0], j[0][1])

# sub的使用
s2 = '123fsfohncczxz123'
k = re.sub('123(.*?)123', '123789123', s2)
print(k)
k1 = re.sub('123(.*?)123', '123%d123'%789, s2)
print(k1)

# 匹配数字
s3 = 'afdsf1234567jgisodg555'
l = re.findall('(\d+)', s3)
print(l)
