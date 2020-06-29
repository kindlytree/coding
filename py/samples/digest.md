
## yml load and merge

```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
from easydict import EasyDict as edict
import numpy as np
#lib_path = os.path.abspath(".")
lib_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(lib_path)

def load_cfg_from_file(filename):
    import yaml
    with open(filename, 'r') as f:
        yml_cfg = edict(yaml.load(f))
        return yml_cfg

cfg = load_cfg_from_file(os.path.join(lib_path, 'base.yml'))


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


def merge_cfg_from_file(filename):
    """Load a config file and merge it into the default options."""
    import yaml
    with open(filename, 'r') as f:
        yaml_cfg = edict(yaml.load(f))

    _merge_a_into_b(yaml_cfg,  cfg)

merge_cfg_from_file(os.path.join(lib_path, 'override.yml'))
```

## yml sample
```
version: '1.0.0'
evaluation:
  eval_type_dict:
    det: 1
    seg: 2
  eval_types:
    - det
    - seg
  default_eval: det_seg
  metrics:
    output_path: /path/to/output
    save_modes: [csv, db]
    default_save_mode: csv
```

## docker exec -c option usage
```
replay_dir = '/path/to/replay_dir' ##valid path
bash_cmd = 'python3 app/app_name.py {}  --code_version={} --model_version={} --save_metrics \
                            && exit'.format(replay_dir, self.code_version, self.model_version)
bash_command="docker exec -it -e {} dfs bash -c '{}'".format(self.env_variable, bash_cmd)
logging.info('dfs command is ....{}'.format(bash_command))
os.system(bash_command)
```

## cv2 waitkey(0)
```
k=cv2.waitKey(0)
if k==ord('z'):
    if(file_path_index == 0):
        continue
    else:
        file_path_index-=1
elif k == ord('r'):  # run
    pause = False
```
## cv draw
```
cv2.rectangle(img, (int(float(x)-float(w)/2), int(float(y)-float(h)/2)), \
    (int(float(x)+float(w)/2), int(float(y)+float(h)/2)), (0, 255, 0), 2)

lane_label = cv2.imread(lane_path, cv2.IMREAD_GRAYSCALE)

cv2.putText(img, label_text, (int(bbox_int[0]), int(bbox_int[1]) - 2), cv2.FONT_HERSHEY_COMPLEX, font_scale, text_color)

```

## airflow
```
airflow trigger_dag lane_coef_filter_dag -c '{"data_path":"/home/to/path", "filter_type":"filter_type"}'

def dfs_start(**kwargs):
    data_path = kwargs.get('dag_run').conf.get('data_path')
    filter_type = kwargs.get('dag_run').conf.get('filter_type')
    filter(data_path, filter_type)
    return 1


t0 = PythonOperator(
    task_id='dfs_start', 
    python_callable=dfs_start,  
    provide_context=True,
    dag=dag)

t0
```

## logging
```
import logging
logging.basicConfig(level=logging.INFO)
logging.critical('{} directory path not exist!!!'.format(data_path))
logging.info('inference type is {} '.format(infer_type))
```

## docker compose
version: '2.3'
services:
  dfs:
    build:
     context: ../../******/docker
     dockerfile: Dockerfile
    container_name: test
    shm_size: '2gb'
    working_dir: /path/to/working_dir
    volumes:
      - ../../:/home/to/path
    command: "tail -f /dev/null"