# logging
- https://www.cnblogs.com/Nicholas0707/p/9021672.html

级别等级依次提高，级别信息量依次减少
|  级别	| 何时使用| 
|-------|--------|
| DEBUG	| 详细信息，典型地调试问题时会感兴趣。 详细的debug信息。| 
|INFO	| 证明事情按预期工作。 关键事件。| 
| WARNING	| 表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。| 
| ERROR	| 由于更严重的问题，软件已不能执行一些功能了。 一般错误消息。| 
| CRITICAL	| 严重错误，表明软件已不能继续运行了。| 
| NOTICE	| 不是错误，但是可能需要处理。普通但是重要的事件。| 
| ALERT	| 需要立即修复，例如系统数据库损坏。| 
| EMERGENCY	| 紧急情况，系统不可用（例如系统崩溃），一般会通知所有用户。| 
```
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d  %H:%M:%S %a'    #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )
logging.info("{} uv points, only {} are available".format(
    eyeq_uvs_count, valid_eyeq_uvs))
logging.warning("Rename camera_df['id'] to camera_df['track_id']")
logging.critical("num set to {}".format(nums))
```