# easydict

```
from easydict import EasyDict as edict
d = edict({'foo':3, 'bar':{'x':1, 'y':2}})
d.foo
d.bar.x


在深度学习中往往利用easydict建立一个全局的变量
from easydict import EasyDict as edict
config = edict()
config.TRAIN = edict() # 创建一个字典，key是Train,值是{}
config.Test = edict()
 config.TRAIN = {} # 这个和上面的那句话是等价的，相当于创建一个字典的key
config.TRAIN.batch_size = 25  # 然后在里面写值,表示Train里面的value也是一个字典
config.TRAIN.early_stopping_num = 10
config.TRAIN.lr = 0.0001
print(config)

```