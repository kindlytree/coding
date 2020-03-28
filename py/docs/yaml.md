# yaml
- [reference1](http://www.ruanyifeng.com/blog/2016/07/yaml.html)
- [reference2](https://blog.csdn.net/qq_38650545/article/details/88424121)
```
a: 1
b: 2
c: 3
d: 4
e: 5
x:
    x1: 3
    x2: 4

import yaml
 
def config_test(filename):
    with open(filename, 'r') as f:
        return yaml.load(f)
 
filename = './test_config.yaml'
test = config_test(filename)
```
- 注意事项
    - 每个散列项冒号和值之间至少有一个空格！
    - 使用空格表示层级关系，空格的个数不重要，只要相同层级的元素左对齐即可,建议层级之间两个空格
