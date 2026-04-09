# _*_ coding: utf-8 _*_

"""类型和运算---类型和运算"""

#-- seek help:
dir(obj) # 简单地列出对象obj所包含地方法名称，返回一个字符串列表
help(obj.func)

#-- 测试类型地三种方法，推荐第三种
if type(L) == type([]):
    print("L is a list")
if type(L) == list:
    print("L is list")
if isinstance(L, list):
    print("L is list")

#-- Python数据类型：哈希类型、不可哈希类型
    # 哈希类型，即在原地不能改变的变量类型，不可变类型。可用hash函数查看其hash值，也可以作为字典的key
    "数字类型: int, float, decimal.Decimal, fractions.Fraction, complex"
    "字符串类型: str, bytes"
    "元组: tuple"
    "冻结集合: frozenset"
    "布尔类型: True, False"
    "None"
    # 不可hash类型：原地可变类型，list、dict和set。它们不可以作为字典的key。

#-- 数字常量
    1234, -1234, 0, 999999999           # 整数
    1.23, 1., 3.14e-10, 4E210, 4.0e+210  # 浮点数
    0o177, 0x9ff, 0x9FF, 0b101010       # 八进制，十六进制，二进制数字
    3+4j, 3.0+4.0j,3J, 3.0J             # 复数常量，也可以使用complex(real, image)来创建
    hex(I), oct(I), bin(I)               # 将十进制数转换为十六进制，八进制，二进制字符串
    int(string, base)                     # 将字符串转换为整数，base为进制数
    # 2.x中，有两种整数类型：一般整数（32位）和长整数（无穷精度）。可以用1或L结尾，迫使一般整数成为长整数
    float('inf'), float('-inf'), float('nan')  # 浮点数的特殊值，无穷大，无穷小，非数

#-- 数字的表达式操作符
    yield x                            # 生成器函数发送协议
    lambda args: expression             # 生成匿名函数
    x if y else z                      # 三元表达式
    x and y, x or y, not x              # 逻辑运算符，与、或、非
    x in y, x not in y                 # 成员运算符，成员对象测试
    x is y, x is not y                 # 身份运算符，对象实体测试
    x<y, x<=y, x>y, x>=y, x==y, x!=y  # 比较运算符，大小比较，结合子集或超集值相等性操作符
    1 < a < 3                          # 链式比较，用于比较多个值，python允许连续比较
    x|y, x&y, x^y                      # 位运算符，按位或、与、异或
    x<<y, X>>y                         # 位移运算符，左移、右移y位
    +, -, *, /, //, %, **               # 真除法、floor除法：返回不大于真除法结果的整数值、取余、幂运算
    -x, +x, ~x                          # 一元减法、识别、按位求补（取反）
    x[i], x[i:j:k]                      # 索引，分片
    int(3.14), float(3)                 # 强制类型转换

#-- 整数可以利用bit_length函数测试所占的位数
    a = 1;          a.bit_length()  # 1位
    a = 1024;       a.bit_length()  # 11位

#-- repr和str显示格式的区别
    """
    repr格式：默认的交互模式回显，产生的结果看起里它们就像是代码。
    str格式：打印语句，转化成一种对用户更加友好的格式。
    """

#-- 数字相关的模块
    # math模块
    # Decimal模块：小数模块，用于精度运算
        import decimal
        from decimal import Deccimal
        Decimal("0.01") + Decimal("0.02")  # 返回Decimal("0.03")
        decimal.getcontext().prec = 4      # 设置全局精度为4 即小数点后边四位
    # fractions模块：分数模块，用于分数运算
        from fractions import Fraction
        x = Fraction(4, 6)     # 分数类型 4/6
        x = Fraction("0.25")   # 分数类型 1/4 接受字符串类型的参数
    
#-- 集合set
"""
set是一个无序不重复元素集，基本功能包括关系测试和消除重复元素
set支持union(联合), intersection(交集), difference(差集)和symmetric_difference(对称差集)等数学运算。
set支持x in set, len(set), for x in set。
set不记录元素位置或者插入点，因此不支持indexing, slicing,或者其他类序列操作
"""
s = set([3, 5, 9, 10])       # 创建一个数值集合，返回{3, 5, 9, 10}
t = set("Hello")     # 创建一个字符的集合，返回{'l', 'H', 'e', 'o'}
a = t | s;   t.union(s)      # t 和 s 的并集
b = t & s;   t.intersection(s)     # t 和 s 的交集
c = t - s;   t.difference(s)     # t 和 s 的差集，项在t中，但不在s中
d = t ^ s;   t.symmetric_difference(s)    # 对称差集（项在t或s中，但不会同时出现在二者中）
t.add('x');    t.remove('H')     # 增加/删除一个item
s.update([10, 37, 42])     # 利用[……]更新s集合
x in s , x not in s     # 集合中是否存在某个值
s.issubset(t);   s <= t     #测试是否 s 中的每一个元素都在 t 中
s.issuperset(t);   s >= t     # 测试是否 t 中的每一个元素都在 s 中
s.copy();     # 复制集合
s.discard(x);     # 删除x，如果x不存在，不报错
s.clear();     # 清空集合
{x**2 for x in [1, 2, 3, 4]}     # 集合解析， 结果：{1, 4, 9, 16}
{x for x in 'spam'}     # 集合解析，结果：{'s', 'p', 'a', 'm'}

#-- 集合frozenset， 与set类似，但不可变，可以作为字典的key
"""
set是可变对象，即不存在hash值，不能作为字典的键值。同样的还有list等(tuple是可以作为字典key的)
frozenset是不可变对象，即存在hash值，可以作为字典的键值
frozenset对象没有add、remove等方法，但有union/intersetcion/difference等方法
"""
a = set([1, 2, 3])
b = set()
b.add(a)     # error：set是不可哈希类型，不能作为字典的key
b.add(frozenset(a))     # ok，将set变为frozenset，可哈希

#-- 布尔类型bool
type(True)    # 返回<class 'bool'>
isinstance(True, int)    # bool类型属于整型，所以返回True
True == 1; True is 1      # 输出(True, False)

#-- 动态类型简介
"""
变量名通过引用，指向对象。
Python中的“类型”属于对象，而不是变量，每个对象都包含又头部信息，比如“类型标识符”“引用计数器”等
"""
# 共享引用及在原处修改：对于可变对象，要主义尽量不要共享引用，而是通过复制来修改
# 共享引用和相等测试：
L = [1], M = [1], L is M     # 返回False
L = M = [1, 2, 3], L is M     # 返回True，共享引用
# 增强赋值和共享引用：普通+号会生产新的对象，而增强赋值+=会在原处修改对象
L = M = [1, 2]
L = L + [3, 4]     # 产生新的对象，L = [1, 2, 3, 4], M = [1, 2]
L += [3, 4]     # 在原处修改对象，L = [1, 2, 3, 4], M = [1, 2, 3, 4]

#-- 常见字符串常量和表达式
S = ''     # 空字符串
S = "spam's"     # 双引号和单引号相同，但前者可以包含单引号
S = "s\np\ta\x00m"      # 包含转义字符
S = """spam"""       # 三引号字符串，可以跨行，一般用于函数说明
S = r'\temp'        # 原始字符串，不转义
S = b'Spam'         # 字节字符串，用于二进制数据
S = u'spam'         # python2.6 文本字符串，用于Unicode文本
s1 + s2, s1*3, s[i], s[i:j], len(s)     # 字符串操作符
'a %s parrot' % 'kind'     # 字符串格式化表达式
'a {1} {0} parrot'.format('kind', 'red')     # 字符串格式化方法
for x in s: print(x)     # 遍历字符串中的字符，字符串迭代，成员关系
[x*2 for x in s]     # 字符串列表解析
','.join(['a', 'b', 'c'])     # 字符串连接，返回'a,b,c'

#-- 内置str处理函数
str1 = "stringobject"
str1.upper(); str1.lower(); str1.swapcase(); str1.capitalize(); str1.title()     # 全部大写，全部小写，大小写转换，首字母大写，每个字母的首字母都大写
str1.ljust(width)      # 获取固定长度，左对齐，右边不够用空格补齐
str1.rjust(width)      # 获取固定长度，右对齐，左边不够用空格补齐
str1.center(width)     # 获取固定长度，居中对齐，两边不够用空格补齐
str1.zfill(width)      # 获取固定长度，右对齐，左边不够用0补齐
str1.find('t', start, end)     # 查找子串，返回索引，可以指定起始和结束位置搜索，找不到返回-1
str1.rfind('t')     # 从右边开始查找子串，返回索引
str1.count('t')     # 统计子串出现次数
# 上面所有方法都可以使用index代替，不同的是使用indext会抛出异常，而find返回-1
str1.replace('old', 'new')     # 替换函数，替换old为new，参数中可以指定maxReplaceTimes，即替换指定次数
str1.strip();     # 默认删除空白字符，可以指定参数删除指定字符
str1.strip('d')     # 删除指定字符
str1.lstrip();     # 删除左边空白字符
str1.lstrip('d')     # 删除左边指定字符，删除str1字符串中开头处，位于 d 删除序列的字符
str1.rstrip();     # 删除右边空白字符
str1.rstrip('d');     # 删除右边指定字符
str1.startwith('start')     # 判断是否以start开头
str1.endwith('end')     # 判断是否以end结尾
str1.isalnum(); str1.isalpha(); str1.isdigit(); str1.islower(); str1.isupper(); str1.isspace()     # 判断是否为字母、数字、小写、大写、空格

#-- 三重引号编写多行字符串块，并且在代码折行处嵌入换行字符\n
mantra = """hello world
            hello python
            hello my friend"""
        # mantra为"""hello world\nhello python\nhello my friend"""

#-- 索引和分片
S[0], S[len(S)-1], S[-1], S[-len(S)]     # 索引，最后一个元素索引，倒数第一个元素索引
S[1:3], S[1:], S[:-1], S[1:10:2]     # 分片，第三个参数指定步长，如`S[1:10:2]`是从1到10，步长为2的分片

#-- 字符串转换工具
int('42'), str(42)     # 字符串转整数，整数转字符串，返回'42'和'42'
float('4.13'), str(4.13)     # 字符串转浮点数，浮点数转字符串，返回'4.13'和'4.13'
ord('s'), chr(115)     # 字符转整数，整数转字符，返回115和's'
int('1001', 2)     # 将字符串作为二进制数字，转化为数字，返回9
bin(13), oct(13), hex(13)     # 整数转二进制，八进制，十六进制字符串，返回'0b1101'，'0o15'，'0x0d'

#-- 另类字符串连接
name = "wang""hong"     # 字符串连接，返回"wanghong"，单行
name = "wang" \
        "hong"     # 字符串连接，返回"wanghong"，多行

#-- Python中的字符串格式化实现1--字符串格式化表达式
"""
基于C语言的'print'模型，并且在大多数的现有的语言中使用。
通用结构：%[(nanme)][flag][width].[precision]typecode    # 其中name为可选参数，flag为格式化标志，width为最小宽度，precision为精度，typecode为格式化类型
""" 
"this is %d %s bird" % (1, "dead")     # 返回"this is 1 dead bird", %d表示整数，%s表示字符串,一般的格式化表达
"%s---%s---%s" % (42, 3.14, [1, 2, 3])     # 返回'42---3.14---[1, 2, 3]', %s表示字符串，%d表示整数，%f表示浮点数，%r表示任意对象
"%d...%6d...%-6d...%06d" % (1234, 1234, 1234, 1234)"     # 返回'1234...  1234...1234...001234', %d表示整数，%6d表示整数，左对齐，右边不够用空格补齐，%-6d表示整数，右对齐，左边不够用空格补齐，%06d表示整数，左对齐，右边不够用0补齐
x = 1.23456789
"%e | %f | %g" % (x, x, x)     # 返回'1.234568e+00 | 1.234568 | 1.234568', %e表示指数形式，%f表示浮点数形式，%g表示自动选择形式
"%6.2f*%-6.2f*%06.2f+6.2f" % (x,x,x,x)     # 返回'  1.23*1.23  *001.23* +1.23', %f表示浮点数，左对齐，右边不够用空格补齐，%-6.2f表示浮点数，右对齐，左边不够用空格补齐，%06.2f表示浮点数，左对齐，右边不够用0补齐，后面跟着的6.2f表示精度为2的浮点数
"%(name1)d---%(name2)s" % {"name1":23, "name2":"value2"}     # 返回'23---value2', %d表示整数，%s表示字符串，可以用字典参数传入参数，基于字典的格式化表达式
"%(name)s is %(age)d" % vars()     # 返回'name is 23', 基于vars()函数的格式化表达式，vars()函数返回当前作用域的变量字典，var()函数调用返回一个字典，包含了所有本函数调用时存在的变量

#-- Python中的字符串格式化实现2--字符串格式化调用方法
# 普通调用
"{0}, {1} and {2}".format('spam', 'ham', 'eggs')     # 基于位置的调用，返回'spam, ham and eggs'
"{motto} and {pork}".format(motto = 'spam', port = 'ham')     # 基于关键字的调用，返回'spam and ham'
"{motto} and {0}".format('ham', motto = 'spam')     # 关键字调用，位置参数在关键字参数之前，返回'spam and ham'
# 添加键 属性 偏移量（import sys）
"my {1[spam]} runs {0.platform}".format(sys, {'spam':'laptop'})     # 基于字典的调用，返回'my laptop runs win32'，基于位置的键和属性
"{config[spam]} {sys.platform}".format(sys = sys, config = {'spam':'laptop'})     # 基于字典的调用，返回'laptop win32'，基于key的键和属性
"first = {0[0]}, second = {0[1]}".format(['A', 'B', 'C'])     # 基于列表的调用，返回'first = A, second = B'，基于位置的偏移量
# 具体格式化
"{0:e}, {1:3e}, {2:g}".format(3.14159, 3.14159, 3.14159)     # 输出'3.141590e+00, 3.142e+00, 3.14159' 
"{fieldname:format_spec}".format(......)     # 基于字段名的调用，返回格式化后的字符串
    # 说明
    """
    fieldname是指定参数的一个数字或关键字，后面可跟可选的".name"或"[index]"成分引用
    format_spec ::= [[fill]]align[sign][#][0][width][,][.precision][type]
    fill        ::= <any character>     # 默认为空格, 填充字符
    align       ::= "<" | ">" | "=" | "^"     # 默认右对齐, 左对齐, 居中对齐, 居中对齐
    sign        ::= "+" | "-" | " "     # 默认正号, 负号, 空格
    width       ::= integer              # 默认0, 最小宽度，字符串宽度
    precision   ::= integer              # 默认6, 精度，浮点数精度
    type        ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    """
    # 示例
    '={0:10} = {1:10}'.format('spam', 123.456)     # 输出'= spam      =    123.456'
    '={0:>10}='.format('test')     # 输出'=     test='
    '={0:<10}='.format('test')     # 输出'=test      ='
    '={0:^10}='.format('test')     # 输出'=   test   ='
    '{0:x}, {1:o}, {2:b}'.format(255, 255, 255)     # 输出'ff, 377, 11111111'
    'My name is {0:{1}}.'.format('Fred', 8)     # 输出'My name is Fred    .'，宽度为8，默认右对齐，填充字符为空格

#-- 常用列表常量和操作
L = [[1,2], 'string', {}]     # 列表元素可以不同类型，嵌套列表
L = list('spam')     # 字符串转列表，列表初始化
L = list(range(0,4))     # 范围转列表，列表初始化
list(map(ord, 'spam'))     # 列表推导式，字符转整数列表
len(L)     # 列表长度
L.count(value)     # 列表元素计数
L.append(obj)     # 列表末尾添加元素
L.insert(index, obj)     # 指定位置插入元素
L.extend(interable)     # 列表末尾添加可迭代对象
L.index(value, [start, [stop]])     # 列表元素索引，找不到返回ValueError，返回列表中值value的第一个索引
L.pop([index])     # 列表元素弹出，默认弹出最后一个元素，返回弹出的元素
L.remove(value)     # 列表元素移除，找不到返回ValueError，只删除第一次出现的value的值
L.reverse()     # 列表元素反转
L.sort(cmp=None, key=None, reverse=False)     # 列表元素排序，cmp为比较函数，key为排序函数，reverse为排序顺序，默认升序
a = [1, 2, 3], b = a[10:]     # 列表切片，b为空列表，超出索引范围不会报错
a = [], a += [1]     # 这里是在原有列表的基础上进行操作，即列表的id没有改变
a = [], a = a + [1]     # 这里是新建了一个列表，即列表的id改变了

#-- 用切片来删除序列的某一段
a = [1, 2, 3, 4, 5, 6, 7]
a[1:4] = []     # 删除索引1到4的元素，结果为[1, 5, 6, 7] 
a = [0, 1, 2, 3, 4, 5, 6, 7]
del a[::2]     # 删除索引为偶数的元素，结果为[1, 3, 5, 7]

#-- 常用字典常量和操作
D = {}
D = {'spam':2, 'tol':{'ham':2}}     # 字典初始化，嵌套字典
D = dict.fromkeys(['s', 'd'], 8)       # 字典初始化，指定键值，输出{'s': 8, 'd': 8}
D = dict(name = 'tom', age = 12)      # 关键字参数初始化,输出{'name': 'tom', 'age': 12}
D = dict([('name', 'tom'), ('age', 12)])      # 键值对列表初始化,输出{'name': 'tom', 'age': 12}
D = dict(zip([('name', 'tom'), ('age', 12)]))      # 键值对列表初始化,输出{'name': 'tom', 'age': 12}
D.keys(); D.values(); D.items()     # 字典键值，值，项
D.get(key, default)     # 字典元素获取，找不到返回default，默认default=None
D.update(D_other)     # 字典更新，D_other为字典，D更新为D_other的键值对，合并字典，如果存在相同的键值，D_other的数据会覆盖掉D的数据
D.pop(key, [D])     # 删除字典中键值为key的项，返回键值为key的值，如果不存在，返回默认值D，否则异常
D.popitem()     # 随机删除字典中的一项，返回(key, value)元组，如果字典为空，抛出KeyError
D.setdefault(k[, d])     # 字典元素设置，如果不存在，设置默认值d，返回值设置D中某一项的默认值。如果k存在，则返回D[k]，否则设置D[k]=d，同时返回D[k]。
del D     # 删除字典，字典中的元素也会被删除
del D['key']     # 删除字典的某一项
if key in D:    if key not in D:    # 判断字典中是否存在某一项
# 字典注意事项：（1）对新索引赋值会增加一项，（2）字典键不一定非得是字符串，也可以为任何的不可变对象
# 不可变对象：调用对象自身的任意方法，也不会改变该对象自身的内容，这些方法会创建心得对象并返回
# 字符串、整数、tuple都不是不可变对象，dict/set/list都是可变对象
D[(1,2,3)] = 2     # tuple作为字典的key

#-- 字典解析
D = {k:8 for k in ['s', 'd']}     # 字典解析，输出{'s': 8, 'd': 8}
D = {k:v for (k, v) in zip(['name', 'age'], ['tom', 12])}     # 字典解析，输出{'name': 'tom', 'age': 12}

#-- 字典的特殊方法__missing__:当查找不到key时，会之星该方法
class Dict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]
dct = dict()
dct["foo"].append(1)     # 有点类似于collections.defalutdict，但是没有设置默认值
dct["foo"]     # [1]

