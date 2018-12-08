"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import keyword
import sys
from untitled1 import TestClass

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
a,b=0,1
c=int(input("请输入数字"))
d=1
while b<40:
    print(b)
    a, b = b, a + b
    d = d + 1
    if(b==c and b>1):
        print("下标在",d)


#猜字谜游戏
number=7
guess=-1
print("/n")
print("数字猜字谜游戏开始！")
while guess!=number:
    guess=int(input("请输入你猜的数字"))

    if guess<number:
        print("小了")
    elif guess==number:
        print("猜对了")
    elif guess>number:
        print("大了")

#迭代器学习
import sys
list=[1,2,3,4,5]
it=iter(list)
for x in it:
    print(x,end=",")

list=[1,2,3,4,5]
it=iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
        
# Filename: support.py
import sys

import untitled1
list = [1, 2, 3, 4, 5]
it =iter(list)
print("我叫 %s 我今年 %d 岁了" % ("小明",10))
TestClass.Test.dl(1)
filename="WF_t1.text";
fp=open(filename,"w")
fp.write("Python 是一门非常好的语言")
fp.close()

"""

if __name__=="__main__":
    car=TestClass.Test()
    car.add_data([1,2,3,4])
    car.add_data([5,6,7,8])
    car.add_data([9,10,11,12])
    car.build()
