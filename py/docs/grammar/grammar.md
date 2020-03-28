# grammar

## syspath

## assert
```
a = -1
assert a > 0, '出错了，a小于0啊'
注意：表达式=false 时，则执行其后面的异常。
```

## import
- Python如何从相对路径下import
```
pkg/
  __init__.py
  libs/
    some_lib.py
    __init__.py
  components/
    code.py
    __init__.py

import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

code中就可以用如下的引用来进行代码模块的import了
from libs.some_lib import something

或者执行
python -m pkg.components.code
然后我们就可以用from ..libs.some_lib import something 来import了。

https://www.jianshu.com/p/4ddd13e737ca

from .A import b：从dirname(__file__)中找A  当前路径中去查找
from A import b：从sys.path中找A

```
## **kwargs
- kwargs.keys() 本身是一个字典， 可以用作可变参数来进行参数传递

## 文件路径访问
import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
