mydict = {}
mydict['one'] = "1 - 菜鸟教程"
mydict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(mydict['one'])  # 输出键为 'one' 的值
print(mydict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

a = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(a)