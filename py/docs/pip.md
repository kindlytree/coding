# pip

## pypi mirros usage
pip install -r reuqirments.txt -i  https://pypi.douban.com/simple
[reference](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

## most popular mirros
- https://pypi.douban.com/simple
pypi 镜像使用帮助
pypi 镜像每 5 分钟同步一次。

临时使用
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
注意，simple 不能少, 是 https 而不是 http

设为默认
升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

NumPy 1.16.0 是最后一个支持 Python 2.7 的版本

pip list

linux: 
修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：
pip config set global.index-url https://****

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

