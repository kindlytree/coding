# __init__.py

## __all__

编写一个库的时候，经常会在 __init__.py 中暴露整个包的 API，而这些 API 的实现可能是在包中其他模块中定义的。
```
__all__ = [
    'voc_classes', 'imagenet_det_classes', 'imagenet_vid_classes',
    'coco_classes', 'dataset_aliases', 'get_classes', 'coco_eval',
    'fast_eval_recall', 'results2json', 'DistEvalHook', 'DistEvalmAPHook',
    'CocoDistEvalRecallHook', 'CocoDistEvalmAPHook', 'average_precision',
    'eval_map', 'print_map_summary', 'eval_recalls', 'print_recall_summary',
    'plot_num_recall', 'plot_iou_recall'
]
```