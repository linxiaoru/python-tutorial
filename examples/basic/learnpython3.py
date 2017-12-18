# 译自 https://learnxinyminutes.com/docs/python3/，对内容有进行修改，加入了自己的理解和补充。

# 单行注释用井号（#）开头。

""" 多行注释用三个双引号（""）包裹，
    通常，三个双引号中要换行可以直接换，
    不需要加换行符切割，可以用作多行字符串，
    并且可以在三个双引号中添加注释。
"""

####################################################
# 1. 基本数据类型和运算符
####################################################

# 数字
3  # => 3

# 数学运算
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

""" 整除法用（//），两个整型相除，得到的还是整型。
    但是,如果一个浮点数除以一个非浮点数得到的还会是一个浮点数，
    并且，计算的结果却是忽略小数部分，运算的结果类似两个整型相除，但是得到一个浮点数。
"""
5 // 3       # => 1
5.0 // 3.0   # => 1.0
-5 // 3      # => -2 同样适用于负数
-5.0 // 3.0  # => 1

# 单斜杠（/）除法即为 float 除法，得到的商会返回为浮点数形式
10.0 / 3    # => 3.3333333333333335

# 模除（求余）
7 % 3   # => 1

# 指数运算
2**3    # => 8

# 使用小括号提升运算的优先级
(1 + 3) * 2  # => 8

# 布尔值也是基本数据类型（注意大写）
True
False

# 加 not 取反
not True    # => False
not False   # => Ture

# 布尔运算符
# 注意（and）和（or）是大小写敏感的
True and False  # => False
False or True   # => True

# 注意使用布尔运算符时要用整型
# False 是 0，True 是 1。这里和 JS 很不一样，JS 里 0 是 false，其他的数字都是 true
# 不要混用布尔类型（整型）和位运算符 and/or（&，|）
0 and 2                 # => 0
-5 or 0                 # => -5
0 == False              # => True
2 == True               # => False
1 == True               # => True
-5 != False != True     # => True

# 判断是否相等用 ==
1 == 1  # => True
2 == 1  # => False

# 判断不等用 !=
1 != 1  # => False
2 != 1  # => True

# 比较判断
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# 比较判断可以链式判断
1 < 2 < 3   # => True
2 < 3 < 2   # => False

# is 和 ==
# is 检查两个变量是否关联的是同一个对象，但是 == 检查的是对象是否指向同样的值
a = [1, 2, 3, 4]    #  a 指向一个新的列表，[1, 2, 3, 4]
b = a               #  b 指向的是 a 所指向的
b is a              # => True，a 和 b 所关联的是同一个对象
b == a              # => True，a 指向的的对象和 b 指向的对象是相等的
b = [1, 2, 3, 4]    #  b 指向一个新的列表，[1, 2, 3, 4]
b is a              # => False，a 和 b 关联的不是同一个对象
b == a              # => True，a 指向的对象和 b 指向的对象的值是相等的。

# 字符串用双引号（"）或者单引号（'）来创建
"This is a string."
'This is alse a string.'

# 字符串也能够相加，但是最好不要这样做
"Hello" + "world!"  # => "Hello world!"
# 字符串表达式（非变量）能够不使用加号（+）直接拼接
"Hello" "world"     # => "Hello world"

# 字符串能够被当作是一个列表的元素
"This is a string"[0]   # => 'T'

# 可以使用 len() 函数来获取字符串的长度
len("This is a string")     # => 16

# 可以使用 .format 来格式化字符串
"{} can be {}".format("Strings", "interpolated")    # => "Strings can be interpolated"

# 可以重复使用格式化参数来减少重复的输入
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"

# 如果不想去数参数，可以使用关键字来代替。就是说上例中的 {0} 代表的是 .format() 的第一个参数，{1} 是第二个参数
"{name} wants to eat {food}".format(name="Bob", food="lasagna")     # => "Bob wants to eat lasagna"

# 如果你的 Python 3 代码也需要运行在 Python 2.5 及以下版本中，可以使用旧的格式化形式
"%s can be %s the %s way" % ("Strings", "interpolated", "old")      # => "Strings can be interpolated the old way"

# None 是一个对象
None    # => None

# 不要使用相等判断号（==）来比较对象和 None
# 使用 is 来代替。这个能够检查对象的值是否相等
"etc" is None   # => False
None is None   # => True

# None，0，空字符串，空列表，空字典，空元组都判定为 False
# 其他的值都是 True
bool(0)   # => False
bool("")  # => False
bool([])  # => False
bool({})  # => False
bool(())  # => False

####################################################
## 2. 变量和集合
####################################################

# Python 有一个用于打印的 print 函数
print("I'm Python. Nice to meet you!")      # => I'm Python. Nice to meet you!

# 默认情况下，print 函数会在输出结束时换行（就是在结尾多输出了一个换行符）
# 可以使用可选参数 end 来改变字符串的结尾，意思就是之前结束的时候是在末尾加了个换行符，现在可以使用 end 参数来改变这个换行符
print("Hello, World", end="!")      # => Hello, World!

# 从控制台获取输入数据的一个简单方式
input_string_var = input("Enter some data: ")   # 将数据作为字符串返回
# 注意：在早期版本的 Python 中，input() 方法被命名为 raw_input()

# 不用声明就可以给变量赋值
# 按照惯例变量使用小写加下划线拼接的形式书写
some_var = 5
some_var    # => 5

# 访问未赋值的变量会发生异常
# 参见下一节《控制流》来学习更多关于异常的处理
some_unknown_var    # 抛出命名错误异常

# if 可以用作表达式来使用
# 相当于 C 语言的三元运算符 "?:"
"yahoo!" if 3 > 2 else 2    # => "yahoo!", 类似于 3 > 2 ? "yahoo!" : 2

# 列表用于存储序列
li = []
# 也可以使用一个预先填充好的列表
other_li = [4, 5, 6]

# 可以在列表末尾添加元素
li.append(1)    # li 变为 [1] 
li.append(2)    # li 变为 [1, 2] 
li.append(4)    # li 变为 [1, 2, 4] 
li.append(3)    # li 变为 [1, 2, 4, 3]
# 使用 pop() 方法可以将列表最末位元素移除,并返回被移除的元素
li.pop()        # => 3, 此时 li 变为 [1, 2, 4]
# 将 3 放回列表
li.append(3)    #  li 又变回 [1, 2, 4, 3]

# 可以像其他语言访问数组一样访问一个列表
li[0]   # => 1
# 获取最末位元素
li[-1]  # => 3

# 越界查询会发生索引错误
li[4]   # => 抛出索引错误

# 可以使用切片语法来查询列表的范围
# 起始索引是包含起始位置的元素的，结束索引没有包含结束位置的元素
# 像数学中的开闭区间一样
# li[start:stop:step], start 是起始索引；stop 是结束索引；step 是要间隔的位数，1 就表示正向隔一个数取一，-2 就表示从列表最末位开始反向隔两位取一
li[1:3]     # => [2, 4]
# 省略结尾,就从起始索引位一直到列表末位
li[2:]      # => [4, 3]
# 省略开头，就从列表首位开始到结束索引前一位元素
li[:3]      # => [1, 2, 4]
# 每隔两位取一个
li[::2]     # => [1, 4]
# 将列表从末尾开始反向隔一位取一
li[::-1]    # => [3, 4, 2, 1]

# 使用切片可以进行深拷贝
li2 = li[:] # => li2 = [1, 2, 4, 3]，但是（li2 is li）返回 False，（li2 == li）返回的是 True

# 使用 del 可以移除列表的任意元素
del li[2]   # li 变为 [1, 2, 3]

# 移除第一个出现的与参数一样的值
li.remove(2)    # li 变为 [1, 3]
li.remove(2)    # 抛出 2 不在列表中的 ValueError 错误

# 在指定索引位置插入元素
li.insert(1, 2) # => li 又变回 [1, 2, 3]

# 获取第一个与指定参数匹配的元素的索引
li.index(2)     # => 1
li.index(4)     # 抛出 4 不在列表中的 ValueError 错误 

# 列表可以相加
# 注意：li 和 other_li 不会被修改
li + other_li   # => [1, 2, 3, 4, 5, 6]

# 使用 extend() 扩展合并列表
li.extend(other_li)     # li 现在是 [1, 2, 3, 4, 5, 6]

# 使用 in 来检查一个元素是否存在于一个列表中
1 in li     # => True

# 使用 len() 来检测列表的长度
len(li)     # => 6

# 元组和列表很相似，但是是不可变的
tup = (1, 2, 3)
tup[0]          # => 1
tup[0] = 3      # 抛出 TypeError（类型错误） 异常

# 注意：长度为 1 的元组应该在元组的最后一位元素后加上一个逗号，
# 但是长度不为 1 的元组不应该在末位元素后面加逗号，即使是长度为 0 的也不要加
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# 使用在列表上的大多数操作也都是可以使用在元组上的
len(tup)            # => 3
tup + (4, 5, 6)     # => (1, 2, 3, 4, 5, 6)
tup[:2]             # => (1, 2)
2 in tup            # => True

# 可以把元组（或列表）中的元素取出来赋值给多个变量
a, b, c = (1, 2, 3) # a 现在是 1，b 是 2，c 是 3
# 也可以进行序列解包，就是把首个或前几个元素与后面几个元素分别提取出来
a, *b, c = (1, 2, 3, 4) # a 现在是 1，b 现在是 [2, 3]，c 是 4
# 如果省略了括号，那么元组会被自动创建
d, e, f = 4, 5, 6
# 来看看交换两个值有多么容易
e, d = d, e     # d 现在是 5，e 是 4


# 字典用于存储键值对的映射关系
empty_dict = {}
# 预先填充的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# 注意：dict 的 key 必须是不可变对象。这是因为 dict 根据 key来计算 value 的存储位置，
# 如果每次计算相同的 key 得出的结果不同，那dict内部就完全混乱了。
# 这个通过 key 计算位置的算法称为哈希算法（Hash），使得 dict 可以进行高速查找。
# 要保证 hash 的正确性，作为 key 的对象就不能变。
# 在 Python 中，字符串、整数、浮点数、元组等都是不可变的，因此，可以放心地作为 key。而 list 是可变的，就不能作为 key。
invalid_dict = {[1, 2, 3]: "123"}       # 抛出一个类型错误：不可进行哈希计算的类型：'list'
valid_dict = {(1, 2, 3): [1, 2, 3]}     # 值可以是任何类型的

# 使用 [] 来查找值
filled_dict["one"]  # => 1

# 使用 keys() 方法将所有的 key 作为一个可遍历的对象来获取。我们需要用 list() 来包裹，将其转化为列表。
# 注意：字典的键的顺序是不能保证的，你得到的结果可能和这个示例不一致
list(filled_dict.keys())    # => ["three", "two", "one"] 

# 使用 values() 方法将所有的 value 作为一个可遍历的对象来获取。同样，我们将其用 list() 来包裹，将其转化为列表。
# 注意：关于他们的顺序问题和上面 key 顺序问题一样，都是随机的。
list(filled_dict.values())  # => [3, 2, 1]

# 检查字典中键的存在性问题使用 in
"one" in filled_dict        # => True
1 in filled_dict            # => False

# 查找一个不存在的 key 会产生键名错误
filled_dict["four"]         # keyError,键名错误

# 使用 get() 方法来避免键名错误
# filled_dict.get("one")    # => 1
# filled_dict.get("four")   # => None
# get() 方法支持传入一个默认参数，当 value 不存在时返回这个默认参数
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# setdefault() 方法可以将一个键值对插入字典，只有当这个键在原先的字典中不存在时成立
filled_dict.setdefault("five", 5)   # filled_dict["five"] 被设置成 5 
filled_dict.setdefault("five", 6)   # filled_dict["five"] 仍旧是 5

# 添加到字典
filled_dict.update({"four":4})      # => {"one": 1, "two": 2, "three": 3, "five": 5, "four": 4}
filled_dict["four"] = 4             # 另一种添加到字典的方法

# 使用 del 来移除字典的键
del filled_dict["one"]      # 从填充好的字典中移除 "one" 键

# Python 3.5 还可以使用附加的解包选项
{'a': 1, **{'b': 2}}    # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}    # => {'a': 2}

# set 用于保存集合
empty_set = set()
# 使用一连串的值来初始化一个 set 集合。是的，看起来和一个字典很像。
# 然而，set 中的键是不能重复的
some_set = {1, 1, 2, 2, 3, 4}      # some_set 现在是 {1, 2, 3, 4}

# 和字典的键累死，集合的元素也是不可变对象
invalid_set = {[1], 1}      # => 抛出类型错误：不可进行哈希计算的类型：'list'
valid_set = {(1,), 1}

# 添加一个项到集合
filled_set = some_set
filled_set.add(5)       # filled_set 现在是 {1, 2, 3, 4, 5}

# 使用 & 计算交集
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# 使用 | 计算并集
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# 使用 - 计算补集
{1, 2, 3, 4} - {2, 3, 5}    # => {1, 4}

# 使用 ^ 计算对称差集
{1, 2, 3, 4} ^ {2, 3, 5}    # => {1, 4, 5}

# 检查左边的集合是否是右边集合的超集
{1, 2} >= {1, 2, 3}         # => False

# 检查左边的集合是否是右边集合的子集
{1, 2} <= {1, 2, 3}         # => True

# 使用 in 来检查一个元素是否存在于集合中
2 in filled_set             # => True
10 in filled_set            # => False



####################################################
## 3. 控制流和可迭代对象
####################################################

# 创建一个变量
some_var = 5

# 这有一个条件语句。缩进在 Python 中很重要！
# 惯例上使用四个空格来锁进，而不是 tab 缩进
# 这会打印出 "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:     # 这里 elif 分句是可选的
    print("some_var is smaller than 10.")
else:
    print("some_var is indeed 10.")

"""
for 循环打印列表：
打印:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # 可以使用 format() 来格式化字符串
    print("{} is a mammal".format(animal))

"""
使用 "range(number)" 遍历一个数字序列，范围从 0 到给定的数
打印：
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
使用 "range(lower, upper)" 遍历一个数字序列，范围从第一个小的参数到第二个大的参数（包括第一个参数，不包括第二个参数）
打印：
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
使用 "range(lower, upper, step)" 遍历一个数字序列，范围从第一个小的参数到第二个大的参数,
间隔第三个参数的位数，例如 step = 2，则意味间隔 2 个位数，当没有指定 step 的值时，默认值为 1。
打印：
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""
while 循环会一直持续循环直到条件不再满足为止。
打印：
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1      # x = x + 1 的简写方式

# 使用 try/except 块来处理异常
try:
    # 使用 raise 来抛出一个错误
    raise IndexError("This is an index error")
except IndexError as e:
    pass                # pass 只是一个空操作。通常你应该在这里做一些恢复工作。
except (TypeError, NameError):
    pass                # 如果需要的话，多个异常可以一起处理
else:                   # try/except 块的可选分句，必须遵循所有的 except 块
    print("All good!")  # 只有当代码在 try 中没有抛出异常时才运行这里
finally:                # 在所有情况下都会执行
    print("we can clean up resources here")

# 可以使用 with 语句替换 try/finally 来进行资源清理
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Python 提供了一个基础的抽象概念叫作迭代器
# 可迭代对象可被当作一个序列来对待
# range 函数返回的对象就是一个可迭代对象

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)     # => dict_keys(['one', 'two', 'three']). 这就是一个实现了我们的可迭代对象接口的对象

# 我们能够遍历它
for i in our_iterable:
    print(i)        # 打印 one, two, three

# 然而我们不能通过元素索引来处理元素
our_iterable[1]     # 抛出类型异常错误

# 迭代器是一个知道如何创建可迭代对象的对象
our_iterable = iter(our_iterable)

# 迭代器时一个能够记住我们遍历它时的状态的对象
# 迭代器是通过next()来实现的，每调用一次他就会返回下一个元素，
# 当没有下一个元素的时候返回一个StopIteration异常，所以实际上定义了这个方法的都算是迭代器。
next(our_iterable)      # => "one"

# 当我们进行迭代时它能够维持状态
next(our_iterable)      # => "two"
next(our_iterable)      # => "three"

# 当没有下一个元素的时候返回一个 StopIteration 异常
next(our_iterable)      # 抛出 StopIteration 异常

# 可以使用 list() 来获取迭代器中所有的元素
list(filled_dict.keys())    # => 返回 ["one", "two", "three"]
