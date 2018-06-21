# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
# 解决方案
# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。 唯一的前提就是变量的数量必须跟序列元素的数量是一样的。

# http://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p02_unpack_elements_from_iterables.html
p=(4,5)
x,y = p
print(x,y)

data = ['cw',50,91.1,(2012,12,21)]
name,shares,price,date = data
print(name,shares,price,date)


name,shares,price,(year,mon,day) = data
print(year,mon,day)

# 有时候，你可能只想解压一部分，丢弃其他的值。
# 对于这种情况 Python 并没有提供特殊的语法。
# 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。
# 你必须保证你选用的那些占位变量名在其他地方没被使用到。


data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_,shares,price,_ = data
print(shares,price)

# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。
# 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

# 解决方案
# Python 的星号表达式可以用来解决这个问题。
# 比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
# 如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？这时候星号表达式就派上用场了：

def drop_first_last(grades):
    first, *middle, last = grades
    return middle

# 另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码。
# 你可以像下面这样分解这些记录：

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name,email,phone_numbers)
