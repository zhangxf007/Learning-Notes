# Intro to Computer Science (closed)

标签（空格分隔）： Udacity

---
[TOC]

# Lesson2 problem set
## find last

```
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

#关于find()的复数用法，s.find(t, -2),意思是从s的倒数第二个字符开始找

def find_last(s, t):    # s means search, t means target
    last_pos = -1
    while True:
        pos = s.find(t, last_pos+1) //这里的+1非常重要，最关键的部分
        if pos == -1:
            return last_pos
        last_pos = pos
  


print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0
```
#Lesson 2.5:how to solve problems




## how old

```
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 

#我写的这个漏洞太多，错的
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    year = year2 - year1
    if month2 < month1:
        month = month2 + 12 - month1
        year -= 1
    else:
        month = month2 - month1
    if day2 < day1:
        day = day2+30 - day1
        month -= 1
    else:
        day = day2 - day1
    return year*365 + month*30 + day + 1

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
```
先写一个简单的例子，nextday,假设每月只有30天
```
def nextDay(year, month, day):
    if day < 30:
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1, 1
        else:
        return year+1, 1, 1
```

##我的错误示例
```
def union(a, b):
    for e in b:
        if e in a:
            pass
        else:
            a + e
            
# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
#print b
#>>> [2,4,6]
```
报错说 list can't connect with list， 看来这个+ operation不能用

正确方法，用`append()`
```
def union(a, b):
    for e in b:
        if e not in a: 
            a.append(e)
```

#lesson 3 problem set 

## Max Pages solution

这个是无限版crawl的例子
```
def crawl_web(see, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page))) 
            crawled.append(page)
    return crawled
```

这个是针对max_pages做出调整的代码
```
def crawl_web(see, max_pages):
    tocrawl = [seed]
    crawled = []  //len(crawled) is length of crawled
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages: // 只要爬过的crawled list数目小于max_pages即可
            union(tocrawl, get_all_links(get_page(page))) 
            crawled.append(page)
    return crawled
```

## Max Depth Solution
这个是无限版crawl的例子
```
def crawl_web(see, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page))) 
            crawled.append(page)
    return crawled
```
根据max_pages做出相应调整的例子
```
def crawl_web(seed,max_depth):    
    tocrawl = [seed]
    crawled = []
    next_depth = []  // 用来记载下一个depth里需要crawl的页面
    depth = 0       //depth一开始的默认值是0
    while tocrawl and depth <= max_depth:   //当tocrawl为零，即没有需要crawl的网页时结束，当depth等于max_depth时也结束
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))    //把tocrawl变成了next_depth, 将下一个depth里的page和当前page合并
            crawled.append(page)
        if not tocrawl:  // 关键，只有在当前层crawl完后才会运行这段代码，进入下一层
            tocrawl, next_depth = next_depth, []  //把下一层的页面赋给tocrawl，将下一层的页面清空
            depth = depth + 1 // 此时tocrawl里全是下一层的页面，故depth+1， 
    return crawled
```
无注释版
```
def crawl_web(seed,max_depth):    
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled
```

## problem set : sudoku 
问题描述
```
# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.
```
我的答案
```
def twice(p, m):    #检查m在p中是否有两个以上的数字
    n = 0
    for i in p:
        if i == m
        n++
    if n == 1:
        return True
    else:
        return False
    
    
def check_sudoku(sudoku):
    for i in sudoku:    #检查是否是方阵n*n
        if len(i) != len(sudoku):
            return False
    for n in sudoku:     #检查数字是否是1到9内的数字，字母也不行，分数也不行
        for m in n:
            if m > num_list and m not in [1,2,3,4,5,6,7,8,9]:
                return False
    for n in sudoku:    #检查行与列是否有相同数字
        // row = sudoku.index(n)
        for m in n:     # 检查每行是否有相同的数字
            if twice(n, m):
                return False
            column = n.index(m)   #得到m的index
            # 下面四行把m所在列的数字放到m_column里
            m_column = []
            i = 0
            while i <= len(sodoku):   
                m_column.append(sudoku[i][column])
            #检查每列是否有相同数字
            if twice(m_column, m):
                return False
     return True
```
答案
思路是不管每个digit是什么，不从数组中取值，直接拿1到9去数组里找
```
def check_sudoku(p):
    n = len(p) # Extract size of grid
    digit = 1 # strat with 1,从1开始逐个与每个digit比较
    while digit <= n: #Go through each digit
        i = 0
        while i < n: #Go through each row and column        
            row_count = 0
            col_count = 0
            j = 0
            while j < n: #for each entry in ith row/column
                if p[i][j] == digit: #check row count
                    row_count = row_count + 1
                if p[j][i] == digit:
                    col_count = col_count + 1
                j = j + 1
            if row_count != 1 or col_count != 1:
                return False
            i = i + 1 #newt row/column
            digit = digit + 1 #next digit
    return True #Nothing was wrong!
```

## Symmetric Square

`zip()`函数能把矩阵变成逆矩阵

```
q = [[0, 1, 2], 
     [-1, 0, 3], 
     [-2, -3, 0]]
```
`print zip(*q)`
```
[(0, -1, -2), 
 (1, 0, -3), 
 (2, 3, 0)]
```
`mutated = [list(i) for i in(zip(*q))]`
`print mutated`
```
[[0, -1, -2], 
 [1, 0, -3], 
 [2, 3, 0]]
```
也不知道`list`起什么作用，能把`()`变成`[]`
全部函数
```
def symmetric(q):
    original = q
    mutated = [list(i) for i in(zip(*q))]
    if original==mutated:
    	return True
    return False
```

# Lesson 4 Responding to Queries
## Add to Index
要求 笔记里也有写
```
# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index_0,keyword,url):
       
        
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]
```

我的代码
```
def check_keyword(index, keyword):   #检查keyword是否在index中
    for i in index:
        if i[0] == keyword:
            return True
        else:
            return False

#把index中keyword的第一层位置返回
def return_keyword_index(index, keyword):  
    for i in index:
        if[0] == keyword:
            return index.index(i)
        

def add_to_index(index,keyword,url):
    if not check_keyword(index, keyword):
        index.append([keyword, [url]])
    else:
        i = return_keyword_index(index, keyword)
        index[i][1].append('url')
```
The answer
```
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])
```

##lookup
返回keyword的所有url，没有对应keyword的话返回empty list
```
# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]
#my code
def lookup(index,keyword):
    for i in index:
        if i[0] == keyword:
           return i[1]
    return []
```
## Add Page to Index Solution
把content(比如说一篇文章）分成每个单词，把单词作为keyword,把url放到这个keyword之后的url list。
```
# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

#待定义的代码
def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)
```
测试的结果
```
add_page_to_index(index,'fake.text',"This is a test")
print index

[['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]
```
## Finish the web crawler
把之前的crawl_web针对index功能做一些修改，实现最终的crawled
```
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = [] #update
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page) #update, the page is the url
            add_page_to_index(index,page,content) # update
            union(tocrawl,get_all_links(content))
            crawled.append(page)
    return index
```

## 3 The Internet
get_page()函数的代码
```
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
```


#Lesson 4 problem set

##Better Splitting

```
 # The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1] + char
    return output
```

##Improving the Index Solution

```
# The current index includes a url in the list of urls
# for a keyword multiple times if the keyword appears
# on that page more than once.

# It might be better to only include the same url
# once in the url list for a keyword, even if it appears
# many times.

# Modify add_to_index so that a given url is only
# included once in the url list for a keyword,
# no matter how many times that keyword appears.

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == url:
            if url not in entry[1]: # 本问题只需要加这一行即可 
   
             entry[1].append(keyword)
            return
    # not found, add new keyword to index
    index.append([url, [keyword]])


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return '''<html> <body> This is a test page for learning to crawl!
<p> It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">
learn to crawl</a> before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body>
</html>'''

        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
</body> </html>'''

        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '''<html> <body> I cant get enough
<a href="http://www.udacity.com/cs101x/index.html">crawling</a></body></html>'''

        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '''<html>
<body>The magic words are Squeamish Ossifrage!</body></html>'''
    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

#index = crawl_web("http://www.udacity.com/cs101x/index.html")
#print lookup(index,"is")
#>>> ['http://www.udacity.com/cs101x/index.html']
```

## Counting Clicks Solution
记载每次搜索某一url的次数
每用一次lookup()函数，就是一次对keyword的搜索，如果能找到url，就说明这个URL的count数+1， 用record_user_click(index, keyword, url) 将其+1. 这要改变原有的数据结构，在每一个url的后面接一个count记载搜索次数。index = [keyword, [[url, count], [url, count] ......]

```
#urls = [[url, count],[url,count]...]

def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1]+1

def add_to_index(index, keyword, url):
    # format of index: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])
```

##  time_execution
```
import time #this is a Python library

def time_execution(code):
   start = time.clock()  # start the clock
   result = eval(code)  # evaluate any string as if it is a Python command
   run_time = time.clock() - start  # find difference in start and end time
   return result, run_time  # return the result of the code and time taken
```
eval()里面必须用string, for example:`time_execution('add_to_index(1,2,3)')`

# Lesson 6
##6.8 implemanting URank
学的page rank之后，修改之前web_crawl()的代码，并返回graph structure.
之前的web_crawl():
```
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index
```
修改后的：
```
def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content） #得到content里所有的links
            
            #Insert Code Here
            graph[page] = outlinks
            
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph
```
所有的代码：
```
# Modify the crawl_web procedure so that instead of just returning the 
# index, it returns an index and a graph. The graph should be a 
# Dictionary where the key:value entries are:

#  url: [list of pages url links to] 


def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            
            #Insert Code Here
            if page not in graph:
                graph[page] = outlinks
            
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipes:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbanzo beans.
<li> Crush them in a blender.
<li> Add 3 tablespoons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        return None
    
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None



index , graph = crawl_web('http://udacity.com/cs101x/urank/index.html') 

if 'http://udacity.com/cs101x/urank/index.html' in graph:
    print graph['http://udacity.com/cs101x/urank/index.html']
#>>> ['http://udacity.com/cs101x/urank/hummus.html',
#'http://udacity.com/cs101x/urank/arsenic.html',
#'http://udacity.com/cs101x/urank/kathleen.html',
#'http://udacity.com/cs101x/urank/nickel.html',
#'http://udacity.com/cs101x/urank/zinc.html']

```

## 6.8.5 完整的page rank code

```
#Finishing the page ranking algorithm.

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            
            #Insert Code Here
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d*(rank[node] / len(graph[node]))

            newranks[page] = newrank
        ranks = newranks
    return ranks



cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""", 
}

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            
            
            graph[page] = outlinks
            
            
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def get_page(url):
    if url in cache:
        return cache[url]
    else:
        return None
    
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)
print ranks

#>>> {'http://udacity.com/cs101x/urank/kathleen.html': 0.11661866666666663,
#'http://udacity.com/cs101x/urank/zinc.html': 0.038666666666666655,
#'http://udacity.com/cs101x/urank/hummus.html': 0.038666666666666655,
#'http://udacity.com/cs101x/urank/arsenic.html': 0.054133333333333325,
#'http://udacity.com/cs101x/urank/index.html': 0.033333333333333326,
#'http://udacity.com/cs101x/urank/nickel.html': 0.09743999999999997}

```

## 6.9 lesson 6: problem set
### 6.9.3 Feeling lucky, 把之前的所有功能整合，给出关键词的最佳page

```
#Feeling Lucky
 
#In Unit 6, we implemented a page ranking algorithm, but didn't finish the final
#step of using it to improve our search results. For this question, you will use
#the page rankings to produce the best output for a given query.

#Define a procedure, lucky_search, that takes as input an index, a ranks
#dictionary (the result of compute_ranks), and a keyword, and returns the one
#URL most likely to be the best site for that keyword. If the keyword does not
#appear in the index, lucky_search should return None.

def lucky_search(index, ranks, keyword):
    if keyword not in index:
        return None
    else:
        keyword_list = index[keyword]
        best_page = ['',0]
        for e in keyword_list:  # keyword_list = ['url1', 'url2',....]
            if ranks[e] > best_page[1]:
                best_page[0] = e
                best_page[1] = ranks[e]
        return best_page[0]


cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""",
}

def get_page(url):
    if url in cache:
        return cache[url]
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
    
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


#Here's an example of how your procedure should work on the test site: 

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

print lucky_search(index, ranks, 'Hummus')
#>>> http://udacity.com/cs101x/urank/kathleen.html

print lucky_search(index, ranks, 'the')
#>>> http://udacity.com/cs101x/urank/nickel.html

print lucky_search(index, ranks, 'babaganoush')
#>>> None

```

上面的lucky_search()是我的思路，下面的是课程的solution，比我的简练
```
def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = page[0]
    for candidate in pages:
        if ranks[candidate] > ranks[best_page]
        best_page = candidate
    return best_page
```

## 6.10 Problem set 6 starred 
### 6.10.1Family tree
要求：
```
# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.

def ancestors(genealogy, person):


# Here are some examples:

print ancestors(ada_family, 'Augusta Ada King')
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

#print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

#print ancestors(ada_family, 'Dave')
#>>> []

```
我的wrong code
```
def ancestors(genealogy, person):
    ancestors = []
    if person in genealogy:
        for e in genealogy[person]:
            if e not in ancestors:
                ancestors.append(e)
                return (genealogy, e)
```
solution
```
def ancestors(genealogy, person):
    if person in genealogy:
        first = genealogy[person]
        for i in first:
            first = first + ancestors(genealogy, i)
        return first
    return []
```
看着solution更改我的code
```
def ancestors(genealogy, person):
    ancestors_list = []
    if person in genealogy:
        for i in genealogy[person]:
            ancestors_list = ancestors_list + ancestors(genealogy, i)
    return ancestors_list
```
还是有错，我感觉是ancestors_list[]的位置不对
```
def ancestors(genealogy, person):
    if person not in genealogy:
        return []
    else:
        for i in genealogy[person]:
            ancestors_list = genealogy[person] + ancestors(genealogy, i)
        return ancestors_list
```
还是有错
```
#my_code，still wrong：

def ancestors(genealogy, person):
    if person in genealogy:
        first = []
        for i in genealogy[person]:
            first = genealogy[person] + ancestors(genealogy, i)
        return first
    return []

#output：
['Anne Isabella Milbanke', 'George Gordon Byron', 'Catherine Gordon', 'Captain John Byron']
['Anne Isabella Blunt', 'Wilfrid Scawen Blunt']
[]

#我的这段代码和下面的solution只有第三和第四行不一样，但是还是出错了。
# forum里有人回答了我的问题
#


#solution:

def ancestors(genealogy, person):
    if person in genealogy:
        first = genealogy[person]
        for i in first:
            first = first + ancestors(genealogy, i)
        return first
    return []
    
#output：
['Anne Isabella Milbanke', 'George Gordon Byron', 'Catherine Gordon', 'Captain John Byron']
['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King', 'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron', 'Catherine Gordon', 'Captain John Byron']
[]

```

这个问题应该分层，第一层是父母，第二层是父母的父母。我和solution的区别在于没有把`genealogy[person]`放在for循环外声明.
我无法通过第二个测试，一会把名字换成数字，这样再算一遍。

forum里有人回答了我为什么错了
It took me a while to see it, but when your for loop iterates over a person who has no record, then `ancestors(genealogy, i)`is empty which resets the entire list it has been building up to that point with only `genealogy[person]`.

在用recursion循环每个person的祖先时，有些祖先并不是genealogy这个`dictionary`的`keyword`,所以对于这样的祖先，会直接返回`[]`.虽然知道了出错的地方，但是解答者给出的答案，其该法我并没有看懂，不明白为什么在`return`后面加`genealogy[person]`.不加的话还是之前的错误答案，加了的话就能得到正确的结果。

明白了，那些`ancestors(genealogy, i)`返回是`[]`的结果，在回到上一层迭代后，用`return first + genealogy[person]`，其中的`genealogy[person]`就能把那些返回是`[]`的祖先加到`return`里，上上层的递归就能得到正确的祖先名。
```
def ancestors(genealogy, person):
    if person in genealogy:
        first = []
        for i in genealogy[person]:
            first = first + ancestors(genealogy, i)
        return first + genealogy[person]
    return []
```


### 6.10.2Khayyam Triangle

```
# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
    prev = e
    result.apend(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for unused in range(0, n):
        result.append(current)
        current = make_next_row(current)
    
    return result
    
    
#For example:

print triangle(0)
#>>> []

#print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

#print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

#print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

```

### 6.10.3 Only a Little Lucky
之前的lucky search 只返回一个最佳网页，但是这次我们要返回有关键字的所有网页，按照ranking value由大到小来排序，即倒序显示(in descending order)

下面是两个需要用到的function，一个是quick sort，根据ranking value来给pages(含有与keyword有关的url）排序，只不过下面的quick sort只是为了理解用的，并没有针对rank page做出相应修改。做出修改的排序算法order search里。还有一个是两种reverse list 的方法。

#### quick sort
```
# quick sort
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    # Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList



def main():
    myList = [7,2,5,1,29,6,4,19,11]
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)
```
####reverse a list python
```
>>> L = [0,10,20,40]
>>> L.reverse()
>>> L
[40, 20, 10, 0]
Or

>>> L[::-1]
[40, 20, 10, 0]
```
#### 整合所有功能的ordered_search
```
# Triple Gold Star

# Only A Little Lucky

# The Feeling Lucky question (from the regular homework) assumed it was enough
# to find the best-ranked page for a given query. For most queries, though, we
# don't just want the best page (according to the page ranking algorithm), we
# want a list of many pages that match the query, ordered from the most likely
# to be useful to the least likely.

# Your goal for this question is to define a procedure, ordered_search(index,
# ranks, keyword), that takes the same inputs as lucky_search from Question 5,
# but returns an ordered list of all the URLs that match the query.

# To order the pages, use the quicksort algorithm, invented by Sir Tony Hoare in
# 1959. Quicksort provides a way to sort any list of data, using an expected
# number of comparisons that scales as n log n where n is the number of elements
# in the list.

# The idea of quicksort is quite simple:

# If the list has zero or one elements, it is already sorted.

# Otherwise, pick a pivot element, and split the list into two partitions: one
# contains all the elements equal to or lower than the value of the pivot
# element, and the other contains all the elements that are greater than the
# pivot element. Recursively sort each of the sub-lists, and then return the
# result of concatenating the sorted left sub-list, the pivot element, and the
# sorted right sub-list.

# For simplicity, use the first element in the list as your pivot element (this
# is not usually a good choice, since it means if the input list is already
# nearly sorted, the actual work will be much worse than expected).

def ordered_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    result = quicksort(ranks, pages, 0, len(pages)-1) # this result is in the acending order
    return result[::-1] # reverse the list
    
def quicksort(ranks, myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(ranks, myList, start, end)
        # sort both halves
        quicksort(ranks, myList, start, pivot-1)
        quicksort(ranks, myList, pivot+1, end)
    return myList    
    
def partition(ranks, myList, start, end):
    pivot = ranks[myList[start]]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and ranks[myList[left]] <= pivot:
            left = left + 1
        while right >=left and ranks[myList[right]] >= pivot:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right    


# Here are some example showing what ordered_search should do:

# Observe that the result list is sorted so the highest-ranking site is at the
# beginning of the list.

# Note: the intent of this question is for students to write their own sorting
# code, not to use the built-in sort procedure.

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

print ordered_search(index, ranks, 'Hummus')
#>>> ['http://udacity.com/cs101x/urank/kathleen.html',
#    'http://udacity.com/cs101x/urank/nickel.html',
#    'http://udacity.com/cs101x/urank/arsenic.html',
#    'http://udacity.com/cs101x/urank/hummus.html',
#    'http://udacity.com/cs101x/urank/index.html']

print ordered_search(index, ranks, 'the')
#>>> ['http://udacity.com/cs101x/urank/nickel.html',
#    'http://udacity.com/cs101x/urank/arsenic.html',
#    'http://udacity.com/cs101x/urank/hummus.html',
#    'http://udacity.com/cs101x/urank/index.html']


print ordered_search(index, ranks, 'babaganoush')
#>>> None
```

这上面的解法代码较为复杂，不过到时普适性强，能用在各种方面。教程里的solution很简洁，没有更改原有pages的顺序，而是直接新建两个list（better，worse），把排好序的url放入这两个list。

```


def quicksort_pages(pages, ranks):
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = ranks[pages[0]   # find pivot
        worse = []
        better = []
        for page in page[1:]:
            if ranks[page] <= pivot:
                worse.append[page]
            else:
                better.append[page]
        return quicksort_pages(better, ranks) + [pages[0]] + quicksort_pages(worse, ranks)

def ordered_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    return quicksort_pages(pages, ranks)
```

# Lesson 7 problem
##7.4Remove Tags
```
# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(string):
    start = string.find('<')
    while start != -1:
        end = string.find('>')
        string = string[:start] + " " + string[end+1:]
        start = string.find('<')
    
    return string.split()

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']
```


## 7.5 Date Converter

```
# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

def date_converter(dic, data):
    first = data.find('/')
    second = data.find('/', first + 1)
    month = data[:first]
    day = data[first + 1 : second]
    year = data[second + 1 :]
    
    return day + " " + dic[int(month)]  + " " + year

def data_converter_2(dic, data):
    month, day, year = data.split('/')
    
    return day + " " + dic[int(month)]  + " " + year
    

print date_converter(english, '5/11/2012')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/5/1791')
#>>> 5 december 1791
```

## 7.7 Find and Replace


```
# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return [match, replacement]


def apply_converter(converter, string):
    #previous = None
    while True:#previous != string:
        first = string.find(converter[0])
        if first != -1:
            end = first + len(converter[0])
            string = string[:first] + str(converter[1]) + string[end:]
        else:
            break
    return string


# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).

```


##7.8 Longest Repetition

![Screenshot from 2015-12-01 19:44:22.png-82.7kB][2]
我的思路一开始就错了，不用想复杂的list和dict,多设几个参数就可以了。

```
# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

# 错误代码，思路错误
def longest_repetition(alist):
    previous = 0
    output = 0
    record = {}
    pre = None
    if len(alist) == 0:
        return None
    else:
        for e in alist:
            if e not in record:
                record[e] = 1  
                pre = e
            elif e in record and e == pre:
                record[e] += 1  
                pre = e            
            else: # e in record and e != pre:
                record[e] = 1
                pre = e          
    for n in record:
        if record[n] > previous:
            output = n
            previous = record[n]
    
    return output

# right solution
def longest_repetition(input_list):
    best_element = None
    length = 0
    current_element = None
    current_length = 0
    
    for element in input_list:
        if element != current_element:
            current_element = element
            current_length = 1
        else:
            current_length += 1
        if current_length > length:
            best_element = element
            length = current_length
            
    return best_element
            

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

```
## 7.9 Deep Reverse
![deep reverse.png-74kB][3]
如图所示，思路就是用recursion，但是不知道该怎么下手

```
# range(2, -1, -1) -> [2, 1, 0],从2开始，到-1结束，第三个args的-1是backwards的意思。
def deep_reverse(p):
    if is_list(p):
        result = []
        for i in range( len(p) - 1, -1, -1): 
            result.append(deep_reverse(p[i]))
        return result
    else:
        return p
```
我想多了，不用`[::-1]`这种tricky的方法，因为要求不能改变原list,所以创建一个`result`来存放结果。

下面是我的错误code和题目
```
# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)
    
    
    
def deep_reverse(out_list):
    result = []
    for e in out_list:
        if is_list(e):
            return deeop_reverse(e)
        else:
            return out_list[::-1]
        


#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]
```


# lesson 7: Changling practice problem
## 7.1 Stirling and Bell 
贝尔数和斯特灵数是组合数学中的两个概念。wiki:
> https://www.wikiwand.com/zh-cn/%E8%B4%9D%E5%B0%94%E6%95%B0

> http://www.wikiwand.com/zh-cn/%E6%96%AF%E7%89%B9%E7%81%B5%E6%95%B0#/.E7.AC.AC.E4.B8.80.E9.A1.9E

我的代码通过了测试……
通过测试有屁用！！
一开始的思路就是混乱的。我是先开始写`Stirling()`的递归部分，出错了才去找在哪些情况下停止，思路完全是错的。

既然是递归，一开始就应该考虑**base case**,之后才是**recursive case**。

![Stirling and Bell.png-108.1kB][4]

the lecture solution：

![Screenshot from 2015-12-03 18:44:41.png-133.5kB][5]

my solution and the question description
```
# One Gold Star
# Question 1-star: Stirling and Bell Numbers

# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group 
# of people Dave, Sarah, Peter and Andy could be split into two groups in 
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# so S(4,2) = 7

# If instead we split the group into one group, we have just one way to 
# do it.

# 1. Dave, Sarah, Peter, Andy

# so S(4,1) = 1

# or into four groups, there is just one way to do it as well

# 1. Dave        Sarah          Peter         Andy

# so S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n 
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# Write two procedures, stirling and bell. The first procedure, stirling 
# takes as its inputs two positive integers of which the first is the 
# number of items and the second is the number of sets into which those 
# items will be split. The second procedure, bell, takes as input a 
# positive integer n and returns the Bell number B(n).

def stirling(n, k):
    if n < k:
        return 0
    elif k == 1 or n == k:
        return 1
    else:
        return stirling(n-1, k-1) + k * stirling(n-1, k)
    

def bell(n):
    summ = 0
    for i in range(1, n+1):
        summ += stirling(n, i)
    return summ


print stirling(1,1)
#>>> 1
#print stirling(2,1)
#>>> 1
#print stirling(2,2)
#>>> 1
#print stirling(2,3)
#>>>0

#print stirling(3,1)
#>>> 1
#print stirling(3,2)
#>>> 3
#print stirling(3,3)
#>>> 1

#print stirling(4,1)
#>>> 1
#print stirling(4,2)
#>>> 7
#print stirling(4,3)
#>>> 6
#print stirling(4,4)
#>>> 1

#print stirling(5,1)
#>>> 1
#print stirling(5,2)
#>>> 15
#print stirling(5,3)
#>>> 25
#print stirling(5,4)
#>>> 10
#print stirling(5,5)
#>>> 1

#print stirling(20,15)
#>>> 452329200

#print bell(1)
#>>> 1
#print bell(2)
#>>> 2
#print bell(3)
#>>> 5
#print bell(4)
#>>> 15
#print bell(5)
#>>> 52
#print bell(15)
#>>> 1382958545

```
##7.2 Combating Link Spam
*What is reciprocal link?*
> A reciprocal link is an agreement between two webmasters to provide a hyperlink within their own website to each other's web site. Generally this is done to provide readers with quick access to related sites, or to show a partnership between two sites. Reciprocal links can also help to increase traffic to your web site in two ways. First you will probably have some viewers visit your site from clicking the reciprocal link directly. Secondly, most Internet search engines also take into account the number of web sites which contain links to your web site; the more hyperlinks to your site found, the higher up in the search engine rankings (depending on the search term) you'll find your site.

就是说两个网页之间互相添加对方的链接，以此来提高互相的排名，也就是link spam.


比如，if A->B is a reciprocal link, then the path length from B to A is equal to or below the collusion level, k. 
In other words, 当B to A 的link path <= k的时候，A->B 才是 reciprocal link。

举例
```
g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

k = 0, a->a link is reciprocal
k = 1, a->a(k=0), a->b, b->a
k = 2, a->a(k=0), a->b, b->a(k=1), a->c, c->d, d->a
```
我知道用递归，但是写不出来递归的code.我的失败code:
```
# Two Gold Stars
# Question 2: Combatting Link Spam

# One of the problems with our page ranking system is pages can 
# collude with each other to improve their page ranks.  We consider 
# A->B a reciprocal link if there is a link path from B to A of length 
# equal to or below the collusion level, k.  The length of a link path 
# is the number of links which are taken to travel from one page to the 
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A, 
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link 
# A->B, which includes one link and so is of length 1. (it requires 
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to 
#   - take an extra input k, which is a non-negative integer, and 
#   - exclude reciprocal links of length up to and including k from 
#     helping the page rank.

def delete_reciprocal_link(g, k):
    if k != int(k) and k < 0:
        return None
    else:
        if k == 0:
            for key in g:
                if key in g[key]:
                    g[key].remove(key)
        elif k == 1:
            for key1 in g:
                for key2 in g[key1]:
                    if key1 in g[key2]:
                        g[key1].remove(key2)
                        g[key2].remove(key1)
        else: # k == 2:
            for key1 in g:
                for key2 in g[key1]:
                    for key3 in g[key2]:
                        if key1 in g[key3]:
                            g[key1].remove(key2)
                            g[key2].remove(key3)
                            g[key3].remove(key1)
        return g    

def compute_ranks(graph， k):
    delete_reciprocal_link(graph, k)
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks





# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}

```

lecture method:
![Combating Link spam.png-348.7kB][6]
检查a->c是否是 reciprocal link？
在k<=2的时候，不是。
在k>=3之后，所有的link都会指向a，所以是reciprocal link.

solution code:
![Screenshot from 2015-12-03 19:44:03.png-215.4kB][7]
在`compute_ranks(graph, k)`里，修改一句。
```
def is_reciprocal_link(graph, source, destination, k):
    if k == 0:
        if destination == source:
            return True
        return False
    if source in graph[destination]:  # 针对k=1的情况
        return True
    for node in graph[destination]: # k >= 2的情况
        if is_reciprocal_link(graph, source, node, k-1):
            return True
    return False

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciprocal_link(graph, node, page, k): # 添加这句
                        newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
return ranks
```

## 7.3 Elementary Cellular Automaton
Question Illustration
![1.png-372.1kB][8]

![2.png-499.2kB][9]

Question Description:
```
# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton

# Please see the video for additional explanation.

# A one-dimensional cellular automata takes in a string, which in our 
# case, consists of the characters '.' and 'x', and changes it according 
# to some predetermined rules. The rules consider three characters, which 
# are a character at position k and its two neighbours, and determine 
# what the character at the corresponding position k will be in the new 
# string.

# For example, if the character at position k in the string  is '.' and 
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up 
# '..x' in the table below. In the table, '..x' corresponds to 'x' which 
# means that in the new string, 'x' will be at position k.

# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142

# To calculate the patterns which will have the central character x, work 
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.

# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all 
# lead to an 'x' in the next line and the rest have a '.'

# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)

# Note that the first position of the string is next to the last position 
# in the string.

# Define a procedure, cellular_automaton, that takes three inputs: 
#     a non-empty string, 
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and 
#     a positive integer, n, which is the number of generations. 
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.
```

我的solution,算然通过了所有测试，但是提交会出错，不管怎么是独立完成了这个程序。
```
def pattern_caculation(p):
    value = { 1:  ['...'], 
              2:  ['..x'], 
              4:  ['.x.'], 
              8:  ['.xx'], 
              16:  ['x..'], 
              32:  ['x.x'], 
              64:  ['xx.'], 
              128:  ['xxx']}
    binary = ''
    dic = {}
    new_value = {}
    
    if p < 0 or p > 255 or int(p) != p:
        return None
    else:
        binary = bin(p)[2:]  # e.x. binary = '1010'，但是这种情况不足8位，会出错
        binary = (8 - len(binary)) * '0' + binary #补足8位
    for i in range(7, -1, -1):
        dic[2**i] = binary[7-i]  # dic = { 128: '1', 64:'0',...}
    for i in dic:
        if dic[i] == '0':
            value[i].append('.')
        else:
            value[i].append('x')
    for i in value:  # value = { 1:  ['...', 'x'], ..., 128: ['xxx', 'x']}  
        new_value[value[i][0]] = value[i][10]
    return new_value  #new_value = { '...': 'x', ..., 'xxx': 'x'}  

    


def cellular_automaton(string, pattern_num, generation_time):
    current = string
    value = pattern_caculation(pattern_num)
    for not_used in range(0, generation_time): # 循环generation_time次
        next_line = '' # 每次循环都要把下一line初始化为empty
        for i in range(0, len(current)):  # 这个for循环是为了根据生成规则，得到next_line,
            if i == 0:  # 特殊情况，i是开头的时候，要有last char
                three_char = current[-1] + current[:2]
                next_line += value[three_char]
            elif i == len(current) - 1:  # 特殊情况，i是last char的时候，要有first char
                three_char = current[i-1] + current[i] + current[0]
                next_line += value[three_char]
            else:  # 普通情况
                three_char = current[i-1] + current[i] + current[i+1]
                next_line += value[three_char]
        current = next_line
    return current
```
看了lecture里的solution后，我的代码有很多可以简化的地方。

+ 首先是`pattern_caculation(p)`函数，利用`/`和`%`就能节省很多工作量。
```
def pattern_caculation(p):
    patterns = {}
    pattern_list = ['...', '..x', '.x.','.xx', 'x..', 'x.x','xx.', 'xxx']
    for i in range(-7, -1, -1):
        if p/(2**i) == 1:
            patterns[pattern_list[i]] = 'x'
            p = p - 2**i
        else:
            patterns[pattern_list[i]] = '.'
    reutrn patterns
```
+ 然后是三种字符的情况
针对i开头的情况，因为python可以直接用[i-1]找到last char，所以这个情况和普通情况是一样的。 而当i是last char的时候，用`string[(i+1)%n]`,其中`n = len(string)`.比如n=8时，i是从0到7，所以i+1是8，%n后正好是0,就能得到first char了。所以其实用one line 就可以了：
```
for i in range(0, n):
    pattern = string[i-1] + stirng[i] + string[(i+1)%n]

```


lecture procedure:
![11.png-316.2kB][11]

![12.png-304.9kB][12]

Solution Code:

the function scheme:
![13.png-147.5kB][13]

the whole code:
![14.png-284kB][14]

# Final Project :  Gamer's Network
把string中的空格和comma去掉，把所有单词提取成一个list
```
my_string = "blah, lots  ,  of ,  spaces, here "
[x.strip() for x in my_string.split(',')]
```

project description：
```
# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
```
## `create_data_structure(string_input)`
descprition
```
# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

def create_data_structure(string_input):
    return network
    
# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

```
我的代码
```
def extract_sentence(sentence):  # sentence: 'John is connected to Bryant, Debra, Walter'
    s = sentence
    user = None
    friends = []
    games = []
    if 'connected' in s: 
        user = s[:s.find('is') - 1]  # -1是为了除去is前的空格，只得到名字。'Levi'
        name_string = s[s.find('to') + 3 :] # 'Ollie, John, Walter'
        friends = [x.strip() for x in name_string.split(',')] 
        return user, friends, 0  # 0 represent this sentence is about friend
    else: # this sentence is about games
        user = s[:s.find('likes') - 1]
        name_string = s[s.find('play') + 5 : ] # 'The Movie: The Game, The Legend of Corgi, Dinosaur Diner'
        games = [x.strip() for x in name_string.split(',')] 
        return user, games, 1  # 1 represent this sentence is about games

#print extract_sentence('John is connected to Bryant, Debra, Walter')
#print example_input.split

def insert_into_network(network, user, items, num):
    if user not in network or len(network[user]) <= 1:  # 这种方法有缺陷，如果一开始是game，想要插入network[A][1]会出错，因为还没有[A][0]
       # 这里除了bug,当第一次有了user后，items是games时，会直接进入下面else的部分，无法创建network[user][1]
        if not num:  # this sentence is about friends
            network[user] = []  # 这个语句必须放在if里，要是放在if上面，games会把friends覆盖
            network[user].append(items)
        else:    # this sentence is about games
            network[user].append(items)
    else:    # if user is already in the network
        if not num:  #  friends
            for item in items:
                if item not in network[user][0]:
                    network[user][0].append(item)
        else:  # games
            for item in items:
                print item
                if item not in network[user][1]:
                    network[user][1].append(item)
    return

def create_data_structure(string_input):
    if len(string_input) == 0:
        return None
    sentences = string_input.split('.')  # 记住，用'.'分句后，最后一个句号分局后还会有一个empty string,''
    sentences = sentences[:-1]
    network = {}
    for sentence in sentences: 
        user = None
        items = []
        num = None
        user, items, num = extract_sentence(sentence)
        insert_into_network(network, user, items, num)      
    return network
```
通过上面的create函数，得到了network,结构如下。`network[user][0]`是connection（friends），`network[user][1]`是games。
```
{'Freda': [['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']], 

'Ollie': [['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']], 

'Debra': [['Walter', 'Levi', 'Jennie', 'Robin'], ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']], 

'Olive': [['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']], 

'Levi': [['Ollie', 'John', 'Walter'], ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']], 

'Jennie': [['Levi', 'John', 'Freda', 'Robin'], ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']], 

'Mercedes': [['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']], 

'John': [['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']], 

'Robin': [['Ollie'], ['Call of Arms', 'Dwarves and Swords']], 

'Bryant': [['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 

'Walter': [['John', 'Levi', 'Bryant'], ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']]}
```



##`get_connections(network, user)`
description:
```
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user not in network:
        return None
    else:
        connections = network[user][0]
        if len(connections) == 0:
            return []
	return network[user][0]

print  get_connections(network, 'Freda')   
```
##`get_games_liked(network, user)`
把上面那个改下变量名就可以了。
description:
```
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user not in network:
        return None
    else:
        games = network[user][1]
        if len(games) == 0:
            return []
	return network[user][1]
```
##`add_connection(network, user_A, user_B)`

```
add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    elif user_B in network[user_A]:
        return network
    else:
        network[user_A][0].append(user_B)
	    return network
```
##`add_new_user(network, user, games)`

```
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user in network:
        return network
    else:
        network[user] = [[]]
        network[user].append(games)
        return network
```

## `get_secondary_connections(network, user)`

```
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    secondary_conn = []
    if user not in network:
        return None
    elif len(network[user][0]) == 0:
        return []
    else:
        primary_conn = network[user][0]
        for person in primary_conn:
            for secondary_person in network[person][0]:
                secondary_conn.append(secondary_person )
        return secondary_conn
```

## `connections_in_common(network, user_A, user_B)`

```
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B):
    num = 0
    if user_A not in network or user_B not in network:
        return False
    else:
        A_friends = network[user_A][0]
        B_friends = network[user_B][0]
        for person in A_friends:
            if person in B_friends:
                num += 1
    return num
```

##`path_to_friend(network, user_A, user_B)`
```
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def path_to_friend(network, user_A, user_B):
	# your RECURSIVE solution here!
	return None
```
**Default Parameter Values in Python**
```
>>> def function(data=[]):
...     data.append(1)
...     return data
...
>>> function()
[1]
>>> function()
[1, 1]
>>> function()
[1, 1, 1]
```
也就是说，在*Default Parameter*只是在一开始定的值而已，它会随程序的运行不断改变，是mutable的。

网上找的代码，写得很好，非常厉害。这里是[地址](https://github.com/tylucaskelley/courses/blob/master/cs/udacity/cs101-intro-cs/code/final-project/social-network.py).
```
def path_to_friend(network, start, end, path=None):
    """Get a possible path from one user to another, based on their connections.
    Keyword arguments:
    network -- a dictionary containing users' connections and games
    start -- the name of a person in the network
    end -- the name of a person in the network
    path -- history (default = [])
    """
    if (start not in network) or (end not in network) or (start == end): 
        return None

    if path is None: # 如果出现上面几种情况，reset path，重新开始找path
        path = []
    path = path + [start]

    if end in network[start][0]:
        return path + [end]

    for node in network[start][0]:
        if node not in path:  # 这个语句避免了出现闭环
            newpath = path_to_friend(network, node, end, path)
            if newpath:
                return newpath
    return None
```

  [1]: http://static.zybuluo.com/bramble/xnfi2wg04u95dyjinbb1ia1i/Screenshot%20from%202015-12-01%2019:44:22.png
  [2]: http://static.zybuluo.com/bramble/xnfi2wg04u95dyjinbb1ia1i/Screenshot%20from%202015-12-01%2019:44:22.png
  [3]: http://static.zybuluo.com/bramble/ydpody8hs7v4vthpyduz4o2l/deep%20reverse.png
  [4]: http://static.zybuluo.com/bramble/6ku05c6binvotqeri3fzsogv/Stirling%20and%20Bell.png
  [5]: http://static.zybuluo.com/bramble/dejgyxiko8xmk1vpveo1x6h1/Screenshot%20from%202015-12-03%2018:44:41.png
  [6]: http://static.zybuluo.com/bramble/cd8elkuush4560e8sq20i4h4/Combating%20Link%20spam.png
  [7]: http://static.zybuluo.com/bramble/0ovg0lahqqaf8t7mpmjh41q8/Screenshot%20from%202015-12-03%2019:44:03.png
  [8]: http://static.zybuluo.com/bramble/pc6m1yymge6xz14pl69jujzv/1.png
  [9]: http://static.zybuluo.com/bramble/hxyov2u9xi3aghrx300m1591/2.png
  [10]: http://static.zybuluo.com/bramble/xnfi2wg04u95dyjinbb1ia1i/Screenshot%20from%202015-12-01%2019:44:22.png
  [11]: http://static.zybuluo.com/bramble/qkxryrat4m0by71qjih59d8y/11.png
  [12]: http://static.zybuluo.com/bramble/qj88lun34jv2maxshygqzka1/12.png
  [13]: http://static.zybuluo.com/bramble/n9uy0wv7bmttfxd7ix8fmnvi/13.png
  [14]: http://static.zybuluo.com/bramble/lood338u1ts1l0ngp5jepl24/14.png