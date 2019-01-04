
#单行注释
'''
多行注释
'''
"""
多行注释
"""



#默认情况下，python3源码文件是utf-8编码，可以认为指定不同的编码如下：
#   _*_ coding: utf-8 _*_


#python保留字，当前版本的所有关键字
print("输出当前版本的所有关键字\n");
import keyword;
print(keyword.kwlist);
print("\n----------------------------------------------\n");



#斐波那契数列
#两个元素的总和确定了下一个数
print("斐波那契数列\n");
#复合赋值
a,b = 0,1;
while b < 10 :
    print(b);
    #复合赋值
    a,b = b,a + b;
print("\n----------------------------------------------\n");



a,b = 0,1;
while b < 1000 :
    #关键字end可以被用于防止输出新的一行，或者在输出的末尾添加不同的字符
    print(b, end = ',');
    a, b = b, a + b;
print("\n----------------------------------------------\n");



'''
python中的变量不需要声明
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建

***变量所指内存中的数据类型:***
* Numbers数字
    - int
    - float
    - bool
    - complex复数
* String字符串
    - str
* List列表
* Tuple元组
* Sets集合
* Dictionaries字典

#String, List, Tuple都属于sequence(序列)
'''
print("内置的type()函数查询变量所指的对象类型\n");
a, b, c, d = 20, 5.5, True, 4 + 3j;
print(type(a), type(b), type(c), type(d));
print("\n----------------------------------------------\n");



#   len()函数输出字符串长度
#   \ 转义特殊字符
s = "hello world\'";
print(s, type(s), len(s));
print("\n----------------------------------------------\n");

#不想让 \ 发生转义，在字符串前添加一个r，表示原始字符串
print(r"hello world\'");
print("\n----------------------------------------------\n");

#字符串可以使用 + 运算符连接在一起， 或者用 * 运算符重复
print("hello" * 3, "liu" + "zhun");
print("\n----------------------------------------------\n");

#没有单独的字符类型， 一个字符就是长度为 1 的字符串
word = "Python";
# word字符串可以看做是***特殊的元组***，不可修改
print(word[0], word[5]);
# 可以从 -1 倒着数，可以从 0 开始正着数
print(word[-1], word[-6]);

print(word[1:5]);
print(word[:]);
print(word[3:]);
print(word[:6]);
print("\n----------------------------------------------\n");



#列表中元素的类型可以不同
list_a = ['ILoveYou', 12, 52.1,'her'];
print(list_a);
list_b = ['Love', 'You'];
# + 操作符串联
list_a += list_b;
print(list_a);
# 与字符串不一样，列表中的元素是可以改变的
list_a[0] = "shit";
print(list_a);
list_a[1:3] = ["it", "is", "test"];
print(list_a);
list_a[1:5] = [];
print(list_a);
print("\n----------------------------------------------\n");



# 元组与列表类似，但元组的元素不能修改
tuple_a = (1994, 8, 9, 'Yu', "Tao");
print(tuple_a, type(tuple_a), len(tuple_a));
#构造包含 0 个或 1 个元素的 Tuple 是个特殊的问题
tuple_b = ();   #空元组
tuple_c = (20, );   #一个元素，需要在元素后添加逗号
tuple_a += tuple_c;
# + 操作符串联
print(tuple_a, type(tuple_a), len(tuple_a));
print("\n----------------------------------------------\n");



# Sets是一个无序无重复元素的集
set_a = set();  # set() 创建一个空set
print(set_a, type(set_a), len(set_a));
# 重复的元素自动去掉
set_b = {'Jim', 'Jack', 'Mary', 'Mary', 'Jim', 'Rose', 'Lose'};
print(set_b, type(set_b), len(set_b));
set_c = {'Jim', 'Rose', 'liuzhun', 'YuYao', 'Tim'};
print(set_b - set_c);   # - 差集
print(set_b | set_c);   # | 并集
print(set_b & set_c);   # & 交集
print(set_b ^ set_c);   # ^ set_a和set_b中不同时存在的元素
print("\n----------------------------------------------\n");



# 字典，映射类型，无序的键 : 值对集合
# 键必须是不可变类型，且不可重复，所以list和tuple不能做键
dic_a = {};    #创建空字典
dic_b = {'Jack':19940809, 'Tim':'19900110', 'Rose':'19800103'};
print(dic_b, type(dic_b), len(dic_b));

print(dic_b['Jack']);   #通过 key 进行查询

del dic_b['Rose'];  # 删除键值对
print(dic_b, type(dic_b), len(dic_b));

dic_b['Baobao'] = 20181228;    # 添加键值对
print(dic_b, type(dic_b), len(dic_b));

list_key = list(dic_b.keys());  # 返回所有key组成的list
list_key = sorted(list_key);
print(list_key, type(list_key), len(list_key));

if 'Baobao' in dic_b:
    print(True);
print("\n----------------------------------------------\n");


'''
运算符
* 算术运算符
* 比较运算符
* 赋值运算符
* 位运算符
* 逻辑运算符
* 成员运算符
* 身份运算符

# 各种运算符有优先级
'''

#算术运算符
print("算术运算符\n");
a,b = 2,3;
c = a + b   # +
print("a + b 的值 c 为:", c);
c = a - b   # -
print("a - b 的值 c 为:", c);
c = a * b   # *
print("a * b 的值 c 为:", c);
c = a / b   # / 除
print("a / b 的值 c 为:", c);
c = a % b   # % 取模，返回除法的余数
print("a % b 的值 c 为:", c);
c = a ** b  # ** 幂，返回 a 的 b 次幂
print("a ** b 的值 c 为:", c);
c = a // b  # // 取整除，返回商的整数部分
print("a // b 的值 c 为:", c);
print("\n----------------------------------------------\n");

#比较运算符
print("比较运算符\n");
a,b,c = 0,1,2;
if a == b:  # ==
    print("a 等于 b");
else:
    print("a 不等于 b");

if (a != b):    # !=
    print("a 不等于 b");
else:
    print("a 等于 b");

if (a < b):     # <
    print("a 小于 b");
else:
    print("a 大于 b");

if (a > b):     # >
    print("a 大于 b");
else:
    print("a 小于 b");
# 还有 <=     >=
print("\n----------------------------------------------\n");

# 赋值运算符(省略)
print("赋值运算符");
print("\n----------------------------------------------\n");

# 位运算符
# 按位运算符是把数字看作二进制来进行计算的
print("位运算符\n");
#   60 = 0011 1100
#   13 = 0000 1101
a,b,c = 60,13,0;
# 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
c = a & b;    # 12 = 0000 1100
print("a & b的值为", c);

# 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
c = a | b;    # 61 = 0011 1101
print("a | b的值为", c);

# 按位异或运算符：当两对应的二进位相异时，结果为1
c = a ^ b;    # 49 = 0011 0001
print("a ^ b的值为", c);

# 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
c = ~a;    # -61 = 1100 0011
print("~a 的值为", c);

# 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
c = a << 2;    # 240 = 1111 0000
print("a << 2 的值为", c);

# 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
c = a >> 2;    # 15 = 0000 1111
print("a >> 2 的值为", c);
print("\n----------------------------------------------\n");

# 逻辑运算符
print("逻辑运算符\n");
a = 10;
b = 20;
if ( a and b ):     # and
   print ("变量 a 和 b 都为 true");
else:
   print ("变量 a 和 b 有一个不为 true");

if ( a or b ):      # or
   print ("变量 a 和 b 都为 true，或其中一个变量为 true");
else:
   print ("变量 a 和 b 都不为 true");

# not
print("\n----------------------------------------------\n");

# 成员运算符
print("成员运算符\n");
a = 10;
b = 20;
list = [1, 2, 3, 4, 5 ];
if ( a in list ):   # in
   print ("变量 a 在给定的列表中 list 中");
else:
   print ("变量 a 不在给定的列表中 list 中");

if ( b not in list ):   # not in
   print ("变量 b 不在给定的列表中 list 中");
else:
   print ("变量 b 在给定的列表中 list 中");
print("\n----------------------------------------------\n");

# 身份运算符
print("身份运算符");
a = 20;
b = 20;
if ( a is b ):  # 是不是引用同一个对象
   print ("a 和 b 有相同的标识");
else:
   print ("a 和 b 没有相同的标识");

if ( id(a) == id(b) ):
   print ("a 和 b 有相同的标识");
else:
   print ("a 和 b 没有相同的标识");
print("\n----------------------------------------------\n");
