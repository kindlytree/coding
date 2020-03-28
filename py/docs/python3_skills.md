# Python3 skills
- [参考](https://mp.weixin.qq.com/s?__biz=MzIzNTg3MDQyMQ==&mid=2247486446&idx=2&sn=a43b59658cbde1b6e182d13bd097d305&chksm=e8e1ca54df964342193d6961a4adc275bfd4a3f025a6023f44baf34e22eb1d177a1e089d34ae&mpshare=1&scene=1&srcid=&sharer_sharetime=1582276690819&sharer_shareid=a0219cecc96d542bc67e4e19834f9520&exportkey=ARQeZZ9SL4tR0a0fUlVS2Q8%3D&pass_ticket=HsLmGYah4W2rcTloiKGnPSoaoI5wreXADp3eWprg8Qw%3D#rd)

## 列表表达式
- [ expression for item in list if conditional ]

```
mylist = [i for i in range(10)]

squares = [i**2 for i in range(10)]

formular =[some_function(i) for i in range(10)]

filtered = [i for i in range(20) if i%2==0]
```

## 使用数据类
- [参考](﻿https://realpython.com/python-data-classes)

## 合并dictionary

```
dict1={'a':1, 'b':2}
dict2={'b':3, 'c':4}
merged = {**dict1, **dict2}

如果有重复的 key，那么第一个词典的这个 key 对应的值会被覆盖掉。
```

## list切片
a[start:stop:step]

```
revarray = [1,2,3,4,5][::-1]
#[5,4,3,2,1]
```

## 使用map
你可以给它一个函数让其执行，然后还要传给它对应的参数。这个参数可以使任何可迭代对象
```
>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
 
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
```