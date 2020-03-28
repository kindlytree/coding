# Regular Expression Library
The re module has the full capability of regular expression.
"compile" function can generate regular expression object by pattern string and optional arguments, the object has series of methods for match and replacement of the regular expression.

## re.match
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
- re.match(pattern, string, flags=0)
  - [flags](https://www.runoob.com/python/python-reg-expressions.html#flags)

```
#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"


matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter

```

## re.search
- re.search(pattern, string, flags=0)

```
#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs";
 
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"


searchObj.group() :  Cats are smarter than dogs
searchObj.group(1) :  Cats
searchObj.group(2) :  smarter

#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print "search --> searchObj.group() : ", matchObj.group()
else:
   print "No match!!"

No match!!
search --> searchObj.group() :  dogs

``` 

## pattern of regular expression
- [reference](https://www.runoob.com/python/python-reg-expressions.html)


```
import re
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())

{'province': '110', 'city': '223', 'born_year': '1990'}
```