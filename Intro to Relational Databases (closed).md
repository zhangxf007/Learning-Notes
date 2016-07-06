# Intro to Relational Databases (closed)

标签（空格分隔）： Udacity

---
[TOC]

```
The exact list of types differs from one database to another. For a full list of types, check the manual for your database, such as this one for PostgreSQL.

Text and string types

text — a string of any length, like Python str or unicode types.

char(n) — a string of exactly n characters.

varchar(n) — a string of up to n characters.

Numeric types

integer — an integer value, like Python int.

real — a floating-point value, like Python float. Accurate up to six decimal places.

double precision — a higher-precision floating-point value. Accurate up to 15 decimal places.

decimal — an exact decimal value.

Date and time types

date — a calendar date; including year, month, and day.

time — a time of day.

timestamp — a date and time together.
```
# lesson 2 
## All the tables in the zoo database

**animals**

This table lists individual animals in the zoo. Each animal has only one row. There may be multiple animals with the same name, or even multiple animals with the same name and species.

- name — the animal's name (example: 'George')
- species — the animal's species (example: 'gorilla')
- birthdate — the animal's date of birth (example: '1998-05-18')

**diet**

This table matches up species with the foods they eat. Every species in the zoo eats at least one sort of food, and many eat more than one. If a species eats more than one food, there will be more than one row for that species.

- species — the name of a species (example: 'hyena')
- food — the name of a food that species eats (example: 'meat')

**taxonomy**

This table gives the (partial) biological taxonomic names for each species in the zoo. It can be used to find which species are more closely related to each other evolutionarily.

- name — the common name of the species (e.g. 'jackal')
- species — the taxonomic species name (e.g. 'aureus')
- genus — the taxonomic genus name (e.g. 'Canis')
- family — the taxonomic family name (e.g. 'Canidae')
- t_order — the taxonomic order name (e.g. 'Carnivora')

 If you've never heard of this classification, don't worry about it; the details won't be necessary for this course. But if you're curious, Wikipedia articles Taxonomy and Biological classification may help.

**ordernames**

This table gives the common names for each of the taxonomic orders in the taxonomy table.

- t_order — the taxonomic order name (e.g. 'Cetacea')
- name — the common name (e.g. 'whales and dolphins')

##The SQL for it

And here are the SQL commands that were used to create those tables. We won't cover the create table command until lesson 4, but it may be interesting to look at:
```
create table animals (  
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);  

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);
```       
*Remember: In SQL, we always put string and date values inside single quotes.*

##The Experiment Page(一些SQL语法实例)

这些全是python语法，所以要注意缩进
```
# Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
# You'll see the results below.  Then try your own queries as well!

#没看懂这个max的选取方法
QUERY = "select max(name) from animals;"

#选取10行
QUERY = "select * from animals limit 10;"

#以日期排序
QUERY = "select * from animals where species = 'orangutan' order by birthdate;"

#日期倒序排序
QUERY = "select name from animals where species = 'orangutan' order by birthdate desc;"

#没看懂offset什么意思嘛
QUERY = "select name, birthdate from animals order by name limit 10 offset 20;"

#min的选取规则是什么，group又是什么
QUERY = "select species, min(birthdate) from animals group by species;"

#count(*)什么意思
QUERY = '''
select name, count(*) as num from animals
group by name
order by num desc
limit 5;
'''
```

## Select Clauses

Here are the new select clauses introduced in the previous video:

... limit count 
Return just the first count rows of the result table.

... limit count offset skip 
Return count rows starting after the first skip rows.

... order by columns 
... order by columns desc 
Sort the rows using the columns (one or more, separated by commas) as the sort key. Numerical columns will be sorted in numerical order; string columns in alphabetical order. With desc, the order is reversed (desc-ending order).

... group by columns 
Change the behavior of aggregations such as max, count, and sum. With group by, the aggregation will return one row for each distinct value in columns.

##Insert - Quiz
The basic syntax for the insert statement:

insert into table ( column1, column2, ... ) values ( val1, val2, ... );

If the values are in the same order as the table's columns (starting with the first column), you don't have to specify the columns in the insert statement:

insert into table values ( val1, val2, ... );

For instance, if a table has three columns (a, b, c) and you want to insert into a and b, you can leave off the column names from the insert statement. But if you want to insert into b and c, or a and c, you have to specify the columns.

A single insert statement can only insert into a single table. (Contrast this with the select statement, which can pull data from several tables using a join.)

##join
To join two tables, first choose the join condition, or the rule you want the database to use to match rows from one table up with rows of the other table. Then write a join in terms of the columns in each table.

For instance, if you want to join tables T and S by matching rows where T.color is the same as S.paint, you'd write a select statement using T join S on T.color = S.paint.

# lesson 3 python DB-API
##3.3 Trying Out DB-API
```
# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()
```
output
```
Row data:
[(u'Diane Paiwonski', 773217), (u'Harry Evans-Verres', 172342), (u'Hoban Washburne', 186753), (u'Jade Harley', 441304), (u'Jonathan Frisby', 917151), (u'Melpomene Murray', 102030), (u'Robert Oliver Howard', 124816), (u'Taylor Hebert', 654321), (u'Trevor Bruttenholm', 162636)]

Student names:
   Diane Paiwonski
   Harry Evans-Verres
   Hoban Washburne
   Jade Harley
   Jonathan Frisby
   Melpomene Murray
   Robert Oliver Howard
   Taylor Hebert
   Trevor Bruttenholm
```

##(prepa install the database
Udacity教程：https://www.udacity.com/wiki/ud197/install-vagrant

In Lessons 3 and 5 of this course, you'll use a virtual machine (VM) to run a database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer.  You can share files easily between your computer and the VM.

1, git
2,virtual box, ubuntu 14.04 必须从官方商店下，不能去virtualbox的官网下
3，vagrant， 去官网直接下最新版，debian
4，在bios里打开VT-x features， http://amiduos.com/support/knowledge-base/article/enabling-virtualization-in-lenovo-systems
5，Use Git/GitHub to fetch the VM configuration， https://github.com/udacity/fullstack-nanodegree-vm  这个库里有各种配置文件和上课用的东西
6，在terminal 配置，change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine.

----------------------------------------
Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type exit at the shell prompt.  To turn the virtual machine off (without deleting anything), type vagrant halt. If you do this, you'll need to run vagrant up again before you can log into it.
Files and commands we’ll be using (Relational Databases)

Files installed for this class are located in the /vagrant directory inside the virtual machine. Everything here is automatically shared with thevagrant directory inside the fullstack directory on your computer. Any code files you save into that directory from your favorite text editor will be automatically available in the VM.

If you’d like to see what was installed in the VM, look in /vagrant/pg_config.sh.

In this class you will mostly be running your work in Python from the command line. In addition you’ll use the psql program to interact with the PostgreSQL database.

To connect psql to the forum database for Lesson 3, type psql forum at the command line. To exit psql, type \q or Control-D (^D).

------------------------------------------

问题：vagrant up -> vagrant ssh -> cd vagrant, 找不到forum文件

解决：`cd ..` 退出到和`home`的同级菜单，发现另一个`vagrant`文件夹，进入这个文件夹，有`forum`文件

-------------------------------------------
##3.5 Running the Forum

vagrant@vagrant-ubuntu-trusty-32:/vagrant/forum$ ls
forumdb.py forum.py forum.sql

vagrant@vagrant-ubuntu-trusty-32:/vagrant/forum$ python forum.py
Serving HTTP on port 8000...
这个命令在本地8000建了一个forum的页面，可以在这个页面里写一些post

`crtl+c` kill 掉进程后，再`python forum.py`重新启动一下。reload网页，发现之前的post都消失了，数据库里并没有保存之前的post。

本课要解决这个问题。
----------------------------------------------------------------------------------------------
## 3.6 Hello PostgreSQL

启动PostgreSQL
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/forum$ psql forum
psql (9.3.10)
Type "help" for help.

forum=> 
```
可以在=>之后直接输入各种命令。

一个小问题
```
forum=> select * from posts  # 这个命令没有写完，所以没有返回结果，必须加`;`
forum-> ;
content | time | id 
---------+------+----
(0 rows)
```

## 3.7Give that App a Backend
###Instructor Notes

The **forum** database has already been created for you. Your code will need to connect to it using `psycopg2.connect("dbname=forum")` and then perform select and insert operations on the posts table.

The existing `GetAllPost`s function returns all the entries from a list. So its database version should return all the entries from the `posts` table.

And likewise, the existing `AddPost` function inserts an entry into a list.

You do not need to provide the **time** column when you insert a post. The table is set up to already provide a timestamp.

The existing `GetAllPosts` function sorts the posts using a Python `sort` function. When you implement this function using the database, can you avoid sorting in Python by doing it in SQL?

**Hint**: When performing insert operations consider using string substitution. Example:
```
name = "Jeffrey"
nickname = "Jeff"
print "Name is %s and nickname is %s" % (name, nickname)
The output would be: Name is Jeffrey and nickname is Jeff
```

###forumdb.py源代码
```
#
# Database access functions for the web forum.
# 

import time

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.
    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    posts.sort(key=lambda row: row['time'], reverse=True)
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.
    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())
    DB.append((t, content))
```
发现其实`GetAllPosts`其实并没有调用database，而且排序也不是用SQL，而是python。`AddPost`也要改，用SQL的方式来添加content。

修改后的
```
#
# Database access functions for the web forum.
# 

import time
import psycopg2

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    
    DB = psycopg2.connect("dbname = forum")
    c = DB.cursor()
    c.execute(
    	"select time, content from posts order by time desc"
    	)
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall()]
    #posts.sort(key=lambda row: row['time'], reverse=True)
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):

    DB = psycopg2.connect("dbname = forum")
    c = DB.cursor()
    c.execute("insert into posts(content) values('%s')" % (content)
			)
    #t = time.strftime('%c', time.localtime())
    #DB.append((t, content))
    DB.commit()
    DB.close()
```
### 漏洞，单引号和SQl injection（ Bobby Tables Destroyer of Posts）

但是还是有问题，两个。
+ 比如当我写一个post, it's not fun! ,会返回error。

因为`c.execute("insert into posts(content) values('%s')" % (content))`中`values('%s')`,会变为`value(' it's not fun! ')`,前两个单引号`'`已经构成了content,后面的`t`无法被识别。

+ 在forum里的post里写`'); delete from posts; --`，会把之前所有的post都删除。

把这个post放入value内，`value(' '); delete from posts; --`,整个语句就变为
```
c.execute("insert into posts(content) value(' '); delete from posts; --" % (content))
```
这样会执行`delete`语句

这是security hole, called an SQL injection attact.

> wiki:SQL攻击（SQL injection），简称注入攻击，是发生于应用程序之数据库层的安全漏洞。简而言之，是在输入的字符串之中注入SQL指令，在设计不良的程序当中忽略了检查，那么这些注入进去的指令就会被数据库服务器误认为是正常的SQL指令而运行，因此遭到破坏或是入侵。

解决方法：（范例）
```
plant = "pumpkin"
c = conn.cursor()
c.execute("insert into garden values(%s)", (plant,))
```
其中`(plant,)`是python tuple，
> A tuple is a sequence of **immutable** Python objects
The empty tuple is written as two parentheses containing nothing −
`tup1 = ()`;
To write a tuple containing a single value you have to include a comma, even though there is only one value −
`tup1 = (50,)`;

在`AddPost`中实际只要改一行即可，原代码
```
c.execute("insert into posts(content) values('%s')" % (content))

#改为
c.execute("insert into posts(content) values(%s)" , (content,)
```
要注意，因为是tuple，连接符不能用`%`，得用`，`

注意事项：

Warning Never, never, NEVER use Python string concatenation (`+`) or string parameters interpolation (`%`) to pass variables to a SQL query string. Not even at gunpoint.
The correct way to pass variables in a SQL command is using the second argument of the execute() method:

```
>>> SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
>>> data = ("O'Reilly", )
>>> cur.execute(SQL, data) # Note: no % operator
```

##3.8 漏洞  Spammy Tables

Paste this text into your forum (including the script tags!) and submit it:

```
<script>
setTimeout(function() {
    var tt = document.getElementById('content');
    tt.value = "<h2 style='color: #FF6699; font-family: Comic Sans MS'>Spam, spam, spam, spam,<br>Wonderful spam, glorious spam!</h2>";
    tt.form.submit();
}, 2500);
</script>
```
结果，每个2、3秒就会自动提交一个写有SPAM！ＳＰＡＭ！的ｐｏｓｔ，一直在运行。

##3.9 Updating Away the Spam - Exercise

###Instructor Notes

The syntax of the update statement:

`update table set column = value where restriction;`

The restriction works the same as in select and supports the same set of operators on column values.

-------------

The `like` operator supports a simple form of text pattern-matching. Whatever is on the left side of the operator (usually the name of a text column) will be matched against the pattern on the right. The pattern is an SQL text string (so it's in `'single quotes'`) and can use the % sign to match any sub-string, including the empty string.

If you are familiar with regular expressions, think of the % in `like` patterns as being like the regex .* (dot star).

If you are more familiar with filename patterns in the Unix shell or Windows command prompt, `%` here is a lot like * (star) in those systems.

For instance, for a table row where the column `fish` has the value `'salmon'`, all of these restrictions would be true:

- fish like 'salmon'
fish like 'salmon%'
fish like 'sal%'
fish like '%n'
fish like 's%n'
fish like '%al%'
fish like '%'
fish like '%%%'

And all of these would be false:

- fish like 'carp'
fish like 'salmonella'
fish like '%b%'
fish like 'b%'
fish like ''

###My Solution
在原有的execute语句前又添加了一句execute
```
def GetAllPosts():

    DB = psycopg2.connect("dbname = forum")
    c = DB.cursor()
    c.execute(
    	"update posts set content = 'cheese!' where content like '%spam%';"
    	) # 添加line
    c.execute(
    	"select time, content from posts order by time desc;"
    	)

    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall()]
    #posts.sort(key=lambda row: row['time'], reverse=True)
    DB.close()
    return posts
```
##3.10 Deleting the cheese

The syntax for the delete command:

delete from table where restriction ;

The restriction works the same way as in select, with the same set of operators allowed.
添加了一句
```
    c.execute(
    	"update posts set content = 'cheese!' where content like '%spam%';"
    	)
    c.execute(
    	"delete from posts where content like '%cheese%'; "
    	)
    c.execute(
    	"select time, content from posts order by time desc;"
    	)
```
如果用`where content = 'cheese'`的话，则不能删除`cheese!`或`cheeses`.

# Lesson 4: Deeper Into SQL
> In this lesson, you'll learn how to design and create new tables and databases. You'll learn about normalized design, which makes it easier to write effective code using a database. You'll also learn how to use the SQL join operators to rapidly connect data from different tables.

Rules for normalized tables

In a normalized database, the relationships among the tables match the relationships that are really there among the data. Examples here refer to tables in Lessons 2 and 4.

1. Every row has the same number of columns. 
In practice, the database system won't let us literally have different numbers of columns in different rows. But if we have columns that are sometimes empty (null) and sometimes not, or if we stuff multiple values into a single field, we're bending this rule.

    The example to keep in mind here is the diet table from the zoo database. Instead of trying to stuff multiple foods for a species into a single row about that species, we separate them out. This makes it much easier to do aggregations and comparisons.

2. There is a unique key and everything in a row says something about the key. 
The key may be one column or more than one. It may even be the whole row, as in the diet table. But we don't have duplicate rows in a table.

    More importantly, if we are storing non-unique facts — such as people's names — we distinguish them using a unique identifier such as a serial number. This makes sure that we don't combine two people's grades or parking tickets just because they have the same name.

3. Facts that don't relate to the key belong in different tables. 
The example here was the items table, which had items, their locations, and the location's street addresses in it. The address isn't a fact about the item; it's a fact about the location. Moving it to a separate table saves space and reduces ambiguity, and we can always reconstitute the original table using a join.

4. Tables shouldn't imply relationships that don't exist. 
The example here was the job_skills table, where a single row listed one of a person's technology skills (like 'Linux') and one of their language skills (like 'French'). This made it look like their Linux knowledge was specific to French, or vice versa ... when that isn't the case in the real world. Normalizing this involved splitting the tech skills and job skills into separate tables.


# Lesson 5 final project
## fetchall()
```
#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.close()
```
When above program is executed, it will produce the following result:
```
Opened database successfully
ID =  1
NAME =  Paul
ADDRESS =  California
SALARY =  20000.0

ID =  2
NAME =  Allen
ADDRESS =  Texas
SALARY =  15000.0

ID =  3
NAME =  Teddy
ADDRESS =  Norway
SALARY =  20000.0

ID =  4
NAME =  Mark
ADDRESS =  Rich-Mond
SALARY =  65000.0

Operation done successfully
```

http://www.tutorialspoint.com/postgresql/postgresql_python.htm

两个final project的实例
基础功能： 
https://github.com/jkrooskos/tournament_results/blob/master/tournament.py

完整功能：
https://benjaminbrandt.com/relational-databases-final-project/
