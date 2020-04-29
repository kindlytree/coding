# Inheritance

```
class Evaluator(object):
    def __init__(self, eval_type, writer):
        self.eval_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        self.eval_type = eval_type
        self.writer = writer

    def evaluate(self):
        pass


class DetEvaluator(Evaluator):
    def __init__(self, eval_type , writer, **kwargs):
        super(DetEvaluator, self).__init__(eval_type, writer)
        # self.det_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        self.data_path = kwargs['data_path']
        self.output_path = kwargs['output_path']
        self.file_list = kwargs['file_list']
        self.input_scale = kwargs['input_scale']
```