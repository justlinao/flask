"""99乘法表"""
# j = 0
# while j < 9:  # 先判断最外层循环多少，循环9层<9
#     j += 1  # 每次循环+1
#     i = 0
#     while i < j:  # 内循环根据外循环变化，始终小于外循环的次数，并且每次循环结束后，重新从0计算，一个内循环打印一行，一直到不满足这个while条件时跳出这个内循环
#         i += 1
#         print(i, '*', j, '=', i*j, end="\t")
#     print()


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
