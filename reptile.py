"""
爬虫脚本，爬取美女图片
"""
from urllib import request
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool

x = 1


def func():
    for i in range(10):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko)"
                                " Chrome/81.0.4044.138 Safari/537.36"}
        url = "https://www.buxiuse.com/?page=.{}".format(i)
        req = request.Request(url, headers=header)
        page = urllib.request.urlopen(req, timeout=20)
        conent = page.read()
        # print(conent, "\n")

        soup = BeautifulSoup(conent, 'html.parser')  # 自带的解析方式
        my_girl = soup.find_all('img')  # 先获取想要的html标签
        print(my_girl)
        for girl in my_girl:
            link = girl.get('src')
            print(link)
            global x
            urllib.request.urlretrieve(link, "image\%s.jpg" % x)
            x += 1
            print('已下载%s张' % x)


if __name__ == '__main__':
    pool = Pool(10)
    for i in range(10):
        pool.apply_async(func)
    pool.close()  # 关闭进程池，关闭后po不再接收新的请求
    pool.join()  # 等待po中所有子进程执行完成，再执行下面的代码,可以设置超时时间join(timeout=)




