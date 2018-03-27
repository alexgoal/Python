import sys;

x = 'runoob';
sys.stdout.write(x + '\n')
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y)
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    ...  # 注意前一行 'end' 的使用 ...
    print(repr(x * x * x).rjust(4))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

str = input("请输入：");
print ("你输入的内容是: ", str)
