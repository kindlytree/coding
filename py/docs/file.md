# File/Folder related operation

## glob 所有匹配的文件路径列表
```
pattern = os.path.join(self.img_dir, "frame_*_{}.bmp".format(img_id))
paths = glob.glob(pattern)

```

## exists, makedirs
```
import os.path as osp
if not osp.exists(dest_lane_img_dir):
    os.makedirs(dest_lane_img_dir)
```

## join, basename, dirname,splitext
```
dest_freespace_img_dir = osp.dirname(dest_freespace_img_path)
dest_label_path = osp.join(sample_info['dest_dir'], dest_ann_relative_path)


out_filename = os.path.join(args.output, os.path.basename(path))
_, extension = os.path.splitext(out_filename)
out_csv_filename = os.path.join(args.output, os.path.basename(path).replace(extension, ".csv"))
```

## 文件路径访问
```
import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
```        