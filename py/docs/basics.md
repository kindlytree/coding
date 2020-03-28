# bascis

map()函数不改变原有的 list，而是返回一个新的 list。
  利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。
由于list包含的元素可以是任何类型，因此，map() 不仅仅可以处理只包含数值的 list，事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。
假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
输入：['adam', 'LISA', 'barT']
输出：['Adam', 'Lisa', 'Bart']
def format_name(s):
    s1=s[0:1].upper()+s[1:].lower();
    return s1;
print map(format_name, ['adam', 'LISA', 'barT'])


r_str = '\n'.join([' '.join(list(map(str,i))) for i in detections])

python3中的map 转list  list（map（fun，your_list））