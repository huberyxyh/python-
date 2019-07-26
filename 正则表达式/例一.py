#\w   匹配字母、数字及下划线
#\W   匹配不是字母、数字及下划线的字符
#\s   匹配任意空白字符，等价与[\t\n\r\f]
#\S   匹配任意非空字符
#\d   匹配任意数字，等价于[0-9]
#\D   匹配任意非数字的字符
#\A   匹配任意非数字的字符
#\Z   匹配字符串结尾，如果存在换行，之匹配到换行前的结束字符串
#\z   匹配字符串结尾，如果存在换行，同时还会匹配换行符
#\G   匹配最后匹配完成的位置
#\n   匹配一个换行符
#\t   匹配一个制表符
# ^   匹配一行字符串的开头
# $   匹配一行字符串的结尾
# .   匹配任意字符，除了换行符，当re.DOTALL标记被制定是，则可以匹配包括换行符的任意字符
#[...] 用来表示一组字符，单独列出，比如[amk]匹配a、m、或k
#[^...]不在[]中的字符，比如[^abc]匹配除了a、b、c之外的字符
# *    匹配0个或多个表达式
# +    匹配1和或多个表达式
# ？   匹配0个或1个前面的正则表达式定义的片段，非贪婪方式
# {n}  精确匹配n个前面的表达式
# {n,m}匹配n到m次由前面正则表达式定义的片段，贪婪方式
#a\b   匹配a 或 b
#（）  匹配括号内的表达式，也表示一个组
import re
content = 'hello 1234657 World_this is a xyh'
result = re.match('^hello\s(\d+)\sWorld',content)
print(result)
print(result.group(1))
#出现空白就用\s匹配 出现数字就用\d匹配
#有一个万能的匹配方法 就是 *
# . 可以匹配任意字符 * 代表匹配前面的字符无限次

result1 = re.match('^hello.*$',content)
print(result1)
print(result1.group())
print(result1.span())
#----------通用匹配------------



#通用匹配* 可能有时候会匹配到并不是我们想要的
result2 = re.match('^he.*(\d+).*',content)
print(result2)
print(result2.group(1)) #输出结果是 7
#--------贪婪匹配与非贪婪匹配----------
#贪婪匹配下，*会匹配尽可能多的字符
#在表达式中 ，*  后面 \d+  也就是至少一个数字 并没有指定具体多少个数字
#于是把123456匹配了 ， 给\d+留下一个可满足条件的数字 7


#非贪婪匹配 写法是 .*?
result3 = re.match('^he.*?(\d+).*',content)
print(result3)
print(result3.group(1))

#贪婪匹配是尽可能匹配多的字符
#非贪婪匹配是尽可能匹配到少的字符

content1 = 'http://weibo.com/comment/xyhczq123'
rexyh = re.match('^http.*?comment/(.*?)',content1)
rexyh1 = re.match('^http.*?comment/(.*)',content1)
print('rexyh',rexyh.group(1))
print('rexyh1',rexyh1.group(1))

#修饰符
#正则表达式可以包含一些可选标志修饰符来控制匹配的模式
content2 = '''hello 12345678 World_this
is a regex Demo
'''
reczq = re.match('^he.*?(\d+).*?Demo$',content2,re.S)
print(reczq.group(1))
#直接报错！！！！ 也就是说正侧表达时没有匹配到这个字符串

#修饰符               描述
#re.I                 使匹配对大小写不敏感
#re.L                 做本地化识别匹配
#re.M                 多行匹配，影响 ^ 和 $
#re.S                 使 . 匹配包括换行在内的所有字符
#re.U                 根据Unicode字符集解析字符，影响\W、\w、\b、\B
#re.X                 该标志通过给予你更灵活的格式以便你将正侧表达式写的更容易理解


#转义匹配
# . 匹配除换行符意外的任意字符  如果目标字符串里面就包含 . 用到转义匹配

content3 = '(百度)www.baidu.com'
rexyh2 = re.match('\(百度\)\www.baidu\.com',content3)
print(rexyh2)

#search()
content4 = 'extra stings hello 1234567 world_this is xyh'
result4 = re.match('^hello.*?(\d+).*?xyh',content4)
print(result4)
#字符串以extra开头 正则表达式以hello开头 整个正则表达式是字符串一部分  但是匹配失败
#match()更适合用来检测某个字符串是否符合某个正则表达式的规则
#search（） 匹配是会扫描整个字符串，返回第一个成功匹配结果
#正则表达式可以是字符串的一部分，在匹配时  search（）方法会依次扫描字符串
#直到找到第一个符合规则的字符串 然后返回匹配内容
result5 = re.search('^hello.*?(\d+).*?xyh',content4)
print(result5)

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2）
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view= "7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view= "4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view= "6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view= "5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view= "5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
#ul 字节里有许多li节点  li节点里有许多a节点，有的不包含a节点 a节点有相对应属性  超链接和歌手名
#提取class为active的li节点内部的超链接包含的歌手和歌名

#正则表达式可以li开头，然后寻找active，中间部分可以用.*?匹配
#提取singer这个属性值 需要写入singer ="(.*?)"  用小括号括起来 以便group（）方法查找
#匹配a节点的文本 ，其中它左边界是 >  右边界是<\a>
#内容依旧用 （.*?）
#最后 <li.*?active.*?singer="(.*?)"<(.*?)(\a)>
#再用search（）方法 搜索整个html文本，找到符合正则表达式的第一个内容返回
#由于代码有换行  所以要传入第三个参数 re.S
result6 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
if result6:
    print(result6.group(1),result6.group(2))
#结果就是class为active的li节点内部的超链接包含的歌手歌名

#result6 = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
#if result6:
    #print(result6.group(1),result6.group(2))
#不加active，search（）方法会返回第一个符合条件的匹配目标
#active去掉后，从字符串开头开始搜索，此时符合条件节点就变成了第二个节点li





#findall()
#获取匹配正则表达式的所有内容
result7 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result7)
print(type(result7))
for res in result7:
    print(res)
    print(res[0],res[1],res[2])




#sub()
#正则表达式提取信息外，还需要借助它来修改文本
#比如：把字符串中的数字都去掉 如果用replace（）方法 很麻烦  这是借助sub（）
cc='54a48de789rvx45sdsdf48wefwef4234fsdf5qw4d8wef'
ccs=re.sub('\d+', '', cc)
print(ccs)

#这里只需要给第一个参数传入\d+来匹配所有的数字，第二个参数为替换成字符串

#提取歌单 用sub（）方法更加简便
xyh = re.sub('<a.*?>|</a>','',html)
print(xyh)
czq = re.findall('<li.*?>(.*?)</li>',xyh,re.S)
print(czq)
for czqs in czq:
    print(czqs.strip())
#a节点经过sub（）方法处理过后就没有了 ，然后再通过findall（）方法直接提取即可
