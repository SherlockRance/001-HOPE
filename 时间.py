# -*- coding = utf-8 -*-
# @Time : 2019/3/16 10:09
# @Author : SharelockRice
# @File :From hope to the now.py
# @Software : PyCharm
import time


def now():
    b = 1552788611.6276736
    a = time.time()
    return int(a - b)


# 平年一年有31536000秒，闰年一年有31622400秒

a = now() / 12 / 30 / 24 / 60 / 60

b = now() / 30 / 24 / 60 / 60

c = now() / 24 / 60 / 60

d = now() / 60 / 60

e = now() / 60
print("距离写这串代码\n到现在已经过去了\n%d年\n%d月\n%d日\n%d时\n%d分" % (a, b, c, d, e))


input()
