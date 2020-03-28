# yaml
- https://blog.csdn.net/qq_38650545/article/details/88424121
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

```
sampe code:


#lib_path = os.path.abspath(".")
lib_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(lib_path)

def load_cfg_from_file(filename):
    import yaml
    with open(filename, 'r') as f:
        yml_cfg = edict(yaml.load(f))
        return yml_cfg

cfg = load_cfg_from_file(os.path.join(lib_path, '../../configs/base.yml'))

def merge_cfg_from_file(filename):
    """Load a config file and merge it into the default options."""
    import yaml
    with open(filename, 'r') as f:
        yaml_cfg = edict(yaml.load(f))

    _merge_a_into_b(yaml_cfg,  cfg)

def _merge_a_into_b(a, b):
    """Merge config dictionary a into config dictionary b, clobbering the
    options in b whenever they are also specified in a.
    """
    if type(a) is not edict:
        return

    for k, v in a.iteritems():
        # a must specify keys that are in b
        if not b.has_key(k):
            raise KeyError('{} is not a valid config key'.format(k))

        # the types must match, too
        old_type = type(b[k])
        if old_type is not type(v):
            if isinstance(b[k], np.ndarray):
                v = np.array(v, dtype=b[k].dtype)
            else:
                raise ValueError(('Type mismatch ({} vs. {}) '
                                'for config key: {}').format(type(b[k]),
                                                            type(v), k))

        # recursively merge dicts
        if type(v) is edict:
            try:
                _merge_a_into_b(a[k], b[k])
            except:
                print('Error under config key: {}'.format(k))
                raise
        else:
            b[k] = v

```