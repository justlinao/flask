"""99乘法表"""
# j = 0
# j < 9:  # 先判断最外层循环多少，循环9层<9
#     j  while += 1  # 每次循环+1
#     i = 0
#     while i < j:  # 内循环根据外循环变化，始终小于外循环的次数，并且每次循环结束后，重新从0计算，一个内循环打印一行，一直到不满足这个while条件时跳出这个内循环
#         i += 1
#         print(i, '*', j, '=', i*j, end="\t")
#     print()
import copy
from datetime import time

"""1-100求和"""
# i = 0
# count = 0
# while i < 100:
#     i += 1
#     count += i
# print(count)


"""递归简单来说就是函数自己调用自己"""
# count = 0
#
#
# def tell_story():
#     global count  # global 设置成全局变量
#     count += 1
#     print('从前有个山，山里有个庙，庙里有个老和尚，老和尚给小和尚讲故事，讲的什么故事呢')
#     if count < 5:
#         tell_story()
#
#
# tell_story()

"""求n！n的阶乘，=（n-1）！*n"""
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1) * n
#
#
# a = factorial(6)
# print(a)


"""深浅copy"""
# word = ['hello', ['1', '2', '3'], 'world']
# word1 = word.copy()  # 浅拷贝 拷贝一个新的对象，但是只拷贝了第一层，第二层的[1,2，3]内存地址没发生变化和word使用的是同一个，word里的[1,2,3]修改后word1 跟着改变
# word2 = copy.deepcopy(word)  # 深拷贝 拷贝一个新的对象，两层都是独立的，第二层的[1,2,3]也是独立的，word里的[1,2,3]修改后word2 不受影响
import time

"""
装饰器，在不修改原有函数代码的情况下增加额外功能，装饰器外层函数返回的是内层函数，内层函数返回被入参函数的对象，常用在增加日志切面需求的场景中
"""


def zhuangshi(fn):
    def inner(n, *args, **kwargs):
        start_time = time.time()
        f = fn(n)
        end_time = time.time()
        print("执行这个函数耗时  %s" % (end_time-start_time))
        return f
    return inner


@zhuangshi
def demo(n):
    count = 0
    for i in range(0, n):
        count += i
    print(count)
    return count


def can_play(fn):
    def inner(name, game, *args, **kwargs):  # **kwargs是传入键值对
        money = kwargs.get('money', 23)  # get方法，如果没有获取到参数money，就给出默认值23
        if args[0] < 22 and money > 20:
            fn(name, game)
        else:
            print("没钱不能打游戏")

    return inner


@can_play
def play_game(name, game):
    print("{}在玩{}".format(name, game))


# play_game("zhangsan", "wangzhe", 20)


"""
迭代器 调用__iter__方法返回的对象就叫做迭代器对象
可迭代对象 该对象里有__iter__方法就叫做可迭代对象
再通过迭代器对象的__next__方法取值,如果取值次数超过源值的数量就会报错
迭代器不通过索引去取值
"""
list = [1, 2, 3]
print(list.__dir__())
list1 = list.__iter__()
print(list1.__dir__())
print(list1.__next__())
print(list1.__next__())

"""
generator 生成器， range（100000000000000000000），占用内存过大，机器性能无法处理
生成器就是边迭代边输出，提高整个系统的效率
用生成器编写斐波那契
函数中使用yiel关键字，相当于函数返回的是生成器对象，该对象可以被迭代，边取边输出
"""


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        if count > n:
            break
        yield a+b  # 相当于把数据用自定义生成器储存起来，获取的时候 就可以边取边输出
        a, b = b, a+b  # a =1 , b =1 /a+b=2 ,a =1,b =2/a+b=3,a=2, b=3/a+b=5,
        count += 1


f = fibonacci(10)
for i in f:
    print(i)
    time.sleep(1)

import random

dic = {}
lis = ['KeLan', 'Monkey', 'Dexter', 'Superman', 'Iron Man', 'Robin']


def redpacket(cash, person, index):
    if cash > 0 and person != 1:
        n = round(random.uniform(0.01, cash - (0.01 * person)), 2)
        dic[lis[index]] = n
        print(str(n).ljust(4, "0"))
        person -= 1
        cash -= n
        index += 1
        redpacket(cash, person, index)
    else:
        dic[lis[index]] = round(cash, 2)

        print(str(cash).ljust(4, "0"))


redpacket(10, len(lis), 0)

print("手气最佳:", max(dic.items(), key=lambda x: x[1]))