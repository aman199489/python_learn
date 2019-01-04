'''
#数字运算

注意
1. / 除法总会返回一个浮点数, 用// 返回整数部分
2. 不同类型的数混合运算时会将整数转换为浮点数
3. 交互模式下，直接运算为赋值时，如：
    >>> a, b = 1, 2
    >>> a * b
   默认赋值给变量 _
    >>> print(_)
'''



'''
#字符串

注意
1. 交互模式下，可使用 \ 续行，说明下一行是上一行的延续
2. 字符串可以被三个双引号或者三个单引号括起来, 换行符不需要转义, 它们会包含在字符串中
3. r" " 使用"原始"字符串，那么 \n 不会被转换成换行，行末的的反斜杠，以及源码中的换行符，都将作为数据包含在字符串内。
4. 字符串可以用 + 串联, * 重复
'''



# 列表
list_a = [1, 2, 3, 'Yu', 'Na'];
print(list_a, type(list_a), len(list_a));
list_a.append(2 ** 3);     # append()方法末尾添加新元素
print(list_a, type(list_a), len(list_a));
list_a[1:3] = [];   # 移除列表元素
print(list_a, type(list_a), len(list_a));
list_a[:] = [];     # 清空列表
print(list_a, type(list_a), len(list_a));
list_b = ['chencahoqun', 'yinxiaogang', 'yinshuguo'];
list_a = [1, 2, 3, list_b];     # 列表中嵌套其它列表
print(list_a, type(list_a), len(list_a));
print("\n=========================================\n");



'''
#
'''
