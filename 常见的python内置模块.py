"""
os 模块里提供的方法是用例调用操作系统的方法
"""
import os
import datetime
import time
# os.name ==>获取操作系统的名字
print(os.name)  # windows ==> nt ,IOS==>posix
print(os.sep)  # ==>打印路径的分隔符
print(os.path.abspath('app.py'))  # 获取绝对路径
print(os.path.isdir('app.py'))  # 判断是否为文件夹
print(os.path.isfile('app.py'))  # 判断是否为文件
print(os.path.exists('app.py'))  # 判断是否存在
print(os.getcwd())  # 获取当前工程路径
print(datetime.datetime.now())  # 获取当前时间
print(time.strftime("%D %H:%M:%S"))
