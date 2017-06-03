# Web Development（closed）

标签（空格分隔）： Udacity

---

Course Syllabus
2.1 Lesson 1: How the Web Works
2.2 Lesson 2: Forms and Input
2.3 Lesson 2a: Templates
2.4 Lesson 3: Databases
2.5 Lesson 4: User Accounts and Security
2.6 Lesson 5: APIs
2.7 Lesson 6: Caching
2.8 Lesson 7: Scaling Up
2.9 Final Project: Build a Wiki

[HTML Playgrount](http://scratchpad.io/merciful-scissors-2786)

[TOC]

#Lesson 1: How the Web Works

## 1.1 Introduction to the Web

![wd1.png-103.8kB][1]

- World Wide Web

![wd2.png-208.3kB][2]

![wd3.png-208.1kB][3]

- File Types

![wd4.png-185.7kB][4]

## 1.2 Components of the Web

![wd5.png-221.3kB][5]

The internet uses HTTP to communicate with you, your browser, and servers.

![wd6.png-329.6kB][6]

## 1.3 HTML Basics

![wd7.png-201.3kB][7]

Udacity提供了一个[HTML Playground](http://jsfiddle.net/WW3bh/),可以在这里做测试。

### 1.3.1 Intro to HTML Tags(介绍各种tags)

![wd8.png-188.1kB][8]

### 1.3.2 Bold Tag

![wd9.png-181.1kB][9]

放在`I am gona <b>fly</b>`，fly会以粗体显示

![wd10.png-251.2kB][10]

###1.3.3 Italics

![wd11.png-105kB][11]

![wd12.png-336.2kB][12]

tags 之间可以嵌套

![wd13.png-141.2kB][13]

![wd14.png-164.9kB][14]

### 1.3.4 Missing End Tag

![wd15.png-192.7kB][15]

## 1.4 HTML Attributes (tag中包含attribute)

### 1.4.1 Making Links
其中`href`叫做 Attribute

![wd16.png-192.2kB][16]

![wd17.png-234.9kB][17]

### 1.4.2 Adding Images

image不需要closing tag， 因为没有content. 这种没有content的tag, called **void tag**. 

这个叫`alt`的Attribute起一个预防的作用，如果图片不能顺利加载，就会显示这个`alt`里写这的文本内容。

![wd18.png-235.1kB][18]

![wd19.png-200.4kB][19]

### 1.4.3 Whitespace

可以用`<br>`表示一个回车，是void tag. 也可用`<p>`,但这个表示Paragraph，用在段落，要有content.

![wd20.png-296.5kB][20]

![wd21.png-363.7kB][21]

![wd22.png-323.5kB][22]

![wd23.png-161.8kB][23]

![wd24.png-409.6kB][24]

![wd25.png-203.7kB][25]

### 1.4.4 Inline vs Block

block 有 height和width，这些都是可以设定的，而inline只是行而已，没有那么多属性。

![wd26.png-173.3kB][26]

### 1.4.5 Span and Div

Span和Div里的`class`是Attribute, 这个`class`是调用css文件的意思。

![wd27.png-159.3kB][27]

## 1.5 HTML Document

### 1.5.1 Document Structure

- **doctype** : 这个类型在html5里更简洁
- **`<html>`** : 这个tag作用就是surround the entire document 
- **`<head>`** : 这个tag里面放一些meta-data, include JavaScript and CSS.
- **`<body>`** : the body tag is the actual contents of the document. And basically, we've been, we've been working just in the body tag in this lesson. And for most of this course, we're really just going to be focusing on generating the content that fits between the body tags.

![wd28.png-310kB][28]

本课程主要关注body tag里的内容

![wd29.png-187.1kB][29]

## 1.6 Introducing URLs

### 1.6.1 URL

For those of you wondering what an IP address is, wikipedia has this to say:

> An Internet Protocol address (IP address) is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. An IP address serves two principal functions: host or network interface identification and location addressing. Its role has been characterized as follows: "A name indicates what we seek. An address indicates where it is. A route indicates how to get there."
The URL is the human readable locator which resolves to a numerical IP Address and represents, as Steve says, "the location of the physical machine which has the document we want to fetch."

An example IPv4 address looks like this: 172.16.254.1

![wd30.png-220.8kB][30]

![wd31.png-234kB][31]

### 1.6.2 Query Parameters

- we add a parameter `p`, whose valse is `1`. 格式是`Name = value`
- we use `?` to separate query parameter from URL. 即`?`后的才是查询参数。
- All of the following parameters are separated from each other using ampersands. 即每个查询参数之间，用`&`分隔。
```
http://example.com//foo ? p = 1
```
![wd32.png-210.3kB][32]

那么这个Query Parameters有什么用？
when you make a request for this path, this is extra information the server gets, and there's all sorts of things you can do with this.具体的之后再讲，但要记住，they are separate from the path. But they are included in part of the whole URL that the server sees when you make a request. 
![wd33.png-211.9kB][33]

###1.6.3 Fragments

用`#`分割URL和Fragment。
A fragment is separated from the rest of the URL by a hash sign. A fragment is generally used to reference a particular part of the page you are looking at.

When you see it in the URL, it is not sent to the server when you make a request. The fragment purely exists in the browser.

If we had a URL with both queries and a fragment, the fragment follows the query parameters. It comes last.

![wd34.png-218kB][34]

### 1.6.4 Port


When you make a web request to a server, this is the host, the name of the machine or, or the location of the machine you're requesting.

In order to make an internet connection you need two things. You need one, the address of the machine, which is represented by the host And two, you also need a port. And by default the port equals 80. If you want to use a different port you can include it in the URL between the host and the path separated by a colon.

![we35.png-156kB][35]

**QUIZ**

The full url is `http://example.com:80/toys?p=foo#blah`

## 1.7 HTTP讲解
### 1.7.1 Get(the request line)

当发送一个URL的时候，会有一个request line，这个request line里有三部分：

1. method: GET(本节小标题),get the document from the server. 此外还有POST。The method line of an HTTP request is generally case-sensitive.
2. path: /foo，this is the document we request from the server. 
3. version: HTTP/1.1

那么，where is the host in this request line?
No, it's not there. But we have the path. The path is conneted to the host, your browser is connected to the host. 如果我们run the url, we made the connection. 

So, the host name is to make the connection, and the path is used for making the request.


![web37.png-238.3kB][36]

**QUIZ**

path的部分比较tricky. The fragments are not included in the path. They're never sent to the server. So when your browser makes a request, for this path, this is all it sends to example.com. The fragment and the hash mark stay purely on the client side, or in, also known as in the browser.

![web38.png-297.9kB][37]

**QUIZ: Most Common Method**

![web39.png-171.1kB][38]

### 1.7.2 Making Requests

The request line followed by a number of **headers**. And header has its own format: `Name: value`. like, `Host: www.example.com` or `User-Agent: chrome`.

![web40.png-186.2kB][39]

### 1.7.3 User Agent Header

这个user agent很重要，拿reddit举例。比如如果有恶意用户伪装成browser去访问reddit的话，可能会降低reddit的反应速度，对其他用户造成影响。那么，reddit 通过判断User agent是否合法，来block spammer. Googlebot是goole的搜索引擎，它的request 频率很高，也会slow down网站，所以通过检查user agent来降低request频率，减小对reddit的影响。

### 1.7.4 Valid Headers

The *name* must be a string of character, the *value* could be anything you wnat.

![web41.png-217.1kB][40]

### 1.7.5 HTTP Responses

根据request line, HTTP 在response的时候，会返回一条**status line**. 这个**status line**包括：HTTP version，status code, reason purose.

其中status code以1，2，3，4，5开头，每个代表不同意思。

### 1.7.6 Response Headers

![web43.png-233.5kB][41]

![web42.png-300.5kB][42]

## 1.8 Servers
### 1.8.1 Web Applications

现在基本所有的网站都是dynamic.
![web44.png-196.2kB][43]

**Dynamic Content Quiz**

![web45.png-192.5kB][44]

# Problem Set 1: Your first site

## 1.1 Google App Engine

![web46.png-322.5kB][45]

效果图，注意url，不是本地，要上传才行。
![web47.png-377.7kB][46]

## 1.2 create the project in local
去官网下了SDK（python版），解压后得到`google_appengin`directory, 放入`/home/xu/Udacity/web/google_appengine`. 运行`export PATH=$PATH:/home/xu/Udacity/web/google_appengine`把`google_appengine`添加到path中，这样就可以调用`google_appengine`文件夹中的一些命令了，比如`dev_appserver.py myapp`

在`/home/xu/Udacity/web/`创建了一个`hello_udacity`来存放app所需文件。
看这个教程[Hello, World! in 5 minutes](https://cloud.google.com/appengine/docs/python/)，在`hello_udacity`创建两个文件，`hello_udacity.py` and `app.yaml`，基本都是根据教程里的文件写的，只是把hello world 改成了 hello Udacity 而已。

---
这一部分我在印象笔记里也有写: *google app engine path setting on ubuntu 14 with zsh*.
这个GAE的地址，`/home/xu/Udacity/web/google_appengine`

在`～/.zshrc`打开*zshrc*. 添加一句：
```
export PATH="/home/xu/Udacity/web/google_appengine:$PATH"
```
再用`source .zshrc`更新

---

用`cd ..`回到web directory, run `dev_appserver.py hello_udacity/`. 这样本地的网页就建好了，在这个端口`http://localhost:8080/`.


## 1.3 upload the application
在google里注册google cloud platform, 在下面的页面中找到App Engine, create a new project and name it `hello-udacity`. 

回到terminal, 在`web` directory, run `appcfg.py -A YOUR_PROJECT_ID update hello_udacity/`, v这个会把本地的app推送到之前创建的project里。这下就可以在云端访问创建的网站了。

打开`http://_your-app-id_.appspot.com/`，能看到创建的网页。

![web51.png-57.3kB][47]

## 1.4 **Google App Engine Solution**

也可以设定一个port显示本地app
![web49.png-612.8kB][48]

![web50.png-246.9kB][49]

# Lesson 2 - Forms and Input
## 2.1 HTML Forms
### 2.1.1 Forms
最简单的form
```
<form>
    <input>
<form/>
```
有了`<input>`后，html会出现一个input box。

![web52.png-262.6kB][50]

**User Input**

![web53.png-259.8kB][51]

**Entering Input**
url里q的部分会变为input的内容，因为这个input box就是q.

![web54.png-456.4kB][52]

### 2.1.2 Submitting Input

![web55.png-233.7kB][53]

![web56.png-296.2kB][54]

submit和之前的enter没有什么不同，输入的东西还是在form里，我们希望把输入的东西存储到别的地方。
![web57.png-419kB][55]

### 2.1.3 The Action Attribute
在`<form>`里添加action这个attribute,就可以把submit的内容发送到action对应的url去。

![web58.png-294.7kB][56]

**quiz**
回跳转到google的搜索结果页面里。那么这个原理是什么，看下一节。
![web59.png-474.1kB][57]

![web60.png-442.1kB][58]

###2.1.4 URL Encoding

![web61.png-299.8kB][59]

三个单词之间为什么会有`+`呢？
这是因为url不允许有space（空格），所以brower 通过 URL encoding,turn spaces to pluses.
![web62.png-727.2kB][60]

`!`在url中用`%23`表示。
![web63.png-658.7kB][61]

##2.2  Hello Webapp World

通过具体的webapp来讲解。下图是google app engine页面的hello world例子

![web64.png-547kB][62]

```
app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
```

最下面的是URL Mapping Section. This line maps to a handler called `Mainpage`.而这个`Mainpage`继承了`webapp2.RequestHandler`.在class Mainpage里，有一个function `get`, 该function有两个功能。

按照官网的方法，创建helloworld文件夹，里面放入`helloworld.py`（上面的代码）和`app.yaml`两个文件，

### 2.2.1 Content Type

the first thing we'd like to do is take this form out of the temporary file we were playing with before and put it in our application.

现在我们的`play.html`代码如下：
```
<form action = "https://www.google.com/search">
	<input name = "q">
	<input type = "submit">
</form>
```
把这个form整合到上一节里的helloworld app里。
1. 创建变量form，把上面的html代码赋给它
2. 把`self.response.out.write('Hello, webapp World!')`改为`self.response.out.write(form)`.

但是运行后发现网页显示的是form的源码（raw html)，而不是input box。

![web65.png-573.2kB][63]

![web66.png-429.8kB][64]

那么原因在哪里？ 
是因为content type不对，function `get`里的第一行把数据类型限制为`text/plain`。
```
self.response.headers['Content-Type'] = 'text/plain'
```
如果把这行注释掉，google app engine会使用默认的数据类型，html,这样就能显示input box了。

![web67.png-353.6kB][65]

![web68.png-513.7kB][66]

这一次在input box中输入文本后也会跳转到goole search，It's working just as it did before, except the difference this time is the HTML is served by our live web application running on our machine instead of just a plain text file.

![web69.png-319.3kB][67]

### 2.2.2 More Handlers

把`form actoin`里的google search变为`/testform`. when we submit,it will submit to `testform` instead of to Google. 

Since our application can only respond to slash, we're going to need to add a handler for thant as well. 修改URL Mapping Section

由`app = webapp2.WSGIApplication([('/', MainPage)], debug = True)`改为
```
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler)],
	 debug=True)
```
`/testform` will be handled by the handler called **TestHandler**, which doesn't exist yet. Let's create that.

```
class TestHandler(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("q")
		self.response.out.write(q)
```
so we've added this new handler called **TestHandler**. This also has a method on it called `get`, like our other handler, and what this does is it sets a variable called `q`, which comes from `self.request`. Like **response** is the object that represents the response we're going to *send back to the client*, **request** represents the *request that came from the browser*, and you can call get on it to get different parameters, so in this case we're going to get the parameter q. And then all we're going to do is we're going to return on the response `self.response.out.write(q)`.

通过**request**查询结果，用**response**来返回结果，显示出来。

So if we go to our browser, we enter some words, and we hit submit,
we see the string hello world! You can see in the URL q = hello World! which is what we answered, so this is hitting the same URL we were hitting before, but this time there's a web application on the other end listening for requests and returning responses.

![web70.png-444.8kB][68]

**QUIZ：something neat**

把`TestHandler`改为下面的样子，在browser测试一下
```
class TestHandler(webapp2.RequestHandler):
	def get(self):
		#q = self.request.get("q")
		#self.response.out.write(q)

		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.response)
```
输入并submit后，we see the HTTP request. 能看到很多header.

我的：
![web71.png-38kB][69]

Steve的：
![web72.png-573.1kB][70]

解释原理：（为什么修改TestHandler后会有这样的效果）
here's what we did. We set the content type to text plain. If we hadn't done that, the response we were looking at **in HTML**, or in the browser would have looked weird, because the browser would have assumed it was HTML, and a lot of that text wouldn't have shown up. So, we set it to plain because I knew what we were going to do. Then instead of writing text or writing out our q parameter, we actually **wrote out this request object itself**, which is the *Python object that represents the request*, but conveniently it prints out very much like HTTP looks, which is not a coincidence.

看到HTTP request有什么用呢？

So--it's a handy little tool though when you're writing web applications and debugging, you want to see--you know--where something broke or what's going on, you can just print out the request and see.

好了，知道这个handy的方法后，我们把这两行注释掉，以后找debug还要用，把`TestHandler`恢复原状，so we could move on to something else.
```
class TestHandler(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("q")
		self.response.out.write(q)

		#self.response.headers['Content-Type'] = 'text/plain'
		*#self.response.out.write(self.response)
```

### 2.2.3 The Method Attribute

我们之前讲过一个method，叫**GET**

这一次我们在`helloworld.py`里添加一段代码，关于method.`<form method = "post" action = "/testform">`

![web73.png-700.6kB][71]

用`dev_appserver.py helloworld`运行后，在browser打开localhost:8080, submit something, 得到了error. 405是static code, 以4开头的static code are considered errors on our side, or on the browser's side.

![web74.png-26.6kB][72]

原因在于我们在form里设定的method是post，但是在class **TestHandler**里，我们定义的method 是**get**, 所以我们把get改为post.
`def get(self)` -> `def post(self)`

### 2.2.4 Methods and Parameters

这一次在browser里测试一下，一切正常，输入的内容被返回后输出。但这一次输入的内容并没有出现再url里。我们每次输入的内容存放在Parameters **p**里，而且会出现在url中，但这次根本没有显示**p**。

![web75.png-431kB][73]

那么**p**去哪了？

![web76.png-117.2kB][74]

用之前的方法返回request的格式为plain/text
![web77.png-79.4kB][75]

在browser里测试。可以看到在最后存放了一个p值。
We can see here, after all of the headers, we have some data:q=some+words--that's what I typed in my form. Remember, spaces get turned into pluses. So one of the big differences between GETs and POSTs is that GETs include parameters in the URL and POSTs include the data in the request body.

![web78.png-237.8kB][76]

### 2.2.5 Differences Between Get and Post
|GET|	POST|
| --------   | -----  |
| Parameters in URL	| Parameters in body|
| Used for fetching documents	|Used for updating data|
| Maximum URL length	|No maximum length|
| OK to cache	| Not OK to cache|
| Shouldn't change the server	| OK to change the server|

如果不遵守这些rules，就会有problems。

###2.2.6 Problems with Get
说实话没怎么看懂这个问题，懒得看就跳过好了。
We've talked about some of the differences between get and post, now let's look at what happens if you follow the rules for using get and post correctly.

Some years ago there was an online program for organising to-do lists and similar tasks called Basecamp, made by a company called 37Signals. Basecamp displayed the to-do list with a 'Delete' link alongside each item in the list.

Now, as we have seen, a normal link using the anchor tag makes get requests. These had been designed to make post requests to delete the item on the to-do list.

Another program which was out at that time was Google Web Accelerator. This was a browser plug-in that sat in the browser and while you were browsing the Google Web Accelerator would make the requests for any links on the page behind the scenes so that when you clicked the links the pages were ready to go.

The problem in this case was that the Google Web Accelerator was hitting the 'Delete' links in Basecamp, so users would go to their Basecamp page, look at their to-do list, and find that their items were deleting on their own. This was a major problem, and an example of what can go wrong if you use get requests to update data on the server. Instead of making links that alter the server, POST requests should be submitted with a form. The form can have special links that submit the form, making a POST request.

###2.2.7 When to Use Post and Get Quiz

Which of these are appropriate for GET requests?

- [X] Fetching a document.
- [ ] Updating data.
- [X] Requests that can be cached.
- [ ] Sending a lot of data to the server.

## 2.3 Passwords
We now want to introduce some more input types. The default type for an input element is "text". We left this out earlier, but we should really be specific with our types, especially as we are now going to introduce some more types.

If we go back to our basic play.html document, adding the type="text" attribute to the first input element gives us:
```
<form>
    <input type="text" name="q">
    <input type="submit">
</form>
```
The first new input type that we want to introduce is type="password". When the input field is a password, any text typed in the field appears as a row of dots:
```
<form>
    <input type="password" name="q">
    <input type="submit">
</form>
```
在browser测试一下，submit后会有什么效果？

哈哈，url暴露了password.
![web79.png-26.1kB][77]
you should use the password form element or the password input type when you're collecting passwords on your site, but you should know that that password is not sent securely to your Server. It's sent either in the URL or in a POST parameter, just like any other parameter--so it's really only to prevent somebody from looking over your shoulder.

##2.4 Checkboxes
Another input type is type="checkbox". You won't be surprised to learn that this will create a checkbox in your form:
```
<form>
    <input type="checkbox" name="q">
    <input type="submit">
</form>
```
If the checkbox is checked, the parameter appended to the URL will be q=on
![web80.png-23.5kB][78]

**quiz**

Checkboxes Quiz

What is the value of the q parameter when I submit the form with the checkbox unchecked?

1. Off.
2. The parameter doesn't appear at all.
3. The parameter is blank.
4. hunter2.

While writing server side software, check only for the condition q=on. If it's anything other than that, we can assume that the checkbox is unchecked. The reason we should do this is that different browsers handle unchecked checkboxes differently.
答案是2。如果没有check the box, url里不会显示q的值。

### 2.4.1 Multiple Checkboxes
Now we have seen how a single checkbox works, but you rarely see a single checkbox. They more commonly appear in groups. In the form below I have added two more checkboxes, named r and s, and also added a line break so we have a little separation from the Submit button:
```
<form>
    <input type="checkbox" name="q">
    <input type="checkbox" name="r">
    <input type="checkbox" name="s">
    <br>
    <input type="submit">
</form>
```

**Multiple Checkboxes Quiz**

When I select the first two checkboxes and click submit, what does the query section of the URL look like?

A: 前两个会出现在url里，状态为on
![web81.png-24.3kB][79]

##2.5 Radio Buttons

Radio buttons are also often used in forms. In this case the type="radio". The form below will display three radio buttons named q, r and s:
```
<form>
    <input type="radio" name="q">
    <input type="radio" name="r">
    <input type="radio" name="s">
    <br>
    <input type="submit">
</form>
```

When you load this in the web browser you will see three radio buttons. However, they do not behave as you would expect them to. Normally when we have radio buttons they behave as a group. and you can only select one button. What we have here are essentially checkboxes that cannot be unchecked.

**Grouping Radio Buttons Quiz**

Which of these yields the "group" behaviour from the radio buttons?

- Give them all the same id.
- Give them all the same name.
- Give them all the same group.
- include the` <input>`s in a `<group>` element.

A: the second one.

###2.5.1 Radio Button Values
So, if we give all the radio buttons the same name, they will behave as we expect radio buttons to do:
```
<form>
    <input type="radio" name="q">
    <input type="radio" name="q">
    <input type="radio" name="q">
    <br>
    <input type="submit">
</form>
```
However, a problem with this set up as it stands is that the parameter passed to the server will be q=on, no matter which of the 3 buttons is selected. 虽然这样radio button实现了只能选中一个button的正常功能，但我们不知道是哪个button选中了，url中只是显示q=on而已。


We can solve this problem using the `value` parameter:
```
<form>
    <input type="radio" name="q" value="one">
    <input type="radio" name="q" value="two ">
    <input type="radio" name="q" value="three ">
    <br>
    <input type="submit">
</form>
```

Keep in mind that the meaning of these values that are passed to the server for each radio button, may be whatever we make of it on the server side. So the server may do something different for each of the radio button selected (which is how it usually is).

**Radio Button Values Quiz**

What is the value of the of the **q** parameter when the form is submitted with the second button selected?

![web82.png-23.4kB][80]

##2.6 Label Elements
给每个button编号，好让选择界面更友好些。

In the previous example, we had our three radio buttons, but how is a user to know what the buttons represent and which button to select? That is what the label element is for.

In order to label each button we need to enclose it in a label element:
```
<label>
    One
    <input type="radio" name="q" value="one">
</label>
```
This will cause the label (in this case "One") to appear next to the button. Our complete form will now be:
```
<form>
    <label>
        One
        <input type="radio" name="q" value="one">
    </label>
    <label>
        Two
        <input type="radio" name="q" value="two">
    </label>
    <label>
        Three
        <input type="radio" name="q" value="three">
    </label>
    <br>
    <input type="submit">
</form>
```
The label doesn't have to match the value of the radio button, but they often do (or at least are often closely related).

![webb82.png-25kB][81]

## 2.7 Dropdowns

There is one last form element I would like to expose you to before we move on, and this is the dropdown.

A drop down has a form that looks like this:
```
    <select name="q">
        <option>One</option>
        <option>Two</option>
        <option>Three</option>
    </select>
```
The dropdown starts with a select element with a name attribute (we have been using q, so why break a winning streak), followed by a number of option elements, and finally the closing select element. Our form will now appear as:
```
<form>
    <select name="q">
        <option>One</option>
        <option>Two</option>
        <option>Three</option>
    </select>
    <br>
    <input type="submit">
</form>
```

**Dropdowns Quiz**
When we select Two from the dropdown, what is the value of the q parameter?

![web83.png-23.5kB][82]

### 2.7.1 Dropdowns and Values

I you want to have more descriptive text in the dropdown, but a different parameter value to appear in the URL, you can use the value attribute.
```
<form>
    <select name="q">
        <option value="1">Number One</option>
        <option value="2">Number Two</option>
        <option value="3">Number Three</option>
    </select>
    <br>
    <input type="submit">
</form>
```
Now, the text displayed in the dropdown will be Number One, Number Two..., but if we select Number Two from the list, the value of the query parameter attached to the URL will be simply q=2.

![web84.png-23.8kB][83]

**The Number One Quiz**

What will q's value in the URL be when we submit the form with the value Number One selected?

- Number One
- 1
- Nothing
- hunter2

A: the second one. 因为只有第一个设定了value=1.如果选第二个，url中会显示q=two.

![web85.png-87.9kB][84]

##2.8 Validation

Let's introduce a new concept. The concept of validation. Validation basically means verifying on the server-side that what we received is what we expected to receive.

Imagine the situation where we have set up our form, and the servers are programmed to respond in a particular way when q=on, and in another way when q is absent. But how will they respond if they receive a request where q=broken? The smart thing to do would probably be to treat the request as if q was unchecked in this case.

However, the point remains that just because we have designed a form to limit the responses that can be sent to our servers doesn't mean that a rogue user can't send a request directly to our servers with almost any arbitrary junk in it. It is up to us to make sure our servers can handle it.

![web86.png-72.1kB][85]

### 2.8.1 What is Your Birthday?

Let's go back to our very simple form as shown below:
```
import webapp2

form = """
<form method="post">
    <input name="q">
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)
app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
```

Notice that we removed the action /testform and so no longer need the handler which dealt with /testform.

the basic form
![web87.png-17.2kB][86]


Instead of a form with just a text-field, we are going to modify the form to ask for the user's birthday, and then validate their inputs. 

![web88.png-142kB][87]

![web89.png-89.4kB][88]

Then we add some lable to look easly, the form now looks like this:
```
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month">
    </label>
    <label>
        Day
        <input type="text" name="day">
    </label>
    <label>
        Year
        <input type="text" name="year">
    </label>
    <br><br>
    <input type="submit">
</form>
```

![web90.png-33kB][89]

**What is Your Birthday? Quiz**

What happens when I hit Submit?

- The form clears.
- We get an Error `405` because we never added a `post()` handler for `/`.
- We see the form values in the URL.
- The app counts down to my birthday.

A: the second one.
![web91.png-39.2kB][90]

### 2.8.2 Handling Posts
So let's add a post function to our page.
```
import webapp2

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month">
    </label>
    <label>
        Day
        <input type="text" name="day">
    </label>
    <label>
        Year
        <input type="text" name="year">
    </label>
    <br><br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
```

This will return the string "Thanks! That's a totally valid day!" to the browser when we post from the form, but what if the date isn't valid?

In the above code, the get method in the class MainPage draws the form and the post method gets called when we POST to the URL by submitting the form.

![web92.png-37kB][91]

month并不是valid,我们要判断是否valid.
![web93.png-19.6kB][92]

###2.8.3 Handling Bad Data Quiz

What are some possible solutions to users entering bad data into our form?

- Use dropdowns to limit what users can actually enter.
- Assume that users will only enter good data.
- Verify what the users enter and complain if the data is bad.
- Make values up.

A: the first and third.

Just because we can limit the input options of a form by using dropdowns doesn't mean that data that users submit will always be valid. Malicious users can make their own forms that post junk to any URL, including our server. Hence, verification of data at the back end should always be done.

### 2.8.4 Valid Month Quiz

Write a function that, given input from the user, returns whether or not it is a valid month.

用`string.capitalize()` function。This is my code.
```
# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    m = month.capitalize()
    if m in months:
        return m
    else:
        return None
```

the neat way
![web94.png-139.2kB][93]

我们想让他更user friendly, I'm going to build a dictionary--a mapping of just the first 3 letters of the month name to the month name itself, so we're only going to match on the first 3 letters of what the user enters.

the output shows the mapping.

![web95.png-198.6kB][94]

modify the main funciton(use advanced python techniques).
`short_month = month[:3].lower()`: 提取输入的前三个字母，并变为lower case.
`month_abbvs.get(short_month)`: use the GET function on a Python dictionary to see if those first 3 letters the user typed in is in that mapping, and if it is, we return the value from that mapping. That's what the GET function does. It says, if our key is in the mapping, return the value. Otherwise, return none. We're going to return either that value or none.

![web96.png-108.3kB][95]

### 2.8.5 Valid Day Quiz

Next, I'd like you to write a function that, given what the user types in for the day, returns whether that day is valid or not.
下面是我的代码
```
# -----------
# User Instructions
# 
# Modify the valid_day() function to verify 
# whether the string a user enters is a valid 
# day. The valid_day() function takes as 
# input a String, and returns either a valid 
# Int or None. If the passed in String is 
# not a valid day, return None. 
# If it is a valid day, then return 
# the day as an Int, not a String. Don't 
# worry about months of different length. 
# Assume a day is valid if it is a number 
# between 1 and 31.
# Be careful, the input can be any string 
# at all, you don't have any guarantees 
# that the user will input a sensible 
# day.
#
# Hint: The string function isdigit() might be helpful.

def valid_day(day):
    m = [i for i in range(1,32)]
    if day.isdigit():
        day_int = int(day)
        if day_int in m:
            return day_int
        else:
            None
    else:
        return None
```

教程里的方法
![web97.png-362.1kB][96]

###2.8.6 Valid Year Quiz

OK, one last function to write, this time to determine whether what the user entered for the year is valid.

my code:
```
# -----------
# User Instructions
# 
# Modify the valid_year() function to verify 
# whether the string a user enters is a valid 
# year. If the passed in parameter 'year' 
# is not a valid year, return None. 
# If 'year' is a valid year, then return 
# the year as a number. Assume a year 
# is valid if it is a number between 1900 and 
# 2020.
#

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year
```
![web98.png-147.2kB][97]

### 2.8.7 Checking Validation

流程示意图

![web99.png-230.7kB][98]

Now that we have the functions to check the users input, let's look at how they fit into the process. We have to do three things:

1. Verify the user's input.
2. On error, render the form again.
3. Include an error message

###2.8.8 Responding Based on Validation

We can now modify our post function to use the validation functions that we have just written and respond to the request appropriately based on the results of the validation. The new post function looks like this:

如果是无效的输入，form会自动清空，有效的话提示thanks！
```
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not(user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks! That's a totally valid day!")
```
The first line of the function calls the valid_month function that we just wrote, and sends the month parameter from the request as the function parameter. Similarly, the next two lines validate the day and the year of the user input. If these are not all valid, the function resends the form. If they are all valid, the function writes the string "Thanks! That's a totally valid day!".

##2.9 String Substitution

Before we go any further, I want to teach you a quick little Python thing about how to do string substitution. This will make generating our HTML a little bit more convenient.

If we have a string in Python something like this:
```
"<b> some bold text</b>"
```
This is exactly the kind of string that we are likely to be returning in our web app - a little bit of HTML with some contents. If we have a lot of bold text, this will get to be rather a pain if we have to generate this entire string every time. Instead, we can do something like this:
```
"<b>%s</b>" % VARIABLE
```
We still have the same basic structure of the string with the` <b>` tags creating some bold contents, but now that contents is represented by the `%s`. What this does is to substitute the %s with the variable %VARIABLE following the string. This is really convenient as we can now have a function that substitutes some variable into the string meaning that we don't have to keep building the string over, and over again.

### 2.9.1 String Substitution Quiz

Write a function 'sub1' that, given a string, embeds that string in the string: "I think X is a perfectly normal thing to do in public." where X is replaced by the given string.
```
given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    return given_string % s
```

### 2.9.2 Substituting Multiple Strings Quiz

If we wanted to substitute multiple strings, the procedure is very similar and will have a format similar to this:
```
"text %s text %s" %(VAR1, VAR2)
```
Write a function 'sub2' that, given two strings, embeds those strings in the string: "I think X and Y are perfectly normal things to do in public.", where X and Y are replaced by the given strings.

```
given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 % (s1, s2)
```

### 2.9.3 Advanced String Substitution

What happens if you want to include the same variable twice in the same string? We can do this by including a name identifier in parentheses:
```
"text %(NAME)s text" % {"NAME": value}
```

Now, instead of just having the variables at the end of the string, we can include a dictionary that maps NAME to a value. NAME can appear in the string multiple times, and we can have multiple names.
```
given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string2 % {'name': name, 'nickname': nickname}
```

###2.9.4 Substituting Into Our Form

Let's improve our form by making it a little more user friendly if the user enters invalid data.

First, let's modify the form itself to include a placeholder for the error message. We will use a `<div>` element as shown, and inside the` <div>` we will use string substitution to print our error message:
```
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month">
    </label>
    <label>
        Day
        <input type="text" name="day">
    </label>
    <label>
        Year
        <input type="text" name="year">
    </label>
    <div style="color: red">%(error)s</div>
    <br><br>
    <input type="submit">
</form>
```
Notice that we have used a simple css format attribute to make text within the `<div>` (the error message) appear in red.

Since we will be writing the form in a couple of places, it makes sense to create a function and then call the function when we need to write the form:
```
    def write_form(self, error=""):
        self.response.out.write(form %{"error": error})
```
The first parameter for all the functions inside a class should be self. The default value of the error parameter taken by the function is the empty string "". `form %{"error": error}`中第一个key `error`代表的是 `<div style="color: red">%(error)s</div>`中的`(error)`, 第二个value`error`是用户输入的一段错误信息，提醒用户输入错误，默认是`""` empty string. 而这个错误信息会出现在form中`<div style="color: red">%(error)s</div>`的位置上。

We can now use this function in the get and post functions where we need to write our form:
The first parameter for all the functions inside a class should be self. The default value of the error parameter taken by the function is the empty string "". We can now use this function in the get and post functions where we need to write our form:
```
import webapp2

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month">
    </label>
    <label>
        Day
        <input type="text" name="day">
    </label>
    <label>
        Year
        <input type="text" name="year">
    </label>
    <div style="color: red">%(error)s</div>
    <br><br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.out.write(form %{"error": error})

    def get(self):
        self.write_form()

    def post(self):
        self.write_form("That doesn't look valid to me, friend.")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
```
We have replaced the default empty string with our desired error message in the post function.

`get`function could draw a empty form, and `post` function could return a error message.

输入unvalid info后，input box会自动清空，并返回error message.

![web100.png-65.4kB][99]

但是我们希望input box不要清空，不然需要用户重新输入所有信息很麻烦。看下节。

###2.9.5 Preserving User Input

It would also be nice if, when we entered invalid data, the form left our original data so that we don't have to re-enter everything again. There is a way to do that, but first we need to learn a little bit more HTML.

![web101.png-28.8kB][100]

We have seen the value attribute applied to some form elements, now we are going to consider how it works with the text input element. A text input element has the form:
```
<input type="text" value="cool">
```
The value of the value attribute ("cool" in this example) is the default value for this element. This is the value that will appear in the text box when it is rendered in the browser. This could be used to render the form with the values that the user just typed in, so that they don't have to keep re-typing them. You can also use this to fill out form fields with default values if you know what the user is likely to enter into the box.

**Preserving User Input Quiz**

Which of theses is a correct input for preserving the user's month?

1. `<input value="%(month)s">`
2. `<input name="month">%(month)s</input>`
3. `<input name="month">`
4. `<input name="month" value="%(month)s">`

A：第四个

### 2.9.6  Problems With HTML Input

We are now in a position to modify our code the preserve the user inputs:
```
import webapp2

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br><br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form %{"error": error, "month": month, "day": day, "year": year })

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)
        else:
            self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
```
So, we have added values to our text input fields, and edited the write_form function (and its associated dictionary) to use the new parameters, **month**, **day**, and **year**.

Next, we edited the post function to use the new variable. To do this, we had to restructure the function and split the act of fetching the parameter out of the request from the act of testing the validity of the user data. We also had to change the validity check to use the correct updated variables.

Lastly, we added the variables *user_month*, *user_day* and *user_year* to the write_form call in the post function.

**Problems With HTML Input Quiz**

Suppose I enter the text `bar">what!` into one of the fields.

What happens when I click submit?

1. We see an error message and our input is in the form.
2. We see an error message, but the quote messes up our HTML.
3. There's an error on the server side.
4. The page renders blank.

A: 第二个

![web102.png-53.5kB][101]

因为function `post` 里的`self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)`，会把用户输入的内容毫无保留地输出。

### 2.9.7 Handling HTML Input

Consider the code that creates the month field in our form:
```
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
```
If we enter the text **November** into the month field is, the python code renders the value attribute to give the input field:
```
        <input type="text" name="month" value="November">
```
Which is what we would expect.

However, if we entered `foo">derp` into the field, the Python code renders the attribute to give the field:
```
        <input type="text" name="month" value="foo">derp">
```
The section of the element highlighted in red will be interpreted by the browser as the complete HTML tag!

Clearly, this isn't the behaviour we want. Worse than that, it allows an unscrupulous user who knows how our website works to enter HTML into the field and compromise the operation of the site. This is something we can't allow.

HTML Escaping

The problem is that we want to prevent the characters "> being used in our inputs. We can check for this, but the nicest way to fix this is through a method called **escaping**.

HTML allows you to change certain characters, or "escape" them. so that when the user types in the quote mark we can still show it in the text box. What we do is, instead of returning the quote in the HTML, we convert it to **`&quot;`**

Similarly, we can convert the closing angle-bracket, >, into **`&gt;`**

Some common escape characters are shown below:
```
" &quot;
> &gt;
< &lt;
& &amp;
```
Using these escape codes what is displayed is the relevant symbol, but they aren't actually HTML.

###2.9.8 Using HTML Escaping

Let's take a look at some of these substitutions in practice.

Type the following text into the text editor of your choice and save it as an html file:

What if I want to talk about HTML in HTML?

When you open the file in your browser you will see the text just as you typed it. Simple text is rendered as text in the browser. No surprises there.

Now, suppose you enclose the first HTML in angle brackets:

What if I want to talk about `<html>` in HTML?

When you load this into your browser, the `<html>` is not displayed. This is because your browser will have interpreted it as an HTML tag. However, if we use the escape codes from the table above:

What if I want to talk about `&lt;html&gt;` in HTML?

The text will now appear as we wanted it to, with the angle brackets in place, in the browser window.

**Using HTML Escaping Quiz**

What is the correct way to include the text `&=&amp;` in rendered HTML?

A:`&amp;=&amp;amp;`

###2.9.9 Implementing HTML Escaping Quiz

Implement the function escape_html(), which replaces :
`> with &gt; < with &lt; " with &quot; & with &amp;`

the solution
```
# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string

def escape_html(s):
    for (i, o) in (("&", "&amp;"),   #循环4次，每次替换一种
                   (">", "&gt;"),
                   ("<", "&lt;"),
                   ('"', "&quot;"))：
        s = s.replace(i, o)  # replace i with o
    return s
```
另一种方法更简单，直接import 一个cgi的库即可。

### 2.9.10 Problems Reinventing the Wheel

In fact, Python has a built in function to implement HTML escaping. in the cgi module. We can therefore implement the function much more easily as follows:
```
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)
```
Generally, it is a good idea to use the built in functions since they are often better and normally bug free. As Steve says: "A word to the wise: use the built-in pre-written escape functions whenever you can."

###2.9.11 Current Limitations

Now that we have the *escape_html()* function we can use it in the *write_form()* function of our form application:
```
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year)})
```
As you can see, we have applied the escape_html() function to each of the user inputs.

Now that we have the error handling more or less sorted, what can we do to improve the behaviour of the application when the user enters valid data?

In its current form the result page displayed when the user enters valid data has a number of limitations. Firstly, you can't link to it. Secondly, if you try to reload the page, your browser will display a message warning you that it needs to re-submit the data to refresh the page. This is because you are trying to reload a page that was created using a post.

两个问题，一个url没有显示成功等消息，没法向别人证明自己NB。另一个是在提交成功的界面reload时browser会发出警告，reload后还是先原先的界面。

###2.9.12 Redirection

The way to work around the problems we were having with the success page is to use a redirect. Instead of rendering the result in a post, we send them to another page that says "Thanks!". If the user's post is successful, the server sends a redirect message that causes the browser to get the "success" page.

原有的结构，two round trips
![web104.png-86.8kB][102]

new way, three round trips.虽然多一个，但能解决上面的两个问题。

![web105.png-87.2kB][103]

###2.9.13 Redirection Advantages Quiz

Why is it nice to redirect after a form submission?

- Because POSTs can't return HTML.
- So that reloading the page doesn't resubmit the form.
- To remove the form parameters from the URL.
- So we can have distinct pages for forms and success pages.

A：第二个和第四个

### 2.9.13 Implementing Redirection

Let's make the change to our application.

To make the change, we need to do three things. We need to:

1. make a "thanks" handler.
2. add the /thanks URL.
3. redirect to the /thanks URL.

The handler will look like this:
```
class ThanksHandler(webapp2.RequestHandler):

    def get(self)
        self.response.out.write("Thanks! That's a totally valid day!")
```
Next, we add the /thanks URL to the mapping area:
```
app = webapp2.WSGIApplication([('/', MainPage),
                              ('/thanks', ThanksHandler)],
                             debug=True)
```
Now we can modify the post() function to redirect to the /thanks URL:
```
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")
```
This gives the final version of our application below:
```
import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br><br>
    <input type="submit">
</form>
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                        'September', 'October', 'November', 'December']

def valid_day(day):
        if(day and day.isdigit()):
                day = int(day)
        if(day < 32 and day > 0):
                return day

def valid_month(month):
        if(month):
                month = month.capitalize()
        if(month in months):
                return month

def valid_year(year):
        if(year and year.isdigit()):
                year = int(year)
        if(year < 2020 and year > 1880):
                return year

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form %{"error": error,
                                       "month": escape_html(month),
                                       "day": escape_html(day),
                                       "year": escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/thanks', ThanksHandler)],
                             debug=True)
```                            

`app = webapp2.WSGIApplication([('/', MainPage),('/thanks', ThanksHandler)], debug=True)` 这个语句里，用`/` mapping `mainpage`, 用`/thanks` 代表 `ThanksHandler`.

提交成功后，url里出现了thanks,即`/thanks`. 这个页面是另一个网页，redirect 后的第三个html页面。reload后也不会出现browser警告的情况。

![web106.png-28.1kB][104]

# Problem set 2
## Rot13

设计一个form，能把输入的字母加13返回
![web107.png-66.1kB][105]

![web108.png-79.1kB][106]

## User Signup

# Lesson 2a: Templates 
##2a.1 Writing a Basic Form

从图中可以看到，一个web app的文件夹下有两个文件即可。`app.yaml`和`template.py`

![web125.png-382.7kB][107]

`app.yaml`:
```
application: template-lesson
version: 1
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /.*
  script: templates.app
```

`template.py`:
```
import os 

import webapp2

class Handler(webapp2.RequestHandler):  # simplfy the output
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

class MainPage(Handler):
	def get(self):
		self.write("Hello, Udacity!!!")  # use calss Handler output easily

app = webapp2.WSGIApplication([('/', MainPage)
							   ],
							   debug = True)
```
这样就能得到最简单的一个form,但是我们并没有使用html语言，而是直接通过class MainPage 输出了`"Hello, Udacity!!!"`.

![web128.png-12.5kB][108]

其实我们可以通过Handler直接return html,以下的修改全在`template.py`里。
1 我们先写个简单的html:
```
form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
<button>Add</button>
</form>
"""
```

再把`self.write("Hello, Udacity!!!")`改为`self.write(form_html)`。

`template.py`:
```
import os 

import webapp2

form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
<button>Add</button>
</form>
"""

class Handler(webapp2.RequestHandler): 
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

class MainPage(Handler):
	def get(self):
		self.write(form_html)  # return html

app = webapp2.WSGIApplication([('/', MainPage)
							   ],
							   debug = True)
```
刷新`localhost:8080`后得到页面

![web129.png-15.5kB][109]

因为we didn't set a method on that form, the default method is going tobe GET， which means if we submit this form, it'll just add that parameter to the URL.

![web130.png-39.4kB][110]

如果再Add一个food,比如orange, the url will update to `/food=orange`,之前的stea消失了。

##2a.2 Hidden Inputs
这次添加一个新的type,叫**hidden**. 在`form_html`里添加一句：`<input type="hidden name="food" value="egg">`。

```
form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
<input type="hidden name="food" value="egg">
<button>Add</button>
</form>
"""
```

`hidden`这个type把一些我们不想让用户看到的内容隐藏起来了，value这部分是hardcoded。但这部分内容能在url中看到，下图中的`&food=egg`就是hardcoded部分。而前面的`steak`是我们输入的。
![web133.png-10.8kB][111]

##2a.3 Shopping List Take 1

这一次我们要在`form_html`中添加`%s`，用来代表别的content，这个是python的语法。
把之前的hidden line改为%s,再添加几个其他的html
```
form_html = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

hidden_html = """
<input type="hidden name="food" value="%s"> //用%s,因为我们要往food里放很多东西
"""

item_html = "<li>%s</li>"

shopping_list_html = """
<br>  //回车
<br>
<h2>Shopping List</h2>  // h2是2号标题
<ul>  //unorder list,无序
%s   //表示要存放的content
</ul>
"""
```
然后我们要修改 `MainPage` handler去输出相应的html.把所有需要表示%s的变量名里都加上output以使区分。I'm going to prefix all of my strings that are holding output HTML with the word output.

```
class MainPage(Handler):
	def get(self):
		output = form_html
		output_hidden = "" #注释

		items = self.request.get_all("food")  #注释
		if items:
    		output_item = ""
    		for item in items:
    			output_hidden += hidden_html % item
    			output_item += item_html % item
    
    		output_shopping = shopping_list_html % output_item
    	    output += output_shopping
    	 
    	 output = output % output_hidden
    	 
    	 self.write(output)
```
- `output_hidden = ""`: I'm going to call that hidden HTML, and that will refer to that'll hold the content that we're going to sub into there, that'll be where our hidden inputs go.
- `items = self.request.get_all("food")` ：this line here gets all of the get parameters, or post parameters for that matter, called food. get_all basically means in, in App Engine, basically says, if there are multiple parameters with the same name, get all of them, and put them in a list. So items will be a list of all the food parameters that are in the URL.
- `output_hidden += hidden_html % item`: for each item in items add to the string hidden HTML substituting the food name. So basically output hidden will be a bunch of input type hiddens where the value is the food from the URL.
- `output_item += item_html % item`:I'm going to add another here we'll call output items, and also for each item and items, we're going to append another little bit of HTML. 此时Steve在form_output里添加了`item_html = "<li>%s</li>"` And this will be a list item that goes inside the shopping list HTML.**So we've got output_hidden which will be a bunch of hidden inputs and output_items will be a bunch of list elements.**
- `output_shopping = shopping_list_html % output_item` : we are going to use our shopping list HTML equals shopping list HTML substituting in our items and then our output.
- `output += output_shopping`:And then to the end of our output we're going to add our shopping list.
- `if items:` : we will only want to add things for our shopping list if they were actual items in the response. So if the response is empty, none of this is going to work. So let's make sure we do this properly.
- `output = output % output_hidden` :finally we're going to take our overall output and substitute in the, the hidden string that we've been building up here.

demo:
![web132.png-128.5kB][112]

##2a.4 Introducing Templates

我们用template简化上面的代码。我们用的templates library叫jinja2,这个是GAE中内建的。
![web134.png-77.2kB][113]

要想使用这个jinja2 library, 首先要在`app.yaml`里添加
![web135.png-111.3kB][114]

然后在`templates.py`里import jinja2
![web136.png-49.1kB][115]

我们要添加两行来initialize jinja2.
![web137.png-28.6kB][116]

I'm going to add a couple lines to initialize Jinja. These two lines are basically where you're using the OS library, which is built into Python. os.path.join, this concatenates two file names. And I'm, so I'm concatenating, `os.path.dirname(__file__)` is basically the directory that my current file is in. And then I'm adding the word templates to this. 

```
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
```
其中`os.path.join`把两个文件的名字连起来。`os.path.dirname(__file__)` 代表的当前的文件地址。不信的话打开terminal试验一下。
![web138.png-116.3kB][117]

the `os.path.dirname`, returns the directory of the current file. That's actually not going to work in the terminal, because underscore underscore file doesn't exist. But it exists when you're running a program.

So this whole line basically says, my template directory will be the current directory I'm in, slash templates. 
所以这行语句就是说`template_dir`指代的就是当前文件的path+文件名。

第二行
```
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
```

next we instantiate what we're going to call the Jinja environment, `jinja_env`. And, basically, this is a new jinja environment, and, we're going to use a `FileSystemLoader` using our `template_dir` which we just defined there. And this basically says, when we render templates Jinja's going to look for those templates in this directory. Current directory slash template.
这行语句创建了一个jinja的环境，写明了在渲染模板的时候，Jinja在`template_dir`这个directory里找template就行了。

Next, I'm going to add a couple of functions to my handler class here. I added two functions. `render_str` and `render`.
在`Handler`里添加两个function.
![web139.png-128.8kB][118]

第一个，`render_str()`:
```
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
```
 So the first function here is called `render_str`. And this basically takes a file name, and a bunch of extra parameters. This is the python syntax for, basically, extra parameters. And we use that Jinja environment that we created earlier above, and we call it get template and give it a file name. This basically causes Jinja to load that file and create a Jinja template. We store it in `t`, and we call `t.render` passing in the parameters that were passed into this function. And this just returns a string。
这个中， `jinja_env.get_template(template)`创建了一个jinja template, 并把这个template存放到`t`里。并用`t.render(params)`返回之前extra parameter `**params`.

另一个render function
```
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
```

I added this other render function, which I'll use all over the place, which again takes a template, a bunch of extra parameters and it just cause render stir this other function, but it also wraps itself in `self.write`. Which is the one that actually sends it back to the browser. 
这个function是把template返回到browser显示用的。

class `Handler` 里的这三个function非常常用，会贯穿整个课程。实际项目中也可以用
![web140.png-124.7kB][119]

接下来我们把`template.py`里的`form_html`这段html代码拿出来，单独放到另一个文件中保存成`shopping_list.html`格式，这样就能在sublime text里看到语法高亮了。

![web141.png-66.6kB][120]

##2a.5 Template Refactor

把html移出后，要重构一下class `MainPage`的代码。把之前写的全都注释掉。
![web142.png-165.3kB][121]

##2a.6  Variable Substitution (in Jinja)
介绍一些jinja的语法

虽然在html里添加了一句，但是`$$name$$`的部分在browser上是看不到，它只是个pram,我们得向里面传递一些东西。
![web143.png-29kB][122]

![web144.png-23.2kB][123]

我们在`templates.py`的`MainPage`里，给`name`添加点东西
![web145.png-14.1kB][124]

这里调用的render就是上面class `Handler`里的那两个render函数。参数传递的过程好好看一下那两个函数也就明白了那两个`**params**`和`**kw`就是用来传递name参数值的，没什么实际意义。其功能就是在渲染模板（render template）的时候，把参数`name`的value显示在browser上。

![web146.png-77kB][125]

##2a.7 Statement Syntax (in Jinja)

可以在`$% if_or_else %$`添加判断语句。
![web148.png-73.1kB][126]

更改`MainPage`, 令`n`为url里输入的值（用GET得到）
![web149.png-15.8kB][127]

修改`shopping_list.html`。
![web150.png-29.3kB][128]

## 2a.8 Testing Statement Syntax

reload page,得到*n does not equal 1*, make sense, 因为我们没有在url中给定n的值。
![web151.png-22.1kB][129]

在url中给定`n=1`，reload
![web152.png-20.8kB][130]

没有出现预想的`n equals 1`。为什么呢？
![web152.png-20.8kB][131]

##2a.9 Templates and Types

回答上一节的问题，是因为类型(type)不一样。
![web153.png-205.4kB][132]

从code中可以看到，我们从request中得到的n是string，而我们是要和int比较，所以得把string变成int.
![web154.png-15.5kB][133]

更改后
![web156.png-90.6kB][134]

reload page,得到了相应的结果
![web157.png-18.1kB][135]

输点别的东西，如果输入一个string，we don't get anything
![web158.png-11.7kB][136]

因为有error，我们想把"Steve" 变成int,所以出错了。这个bug之后再fix,讲这么多其实就是要让你注意type很重要，bug重灾区。

##2a.10 For Loop Syntax(in Jinja)

`$%`里面的`for statement` 和`endfor`是jinja语法。只要符合就执行body部分
![web160.png-85.2kB][137]

`<ol>`是order list的意思，自动显示序号。`<li> </li>`表示list，其中的`{{ }}`表示print,
![web161.png-47.6kB][138]

在url里输入n=10, reload page, 得到结果
![web162.png-50.2kB][139]

这是render后产生html文件
![web164.png-70.5kB][140]

把`<ol>`换成`<ul>`, 序号就变成了点
![web166.png-28.2kB][141]

##2a.11 FizzBuzz(一个测试小程序)
FizzBuzz是一个测试小程序，而且我们要用这个程序来练习jinja的if和for statement。
![web167.png-88.8kB][142]

![web168.png-65.6kB][143]

输出的html结果
![web169.png-78.3kB][144]

`template.py`里添加了一个新的handler。可以看到函数的最后一行是`self.render('fizzbuzz.html', n = n)`。这一次的quiz就是这个`fizzbuzz.html`怎么写？
![web170.png-109.8kB][145]

the solution
![web171.png-155.5kB][146]

## 2a.12 Shopping List Take 2
把`template.py`和`shopping_list.html`恢复到原状：
![web173.png-96.5kB][147]

![web174.png-28kB][148]

page回到了原来的状态：
![web175.png-22.2kB][149]

好了，我们在mainpage里添加一些之前添加过的functions。把之前uncomment的部分全删了，因为我们现在有了template，所以基本用不到。变成下面这个样子
![web176.png-19.8kB][150]

删掉`template.py`里的`hidden_html`部分，我们直接在`shopping_list.html`里添加相关内容就行了。
![web177.png-53kB][151]

在browser测试一下，发现输入的item通过`&`都显示在了url里
![web178.png-20.2kB][152]

查看source code，发现我们的刚才添加的function起作用了
![web179.png-70.2kB][153]

再向`shopping_list.html`添加一些内容，把我们输入的food显示出来
![web180.png-103.6kB][154]

在browser测试。成功了。出现在url里的food也出现在页面下方的shopping list里。如果我们把url里的内容删除，下方的内容也会消失。
![web181.png-30.7kB][155]

可以查看一下source code的情况
![web182.png-119.1kB][156]

总结一下，通过jinja 这个template，我们极大的简化了mainpage里的function，而且把html代码从`.py`中拿出来单独创建`.html`文件也使结构更加合理。

但是有个小问题，直接输入html语法后，template会直接将其render出来，无法去除格式。
![web183.png-64.1kB][157]

![web184.png-116.3kB][158]

查看source code发现，输入的内容直接放入html语法中。解决方法在下一节
![web185.png-48.9kB][159]

##2a.13 Escaping Templates

jinja有两种方式来解决这种问题。第一种方式是我们添加一个filter（built-in function in jinja)，叫做escape. 写法：`{{ item | escape }}`
![web186.png-111.5kB][160]

回到browser reload，发现成功了。
![web187.png-104.2kB][161]

查看source code,发现所有输入的内容都被转换过一次，就像我们之前做的那样
![web188.png-112.2kB][162]

但是老师不推荐上面这种方式，因为如果忘了会很麻烦。
所以，我们要介绍第二种方法来escape。直接在initialize jinja的时候自动escape，即在init语句里添加`autoescape = True`. 

![web189.png-44kB][163]

但是如果我们已经开启了`autoescape`,但又想要让某个comment直接展示出用户输入的html呢？

那么我们利用另一个filter，`| safe` (pipe safe). 可以理解成开启`autoescape`后是safe的，通过添加`| safe` 使其变为unsafe.负负得正
![web190.png-62kB][164]

## 2a.14 Helpful Tips
小贴士，Steve多年来的心得
![web191.png-53kB][165]

##2a.15 Template Inheritance

以下图为例进行解说。两个page有相同的`Title`和`Footer`,只有中间的`body`(即content)部分不一样，所以我们不希望每次打开这两个page的时候都重新render ``Title`和`Footer`。比如写一个`base.html`存放`Title`和`Footer`，把中间的`body`的不同内容写在`shopping_list.html`和`fizzbuzz.html`里。
![web192.png-83.7kB][166]

好了，下面是实操部分。
先创建一个`base.html`，包括了主要的html框架，别忘了开头要写doctype。其中最主要的是
```
{% block content %}
{% endblock %}
```

这两句是jinja的语法，意思是这里的content有外部的其他文件来填充
![web193.png-88.5kB][167]

好了，然后我们转到`shopping_list.html`里，通过修改代码来利用刚才写好的`base.html`.
在顶端写两个语句。`{% extends "base.html" %}` tell this template we are going to be a part o `base.html`. 即说明`shopping_list.html`是通过修改代码来利用刚才写好的`base.html`的一部分。现在reload browser的话只有标题，没有content：
![web197.png-26kB][168]

所以添加第二个语句：`{% block content %}`,这个语句matches `base.html`里的同一句话，最后要在结尾添加`{% endblock %}`。

![web195.png-114.5kB][169] 

我们可以这么理解，在`shopping_list.html`里，通过`{% block content %}`和`{% endblock %}`这两个语句把整个`shopping_list.html`里原先的内容都包括起来，传送到`base.html`里相应的位置里。

打开browser，reload发现所有的内容都出现了
![web196.png-67.1kB][170]

查看source code，可以看到内容分成了两部分，一部分是`base.html`里的，一部分是`shopping_list.html`里的。这样做结构清晰。这个功能广泛应用于blog.
![web198.png-151.4kB][171]

## 2a.16 FizzBuzz Inheritance

和`shopping_list.html`里的操作差不多
![web199.png-87.1kB][172]

## 2a.17 Conclusion
总结就是一句话，能用template的时候就直接用，别自己造轮子。
![web200.png-50.1kB][173]

#Lesson 3 - Databases
## 3.1 Databases (一些基本知识)

示意图
![web201.png-199.2kB][174]

### 3.1.1 What Is a Database?
![web202.png-67.3kB][175]

###3.1.2 Tables

下表讲了column, row。不同的数据类型：int, date, string.每当用户投票一次，就新建一个row。上面的column user连接到另一个table，即下面的table user。
![web203.png-318.7kB][176]

###3.1.3 Implementing Tables in Python
```
from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]


# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# make the function query() return the number of votes for the link whose ID is
# 15

def query():

```
solution
![web204.png-144.2kB][177]

### 3.1.4 Querying

把上一节的问题再复杂一点
```
# TASK
#
# make the function query() below return:
# - a list of Links submitted by user 62443
# - sorted by ascending submission time

from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]


# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# make the function query() return a list of Links submitted by user 62443, by
# submission time ascending
def query():

```
solution
要求是返回用户ID是62443的link,按升序排列。
返回的结果有三个link，但是从这里我们也可以发现写一个函数，再按升序排列是很麻烦的。所以我们才用database来简化这些操作。
![web205.png-591.6kB][178]

### 3.1.5 Why Databases?

除了操作复杂外，上一节写函数的方法最致命的是slow,当数据量很庞大时，会大量花时间。

![web206.png-27.6kB][179]

###3.1.6 Types of Databases

本课程用的是sqlite，因为不用处理大量的数据，这个很方便。
![web207.png-79.6kB][180]

###3.1.7 SQL
SQL也是一个language.
A basic SQL query may look something like this:
```
SELECT * FROM links where id = 5;
```
What this is actually saying is:

SELECT (i.e. fetch data) * (i.e. all columns) FROM links (i.e. from the table 'links') WHERE id = 5 (i.e. where the value in the id column is equal to 5).

The query can be considered as several parts:

SELECT * is what we are retrieving. The * could actually be a list of specific columns. So, if you just wanted to retrieve the URL from table links, you would enter SELECT url.

FROM links is where we will retrieve the data from.

WHERE id = 5 is what is known as a 'constraint', which limits which rows will be returned by the query.

![web208.png-186.2kB][181]

##3.2 Databases in Python
###3.2.1 Databases in Python

cursor储存的data是tuple,tuple使用`()`包起来的。
![web209.png-488.8kB][182]

我们也可以把tuple变成list，`link = Link(*link_tuple)`把tuple变成list,`Link`是已经定义好的class,具体可见下面的代码。不怎么明白的话直接查文档。
![web210.png-111.7kB][183]

We can use SQL in Python by importing the module SQLite3 which is built into Python:

import sqlite3

This will allow us to use SQLite in Python. In the Python code used for the last examples, we have added some code to make - and populate - an in-memory SQL database:
```
# make and populate a table
db = sqlite3.connect(':memory:')

db.execute('create table links ' +
          '(id integer, submitter_id integer, submitted_time integer, ' +
          'votes integer, title text, url text)')

for l in links:
    db.execute('insert into links values (?, ?, ?, ?, ?, ?)', l)

# db is an in-memory sqlite database that can respond to sql queries using the
# execute() function.
```
The db variable represents our SQLite database.

The SQL code that actually creates the table is:
```
create table links (id integer, submitter_id integer, submitted_time integer, votes integer, title text, url text)
```
The fields are those we have seen before, but notice that the data type is specified.

To run SQL code on db within Python, we use the execute() function. To run the SQL statement we saw earlier we would simply enter the code as:
```
c = db.execute("select * from links where id = 5")
```
c is what is known as a "cursor" to the results of the query. The cursor is essentially a position in the database.

We can now use the fetchall() function on the cursor, c, to load all of the data from the database into this list of results. These results won't be Links; rather, they'll be tuples.

Putting a * in front of a tuple and passing it to a function the arguments get put in place to create the links. For example the object constructor:
```
link = Link(*link_tuple)
```

下面是完整的代码，注释部分很重要
```
from collections import namedtuple
import sqlite3

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]

# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# make and populate a table
db = sqlite3.connect(':memory:')
db.execute('create table links ' +
          '(id integer, submitter_id integer, submitted_time integer, ' +
          'votes integer, title text, url text)')
for l in links:
    db.execute('insert into links values (?, ?, ?, ?, ?, ?)', l)

# db is an in-memory sqlite database that can respond to sql queries using the
# execute() function.
#
# For example. If you run
#
# c = db.execute("select * from links")
#
# c will be a "cursor" to the results of that query. You can use the fetchmany()
# function on the cursor to convert that cursor into a list of results. These
# results won't be Links; they'll be tuples, but they can be passed turned into
# a Link.
#
# For example, to print all the votes for all of the links, do this:
#
# c = db.execute("select * from links")
# for link_tuple in c:
#     link = Link(*link_tuple)
#     print link.votes
#
# QUIZ - make the function query() return the number of votes the link with ID = 2 has
def query():
    c = db.execute("PUT YOUR SQL HERE")

    link = Link(*c.fetchone())
    return link.votes
```

**Databases In Python Quiz**

Add the SQL code to make the function query() return the number of votes the link with ID = 2 has

![web212.png-138.5kB][184]

### 3.2.2  More Advanced SQL

We have seen how to select rows from a table where a specific constraint has been met:
```
select * from links where id = 5;
```
Let's look at how we can make this a little fancier. We can have more complex constraints, for example:
```
select * from links where submitter_id = 5 OR votes > 23;
```
This will return all the links submitted by user 5, or where the link has more than 23 votes. This allows us to ask quite sophisticated questions of our database.

### 3.2.3 Advanced SQL In Python Quiz

Make the function query() return the ID of the link that was submitted by user 62443 and has > 1000 votes.

![web214.png-122.8kB][185]

## 3.3 一些SQL语法
### 3.3.1 Order By

Next, let's see how to sort our results. Consider the SQL statement:
```
SELECT * FROM links WHERE votes > 10 ORDER BY votes;
```
This will select all the links with more than 10 links, and will order them by the number of votes. By default, the votes will be in ascending order. You can make the order explicit by specifying either ASC or DESC in the ORDER by clause:
```
SELECT * FROM links WHERE votes > 10 ORDER BY votes DESC;
```

**Order By Quiz**

Make the function query() return a list of the IDs of the links that were submitted by user 62443 sorted by submission time ascending.

The solution to this problem follows the format we have been using in earlier quizzes. If we were actually to make a function just to return the ids of the links this solution is actually quite wasteful.

If all we are interested in is a list of ids, we don't need to select * from links, we just need to select id:
```
select id from links where submitter_id = 62443 order by submitted_time asc
```
We also don't need to create a Link object for every row of the results, we can return the ids almost directly. Since the SQLite library in Python returns tuples of the results, and since we're only retrieving the id, we know that the first column will be the id. So what we need to do is to make a list of the first elements in the tuples for all the tuples in the cursor:
```
results = [t[0] for t in c]
```
This would make the solution:
```
def query():
    results = []
    c = db.execute("select id from links where submitter_id = 62443 order by submitted_time asc")
    results = [t[0] for t in c]
    return results
```
我用的是另一个方法
```
results = c.fetchall()
    return [i[0] for i in result]
```
如果直接打印出，result的话，是这样：`[(15,), (18,), (101,)]`，所以用`[i[0] for i in result]`来提取id,得到的结果是`[15, 18, 101]`。

###3.3.2 Joins

Let's see how we can create SQL statements involving multiple tables. Recall the structure of the **links** table that we saw earlier:

ID	Votes	User	Date	Title	URL
5	207	22	13:59	Zombie Dogs!	www.zombiedogs.com
6	0	27	20:00	...	...
...	...	...	...	...	...

The User ID in the links table refers to the ID field in the **users** table:

ID	Name	Date	Password
22	fred	5/20/05	hunter2
...	...	...	...

There should be a valid entry in the users table for every unique user on the system.

One of the things that you can do in most SQL databases is something called a **JOIN**. This is a SQL statement that involves two tables. Consider a basic SQL statement that looks something like:
```
SELECT * FROM link WHERE user_id = 22
```

This will return all of the links submitted by user 22. But what if we don't know the user's ID? What if we want to extract a list of all of the links submitted by users with the name 'Fred'?

In fact, there are a couple of ways we could achieve this. We could do a look up for the ID of the person name 'Fred' and then use this ID to search for links. Alternatively, instead of running two queries, we could combine this into one query:
```
SELECT link.* from links, users WHERE link.user_id = user.id AND user.name = Fred;
```
这个语句其实细节上有问题，可能是为了让学生便与理解，不必太当真。
In reality, however, we don't use joins very often in web software. We'll see the reasons for this later in this lecture.

###3.3.3 Indexes

So far, we have been doing what is known as **sequential scans**. A sequential scan is where you have a list of something, in this case links, and work through them in sequence. This works fine with relatively few items, but are very slow with large amounts of data (e.g. millions or even billions of links!).

An **index** on a computer is just like an index in a book. They make lookups faster. An index that you will already be familiar with in Python is the **hash table**. In Python you can have a dictionary that looks something like this:
```
index = {1: link1, 2: link2, 3: link3, ...} 
```
This provides a mapping of keys to values. You can do very fast lookups by writing something like:
```
index[2]
```
This refers to index key 2 of the hash table, and when we hash this value and find it in the hash table and return the value. We don't have to scan every value in the list, we can jump immediately to that element. This makes queries run much faster.

###3.3.4 Querying Links Quiz

Implement the function link_by_id() that takes a link's ID and returns the link itself.

![web215.png-156.2kB][186]

###3.3.5 Using Dictionaries As Indexes Quiz

Implement the function build_link_index() that creates a Python dictionary that maps a link's ID to the link itself.

通过把links里面的数据变成dictionry这种数据结构，即hash table，可以方便我们进行快速查询。

![web216.png-129.9kB][187]

###3.3.6 Lookup

We now have a function that will build our index. Let's use it. If we assign the result of the function build_link_index() to the variable link index, we can re-write our function link_by_id() as:
```
def link_by_id(link_id):
    return link_index[link_id]
```
Now this works fine as long as the value link_id is found in our data, but if the value isn't there then the Python code will generate an error.

It turns out that this is easy to fix. Instead of using the braces [] for link_index, we can use the Python hash table function get, thus:
```
def link_by_id(link_id):
   return link_index.get(link_id)
```
What `get` does is to check whether the key is in the hash table. If it does, it returns as before, otherwise it returns None.

So, we no longer have to scan all the way through the table when we want to run a query. Now we can just use the index.

这个方法很有用。如果直接给一个key去dict里找的话，如果这个key不存在于dict里，python就会返回一个error。所以我们用hash table里的GET来查找，如果找不到的话返回一个None. Neat!

**Lookup Quiz**

There's one more function that we need. Implement the function add_new_link() that both adds a link to the "links" list and updates the link_index dictionary.

![web217.png-273.9kB][188]

**Advantages Of Indexes Quiz**

Which of these statements are true?

- [x] Indexes increase the speed of database reads.
- [ ] Indexes increase the speed of database inserts.

第二个是错的，其实会decrease the spedd. 
They probably decrease the speed of database inserts. That is because when we're inserting a new round to our table, we probably also have to update all of our indexes, and that takes time. So there's a tradeoff.

We can probably get faster reads at the expense of slower inserts. And probably slower writes in general, for just updating a row, but there's actually a few perverse cases where an index can actually increase the speed of an update. 

Let me give you a little real demo of how indexes can affect things in the real world.(下一节举例子说明)

###3.3.7 Real World Example

Steve illustrated the benefits of using indexes using the PostgreSQL database on Hipmunk.

As an example, Steve used the hotels table on Hipmunk, which had approximately 312,000 entries.

Running the SQL command:
```
select name from hotels where id = 51492;
```
returned one result.

Using the additional PostgreSQL command explain analyze with the above SQL command, we saw that the query ran a sequential scan on hotels which took 142ms.

Next, Steve created an index on the id field and ran the query again. This time the query only took 0.163ms. That is a substantial improvement!

通过创建index，极大的减少了查询所用的时间。142ms->0.163ms.

###3.3.8 Indexes For Sorting

我们之前用的是hash table,但是这种结构是没有排序的，另一个tree的结构有排序，但是速度比hash table慢。
One last thing to consider is the use of indices for sorting.

So far we have been talking about using hash tables to create an index. But one of the characteristics of a hash table is that they are not sorted. So we lose our sorting information when we use a hash table.

There is a different kind of mapping that we can use. This is called a tree. Trees are a basic data structure that accomplish something similar to a hash table, but have the additional nice property that they are sorted.

So why would you ever use a hash table when you could use a tree instead? Well, the downside to trees is that lookups are slower. In general, the time taken to look up a particular key in a hash table is not a function of the number of keys in the hash table. Hash tables have constant time lookups. In trees, lookup time is roughly a function of log(n), where n is the number of elements in the tree. Lookup speeds decrease as the size of the tree increases.

###3.3.9 Another Real World Example

The Reddit Hotness Algorithm

If you've used Reddit, you'll know that it is just a big list of links, and that users can vote on those links, up or down. The front page is whatever is the most popular. Good links stay at the top of the page for a long time, while mediocre links may make an appearance but disappear after a short while. This is a really cool feature of Reddit and it's not that hard to compute. What they do is to use a special index. Let's look at how that works.

Reddit uses a link table similar to the one we have been using:

ID	ups	downs	date	score
...	10	1	...	25
...	...	...	...	...
The **score** column is the total score for the link.

The way that the Reddit hot algorithm works is that there is an index on the score field, called **hot_idx**.

One approach to generating the front page might have been to take all of the links submitted in the last 24 hours, do some fancy maths, sort them by how many up votes and down votes each has, and then display the page. However, this wouldn't capture the 'hotness' of how things rise and fall, so what Reddit actually does is that every time someone adds one up vote, Reddit increments the score by some other amount. The amount, **amt**, is computed through the 'hot' function which looks something like this:
```
amt = hot(ups, downs, date)
```
The function takes the number of up votes, the number of down votes and the submission date of the link. What happens is that, over time, the value of an up vote increases. This causes scores to constantly increase over time, so that newer links always have higher scores than older links. so that a link that is 1 day old with lots of votes may have the same score as a link that is 1 minute old with just a few votes, and this is what keeps the Reddit front page churning.

The page content can be generated from a simple and fast SQL statement like:
```
SELECT * FROM link ORDER BY score DESC;
```

![web220.png-244.2kB][189]


## 3.4 Datebase和GAE的一些comcepts

###3.4.1 Scaling Databases

Let's talk for a moment about how to scale databases. Like databases themselves, this is a very broad topic, but there are a couple of concepts that we need to introduce.

There are two reasons why you may need to scale your database:

- Too much load - the database is just doing too much work.
- Too much data for one machine.

In the first case, what you might do is to replicate the data to other databases. All data writes go to the master database, and are then replicated to the subordinate slave databases. Database reads can then be serviced from the slave databases.

There are some downsides to this approach. One is that it doesn't increase the speed of writes. Another is the problem of replication lag where a read can occur an a slave database before the write to the master has been propagated,

One approach to dealing with the second case. where we have too much data for one machine is to **shard** the database. This is a fairly simple technique where, instead of having just one master, you have several. This also improves the write speed since there are now multiple masters to handle the load. A downside of sharding is that queries get much more complex. Another downside is that joins become difficult, or even impossible!

**Scaling Databases Quiz**

Which is an appropriate technique for increasing the read speed from a database?

- Get a faster machine.
- Replicate the database.
- Store less data.
- Press the turbo button.

只有第二个是对的。
the answer I'm looking for, obviously, is the thing we just talked about replicate the database.

Now, yes, you can get a faster machine, but sometimes you don't have access to a faster machine, and that's obviously not what I was asking.

Of course, you can store less data. That was something we used to say. I read it all the time. This site would be a lot faster if we didn't have any users.

Or you could press the turbo button, which is really just a subset of get a faster machine.

**Growing Databases Quiz**

Which is an appropriate technique for growing a database that won't fit on one machine?

- Replicate the database.
- Get a bigger hard disc.
- Shard the database.
- Store less data.

答案只有第三个
You wouldn't replicate the database，because if it won't fit on one machine, it's probably not going to fit on the next machine, and it still doesn't solve the machine we're talking about.

Get a bigger hard disk--well, that is technically true, but if you put this, you did not get the correct answer.

Shard the database--that's what we just talked about. That allows you to take your data and spread it across multiple machines, where each machine is storing just a piece of the data. Take your data and spread it across multiple machines. That's what sharding a database is.

Or you could store less data. You can delete some data from your database and of course it will fit, or you can use Mongo and it will do it for you.

###3.4.2 Acid

There's one last set of concepts that we need to cover before we move onto some actual programming, and this is ACID. This stands for:

Atomicity - all parts of a transaction succeed or fail together.
Consistency - the database will always be consistent.
Isolation - no transactions can interfere with another.
Durability - once the transaction is committed, it won't be lost.

One thing to be aware of is that it is very hard to create a database that is completely atomic, always consistent, where all transactions are isolated and which is completely durable. There is always an element of trade-off.
理想丰满，显示骨感。真是的数据库不可能将上面四点全部做到，总有trade-off.

###3.4.3 Google App Engine Datastore(下面几小节都是关于GAE里的概念)

Let's start working on some real code. We will work on an extended example that will reflect quite closely what you are expected to do for your homework for this lesson.

We will be using the Google App Engine Datastore. This is the database provided by App Engine. There are a couple of things you need to know about Google App Engine Datastore.

What we have been referring to as tables are known as entities in Google App Engine Datastore:

**Tables → Entities**

Entities serve basically the same purpose as tables i.e. organising things of the same data-.type together.

A few important things to note about entities:

- The columns are not fixed

    - You can have whatever columns you want
    - You can even change the columns while developing the database

- Entities all have an id

    - id can be assigned automatically by the Datastore
    - You can make up your own id using integers or strings
- Entities have the notion of parents and ancestors.
    - Giving entities a parent can get around some of the limitations on consistency.

![web221.png-46.8kB][190]
    
###3.4.4 GQL

So far in this class we have been talking about SQL. In the App Engine Datastore we have something a little different, called **GQL**. GQL is basically a simplified version of SQL that only works in the Datastore.

The main difference between GQL and SQL is that all queries begin with SELECT *. There is no way to select individual columns. This also means we cannot do joins.

Another difference is that, in the generic SQL databases we have been talking about, we have been able to run arbitrary queries, no matter how slow, with or without indices. In App Engine, all queries must be indexed. For the most part, in the type of work we will be doing, you won't have to build any indexes yourself. App Engine will build the indices for you.

![web222.png-53.5kB][191]

### 3.4.5 Automatic Sharding And Replication

One last thing to consider is that the Datastore is sharded and replicated. Google doesn't share details of how this is implemented, but a lot of the constraints that we will be dealing with imply that the database is both sharded and replicated.

Some benefits for us are:

- We won't have to think about scaling (too much).
- Queries will be quick (because they have to be simple).

However, we will have to think about consistency.

![web223.png-223.2kB][192]

##3.5 ASCII Chan（我们要完成的一个项目）
Chan是channel的缩写
We are going to build a website called ASCII Chan. This will be a message board for sharing ASCII art.

It will have the general structure where we will have a form that takes a title, some ASCII art and a submit button. A user can submit this and below the form the users will see ASCII art that has been submitted by other people.

This will be a one page website with the form at the top and the content below.

这是一个one page web site

![web224.png-26.1kB][193]

这种画被叫做ASCII art，哈哈。我们这个网站就是要分享这个art。
![web225.png-285.1kB][194]

###3.5.1 Getting Started on ASCII Chan

Shown below is the framework for a basic application:（创建**asciichan.py**,写入代码）
```
import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.write("asciichan!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
```
This uses templates which allow us to keep the HTML in separate files that look like HTML with just little escapes for variables, rather than doing string substitutions for large wads of HTML.

Much of the code above will already be familiar to you. The class Handler includes some convenience functions, so the function `write()` saves us from having to type self.response.out.write() all the time.

The function `render_str()` takes a template name and returns a string of that rendered template, while the function `render()` which instead of returning just the string, calls write() on it.

At present, all the app does is to display the text string "asciichan" in the browser.

现在browser端的效果
![web226.png-16.8kB][195]

###3.5.2 Creating The Form

Let's take a brief look at how the template works. Consider the file **front.html**:(创建一个**front.html**文件，存放html)
```
<!DOCTYPE html>

<html>
    <head>
        <title>/ascii/</title>
    </head>
    <body>
        <h1>/ascii/</h1>
    </body>
</html>
```
The `<h1>` tag is a header tag.

If we now modify the MainPage handler in our app as follows:
```
class MainPage(Handler):
    def get(self):
        self.render("front.html")
```
The app will now display the template front.html. If this causes an error, you can try creating a folder called "templates" in your app directory

OK, now we want to add our form to **front.html**. Initially, we add a text input field to allow the user to enter the title of their ASCII art:
```
<form method="post">
    <label>
        <div>title</div> <input type="text" name="title">
    </label>
</form>
```
Now we want to add an element to allow the user to enter their ASCII art.


![web227.png-128.1kB][196]

browser效果
![web228.png-17.9kB][197]

但既然是想让用户画图，就应该给一个text area，而不是一个box去input

![web229.png-60kB][198]

###3.5.3 Textarea

Now we can add the `<textarea>` element to our form, remembering that `<textarea>` is not a void element like `<input>`, and it requires a closing tag:
```
<form method="post">
    <label>
        <div>title</div> <input type="text" name="title">
    </label>
    <label>
        <div>art</div> <textarea name="art"></textarea>
    </label>
    <input type="submit">
</form>
```
I have also added the submit button. The next thing we need to do is to add the form handling, by adding the post method in our application

![web230.png-59.6kB][199]

browser效果
![web231.png-37.6kB][200]

接下来添加post function

###3.5.4 Form Handling

这节课内容挺多，有必要的话直接再看一遍[视频](https://www.udacity.com/course/viewer#!/c-cs253/l-48756013/m-48369786)

The first thing that we need the handler to do is to get the user input strings title and art from the form:
```
def post(self):
    title = self.request.get("title") 
    art = self.request.get("art")
Now we add some error handling as follows:

if title and art:
    self.write("thanks!")
else:
    error = "we need both a title and some artwork!" self.render("front.html", error = error)
```
If the user has entered both a title and some artwork, then we will display a simple "thanks!" message for now.

If either the title or the artwork are missing then we want to re-render the page with the error message "we need both a title and some artwork!". The message is stored in the variable error, and so we now need to add a place for this error in our template.

We will add the error at the bottom of the form:
```
<form method="post">
    <label>
        <div>title</div><input type="text" name="title">
    </label>
    <label>
        <div>art</div><textarea name="art"></textarea>
    </label>
    <div class="error"> { { error }}</div>
    <input type="submit">
</form>
```
We set the error message div's "class" attribute to "error" because we intend to style this later using CSS styles. The double curly-brackets, { { * }}, are part of the template language and will render any variable in place.

We now have a functioning form, but we can make it better. First, we are going to be calling self.render("front.html", error = error) from both post and get, so let's make it a function in it's own right called render_front()
```
def render_front(self, title="", art="", error=""):
    self.render("front.html", title=title, art=art, error = error)
```
We can then modify the post and get functions to use this new function, and our MainPage handler becomes:
```
class MainPage(Handler):
    def render_front(self, title="", art="", error=""):
        self.render("front.html", title=title, art=art, error = error)
    def get(self):
        self.render_front()
    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        if title and art:
            self.write("thanks!")
        else:
            error = "we need both a title and some artwork!"
            self.render_front(error = error)
```
Now, we just need to add the variables for title and art to our form in front.html to preserve the user input if they forget to complete one of the fields like so:
```
<form method="post">
    <label>
        <div>title</div><input type="text" name="title" value= { {title}}>
    </label>
    <label>
        <div>art</div><textarea name="art"> { {art} } </textarea>
    </label>
    <div class="error"> { {error}}</div>
    <input type="submit">
</form>
```
And our form is ready.
Or is it?
当然not。用户提交的信息如果不正确，其信息会丢失。我们要像之前做的那样即使用户输入错误，其信息也不会消失。
下一节解决这个问题。

### 3.5.5 Form Handling Continued

If we run our application in a browser it does seem to work, but the user input still isn't preserved. This is simply because we didn't add the parameters title and art to our post function. Adding them as shown below makes the form work as intended:
```
def post(self):
    title = self.request.get("title")
    art = self.request.get("art")
    if title and art:
        self.write("thanks!")
    else:
        error = "we need both a title and some artwork!" self.render_front(title, art, error)
```
What about escaping risky HTML code if a user enters it into our form?

In fact, the form handles risky HTML perfectly. Try it for yourself. But we didn't add any escape functions in our code, so how does the form handle these characters?

We have been using jinja as the template language to render the HTML in our application:
```
import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
```

When we initiated the jinja environment we set the parameter autoescape=True, which will automatically escape anything we include from a variable.

![web232.png-392.4kB][201]

即使输错也不会消失
![web233.png-28kB][202]

###3.5.6 Creating Entities

专门用一个class（类）来表示输入的art.

Now that we have our form, we can begin to add the database so that we can store the artwork submitted by our users.

The way to define an entity in Google App Engine is to define a class:
```
class Art(db.Model):
```
This inherits from **db.model** (which we imported near the top of the app).

![web234.png-113.7kB][203]

###3.5.7 Datastore Types

Google App Engine has a number of different options for the types of the properties of an entity (similar to the column types we saw earlier). Some of the most popular are:
```
Type	Usage
Integer	for storing integers
Float	for storing floating-point numbers
String	for storing strings
Date	for storing dates
Time	for storing times
DateTime	for storing dates and times
Email	stores emails
Link	stores links
PostalAdd	stores postal addresses
```

**Datastore Types Quiz**

We are going to use three properties in our entity:

Title
Art
Created (when the artwork was added)
What types should we assign to each of these properties?

![web235.png-239.7kB][204]

### 3.5.8 Creating Entities Continued

In fact, we are actually going to use the type **Text** for the Art property.

The difference between **String** and **Text** is that a string must be under 500 characters and can be indexed, Text can be more than 500 characters, but cannot be indexed.

So, we now add the property types to our entity. The general format is:

`property_name = db.TypeProperty()`

So our entity will be:
```
class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
```
The parameter **required=True** means that the property is required in the database. If we try to add ASCII art to our database without a title (or without art!) we will get an exception from Python.

The parameter **auto_now_add=True** automatically adds the current date and time to the property.

![web237.png-450.1kB][205]

###3.5.9 Working With Entities

We now need to extend the success case to add the new artwork.

First, we create a new piece of art a, passing in the **title** and **art** variables. We don't need to add anything for created as the property is automatically created. We can then use a.put() store the new piece of art to our database.

Finally, we redirect to the front page, "/", to avoid the annoying reload message:
```
if title and art:
    a = Art(title = title, art = art)
    a.put()
    self.redirect("/")
```
This should now be working, but we have now way of knowing until we add the last feature to draw the artwork below the form.

![web238.png-403.9kB][206]

到现在位置，我们输入的art已经存在database里了。现在还需要最后一个feature，把输入datebase里的art显示到页面下方
![web239.png-36.9kB][207]

### 3.5.10 Running Queries

We want to look up all the artwork in our database so that we can display it on our front page. We want to do this every time we render the front page so that we can display both the form and all the artwork.

To do this, we need to modify our **render_front()** function:

We add a GQL query using an expression of the form:

`arts = db.GqlQuery("")`

The actual GQL query goes between the quotes.

**Running Queries Quiz**

Write the SQL (or in this case, GQL) for the query we need to fetch all of the Arts from the database sorted by creation time ("created"), most recent first?

![web240.png-212.2kB][208]

Now we are in a position to complete the **render_front()** function.
```
def render_front(self, title="", art="", error=""):
    arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
    self.render("front.html", title=title, art=art, error = error, arts = arts)
```

We have added the GQL query to look up all the artwork in our database and passed the variable `arts` into the `render()` function. Now, all that is left is to modify our template to use this arts variable.

![web241.png-447.5kB][209]


First, we are going to add a horizontal rule tag,` <hr> `below the form, as a visual separator between our form and the users' artwork.



Next, we are going to create a loop in the template by using Python code embedded in the HTML.

The way to embed Python code when you are using jinja is to use a construct like this:

 `{% code %} `

To go through all the artwork in arts we need the Python construct:

` {% for art in arts %} `  # 这个是jinja的语法

Next we will construct an HTML structure to display the artworks and their titles:
```
<div class="art">
    <div class="art-title"></div>
    <pre class="art-body"></pre>
</div>
```
So, we have created a div which we have called class="art" (for when we apply styles to our HTML), within which there are two further structures for the title and the artwork itself.

The title we are going to hold in another` <div>`, this time the class="art-title". The variable `art.title` is shown in the double curly-brackets.

For the actual artwork, we are going to use a `<pre> `element (having the class="art-body") as the container. The `<pre>` element represents a block of preformatted text which preserves the whitespace within it. Again, the variable `art.art` is shown inside double curly-brackets.

This should display our ASCII art as it was intended to be shown.

Finally, we need to indicate that the loop is complete. We do this with the statement:

 `{% endfor %} `

The body of our template now looks like this:
```
<body>
    <h1>/ascii/</h1>
    <form method="post">
        <label>
            <div>title</div> <input type="text" name="title" value="">
        </label>
        <label>
            <div>art</div>
            <textarea name="art"></textarea>
        </label>
        <div class="error"></div>
        <input type="submit">
    </form>
    <hr>
    {% for art in arts %}  
    <div class="art">
        <div class="art-title">{ {art.title}}</div>
        <pre class="art-body">{ {art.art}}</pre>
    </div>
    {% endfor %}
</body>
```
![web242.png-299.2kB][210]

browse效果
![web243.png-261.9kB][211]

### 3.5.11 Styling

通过添加一个CSS语句让form看起来更舒服些。

We've been including classes with out HTML template, and we've mentioned a few times that these can be used for styles which can improve the appearance of our web pages. Let's take a look at some of these styles.

Styles can be defined using the http://www.w3.org/TR/html4/present/styles.html#edef-STYLE element:
```
<style type="text/css">
</style>
```
Within the style element, we can specify the characteristics for the various elements in our HTML code. As an example, we can define the default style for the body (i.e. between the `<body>`and `</body>` of our web page using the following:
```
body {
    font-family: sans-serif; width: 800px; margin: 0 auto; padding: 10px;
}
```
As you can see, we are able to specify the font-family (and we can also set the font size), the on-screen width, any margin and the padding that we want to apply.

Padding is space between the outside of the element and the contents.

The complete style specification that we are going to use for this page is shown below:
```
<style type="text/css">
    body {
        font-family: sans-serif; width: 800px; margin: 0 auto; padding: 10px;
    }
    error {
        color: red;
    }
    label {
        display: block; font-size: 20px;
    }
    input[type=text] {
        width: 400px; font-size: 20px; padding: 2px;
    }
    textarea {
        width: 400px; height: 200px; font-size: 17px; font-family: monospace;
    }
    input[type=submit] {
        font-size: 24px;
    }
    hr {
        margin: 20px auto;
    }

    .art + .art {
        margin-top: 20px;
    }
    .art-title {
        font-weight: bold; font-size: 20px;
    }
    .art-body {
        margin: 0; font-size: 17px;
    }
</style>
```

效果
![web244.png-46.9kB][212]

![web245.png-63.8kB][213]


# Problem Set 3 - Building a Basic Blog

这部分练习等考完试之后再做。

https://www.udacity.com/course/viewer#!/c-cs253/l-48198869/e-48508425/m-48648729

之后可以把这门课程所有的problem set 全放到一个笔记里。

# Lesson 4: Lesson 4: User Authentication and Access Control

##4.1 Cookies
Cookies are small pieces of data stored in the browser for a website. 'Small' in this context means less than 4 kilobytes, and in practice, typically only a hundred bytes. A cookie is really just a simple string. Conceptually, cookies take the format:

name = value

In practice, this might look something like this:

user_id = 12345

Cookies are really commonly used for the kinds of temporary information that needs to be stored by the browser. A good example of this type of information is whether you are logged into a particular website. Your browser will store a cookie that shows you are logged in as (for example), user 12345.

When the browser makes a request to a web server, the server may send back some cookie data in the form of an HTTP header in its response. The browser just stores the cookie, and each time it makes a request to that website in the future, the browser will send the cookie data back to the server.

You can generally save up to about 20 cookies per website. This is determined by the browser.

We have already said that cookies must be less than 4 kilobytes. In practice they should always be much less. There is a lot that can go wrong with longer cookies. Some browsers don't handle multi-line cookies properly. Indeed, some web-servers don't handle multi-line cookies properly!

Another limitation is that a cookie must be associated with a particular domain. A cookie for udacity.com is only sent to udacity.com, and udacity.com can only set cookies for udacity.com.

These are all enforced on the client-side by the browser.


**Good Uses For Cookies Quiz**

What are good uses of cookies?

Storing login information.
Storing small amounts of data to avoid hitting a db.
Storing user preference information.
Tracking you for ads.

![web246.png-81.5kB][214]


###4.1.1 Cookie Headers

As we said earlier, cookies are sent in HTTP headers. When a server wants to send a cookie to your browser, it sends an HTTP response header that looks something like this:

Set-Cookie: user_id = 12345

The **Set-Cookie** header will set the cookie named user_id to the value 12345. If the server wants to send multiple cookies, it simply needs to send multiple Set-Cookie headers:

Set-Cookie: user_id = 12345

Set-Cookie: last_seen = Dec 25 1985

The server can send as many cookies as it wants. It is up to the browser to decide whether or not it stores them! For this reason, keep cookies to less than 20.

In future requests, the browser will then send its own header within the request:

Cookie: user_id = 12345

If the browser will be sending multiple cookies, they are separated by a semi-colon, thus:

Cookie: user_id = 12345; last_seen = Dec 25 1985

It is therefore a good idea to avoid using semi-colons in the values of your cookies! If you really need to incorporate semi-colons in your cookie values, use some encoding on the cookie values to ensure that you escape the semi-colons otherwise you will effectively corrupt the incoming cookie header.

![web247.png-57.9kB][215]

###4.1.2 Cookie Examples

Steve used telnet to view the header information in the HTTP response from Google.com. The cookies below appear:
```
Set-Cookie: PREF=ID=9dc1d7062ae5fd16:FF=0:TM=1336504404:LM=1336504404:S=KVV_FUsYL5CImBd4; expires=Thu, 08-May-2014 19:13:24 GMT; path=/; domain=.google.com

Set-Cookie: NID=59=poGaObJlWuDDoF4zB0fxk2gYic2IT66JXfwFVTYg0Yx1lV_BwI9G_-1NNAKFi9B1eqlAlxDAyJnAEFKCIkg0PtfrdKu9dcsKTzljNqgPIjuTYP3rGAuK6L5suIyp57y-; expires=Wed , 07-Nov-2012 19:13:24 GMT; path=/; domain=.google.com; HttpOnly
```
The first cookie is named PREF and is set to the value:

ID=9dc1d7062ae5fd16:FF=0:TM=1336504404:LM=1336504404:S=KVV_FUsYL5CImBd4

This is actually an example of Google storing multiple pieces of data in one cookie. The cookie value is terminated with a semi-colon, and is then followed by some additional parameters (each also separated by semi-colons). The first of these is the expires time:

expires=Thu, 08-May-2014 19:13:24 GMT

After this time, the cookie will have expired and will no longer be sent.

The cookie is only valid for the path and domain set by the parameters:

path=/; domain=.google.com

The next cookie is named NID, and includes similar parameters.

查看cookies的方法
Steve then demonstrated that Linux/Unix or Mac users can use the curl -I command to view the HTTP headers instead of telnet.

One other way to view HTTP headers is to use the debug tools in your browser. Steve demonstrated these tools using Google Chrome.

![web248.png-425.6kB][216]

**Sending Cookies Quiz

Which header does a browser use to send a cookie to a server?

 ![web249.png-29.7kB][217]

**Setting Cookies Quiz**

Which header does a server use to set a cookie?

![web250.png-49kB][218]

###4.1.3 Cookie Domains

As we have seen, cookies can have additional parameters, not just the value. Consider the following Set-Cookie header:

Set-Cookie: name = Steve, Domain = www.redit.com; path = /;

In this case, the name parameter is '**name**', and its value is '**Steve**'. This is followed by a parameter named '**Domain**' with the value '**www.redit.com**' which is the domain that this cookie is relevant to. Lastly, there is the parameter named '**path**' which has the value '/' ('/' is always the default path).

Let's look at the Domain parameter. With this parameter specified, the cookie will not be sent to the server unless the server's domain is the same as the value of the Domain parameter or ends with the value of the Domain parameter, in this case, '**www.redit.com**'.

So, in this case, the cookie will be sent to **www.reddit.com** and to **foo.www.reddit.com**, but it will not be sent to **bar.reddit.com** or even to just **reddit.com**.

![web251.png-299.1kB][219]

**Valid Receivers Quiz**

Which of these domains would receive this cookie?

Set-Cookie: user=123; Domain = ide.udacity.com

udacity.com
ide.udacity.com
other.ide.udacity.com
other.udacity.com

![web252.png-50.2kB][220]

**Valid Setters Quiz**

Which of these domains could set this cookie?

Set-Cookie: user=123; Domain = ide.udacity.com

udacity.com
ide.udacity.com
other.ide.udacity.com
other.udacity.com

![web253.png-59.7kB][221]

###4.1.4 Cookie Settings

Browsers will normally all have a preferences page. These will allow you to set your personal preferences for how the browser uses cookies.

When designing web applications you should never assume that cookies will always be allowed, and that your cookies will always be there, since your users may have modified the cookie settings in their browsers.

![web255.png-331.1kB][222]

###4.1.5 Ad Networks

Let's take a moment to consider Ad Networks. These aren't strictly relevant to this class, but they do provide an interesting illustration of how cookies can be used.

Let's say that your browser makes a request to some website, and that website responds with a page of HTML. One of the things in this HTML could be a little 1-pixel hidden image, that you do not even see, but which makes a request to another site, for example, www.google.com.

This does actually happen. Google provides an analytics package that a lot of websites use to track traffic and what users are doing. Google may respond with a cookie that assigns you an i.d. so that when you come back to the website again, Google can track that you are the same user returning to the site. This is an example of a "3^rd^-party-cookie".

This is a quite legitimate use of cookies. Google analytics is used by Udacity, Reddit and Hipmunk to monitor traffic and so forth. However, it does mean that Google is able to build up quite a lot of data about the sites that you are visiting.

![web256.png-54.6kB][223]

###4.1.6 Cookie Expiration

Let's consider the following cookie:

Set-Cookie: user = 123; Expires = Tue, 1 Jan 2005 00:00:00 GMT

The extra parameter '**Expires**' sets an expiration date for the cookie. The browser will hang onto the cookie until the given expiry date, in this case, **Tue, 1 Jan 2005**.

If no 'Expires' parameter is provided, the cookie will expire when the browser window is closed. In this case, the cookie is known as a **session-cookie**. A common example of this is the remember me check-box on a login box. If the box is checked, then an Expires parameter is set for the cookie. If not, the cookie is as session cookie.

![web257.png-55.1kB][224]

**Cookie Deletion Quiz**

When does a cookie with no Expires parameter get deleted from your browser?

Jan 1, 2025.
Never.
When you close your browser.
In 1 day.

![web258.png-63.9kB][225]

###4.1.7 Cookies In App Engine

What we will do now is to build a little web application that uses cookies to keep track of how many times you have visited a web site. This will illustrate how to use cookies in App Engine and highlight a few things that you should bear in mind.

Let's begin with the basic app template that we are all familiar with:
```
import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                                autoescape=True)

class Handler(webapp2.RequestHandler):
        def write(self, *a, **kw):
                self.response.out.write(*a, **kw)

        def render_str(self, template, **params):
                t = jinja_env.get_template(template)
                return t.render(params)

        def render(self, template, **kw):
                self.write(self.render_str(template, **kw))

class MainPage(Handler):
        def get(self):
                self.write('test')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
```

The first thing that we want to do is to set the content type to text so that we don't have to deal with HTML at this stage, by adding the line:
```
        self.response.headers['Content-Type'] = 'text/plain'
```
to the class MainPage(). The next thing we need to do is to add a line to get a cookie, called visits:
```
        visits = self.request.cookies.get('visits', 0)
```

The way this works is to look at the **request** object, which is always on **self**. The request object will have a **cookies** object. This is a dictionary-like object where App Engine stores the cookies when it parses the HTTP headers. We call the dictionary function get on the **cookies** object to see whether the key '**visits**' is in the dictionary. If it is, we the get the value of the key, and if not then we get the default value which we have set to be 0.

Lastly, we will add a line to show the user how many times they have visited the site:
```
        self.write("You've been here %s times!" % visits)
```
Our MainPage() class now looks like this:
```
class MainPage(Handler):
        def get(self):
                self.response.headers['Content-Type'] = 'text/plain'
                visits = self.request.cookies.get('visits', 0)
                self.write("You've been here %s times!" % visits)
```

So far so good. When a user visits our page they will see the text:

```
You've been here 0 times!
```

Now what we need to do is to update the value of visits each time that the user visits our site and then store the updated value in the cookie:
```
class MainPage(Handler):
        def get(self):
                self.response.headers['Content-Type'] = 'text/plain'
                visits = self.request.cookies.get('visits', 0)
                visits += 1
                self.response.headers.add_header('Set-Cookie', 'visits=%s' % visits)
```
So, we increment the value of visits and then call add_header to add the **Set-Cookie** header. We won't worry about domain or path for now.

When we re-load the page we get:
```
You've been here 1 times!
```
which is good, but when we refresh we get an error!

###4.1.8 Internal Server Error

紧接上一节
The server has either erred or is incapable of performing the requested operation.
```
Traceback (most recent call last):
  File "D:\Program Files (x86)\Google\google_appengine\lib\webapp2\webapp2.py", line 1536, in __call__
    rv = self.handle_exception(request, response, e)
  File "D:\Program Files (x86)\Google\google_appengine\lib\webapp2\webapp2.py", line 1530, in __call__
    rv = self.router.dispatch(request, response)
  File "D:\Program Files (x86)\Google\google_appengine\lib\webapp2\webapp2.py", line 1278, in default_dispatcher
    return route.handler_adapter(request, response)
  File "D:\Program Files (x86)\Google\google_appengine\lib\webapp2\webapp2.py", line 1102, in __call__
    return handler.dispatch()
  File "D:\Program Files (x86)\Google\google_appengine\lib\webapp2\webapp2.py", line 572, in dispatch
    return self.handle_exception(e, self.app.debug)
  File "D:\Program Files (x86)\Google\google_appengine\lib\webapp2\webapp2.py", line 570, in dispatch
    return method(*args, **kwargs)
  File "E:\Applications\cookies\main.py", line 25, in get
    visits += 1
TypeError: coercing to Unicode: need string or buffer, int found
```
We have a Type Error and, in fact, when we think about it, this makes sense.

The browser doesn't care what data-type a cookie is. However, we specified the value of visits to be the **string** %s: **visits=%s** and then we tried to use it as an **integer** in the expression **visits += 1**.

We can modify the MainHandler() class to manage the data type as follows:
```
class MainPage(Handler):
        def get(self):
                self.response.headers['Content-Type'] = 'text/plain'
                visits = self.request.cookies.get('visits', '0')
                #make sure visits is an int
                if visits.isdigit():
                        visits = int(visits) + 1
                else:
                        visits = 0

                self.response.headers.add_header('Set-Cookie', 'visits=%s' % visits)

                self.write("You've been here %s times!" % visits)
```
Now let's do something with the cookie value. Let's say that we want to reward users with a special message of thanks if they have visited our website more than 100 times. We can do this quite simply as follows:
```
        if visits > 100:
                self.write("You are the best ever!")
        else:
                self.write("You've been here %s times!" % visits)
```
Now, users who have visited more than 100 times will see the message "You are the best ever!", and everyone else will see how many times they have visited the site as before.

![web259.png-87.9kB][226]

**Cheating Quiz**

What can we do to get 10,000 visits?

Reload the page 10,000 times.
Send the link to 10,000 friends
Edit the cookie in our browser.

![web260.png-46kB][227]

**How To Cheat**

Cookies can be edited in most browsers, and their values changed. The exact method varies from browser to browser.

![web262.png-149.2kB][228]

既然能通过cheating做到，那么该如何预防呢？
So how do we prevent users from cheating like this?


##4.2 Hashing

We are going to talk about a technique called **hashing**. Hashing is a technique that we can use to verify the legitimacy of our data.

So what is a 'hash'?

A hash is a function, let's call it **H()**, which when applied to a piece of data, x, returns a fixed-length bit-string, y:

**H(x) → y**

x is data

y is fixed-length bit-string

x can be of any size. y can be of arbitrary, fixed length, but, depending on the algorithm used, y is usually on the order of 32 - 256 bits long (certainly with the common algorithms that we will be dealing with).

Let's consider some of the properties of the hash function, **H()**:

- It is generally very difficult to identify a piece of data that hashes to a specific value of y.
- It is infeasible to find a particular value of x for a given output value of y.
o The hash function is a 'one-way' function.

* You can't modify x without modifying y.

Hash functions are covered in much more detail in the Udacity course CS387 - Applied Cryptography.

###4.2.1 Hash Algorithms

There are many popular hash algorithms. In general, if you are going to use hashing for security purposes, **DON'T WRITE YOUR OWN HASH ALGORITHM!**

Some popular algorithms are

- CRC32 - Designed for checksums. Fast.
- MD5 - Relatively fast, but not secure. Still the most popular hashing algorithm.
- SHA-1 - Not as fast as MD5. Fairly secure. 2^nd^ most popular algorithm.
 -SHA256 - Pretty good security, but slower.

> Collision: - when two things hash to the same value.

越安全，速度也越慢。trade off.
![web263.png-246.5kB][229]

###4.2.2 Hashing In Python

Let's start looking at how we can do hashing in Python, since we are going to be doing a lot of it in this class.

To perform hashing in Python, one thing we can use is the hashlib library. This library incorporates a number of hashing functions:

md5()
sha1()
sha224()
sha256()
sha384()
sha512()
to hash a string like the word "Hello!" in Python, we would enter:
```
import hashlib

x = hashlib.md5("Hello!")
```
To see the hashed value we would call the hexdigest() function on x:
```
x.hexdigest()
'952d2c56d0485958336747bcdd98590d'
```
If we hash the phrase "Hello, World" we will get the hash shown below:
```
hashlib.md5("Hello, World").hexdigest()
'82bb413746aee42f89dea2b59614f9ef'
```
But if we change a single letter and hash "Hello, world", with a lower case w, we now get a completely different result from the hash function:
```
hashlib.md5("Hello, world").hexdigest()
'bc6e6f16b8a077ef5fbc8d59d0b931b9'
```
A nice thing about MD5 is that it is available on every system, and if I hash the phrase "Hello, World" on any system I will get the same result.

![web264.png-475.8kB][230]

**Hashlib and SHA256 Quiz**

Use the hashlib library in Python to find the sha256 hash of the string udacity (lowercase).

![web266.png-48.4kB][231]

###4.2.3 Hashing Cookies

Now that we have learned how to hash data we can put our new-found knowledge to good use in order to prevent people from cheating with our cookie. The algorithm will look something like this:

Instead of simply saying:

`Set-Cookie: visits=5`

we will add a hash of the value, something like:

`Set-Cookie: visits=5, [hash]`

Now, a would be cheat cannot forge a cookie without knowing what hashing algorithm we are using.

When we receive the cookie, we just hash the value and compare it with the hash to ensure that the value hasn't been tampered with:
```
if H(value) == hash:

valid
else:

discard...
```

![web267.png-146.5kB][232]

### 4.2.4 Making Hashed Cookies Quiz

Implement the function make_secure_val, which takes a string and returns a string of the format: s,HASH

![web268.png-147kB][233]



### 4.2.5 Verifying Hashed Cookies Quiz

Implement the function check_secure_val, which takes a string of the format s,HASH and returns s if hash_str(s) == HASH, otherwise it returns None.

![web269.png-227.5kB][234]

my code:
```
def check_secure_val(h):
    ###Your code here
    s,ha = re.compile('\w+').findall(h)
    if hash_str(s) == ha:
        return s
    else:
        None
```

### 4.2.6 Putting It Together

We can now restructure our program to use our new secure functions. First, we add the functions themselves to our program:
```
import hashlib

def hash_str(s):
        return hashlib.md5(s).hexdigest()

def make_secure_val(s):
        return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
        val = h.split('|')[0]
        if h == make_secure_val(val):
                return val
```

Note: we have replaced the comma, ',' in the cookie value with the pipe,'|'. This is because of because of an issue that Google App Engine has with commas in cookies, where a comma in a cookie has a special meaning.

Next, we will change the variable used to store the value of visits held in the cookie to **visit_cookie_str**. The variable **visits** will now be the actual visit count, which will be zero by default:
```
    visits = 0
    visit_cookie_str = self.request.cookies.get('visits')
```

Now, we need to test if the cookie for visits exists (i.e. if the user has visited our site before). If it does, then we run the function **check_secure_val()** on visit_cookie_str. If the cookie is valid, we then update the **visits** variable accordingly:
```
    if visit_cookie_str:
            cookie_val = check_secure_val(visit_cookie_str)
            if cookie_val:
                    visits = int(cookie_val)
```


At this point, the value of **visits** will either be 0 (if this is the user's first visit or the cookie is invalid) or it will be the value stored in the cookie. Now we increment visits to count the current visit:

visits += 1

The next thing that we need to do is to update the cookie value. We need to use our new **make_secure_val()** function and then add the Set-Cookie header:
```
        new_cookie_val = make_secure_val(str(visits))

        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)
```

The complete MainPage() class now looks like this:
```
class MainPage(Handler):
        def get(self):
                self.response.headers['Content-Type'] = 'text/plain'
                visits = 0
                visit_cookie_str = self.request.cookies.get('visits')
                if visit_cookie_str:
                        cookie_val = check_secure_val(visit_cookie_str)
                        if cookie_val:
                                visits = int(cookie_val)

                visits += 1

                new_cookie_val = make_secure_val(str(visits))

                self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

                if visits > 100:
                        self.write("You are the best ever!")
                else:
                        self.write("You've been here %s times!" % visits)
```

When we run this in the browser a few times and check the cookie we see the value is now:

5|e4da3b7fbbce2345d7772b0674a318d5

![web270.png-374.5kB][235]

有了hash就不能作弊了
![web271.png-229.6kB][236]

### 4.2.7 Cookie Hashing

继续增强安全性

What we are doing with our application now is that we are storing a cookie that looks something like this:

visit = 1|HASH

On the server side, we are comparing the hashed value of 1 with the hash value stored in the cookie. If they match, we accept the value as valid, and if it doesn't then we discard it.

Does this actually solve our problem?

Well, it is certainly an improvement, but if they know we are using MD5 (which is pretty easy to guess), it is easy to forge a cookie by simply changing the cookie value, hashing that new value using MD5 and storing the new hash in the cookie.

What we need to do is to incorporate some secret knowledge that cheats do not know. Instead of hashing the value (in this case, 1) to produce the hash, we will hash a secret string plus the value:

H(SECRET + 1) = [HASH]

As long as the secret string remains secret, a would-be attacker won't be able to forge the cookie even if they know our algorithm.

Before we add this functionality to our application, let us introduce a new bit of Python.

Up until now, we have been using hashlib to run basic hashes. There is a second library, specifically for doing message authentication called **HMAC**:

Hash-based Message Authentication Code

This is basically a special algorithm, built into Python, for when you want to combine a key with your value to create a hash. HMAC looks something like this:

hmac(secret, key, H) = [HASH]

H is the hashing function.

To see how this works in the Python interpreter, we can hash the message "udacity" with the keyword "secret" as follows:
```
>>> import hmac
>>> hmac.new("secret", "udacity").hexdigest()
'fd4c2d860910b3a7b65c576d247292e8'
```
![web273.png-53.7kB][237]

![web274.png-98.5kB][238]

### 4.2.8 HMAC Quiz

Implement the hash_str() function to use HMAC and our SECRET instead of md5.

![web275.png-256kB][239]

### 4.2.9 Incorporating HMAC

先演示chit方法
![web276.png-23.3kB][240]

![web277.png-116.6kB][241]

![web278.png-66.9kB][242]


OK, so let's incorporate the new functions that we have written into our code:
```
SECRET = 'imsosecret'

import hmac
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()
```
Normally, SECRET would be held in another module that you don't publish or share.

![web279.png-25.2kB][243]

###4.2.10 Password Hashing

OK, we've spent a lot of time looking at how we can use hashing, and the HMAC variant of hashing, to make cookies that won't be tampered with. Now let's look at using hashing for passwords.

Let's say that our database has a table for users. This table has one column for the username and the other column for the password:
(如果把用户的密码按下面的方式存储，那么就太不安全了，你会背官司的！因为侵犯了用户隐私）
name	password
Spez	hunter2
Kn0thing	metallica

In order to check that a user is valid, we would probably have a function something like this:
```
def valid_user(name, pw):
    user = get_user(name)
    if user and user.password == pw:
        return user
```

The problem with this is that, if your database gets compromised you are in real trouble. You have given away all your user's passwords! This means that, not only are your users going to be angry because you have compromised their privacy, your website is also in trouble because you have bad-guys logging in and messing around with people's accounts because they now know everybody's passwords.

To protect the passwords, instead of storing the actual plaintext passwords in our database, we can store a password hash in the database:
（所以，为了增强安全性，我们通过hash给密码加密，增加安全性）
name	Password hash
Spez	H(hunter2)
Kn0thing	H(metallica)
Now, if our database gets compromised, all the attacker has is a bunch of password hashes, and we have already seen that it is very, very difficult, if not impossible, to turn the hash of a string back into the original string.

Our user validation function also changes to compare the hash of the password entered by the user with the password hash stored in the database:
```
def valid_user(name, pw):
    user = get_user(name)
    if user and user.password_hash == H(pw):
        return user
```

This actually takes very little work and makes your site much more secure.

So, this is a very important strategy that you should employ when you're building user registration systems (such as in this week's homework...).

**Why Hash Passwords Quiz**

Why do we hash passwords?

To keep snooping Sys Admins from knowing everyone's passwords
Because people often use the same password for many websites
If the db is compromised, the passwords are reasonably safe.
If you don't, you will regret it!

![web280.png-81.9kB][244]

**Storytime**

哈哈，Steve讲了他的sad story. 一开始创建reddit的时候用户量少，他犯懒没有尽早hash，所以用户密码是plain text，之后他电脑丢了，通过他的电脑所有用户和密码都能被别人获取……所以，能使用hash就使用hash，

###4.2.11 Rainbow Tables

Now that you have your passwords hashed, are you completely safe?

Absolutely not!

彩虹表是一个用于加密散列函数逆运算的预先计算好的表,常用于破解加密过的密码散列。

The problem is that there are just a handful of good hashing algorithms that people use. If someone were to create a mapping of every word to the hash of that word for each of these algorithms that would create a problem. An attacker would just need to look up the password for any given hash! Tables of these mappings are known as rainbow tables.

These rainbow tables already exist and can be found and downloaded from the Internet.

- There is a simple way to get around this problem. We have already seen from the way we secured our cookies that all you need to do is to add some secret to the password to defeat the rainbow tables. However, you cannot always use the same secret or your password database would become vulnerable to the same technique.

What we do instead is to use something called a **salt**.

A salt is just some random characters which are added to the password before it is hashed. This effectively defeats the quick lookup using rainbow tables from working. Our hash is now created by applying the hashing function to the password plus the salt:

`h = H(pw + salt)`

In the user table we now store the username and the hash. The salt can be stored in the clear along with the hash in the password field.

name	Password hash
Spez	H(hunter2 + salt), salt
Kn0thing	H(metallica+ salt), salt

Outside of this class, you should think very hard before doing this yourself. As with all cryptography, you should probably not be implementing these functions yourself. You should also think very carefully before using a third-party library since many of these also get it wrong!

Let's try implementing some naive functions for hashing and salting a password to see how the flow works, and then we will discuss some of the things that you should look for when you are evaluating someone else's approach.

###4.2.12 Making Salts Quiz

Implement the function make_salt() that returns a string of 5 random letters using python's random module.

Note: The string package might be useful here.
```
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))
```
运行这个函数，每次能都到一个随机的5字母。
![web283.png-133.8kB][245]

###4.2.13 Hashing Salts Quiz

Implement the function make_pw_hash(name, pw) that returns a hashed password of the format:

HASH(name + pw + salt),salt

Use sha256
```
def make_pw_hash(name, pw):
    salt=make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)
```

同样一个，name和password，每次运行这个function都能得到不同的hash和salt。
![web284.png-236.9kB][246]

###4.2.14 Validating Salts Quiz

用户在登陆上检查输入的密码和是否匹配

We previously created the function `make_pw_hash()` that returned a salted version of the password.

Now you need to implement the function `valid_pw()` that returns True if a user's password matches its hash.

TIP: You will need to modify `make_pw_hash()` to make this work.
```
def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt=make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)

h = make_pw_hash('spez', 'hunter2')
print valid_pw('spez', 'hunter2', h)
```

###4.2.15 Bcrypt

What we have seen so far for password hashing is good to understand, and most modern computers hash passwords in just the way that we have shown you.

The problem with most hashing functions is that they are designed to be fast. This is generally a good thing, and is really great for verifying cookies and so forth. However, for cases like passwords where it is much more likely that you will be subject to a brute-force attack, it would be really useful if we had a function that is both really good (like SHA256) but is also rather slow, so that as computers get faster and faster the hash function stays the same speed.

Fortunately, there is just such a function. It is called bcrypt.

bcrypt basically takes an extra parameter which is "how long do you want this to take", giving us a function that will stay slow forever because we can make it slow.

A downside is that it is not built into Python and needs to be installed separately.

In future, outside this course, instead of using SHA256, you should be using bcrypt.

bcrypt是一个跨平台的文件加密工具。由它加密的文件可在所有支持的操作系统和处理器上进行转移。它的口令必须是8至56个字符，并将在内部被转化为448位的密钥。

###4.2.16 HTTPs

One last thing about passwords. Although we now know how to store our passwords securely on the server, we still have the problem of sending the password from the browser to your server.

When we looked at forms, we saw that when a password is entered into a form, and the form is submitted, the password is sent in clear text over the Internet. To protect the password while it is in transit, and prevent attackers from sniffing the password off the wire, we should use HTTPs ("HTTP secure").

HTTPs is just like HTTP, except it is encrypted over SSL. An attacker then shouldn't be able to read anything coming over the wire.

![web286.png-41.1kB][247]

###4.2.17 The Best Quiz

When given the choice, which is the best hashing algorithm to hash passwords?

MD5
SHA256
HTTPs
bcrypt

这个问题是有唯一选项的。
![web287.png-51.1kB][248]

# Problem Set 4 - Setting Up Users

这次homework关于，Registration，Login，Logout这三项的。怎么implement这三项。

#Lesson 5: APIs

## 5.1 Introduction

Okay, so welcome to Lesson 5. In this lecture we're going to be talking about how to make your web service--your web application--talk to other computers. So up until now we've had your programs basically outputting HTML that a browser will interpret for a user to see--to make something pretty. But your web application can also return things like XML and JSON that other computers can interpret so they can build websites or services that interact with your data. So we're going to be talking about those formats--XML and JSON-- how to read them, how to interpret them and manipulate them, and that sort of thing. And then we're going to be adding a feature to ASCII Chan that is built on Google Maps, so we can see where it uses our posting from. And then, when we're all done, you're homework will be basically making your blog output itself in JSON. So it should be fun. It's a little bit of a change of pace from the last two lectures. Let's jump right in.

##5.2 HTTP Clients

这节讲server之间是如何传递数据的，这也是最常见的一种情况。

![web288.png-69.8kB][249]

What I'd like to do now is actually explain how Hipmunk works a little bit, because we do a lot of this type of communication. Okay, let's change our picture a little bit to be a little bit more about Hipmunk, because I'd like to explain how our architecture works. So in this case, this is still-- we call users customers when they're actually paying-- and this is me--Steve--and this is Hipmunk servers. When a user does a flight search, what we do is we hit a bunch of our data providers where we actually get our flight data from. So the first thing we'll do is we'll take your flight search and we'll send it to ITA, we'll send it to an airline, and in some cases we'll even send it to Amtrak, if that's appropriate. Each of these guys are their own-- these are companies who have their own services that we work with. So ITA will run our flight search, and they will send us data back. The Airline, too, will run their own flight search on their own system and they'll send it back to us. And Amtrak will do its thing and send their data back to us. So then on our server, we have all this flight search data, represented by this blob here. We will manipulate all this data, collate it, make you nice results, and then we'll send back our HTML response. So what we're going to be working on in this lesson is how do we make our server speak to other servers when there's no browser involved. We're still using HTTP, but we are now communicating over other protocols.


![web289.png-80.6kB][250]


##5.3 urllib

urllib2是python里用来和url交互的库。下图里我们把data存放在了`p`里，现在`p`代表一个文件，我们必须用函数打开它才能看到里面的内容，所以用`p.read()`把内容赋给`c`。
![web290.png-91.6kB][251]

输入`c`查看里面的内容，返回的就是google front page里的内容
![web291.png-410.6kB][252]

可以用`dir()`来查看`p`里有什么东西
![web292.png-79.8kB][253]

还可以在p后面加函数，查看不同的内容
![web293.png-162.4kB][254]

Now, I happen to know that this is a dictionary, and dictionaries have a function on them called items. If we were to run items on this in Python, this is what you can call in any dictionary--items-- to view the keys and the values, and it will actually print them, generally, nicely for you. We can see all of the headers we got back from Google. This is an actual dictionary, so we can say p.headers, for example, content type, and we can see the content type that we got back from Google.

```
import urllib2
import urllib

p = urllib2.urlopen("http://www.google.com")
p
c=p.read()
c
dir(p)
p.url
p.headers
p.headers.items
p.headers['content-type']
```

##5.4 Using urllib

![web295.png-40.9kB][255]

![web294.png-90.7kB][256]

##5.5 XML

如果服务器之前用html,可能会出问题。比如你have an opening tag to make some text bold, and you can forget to put the closing tag。But HTML is not an ideal language for computer-to-computer communication. It turns on Amtrak, we actually get their HTML, and I'm going to show you some of the heartache we have to go through to actually parse this HTML. 

所以我们用XML来parse the html.

![web29.png-90.7kB][257]

## 5.6 XML and HTML

![web296.png-63.2kB][258]

##5.7 Parsing XML

how do we parse XML? 

use the built-in parser in Python. Python has a library called "minidom,"
 
one thing I would like to point out real quick here is when you're working with XML you'll often see this word "dom" up here. What this stands for is "document object model." This basically refers to the internal representation of an XML document.

Dom refers to the computer representation of the XML, and minidom is a handy library for manipulating this stuff in Python.

![web297.png-36.9kB][259]

![web298.png-145kB][260]

最后一个语句，执行，发现错误，因为children打错了。typo
![web299.png-466.3kB][261]

更正后，再试一边，用`dir(x)`查看x里的内容，这次成功了。

![web300.png-107.4kB][262]

![web301.png-333.8kB][263]


第16个命令中，`("item")[0]`指的是下面第一个`<item> </item>`,`childNodes[0]`能访问第一个child, `nodeValue`指得是item里的数字1.

Looking at the first tag called "item," we can see that we have an item. If we were to look at its children, we can call child nodes to see a list of children. We can see that we have one text node. If we were to look at the first one of those, we can access the node value attribute and see that it's 1. 

![web302.png-370.4kB][264]

##5.8 RSS

![web303.png-34.3kB][265]

rss 订阅网页

![web304.png-696.1kB][266]

##5.9 Parsing RSS

![web306.png-70.7kB][267]

把内容存储到变量`contents`中

![web308.png-42.6kB][268]

输入`contents`，回车，能看到内容
![web307.png-432.6kB][269]

把parse contents with Mini Dom, 现在变量`d`就是一个document instance,然后用第七个命令调出所有的item
![web309.png-133.4kB][270]

y用`len`来计算有多少个，结果是18，和一开始的答案不一样，是steve一开始写错了
![web310.png-168.9kB][271]

##5.10 JSON

JSON能像python一样使用相应的语法，但是不要用eval来parse JSON

eval(j), and what eval does is it actually treats this as Python code as if I had just typed this at the prompt. This is the result we get. Now, that's a neat thing you can do. Never, ever do it. Because in addition to having eval JSON in here, somebody could actually have code that might do something to your computer. Never use eval for parsing JSON. I just wanted to show that you can use eval to parse JSON. 

![web312.png-139.3kB][272]

##5.11  Parsing JSON

quiz
![web314.png-62.2kB][273]

用`.loads()`把内容变为JSON
![web318.png-393.2kB][274]

用`dir(j)`能看到所有的dictionary.
![web319.png-89kB][275]

但这些dictionary并不是都有用，我们用`j.key()`查看最关键的

![web320.png-40.9kB][276]

key里有kind和data,我们用`j['data']`来查看里面的内容，又一大堆
![web322.png-96.9kB][277]

用`j['data'].key()`查看data里的key,发现只有四个
![web323.png-31.5kB][278]

我们想看`children`里的，用`j['data']['children'].key()`,结果发现有错误，错误信息说里面是个list,那么就直接用`j['data']['children']`查看里面的内容。
![web324.png-145.1kB][279]

children里的第一个有key，`j['data']['children'][0].key()`
![web325.png-250.2kB][280]

找到了目标ups,`j['data']['children'][0]['data']['ups']`

![web326.png-138.9kB][281]

换一个children就能得到另一个对应的值
![web328.png-85.7kB][282]

好了，把这些整合到function里
![web329.png-278.3kB][283]

##5.12 APIs

we can get any page in JSON or we can also get it in XML by changing our extension, and a lot of webpages have this feature where you can get their content in different formats. Another good example is Twitter. If we were to go to Twitter and do a search--let's look for Udacity-- we can see all the tweets about Udacity.

Now, if we want to get a JSON listing of this--I happen to know the URL-- we can go to search.twitter.com/search.JSONq=Udacity. Now we get a JSON listing of the search result that we were just looking at at Twitter. 

通过修改url的后缀，能得到不同格式的页面。通过查看twitter的API，就能得到很多这样的用法。
![web330.png-61.6kB][284]

![web331.png-50.5kB][285]

![web333.png-61.8kB][286]

##5.13 JSON Escaping

用slash来转义一些字符，以免系统识别出现错误

第二个命令中间多加了一个quote，会导致错误
![web334.png-27.6kB][287]

![web335.png-182.7kB][288]

两种解决方法。第一，前面加两个slash,'/',来escap，一个是python的/，一个是JSON的。第二，前面加一个`r'`,说明这个语句是raw string,里面包含所有quotes。
![web336.png-31.9kB][289]

##5.14  Escaping JSON in Python

用python的方法来实现escaping JSON, 用dump.从第三个命令开始。
![web337.png-209.8kB][290]

What is the valid JSON for this Python datastructure:
`{"blah":["one", 2, 'th"r"ee']}`
Note that JSON must use double quotes to enclose strings, it cannot use single quotes.
![web338.png-52.8kB][291]

##5.15 Being a Good Citizen

1 选一个好的库，比如urllib2
2 限制自己的访问次数，不然有会被block的危险

![web339.png-55.3kB][292]


##5.16 SOAP

SOAP是针对XML的，还有一些其他的protocol用来做machine和machine之间的通信
![web340.png-46kB][293]

##5.17 Good Habits

![web342.png-65.6kB][294]

##5.18  ASCII Chan 2

根据前面的的1-17节，利用API来重新设计ASCII Chan的front page。
在右侧添加一个map,显示提交post的用户所在地
![web343.png-74kB][295]

具体做法
![web344.png-71.5kB][296]

该网站可以根据ip，得到用户的经纬度坐标
![web344.png-71.5kB][297]

![web345.png-189.6kB][298]

该网站的API也能便利，通过在URl里输入IP，就能得到相应的XML，得到所在的经纬度和相关信息。
![web346.png-151.8kB][299]

好了，得到了经纬度，怎么draw a map?
用google map，其中有个工具，叫static map

![web347.png-74.4kB][300]

只要给出一个url,就能得到一个静态的map图。
![web349.png-183.8kB][301]

###5.18.1 Geolocation（地理定位）

修改post
![web350.png-49.8kB][302]

用一个函数通过ip得到经纬度
![web351.png-39.5kB][303]

```

xml = """<HostipLookupResultSet xmlns:gml="http://www.opengis.net/gml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.1" xsi:noNamespaceSchemaLocation="http://www.hostip.info/api/hostip-1.0.1.xsd">
           <gml:description>This is the Hostip Lookup Service</gml:description>
           <gml:name>hostip</gml:name>
           <gml:boundedBy>
             <gml:Null>inapplicable</gml:Null>
           </gml:boundedBy>
           <gml:featureMember>
             <Hostip>
               <ip>12.215.42.19</ip>
               <gml:name>Aurora, TX</gml:name>
               <countryName>UNITED STATES</countryName>
               <countryAbbrev>US</countryAbbrev>
               <!-- Co-ordinates are available as lng,lat -->
               <ipLocation>
                 <gml:pointProperty>
                   <gml:Point srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
                     <gml:coordinates>-97.5159,33.0582</gml:coordinates>
                   </gml:Point>
                 </gml:pointProperty>
               </ipLocation>
             </Hostip>
           </gml:featureMember>
        </HostipLookupResultSet>"""
```
```
# QUIZ - implement the get_coords(xml) function that takes in an xml string 
# and returns a tuple of (lat, lon) if there are coordinates in the xml.
# Remember that you should use minidom to do this.
# Also, notice that the coordinates in the xml string are in the format:
# (lon,lat), so you will have to switch them around.

from xml.dom import minidom

def get_coords(xml):
    ###Your code here
```
注意，上面蓝色的XML里，有一段是包含IP信息的，用这个来定位。
![web354.png-117.6kB][304]

###5.18.2 Debugging

![web356.png-71kB][305]

测试一下
![web358.png-79kB][306]

好了，第一个功能实现了，能得到坐标
![web359.png-109.4kB][307]

###5.18.3 Updating the Database

第二步，实现draw a map
![web360.png-44.4kB][308]

如果有坐标，add to the art
![web362.png-41.7kB][309]

把图片给coords
![web363.png-32.9kB][310]

回到post部分修改一些函数
![web365.png-53kB][311]

上面这些功能会把用户post的简笔画上传的GAE上，我们能在GAE上看到上传的所有arts
![web367.png-123kB][312]

###5.18.4 Querying Coordinate Information

![web369.png-196.7kB][313]

有bug，添加一个语句，解决同时运行多个查询的问题
![web370.png-218.2kB][314]

###5.18.5 Creating the Image URL

写一个function
![web371.png-145.3kB][315]

```

from collections import namedtuple

# make a basic Point class
Point = namedtuple('Point', ["lat", "lon"])
points = [Point(1,2),
          Point(3,4),
          Point(5,6)]

# implement the function gmaps_img(points) that returns the google maps image
# for a map with the points passed in. A example valid response looks like
# this:
#
# http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&markers=1,2&markers=3,4
#
# Note that you should be able to get the first and second part of an individual Point p with
# p.lat and p.lon, respectively, based on the above code. For example, points[0].lat would 
# return 1, while points[2].lon would return 6.

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"

def gmaps_img(points):
    ###Your code here
```

![web375.png-113.3kB][316]

###5.18.6 Putting It All Together

更新post
![web377.png-147.9kB][317]

更新front.html
![web378.png-32.8kB][318]

命名一个class map是为了把map放到页面的右侧，用css
![web379.png-92.7kB][319]

效果
![web380.png-153.4kB][320]

# Lesson 6: Caching 

# 6.1 Introduction

之前我们学的基本已经覆盖了web的很多方面。但我们写的web app只是一个toy，并不能算是真正能用的产品，所以如何搭建大规模的web app，这就用到了cach.
What we haven't talked about is how to run your applications at a large scale.

When we talk about scaling, this may mean running your application on multiple machines, or storing huge amounts of data, or consuming large amounts of bandwidths. There are a whole range of resources that we need to think about. In this lesson we'll discuss different strategies for handling these types of issues.

**Quiz: Why Scale**

So that we can serve more requests concurrently.
So we can store more data.
So that we're more resistant（能复原的） to failure.
So we can serve requests faster.

全选

**Quiz: What To Scale**

Bandwidth.
Computers (memory, CPU).
Power.
Storage.

全选

**Techniques For Scaling**

Let's think about some techniques for scaling.

- Optimise code.

    - cost of development time

- Add additional computers.

    - cost of hardware

    - cost of maintenance

- Upgrade computers

    - more memory
    
    - more disk space
    
    - faster CPUs

- Cache complex operations.

The first thing you should think about is optimising your code. If you have a choice between buying a second machine or optimising your code so that your app works twice as fast then this is something you should consider. There are still costs involved, whichever option you eventually select. It takes effort to optimise code, so there is the cost of development time. This has to be set against the cost of additional machines (including additional maintenance costs).

Essentially, optimising code is about programming better. This comes with experience and in time you'll be able to write better and tighter code.

Upgrading the hardware to provide more memory, more disk space or faster CPUs is often a good option, but it's one that may not be available to you if you are using a shared platform where you don't have control of the actual machines. Every couple of years, machines get substantially faster and cheaper (Moore's Law) and this can often be one of the easiest and cheapest ways to scale without the risk of breaking your website.

Another technique is to cache complex operations. We will be spending a lot of time on caching in this lecture.

先理解一下scale的含义，指扩展
> scalable——capable of being scaledcapable of being easily expanded or upgraded on demand<a scalable computer network>一般指可扩展性/易拓展性，指随规模的扩大而易于按需扩展或者升级。

除了本节说到的三种技巧，cache也是一种技巧，而本章重点讲这个。

##6.2 Caching

caching是指把运算过一次的结果放在cache里，这样下次query的时候，就不用从hash table或数据库里调用了，从cache里调取数据非常快。100ms vs `<1ms`的差别。 

Caching refers to storing the results of an operation so that future request return faster.

Basically, if you have an operation that might be slow to run, say a database query, or rendering some HTML, you store the results when you run it so that you don't have to do the computation a second time. This way, you just need to reference the previous result.

So when should we cache the results?

When the computation is slow.

When the computation will run multiple times.
When the output of the computation is the same for a particular input.
When your hosting provider charges for db access.
Google App Engine allows you a fixed number of free reads and writes to the datastore in a particular day. If you exceed this limit, you have to pay for it. So even if your website doesn't get a huge amount of traffic, caching requests so they don't have to hit the database over-and-over is a great way to save some money!

Let's think about how we could implement caching.

Image we have a function called db_read() that reads from the database. The function is slow. It takes 100ms to run the query. This means you can only do 10 requests per second. If you're trying to serve thousands of requests which all need to run db_read() you're database is going to get pummelled. So how would we cache db_read()?

The cache is basically a large mapping of keys to values, just like a hash table. In this case, the request is the key to the cache, so the pseudo code for hashing our function db_read() will look something like this:
```
if request in cache:
    return cache[request]
else:
    r = db_read()
    cache[request] = r
    return r
```
So, instead of calling db_read() on every request, the first thing we do is to check whether that request is in the cache. If it is, we return the cached value. This is called a cache hit. Only if the request is not in the cache do we run our query, db_read(), and this is called a cache miss. What we do on a cache miss is to store the result of the operation in the cache and then return the result. Now, in future this request will just bounce off the cache.

Now you can obtain substantial performance improvements just by wrapping this simple algorithm around your slow pieces of code. In the case of a hash table, depending on the size of the hash table we would expect to achieve a considerable improvement in speed. We might expect to retrieve the result in less than 1ms. Now, obviously, if the hash table is huge, and you're caching lots of things, you will need to take the performance characteristics of your hash tables into account, but you can still gain substantial performance improvements.

###6.2.1 Quiz: Caching

Improve the cached_computation() function so that it caches results after computing them for the first time so subsequent calls are faster.

```
import time

# complex_computation() simulates a slow function. time.sleep(n) causes the
# program to pause for n seconds. In real life, this might be a call to a
# database, or a request to another web service.
def complex_computation(a, b):
    time.sleep(.5)
    return a + b

# QUIZ - Improve the cached_computation() function below so that it caches
# results after computing them for the first time so future calls are faster
cache = {}
def cached_computation(a, b):
    ###Your code here.

#start_time = time.time()
#print cached_computation(5, 3)
#print "the first computation took %f seconds" % (time.time() - start_time)

#start_time2 = time.time()
#print cached_computation(5, 3)
#print "the second computation took %f seconds" % (time.time() - start_time2)

```

**solution**

代码
![web381.png-282kB][321]

通过测试能看到用cache提升速度非常快
![web382.png-247.3kB][322]

###6.2.2 Scaling ASCIIChan

Let's look at how we might improve ASCIIChan.

When a user makes a request to ASCIIChan we have to carry out a number of operations:

* Process the request

    - parse the HTTP

    - parse the URL

    - map the URL to the handler

        - Query the database
        - Collate the results
        - Render HTML
        
The first operation takes very little time, but can still be significant if you're going to be processing large numbers of requests.

The next operation, querying the database, is much more substantial. Depending on the complexity of the query it may take a lot of time, and it may also not be free.

Collating the results also takes time. We may have do some sorting, or prune some results because the are spam. We need to convert the results into Python objects and a range of other maintenance tasks.

Rendering the HTML can take a lot of time. If there is a lot of HTML, as on Reddit for example, the time involved in rendering the HTML can be non-trivial and may require some optimisation.

**Quiz: Scaling ASCIIChan**

Which of these is the best place to start when we are looking to improve our website?

Process the request
Query the database
Collate the results
Render HTML

第二个，因为优化这个能极大得加快访问速度。

###6.2.3 Optimizing Queries


这一节有点长，主要是优化之前的代码。如果不深究的话就不用仔细看了。

![web383.png-84.9kB][323]


We have already seen some of the main techniques for scaling:

Optimise code.
Add additional computers.
Upgrade computers
Cache complex operations.
When we talk about databases, we're not talking about optimising code as such. Rather we are looking to ensure that we have the appropriate indexes, making sure the query is "sane", making sure that the query is simple and that you're only querying for things that you actually need.

We don't actually need to do this for ASCIIChan, because the query itself is very simple, and because Google App Engine makes the indexes for us. However, this is always the first thing that you should check. If the index that Google App Engine creates isn't optimal for the query you're running then you may need to build something by hand.

In essence, the first step is to limit the work that the database has to do in the worst case.

Adding more machines or upgrading the machines isn't something that we really have control of in this case since App Engine takes care of all of that for us. If we weren't using App Engine then these are techniques that we would need to consider.

This leaves us with the option of caching the query to improve the performance of our application.

In ASCIIChan, the front page only changes when somebody submits a new piece of ASCII art. This makes it an ideal candidate for caching the results of the database query.

The get() function of our mainpage handler simply calls the render_front() function:
```
def get(self):
    return self.render_front()
The render_front() function looks like this:

def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * "
                        "FROM Art "
                        "WHERE ANCESTOR IS :1 "
                        "ORDER BY created DESC "
                        "LIMIT 10",
                        art_key)
        arts = list(arts)

        img_url = None
        points = filter(None,  (a.author_loc for a in arts))
        if points:
                img_url = gmap_img(points)

        self.render("front.html", title = title, art = art, error = error, arts = arts, img_url = img_url)
```
This runs the datastore query, written in GQL, which looks up the ten most recent pieces of art:

SELECT * FROM Art WHERE ANCESTOR IS art_key ORDER BY created DESC LIMIT 10
Since most users visiting ASCIIChan only view the font page, the front page won't change very often. So we don't actually need to run the query every time someone visits. What we want to do is to cache the query.

Let's take the code that runs the query out of the function render_front() and put it into its own function which we will call top_arts():
```
def top_arts():
        arts = db.GqlQuery("SELECT * "
                                "FROM Art "
                                "WHERE ANCESTOR IS :1"
                                "ORDER BY created DESC "
                                "LIMIT 10",
                                art_key)
        arts = list(arts)
        return arts

```
Now, there is a technique that we can use when developing code like this that will show us when we are actually running the query. We will add the line:

`logging.error("DB QUERY")`
at the beginning of our function. This will print out the string "DB QUERY" in our Error Console. Now, normally you should probably use logging.debug() for this purpose, but this makes the demonstration a little easier. We also need to import the logging module.

Now, when we refresh the page in the browser, we see the following in the log console:

ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 -

So we are printing ERROR and DB Query, which is the string that we added, and which will be printed every time the db query runs. Then the browser fetched '/', which is the actual request to ASCIIChan and also requested favicon.ico (which we haven't created).

Each time we reload the page in the browser these lines will be repeated:

ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 - ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 -

Now we will add some caching to the db query using the same algorithm we saw earlier.
```
CACHE = {}
def top_arts():
        key = 'top'
        if key in CACHE:
                arts = CACHE[key]
        else:
                logging.error("DB QUERY")
                arts = db.GqlQuery("SELECT * "
                                        "FROM Art "
                                        "WHERE ANCESTOR IS :1 "
                                        "ORDER BY created DESC "
                                        "LIMIT 10",
                                        art_key)
                arts = list(arts)
                CACHE[key] = arts
        return arts
```
We have added the dictionary CACHE. We have to have a key to cache, and we are going to store it in a variable and call the key 'top'. This is how we're going to reference the result of our query in our cache. Then we just added the rest of the caching algorithm.

Now if we refresh the browser, and check the log console, we see that the db query ran and our message DB QUERY is displayed.

ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 - ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 - ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 -

But, if we refresh the browser again, we see that the page loaded, but that DB QUERY isn't displayed. i.e. the query results were retrieved from the cache:
ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 - ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 - ERROR 2012-05-21 22:34:38,645 main.py:67] DB QUERY INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 - INFO 2012-05-21 22:34:38,670 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-21 22:34:38,808 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 404 -

No matter how many times we refresh the page, DB QUERY will not appear in the console because the query results are now held in the cache.

###6.2.4 Broken Submissions

看图说话，通过cache直接返回结果，不用去访问database.

![web385.png-64.1kB][324]

**Quiz: Broken Submissions**

How can we fix our stale cache problem? (stale cache: 陈旧的缓存)

Choose all that apply.

Improve the cache to automatically expire things after some time.
After submitting, clear the cache.
After submitting, update the cache.
Don't cache. Find a different approach.

![web386.png-75.7kB][325]

###6.2.5 Cache Clearing

之前我们做的是通过cache存放数据，这样用户在访问过一次数据库后，加载的网页就会存放在cache里，用户就不必频繁访问数据库，造成不必要的访问。

现在要做的是改进这个机制。因为存放在cache里的page是固定的，即使通过page向里面添加了一些post，还是无法看到最新的post，因为cache是陈旧的。所以我们要做的是，当用户提交一个post后，自动clear 之前的cache，再访问一边数据库，更新最新的post，再把这个最新版的网页存放到cache里，这样用户就能看到自己或别人提交的最新post了。

总的来说，clear cache是为了更新cache来保持网页处于最新的状态。

![web387.png-80.4kB][326]

Now we can improve our caching technique. What we will do is to modify our post() function so that when we submit a new piece of art to ASCIIChan, it will write that piece of art to the database and then clear the cache before redirecting us back to the homepage.

Python includes a function, clear() which can be used to clear dictionaries, so all we need to do is to add this to our post() function:
```
def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
                p = Art(parent=art_key, title = title, art = art)
                #lookup the user's coordinates from their IP
                coords = get_coords(self.request.remote_addr)
                #if we have coordinates, add them to the art
                if coords:
                        p.coords = coords

                p.put()
                CACHE.clear()

                self.redirect("/")
        else:
                error = "we need both a title and some artwork!"
                self.render_front(error = error, title = title, art =art)
```
Note: you should always use clear() to empty a dictionary rather than setting the dictionary empty directly, i.e. you should use:` d.clear()` not `d = {}` The reason for this is that setting the dictionary empty directly can be the source of some subtle bugs.

So now we are only doing as many database queries as we actually need to do. Now there is no need for every visitor to hit the database unless they are making a new submission to ASCIIChan.

The name of the game when you're scaling websites is to only do the minimum number of database reads that you need to.

###6.2.6 Cache Stampede

大量的用户同时访问数据库去更新cache，而有时候database刚好clear cache还没来得及生成新的cache，这会导致响应速度变慢，或者始终无法返回page。这种情况为缓存溃败。

We'd like to introduce you to a new concept: the cache stampede.

Now that we have modified our cache algorithm, when a user visits ASCIIChan their request causes a query to the database which will return a set of results. these are then stored in the cache and are used in response to subsequent requests from users. When a user submits a new piece of art, the post() function writes that piece of art to the database, clears the cache and redirects the user back to the front page.

The problem comes when there are many users. Say one user posts a new piece of art which is written to the database and then the cache is cleared. If a large number of requests come into the site at the same time, while the cache is empty, they will all attempt to read from the database (with exactly the same query) at the same time. This is called a cache stampede. Now, a query which may only have taken a few milliseconds might take much longer, or even never return at all, because all of the queries are blocking each other.

**Cache Stampede - When multiple cache misses create too much load on the database.**

![web388.png-68kB][327]

**Quiz: Cache Stampede**

How can we avoid a cache stampede?

Replicate the db to handle more reads.
Only allow one web request at a time.
Only allow one db request at a time.
Don't clear the cache, but instead overwrite it with new data.

答案是第四个。为了防止出现clear cache后cache为空，此时用户访问的话会导致Cache Stampede。所以我们不clear cache, 而是当有new data的时候，把new data添加到cache里，这样就能保证cache不会出现空的情况，这样的cache称作warm cache. 

Let's see how we might overwrite the cache, rather than clearing it in ASCIIChan. Firstly, we need to modify our top_arts() function.
```
def top_arts(update = False):
        key = 'top'
        if not update and key in CACHE:
                arts = CACHE[key]
        else:
                logging.error("DB QUERY")
                arts = db.GqlQuery("SELECT * "
                                    "FROM Art "
                                    "WHERE ANCESTOR IS :1 "
                                    "ORDER BY created DESC "
                                    "LIMIT 10",
                                    art_key)
                arts = list(arts)
                CACHE[key] = arts
        return arts
```
What we have done is to add the parameter update to the function and set its default value to False. Now, if update is False then the function should use the cache as before, but if update is True, it should update the cache.

Now we can replace CACHE.clear() in the post() function with top_arts(True):
```
def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
                p = Art(parent=art_key, title = title, art = art)
                #lookup the user's coordinates from their IP
                coords = get_coords(self.request.remote_addr)
                #if we have coordinates, add them to the art
                if coords:
                        p.coords = coords

                p.put()
                #rerun the query and update the cache
                top_arts(True)

                self.redirect("/")
        else:
                error = "we need both a title and some artwork!"
                self.render_front(error = error, title = title, art =art)
```

###6.2.7 Caching Techniques

这部分总结了之前的内容。三种cache的方法，一种完全不cache，直接访问database,第二种naive cache，但大规模会有bug，第三种 refresh cache,利用clear cache。这是之前讲的三种。这里steve还说了第四种，最厉害的,update cache。reddit也用了这种方法，因为网站量级越大，越适合用这种技术

![web389.png-92kB][328]

Let's have a brief review of caching techniques.

The first technique was not to cache at all. This meant that every time the page was loaded there was a db read, but no db read when art was submitted.

Next we had what might be called naive caching, using the basic cache algorithm. This only did a db read in the event of a cache miss, and still didn't do a db read when art was submitted, but suffered from a major bug in the form of a stale cache.

To avoid the problem of the stale cache we started clearing the cache. Again, this only did a db read in the event of a cache miss and no db read when art was submitted, but might be susceptible to a cache stampede if we are scaling the application.

We improved the technique to refresh the cache. Now we only do a db read on a page view when the cache is empty (i.e. when the app is turned on), and we do one db read each time a new piece of art is submitted to the database. In effect, a normal user browsing the site never touches the database. This is a really good property to have:

Simple users should never touch the database.

This will improve the user experience because their requests will be handled faster. This will also keep your load down since you can have a great many of these users and because their requests are bounced off the cache you don't have to do much work to serve them.
Now, there is a fourth approach that we haven't looked at yet, and which is the most aggressive of all these techniques. We might refer to this technique as updating the cache (distinct from refreshing the cache). This can allow us to achieve the state where we never do a db read on a simple page view, and we don't do any database reads on submission either. We will look at how to implement this technique in the next section.

The techniques are summarised in the table below:

|Approach|	db read/ page-view |	db read/ submit |	Bugs|
|----| ----|----|---|
|No caching|	Every|	None	|   |
|Naive caching|	Cache miss|	None|	Yes|
|Clear cache|	Cache miss	|None|   |	
|Refresh cache|	Rarely	|1	|  |
|Update cache|	0|	0	|   |

要记住，越准确的cache，代码就越复杂
![web390.png-84.7kB][329]

**Cache Updating**

With cache updating, a user viewing a page on the site is served from the cache in the same way we have seen before. However, when a user submits a new piece of art to ASCIIChan, the post() function will write the art to the database and simultaneously write it to the cache as well. Now this is a little more complex than the techniques we have seen so far, but it means that we never have to do a db read.

Using this technique means that the only time we ever have to do a database read is when we start up the site, and we may actually set up a program to do this for us so that no user ever has to do a database read. This is the approach taken by Reddit. Every page that you can look at is stored in its own cache. When you post a link or update a vote they then update the appropriate caches.

This effectively introduces the trade-off between complex inserts (and improved speed) versus database reads. In general, the more accurate the cache, the more complex the code will need to be.

The additional complexity is probably not justified for ASCIIChan right now. The site simply isn't at that scale. However, large sites like Reddit gain huge benefits from using this technique.

###6.2.8 App Server Scaling

Process the request
Query the database
Collate the results
Render HTML

这四个方面能改善site，我们用cache来提升Query the database,其他三项怎么提升呢？

我们adding additional app servers。如果site只有一个machine，访问太多的话负载太大，崩溃，所以通常会有多个machine来负责返回site内容，但是向哪个machine发送query也是门技术。我们添加load balancer来处理选择哪个serve来query，而选择的算法也有一些，具体可见下面材料。

![web392.png-73.6kB][330]

OK. So now we have taken a fair amount of load off our database by using caching to minimise, or even eliminate, database reads. Let's go back to the steps involved in a request to see what else we can do to improve the performance of our site:

Process the request
Query the database
Collate the results
Render HTML

We have improved the db query, but what can we do to improve the other steps involved in handling a request? We could certainly use caching to render the HTML. But there is another technique that we could use to improve all three other parts of the request, which is adding additional app servers.

Up until now, conceptually we have had a single program, ASCIIChan, running on a single server, that handles all of our requests. If we have so many requests coming in that a single machine can no longer handle the load, what we can do is to add multiple machines to take up some of the load. Each machine will have its own cache, and will probably interact with the database as appropriate. But how do we get requests to multiple machines?

There will be a piece of technology that sits between the users and all of our app servers. This is a physical machine, just like the servers, that is optimised for performing just one task: spreading requests between multiple machines. The load balancer will have a list of all the app servers that are available, and decides which of these the requests from users should be directed to.

All the load balancer does is to take in the request, select a server, and then pass that request along. This is why it can handle so much traffic when the application servers can't. You will probably never have to write a load balancer. If you are using Google App Engine, or something similar, they do all of this for you, but it is good to know how they work.

There are a number of algorithms that a load balancer can use to decide which server to send a request to:

Random - select an app server at random.
Round Robin - requests are directed to app servers in turn.
Load-based algorithms - allocates based on current app server load.

###6.2.9 Quiz: Round Robin（server选择算法）

实现一个选择算法。其实很简单，利用余数循环即可。
Implement the function get_server(), which returns one element from the list SERVERS in a round-robin fashion on each call.

![web391.png-383.9kB][331]

###6.2.10 Caching With Multiple Servers

Why is our dictionary cache problematic with multiple app servers?

Check all that apply.

It's not! This is a trick question.
Multiple app servers = multiple caches. How do we keep them in sync?
Each app server may have to hit the db to update its cache.
We'll be caching data redundantly.

![web393.png-98.5kB][332]

使用多个app servers的话可能出现的问题：
1 多个serve，就有multiple caches，怎么让这些cache之间同步也是个难题
2 每个serve都要单独去访问database。

解决的方法是建立一个shared cache，让不同的serve都访问这个shared cache。当时这个cache只包含一些最关键的信息。这个cache叫做memcache，下一节具体介绍。

##6.3 Memcached

memcached是一套分布式的高速缓存系统，memcached的API使用三十二比特的循环冗余校验（CRC-32）计算键值后，将数据分散在不同的机器上。当表格满了以后，接下来新增的数据会以LRU机制替换掉。由于memcached通常只是当作缓存系统使用，所以使用memcached的应用程序在写回较慢的系统时（像是后端的数据库）需要额外的代码更新memcached内的数据。

![web394.png-85.2kB][333]


Memcached is essentially a very fast, in-memory cache. It is a free and open source, high-performance, distributed memory object caching system which was developed back in 2003 by a company called Danga Interactive for a system called LiveJournal. This was a very popular site where people maintained their own blogs before apps like FaceBook took over the world.

These days, just about every major website on the Internet, including FaceBook, Twitter, YouTube and Reddit, uses Memcached. It has become an essential piece of software when you are writing web applications. In fact, other than Linux, Memcached is probably the piece of software that most online sites have in common.

Memcached is a process which may be run on its own machine, but which may also be run on the same machines as the app servers. The algorithm is pretty simple and essentially similar to what we have been doing with caching up to now. What is handy about it is that all of your app servers can interact with Memcached. Memcached is fast enough, and can support a great many sockets so that is works well in a multi app server scenario. Also, most Memcached libraries have the built-in ability to use multiple Memcached machines.

Because Memcached is just a key-value store - basically like a giant hash table - you can hash on the keys to decide which server to send your data to. Because it is a cache, it is OK if you occasionally lose data since the authoritative copy is always held on the database. It is very common to run a little Memcached server on each machine and allow each app server to communicate with each of the caches.

- So, Memcached is a very simple protocol, and the operation that it does are very simple. Ultimately, we are going to be storing values to keys, where both the keys and values are strings. The operations look something like this:

SET(key, value)

GET(key) → value

DELETE(key)

There are other operations, and there are other parameters, but these are the main basic operations. With just these basic operations, we can implement all of the caching we have been doing in ASCIIChan in a system that will scale a lot better than just having a dictionary. We also have the advantage that, if our process is restarted, we don't start with an empty dictionary.

###6.3.1 QUIZ implement the basic memcache functions

```

# QUIZ implement the basic memcache functions

CACHE = {}

#return True after setting the data
def set(key, value):
    ###Your set code here.

#return the value for key
def get(key):
    ###Your get code here.

#delete key from the cache
def delete(key):
    ###Your delete code here.

#clear the entire cache
def flush():
    ###Your flush code here.

#print set('x', 1)
#>>> True

#print get('x')
#>>> 1

#print get('y')
#>>> None

#delete('x')
#print get('x')
#>>> None
```
![web396.png-186.6kB][334]

![web395.png-257.6kB][335]

###6.3.2 Properties Of Memcached

One of the main properties of Memcached, and one of the things that makes it different from a normal database, it that it stores everything in memory. This is what makes it so fast. Reading from memory is very fast, while reading from disk can be relatively slow. This gives Memcached a couple of properties:

- It is very fast.
- It is not durable. If you re-start Memcached you will lose all your data.
- The amount of data we can store is limited by the amount of memory that machine has.


**Quiz: Properties Of Memcached**

What happens when you store more data in Memcached than there is memory available?

Error
Throw away data that is least frequently used.
Throw away data that is least recently used.
Write the extra data to disk.

###6.3.3 Memcached And ASCIIChan

![web398.png-90.1kB][336]

So let's replace our dictionary cache in ASCIIChan with Memcache.

Fortunately, there is a version of Memcache built into the App Engine that we use on our local machines. This lets us use it when we are developing apps, and then when we deploy to App Engine, Google has it ready installed so we don't have to deal with it. The first thing we need to do is to import Memcache which is in the Google App Engine API:

from google.appengine.api import memcache
Now we are ready to replace our dictionary cache with Memcache. The current function of our cache and top_arts() function looks like this:
```
CACHE = {}
def top_arts(update = False):
        key = 'top'
        if not update and key in CACHE:
                arts = CACHE[key]
        else:
                logging.error("DB QUERY")
                arts = db.GqlQuery("SELECT * "
                                    "FROM Art "
                                    "WHERE ANCESTOR IS :1 "
                                    "ORDER BY created DESC "
                                    "LIMIT 10",
                                    art_key)
                arts = list(arts)
                CACHE[key] = arts
        return arts
```
We no longer need the CACHE dictionary, and we can delete it.

Next, in the function top_arts() we need to try to look up arts from Memcache:

`arts = memcache.get(key)`

Now, in the official Memcached protocol, both keys and values need to be strings. In the Memcache library that Google provides, the values can be Python datatypes which the library will convert into strings. When you fetch the data back from the cache, the Memcache library will convert it back into your Python datatype. So we can still store our art objects directly into the cache, but the keys have to be strings.

The next thing we are going to do is to modify the if statement in top_arts(). If arts isn't in the cache, the value of arts will be None, so we can say:

if arts is None or update:
If this is True, the we run the db query.

Lastly, we need to modify the line that updates the cache if we had to run the db query as follows:
```
memcache.set(key, arts)
So, the top_arts() function now looks like this:

def top_arts(update = False):
        key = 'top'
        arts = memcache.get(key)
        if arts is None or update:
                logging.error("DB QUERY")
                arts = db.GqlQuery("SELECT * "
                                        "FROM Art "
                                        "WHERE ANCESTOR IS :1 "
                                        "ORDER BY created DESC "
                                        "LIMIT 10",
                                        art_key)
                arts = list(arts)
                memcache.set(key, arts)
        return arts
```
If we now refresh the browser a couple of times to reload ASCIIChan, and then check the log file we see:

>packages\\setuptools-0.6c11-py2.7.egg-info' ERROR 2012-05-23 11:22:27,759 main.py:67] DB QUERY INFO 2012-05-23 11:22:27,986 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-23 11:22:28,157 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 304 - INFO 2012-05-23 11:25:00,576 dev_appserver.py:2891] "GET / HTTP/1.1" 200 - INFO 2012-05-23 11:25:01,019 dev_appserver.py:2891] "GET /favicon.ico HTTP/1.1" 304 -

When we first reloaded the page we got a db Read, as we would expect since the Memcached cache would be empty, and on the next reload there was no db read as the art was loaded from Memcache.

Now, if you're running App Engine, there is a built-in Admin tool for Memcache. If you are running App engine, you can go to _ah/admin/memcache and you will see the Memcache viewer. This shows you information about the cache and provided tools, including "Flush Cache", which are useful for helping you test the caching in your apps.

Google App Engine documentation for Memcache


###6.3.4 Stateless

Adding Memcached to ASCIIChan has given us two new properties which are really nice.

- The cache will now survive restarts (of the app).
- The app is now stateless.

Statelessness is the key to scaling. What it means is that the app doesn't store any state information between two requests. A number of properties stem from the fact that the app is now stateless:

- There is no state between requests
- Apps are now interchangeable.
- Adding/removing apps is easy
- Apps can be scaled independently of the cache and database.

Now, when your app is constrained in different ways, perhaps by database reads, caching, or maybe by processor requirements, any part of the system can be scaled independently of all the others. This is a large part of what scaling is about.


![web397.png-95.9kB][337]

###6.3.5 Advanced Cache Updates

这一节提出了一个问题。如果是multi-server,不同的server互相之前提交cache的时候可能会覆盖别的server的data.下一节提出了解决办法。

![web399.png-78.9kB][338]

Consider the following problem:

**Multiple users submit to the app at the same time, update the cache at the same time and overwrite each others data.**

What are the possible implications of this?

Imagine the scenario where we have two users, User A and User B, each being served by a different app server, and both trying to submit data to the database. The database currently holds two pieces of data, element1 and element2. User A submits element3 to the database at the same time as User B submits element4.

So far, there's no problem. The database is designed to handle this situation and it will now contain the four elements: element1, element2, element3 and element4. Now we come to update the cache, and this is where the problem manifests.

If each app server manipulates the cache directly (without communicating with other app servers) the first app server will attempt to update the cache to store element1, element2, and element3 at the same time as the second app server tries to update the cache with element1, element2, and element4. One app server will overwrite the other, and whichever data makes it to the cache will be wrong!

If we were using our earlier approach where we read from the db after data was submitted and then updated the cache from the db read we would still have a problem. The first app server will insert element3 and then read the database, getting the result element1, element2, element3. The second app server inserts element 4, reads the db and gets element1, element2, element3, element4. **Now there is no way to guarantee which app server will write to the cache first.** Therefore we cannot guarantee that the contents of the cache will be correct after the update.

If we redirect the user to the front page to do the update that way, the odds of the 'wrong' data being stored in the cache are even greater because of the additional delays introduced be the need to communicate with the user.

Let's look at a possible solution to this problem.

###6.3.6 CAS

这种方法是用cas(key, value, unique) 里面的unique来当判断的钥匙，只有当unique match的时候一个app server才能overwrite.如果A server想要修改的data已经被B server修改过了，那么也不能进行overwrite.

![web400.png-81.6kB][339]

Memcache has a couple of ways of dealing with the problems we saw in the last section. The first of these is called CAS, which stands for Compare and Set. CAS adds two commands to the Memcache protocol:

gets(key) → value, unique

cas(key, value, unique) → True/False

gets() is an alternative to the get() function, and cas() an alternative to set(). unique is like a hash of the value which is unique to the specific value in Memcache.

The way that the cas() function works is that, if the unique matches the unique that you get out of Memcache it is OK to overwrite the value and return True. If you don't pass a unique, or the key isn't in the cache, or the unique has changed, then the cas() function won't set the value and will return False.

Now you have two commands that you can use to prevent two people from overwriting the same key in the cache.

The code that an app server would use to update the cache might look something like this:
```
val, unique = memcache.gets(key)
r = memcache.cas(key, newval, unique)
while r == False:
    val, unique = memcache.gets(key)
    r = memcache.cas(key, newval, unique)
```
The loop gets the new unique out of Memcache and tries to update val to newval. When r is true you know that you have successfully updated the value.

###6.3.7 Quiz: Implementing CAS

Implement the gets() and cas() functions for our simple simulation of Memcached.

For gets(), return a tuple of (value, h), where h is hash of the value. A simple hash you can use here is hash(repr(val)).

For cas(), set key = value and return True if cas_unique matches the hash of the value already in the cache. If cas_unique does not match the hash of the value in the cache, don't set anything and return False.

```

CACHE = {}

#return True after setting the data
def set(key, value):
    CACHE[key] = value
    return True

#return the value for key
def get(key):
    return CACHE.get(key)

#delete key from the cache
def delete(key):
    if key in CACHE:
        del CACHE[key]

#clear the entire cache
def flush():
    CACHE.clear()

# QUIZ - implement gets() and cas() below
#return a tuple of (value, h), where h is hash of the value. a simple hash
#we can use here is hash(repr(val))
def gets(key):
    ###Your gets code here.

# set key = value and return True if cas_unique matches the hash of the value
# already in the cache. if cas_unique does not match the hash of the value in
# the cache, don't set anything and return False.
def cas(key, value, cas_unique):
    ###Your cas code here.

#print set('x', 1)
#>>> True
#
#print get('x')
#>>> 1
#
#print get('y')
#>>> None
#
#delete('x')
#print get('x')
#>>> None
#
#set('x', 2)
#print gets('x')
#>>> 2, HASH
#
#print cas('x', 3, 0)
#>>> False
#
#print cas('x', 4, HASH)
#>>> True
#
#print get('x')
#>>> 4
```

![web401.png-430.8kB][340]

执行后看输出结果
![web402.png-164.8kB][341]

###6.3.8 Quiz: Separating Services

Why do we separate our services?

Choose all that apply.

So they can be scaled independently.
To increase fault tolerance.
So two very different processes aren't competing for resources.
So they can be updated independently.

![web403.png-82.9kB][342]

###6.3.9 Additional Pieces

通过DNS来分配负载（load）。负载平衡（Load balancing）是一种计算机网络技术，用来在多个计算机（计算机集群）、网络连接、CPU、磁盘驱动器或其他资源中分配负载，以达到最佳化资源使用、最大化吞吐率、最小化响应时间、同时避免过载的目的。

![web404.png-82.5kB][343]

第三方
![web406.png-84.1kB][344]


Let's close this lecture by looking at a few final pieces that would be needed for a major website, but that we haven't really talked about yet.

Firstly, what happens if we get really big, and we're receiving so much traffic that a single load balancer can no longer handle it. We can add a second load balancer, but what load balances the load balancers? What you would generally do in tis situation is something called DNS Round Robin.

DNS is the system that converts a domain name into an IP address. It is cached across the Internet with DNS machines all around the world. What you would do is, instead of mapping your site to a single IP address, you would map it to several IP addresses, one for each load balancer. This can allow you to spread potentially huge amounts of traffic across multiple load balancers.

Another thing that you may have is another cache just for HTML. This cache may intercept requests before they even reach that app servers. The HTML cache may hold HTML and images and so forth that are not going to change for a particular user or group of users (e.g. users who are not logged in). Some examples of the technology available to provide HTML caching are Varnish (used at Reddit and Hipmunk) and Squid, although many companies may well develop their own bespoke system to exactly match their requirements.

Another thing that you may use is a CDN or Content Delivery Network. These are 3^rd^-party companies that you pay to cache your content all across the internet. They have machines all over the world that can intercept your DNS requests and, if they have the page that your customer has requested in their cache, respond without passing the request on to your servers.

So the name of the game is caching, and the real question is at what level do you cache? The issue is how much content is actually different on each request and how much is the same. Content that is the same can be cached, and ideally, you will push that content further away from you, and closer to your customers to achieve higher speeds.

##6.4 ASCIIChan 2

The final version of ASCIIChan 2 now looks like this:
```
import os
import re
import sys
import urllib2
import random
import logging
from xml.dom import minidom
from string import letters

import webapp2
import jinja2
from google.appengine.api import memcache
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

art_key = db.Key.from_path('ASCIIChan', 'arts')

def console(s):
        sys.stderr.write('%s\n' % s)

IP_URL = "http://api.hostip.info/?ip="
def get_coords(ip):
        ip = "4.2.2.2"
        url = IP_URL + ip
        content = None
        try:
                content = urllib2.urlopen(url).read()
        except URLError:
                return

        if content:
                d = minidom.parseString(content)
                coords = d.getElementsByTagName("gml:coordinates")
                if coords and coords[0].childNodes[0].nodeValue:
                        lon, lat = coords[0].childNodes[0].nodeValue.split(',')
                        return db.GeoPt(lat, lon)

class Handler(webapp2.RequestHandler):
        def write(self, *a, **kw):
                self.response.out.write(*a, **kw)

        def render_str(self, template, **params):
                t = jinja_env.get_template(template)
                return t.render(params)

        def render(self, template, **kw):
                self.write(self.render_str(template, **kw))

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"
def gmap_img(points):
        markers = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in points)
        return GMAPS_URL + markers

class Art(db.Model):
        title = db.StringProperty(required = True)
        art = db.TextProperty(required = True)
        created = db.DateTimeProperty(auto_now_add = True)
        coords = db.GeoPtProperty( )

def top_arts(update = False):
        key = 'top'
        arts = memcache.get(key)
        if arts is None or update:
                logging.error("DB QUERY")
                arts = db.GqlQuery("SELECT * "
                                        "FROM Art "
                                        "WHERE ANCESTOR IS :1 "
                                        "ORDER BY created DESC "
                                        "LIMIT 10",
                                        art_key)
                arts = list(arts)
                memcache.set(key, arts)
        return arts

class MainPage(Handler):
        def render_front(self, title="", art="", error=""):
                arts = top_arts()

                img_url = None
                points = filter(None, (a.coords for a in arts))
                if points:
                        img_url = gmap_img(points)

                #display the image URL
                self.render("front.html", title = title, art = art, error = error, arts = arts, img_url = img_url)

        def get(self):
                self.render_front()

        def post(self):
                title = self.request.get("title")
                art = self.request.get("art")

                if title and art:
                        p = Art(parent=art_key, title = title, art = art)
                        #lookup the user's coordinates from their IP
                        coords = get_coords(self.request.remote_addr)
                        #if we have coordinates, add them to the art
                        if coords:
                                p.coords = coords
                        p.put()
                        #rerun the query and update the cache
                        top_arts(True)

                        self.redirect("/")
                else:
                        error = "we need both a title and some artwork!"
                        self.render_front(error = error, title = title, art =art)

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
```                            

# Lesson 7: Changing the World - Building a successful web application project
##7.1 Introduction and Overview

这一章主要讲一些现实生活中怎么设计网站，reddit, udacity遇到的问题。

This lesson is basically a wrap-up lesson, but it will contain some fun stuff. It is all about real-world issues. Things like what to look for in a web framework, how to get hosted and some of the decision making that should underpin these choices.

We will talk about how Reddit began on a single machine and how they grew and scaled, learning as they developed. This will include fascinating insights from guest speakers from Reddit and Udacity who can provide further real-life insights into some of the issues that we have discussed on this course.

There are no quizzes in this lesson.

##7.2 Code Organisation

steve讲了自己如何组织代码，以及文件结构

![web408.png-303.2kB][345]

![web407.png-121.8kB][346]

A question that comes up a lot is "How do I organise code?". You don't want to keep all your code in one Python file, so what is the correct way to organise things?

Well, the first thing to point out is that there is no, one, correct answer. Whether you are writing web apps, or any other kind of software, how you organise your code is something that is personal to you, and will come from your own experience. Steve goes on to explain his approach:

When he starts out, Steve tends to begin with everything in a single file. The file will probably have sections for:

- handlers, which define what to do when a particular URL is hit
- URL mappings, which map URLs to the correct handlers
- db Models

Alongside these, Steve will have a number of separate files for static content, including things like css, JavaScript, images, and so forth. Another thing that Steve will almost always keep separate from the beginning are his template files.

Steve's main Python file is often called simply main.py.

The first thing that he does with main.py is to pull out the db models into a separate file. If you are not using Google App Engine, you may need to write an additional piece of code called the ORM (Object Relational Mapping), which maps your Python objects to the relational database. We haven't had to deal with that in this class because App Engine provides this functionality. Steve will generally have a separate file for each type of data, e.g. posts, art, users, etc. Class specific functions would go into the appropriate file, so, for example password hashing functions would go in the users file, and functions to get the top posts etc. would go into the posts file.

The next thing that Steve almost always has is a file called utils.py (which might actually be a series of files in a directory). This holds all the 'random stuff' and handy 'things'. Things like make_secure_val() or make_salt() or random_string(). In general, Steve likes to put as much into utils as he can, so it will include a lot of date-manipulation and string-manipulation functions and also escaping functions. This should be just a list of 'flat' functions - functions that have no dependencies on any other part of the project. It is really important that it is only a one-way inheritance. Handlers can import from utils. Database can import from utils. Anything can import from utils, but functions in utils never import from other parts of the project. In the Reddit source code there are about 100 functions that are used all over the rest of the code.

The final thing that Steve does (and this might be quite time-consuming) is to take the handlers out of main.py. There may be separate files for each type of handler.

So by now, main.py is just the URL mappings and a bunch of imports.

For the file structure, Steve uses a structure something like this:

- /main.py
- handlers.py
- blog.py
- ROT13.py
- etc.

    - /lib
    - utils.py

        - /db models
    - /templates

    - base.html front.html
    - etc.
    - /static
    - main.css etc.
    


At the top-level in the main directory there will be main.py and something like a handlers.py file that hold the generic handler for things that happen on every request, together with the specific files for the project (like blog.py or ROT13.py etc.). The bulk of the code is in these files. Below that directory there will probably be a directory called 'lib' which contains stuff like the utils file and, within that directory, a further sub-directory for the database stuff.

There will also be directories called 'templates' and 'static' which contain the template files and static files like CSS.

##7.2 Hosting

Steve Huffman

There are a range of questions about hosting. We have been using Google App Engine, but what other choices are there? What issues does each potential solution bring with it? Let's see if we can't answer a few of these questions here.

###7.2.1 Local Hosting

The first option is to run your website locally. Essentially, running your website from a machine that might be in your home or small office.

This works fine for a single user (the sort of thing we have been doing in this class) where the site doesn't have to be on all the time, but in almost every other type of use, this option really doesn't make sense. Some of the main drawbacks are:

- The site isn't always on.
- The site isn't always accessible.
- Your IP may change (or you may need to pay extra for a static IP address).

![web410.png-34.9kB][347]

### 7.2.2 Co-location Hosting

The next thing that you can do is to 'co-locate'. Basically, this means buying space on a rack in a datacentre. You still buy your own machine (or machines) and then install them in the datacentre. This means that you still have control over the machines and just pay for rent, power and bandwidth.

The downside is that it involves a lot of work maintaining the system. You need to administer the machines, install software (and software upgrades), and maintain the machines.

Very few large websites don't control their own machines.

###7.2.3 Managed Hosting

![web412.png-281kB][348]

Another option is .managed hosting'. This industry is changing right now. Just a few years ago, you would rent the number of preconfigured machines that you needed from a datacentre. Now there is a move towards managed hosting in the cloud from companies like AWS, Rackspace and Linode. Reddit and Hipmunk both use AWS

You rent machines from the provider and pay an agreed amount for bandwidth. Although you can install the OS, in reality you are probably just going to be configuring the OS so you are reducing the number of sysadmin tasks that you need to carry out. From your perspective all the admin and maintenance tasks are carried out virtually.

Reddit progressed from local hosting, through co-location hosting and is now operating in a managed hosting environment with AWS.

###7.2.4 Zero System Administration

![web413.png-281.1kB][349]

At the next level up, we have things like Google App Engine and Heroku which are completely managed for you. You don't even need to think about machines or OS, you just upload your code and they run the databases, sharding etc. There is virtually no sysadmin. A lot of big websites have been built in just this environment - Udacity being one of them.

However, it can be very difficult to customise things. It can be difficult to do anything that the providers of the systems haven't already thought of beforehand.

There is no real penalty for choosing the 'wrong' hosting solution when you start out. You can just move to a different model. That doesn't mean that moving will necessarily be easy. When Reddit moved from co-location to AWS, they were already a fairly large website. They needed to run two infrastructures in parallel for a while as they slowly migrated from one to the other.

##7.4 Web Frameworks

![web414.png-249kB][350]
Another good question is about how to choose between web frameworks. The web framework is the application that interfaces between your program and the Internet. In this class we have been using the Google App Engine framework, webapp2. This handles HTTP, scheduling, parsing basic headers,, converting your response object into the appropriate HTTP to send to the browser, URL mapping and so forth. Different web frameworks give you more or less control and so require you to do more or less work.

Google App Engine operates at the level that Steve likes to work at. From his point of view, the important features are:

- Direct access to GET and POST

    - Understanding web apps at the method level is very important.
- Direct access to the request

In other words, you have access to the low-level stuff that you may want to modify, but it isn't so low that you're having to worry about HTTP versions or host headers (unless you really want to).

A lot of frameworks provide features that Steve would consider unimportant, such as:

- Sessions
- Caching
- Automatic forms
- db - ORM

The problem with these tools is that they may not allow you to manage custom behaviours in quite the way that you would want to do. As a guide, avoid systems that seem too "magical". If you are so far away from the actual request that you don't actually understand what just happened, you are asking for trouble down the line.

###7.4.1 Templates

Template languages come in all shapes and sizes. One that Steve is partial to is called Mako. Mako templates are written in Python. The template language that we have been using in this class is called jinja2, which Steve has also found to have worked well.

The key to using templates is having the discipline to separate code from templates. A lot of these template systems allow you to put arbitrary code into them, but you should try to keep the amount of code in your templates to an absolute minimum. You have a whole programming language (in our case Python) which lets you do all sorts of wonderful things. Why would you choose to use a broken subset of that in your templates?

## 7.5 How I Work

Steve展示了自己平时的编程状态
![web417.png-206.3kB][351]

Here, Steve describes how he works when developing a web app.

When developing a web application you will generally have a browser window and your editor open together. Side-by-side is ideal, but not always practicable.

Something that people often neglect is to have the Terminal open nearby. Steve almost always runs the app server out of a terminal (even when using App Engine), so that he can see the logs. If you are developing without the ability to see your logs, there is a lot of stuff that you are going to miss. You can find many, many bugs by running the web site in the browser and watching the logs. In many cases, there might be an error that you aren't even aware of, but that could be a big deal in production, which you can spot and fix in 10 seconds if you are monitoring the logs.

- Another thing that Steve sees as a problem with App Engine right now is that if you are writing code that writes to a database, it is critical that the queries that you run are printed to the log. If you have a complicated setup with your database and your cache or memcache, you need to make sure that it is working. If you are scrolling through your site and see lots of database queries appearing in the logs, that is a sign that something is broken! In general, you will want to make sure that every page you run doesn't hit the database unless absolutely required.

Try to get into the habit that when you switch from your editor to your browser, you instead switch to your browser plus the Terminal so that you can see things working. If you get a sense of how the logs scroll when your website is working normally, when it deviates from this you will spot it and so pick up bugs more quickly.

##7.6 Reddit

![Steve Huffman][352]

We have referred to Reddit quite a lot over the course of this class. We've looked at database examples and system architecture examples, and seen some of the mistakes that Steve made while developing Reddit. Let's now take a look at how Reddit was built, and how it grew over the years.

Reddit began in June 2005 with Steve Huffman and his co-founder (and college roommate) Alexis Ohanian. Steve was the engineer, and Alexis was the everything-else guy.

The first version of Reddit was written in Lisp. Everything was created in Lisp. This included the handlers, HTML CSS and JavaScript (Lisp is a language that lends itself to generating other languages and other pieces of code really nicely). This meant that the entire site was built from Lisp and Postgres. There was no memcache at that time, Steve just stored everything in an in-memory hash-table.

###7.6.1 Reddit Architecture

![web419.png-54.1kB][353]

The original Reddit architecture was something like this.

They had a single rented machine which ran Lisp and Postgres. The database structure had tables for:

- Links (score, title, URL)
- Votes (link-id, direction)
- Users (name, password)
(Reddit didn't include comments for a long while).

The database also had a lot of joins.

The initial setup lasted for about six months. At about that time, Reddit merged with another company called Infogami and added a couple of engineers, Aaron Swartz and Chris Slowe, to the team. The expanded team re-wrote Reddit from Lisp into Python, and also moved the database onto a second machine. Going from a single machine to two machines and separating the app server from the database gave about a four-times improvement in speed.

At this time, the major issue was downtime. Whether in Lisp or Python, sometimes the site would just crash and they would get a notification and one of the team would have to bring the site back up. In retrospect, Steve says that it makes him cringe to think about how much stress he went through worrying about whether their website was up or not. Particularly since there are so many easy ways to avoid that scenario. Shortly after that, they added a piece of software called Supervise which monitored the app server, and if the application crashed it simply restarted it.

Essentially, they were very lucky that they never lost an actual machine through hardware failure. Especially since losing the database machine would have meant losing all the data (they weren't doing good backups!). Hardware failure is a fact of life. If you run your machines 24 hours a day, 7 days a week, at high load you are going to get hardware failures including hard disks, memory, etc.

###7.6.2 Reddit Architecture 2

![web420.png-100.3kB][354]

The next step in improving the speed of the site was to add another database. This was using a piece of software called Slony to replicate the database. There was still only the one app server at this time, and the caching was relatively limited, so they were making a lot of database requests.

The app server was hitting both of the database machines, and this was when they first ran into the problem of database lag. Slony was pretty good at replicating the database, but it was possible for the slave system to lag behind the master database by up to 5 seconds. Their solution was to improve their caching, but since they had two python applications running on the app server, and two databases they also faced the problem of keeping their caches in sync. They did this using a library called Spread. Spread is a network library which, if you send a message to one host, ensures that it is sent to all hosts.

Spread was also used to keep the hash tables in sync when they added an additional physical machine as a second app server. Obviously, this solution wouldn't scale very well since as the number of servers increased there would be a huge increase in network traffic as Spread attempted to keep them all in sync. The solution would be to use memcache, but this wouldn't happen until after the database was re-written.

Shortly after adding the second app server machine, Reddit added comments. The first version of comments was just another database table. It had a link-id, contents, author-id. Nothing very complicated. But the database still had a lot of joins. It was about this time that Reddit changed to a more flexible database architecture.

The challenge that they faced was that every time they added a new feature, they might have to add a new table, or they might need to a new column to an existing table. Adding columns would take time, and making the changes might require a data migration. or updating indexes all of which would add further load to the system and hit performance. The rate at which they could add features was limited by the rate at which they could make changes to their database and do these large migrations. In Steve's words, "It was a total pain!".

###7.6.3 Thing Db

![web421.png-88.5kB][355]

The flexibility that they were looking for in the database was provided by something called ThingDb. If you find any references to TDB or TDB2 in the Reddit code, this is what it is referring to.

Instead of having a table that looked like this:

Link:

URL	title	date	score
They would instead have a table, called a thing table, with just a few properties on it like this:

Link

score	author	date
These are the properties that everything has. Whether it's a link, a comment, or anything else. Then they had a separate table for each datatype that held just 3 things: the thing-id, a key and a value:

Data:

thing-id	key	value
So a link might have a row in the thing table like this:

1	5	0	06/01/05
and then several rows in the data table:

1	URL	...
1	title	...
There is therefore a row in the data table for every property of a thing that isn't common across all of the things. These are now different database tables, and they don't even have to be located on the same machine.

This allowed them to add features much more quickly and easily. If they wanted to add a new datatype to links, the new links would just have extra rows in the data table. Then they could just say, in effect, if the link doesn't have a value for this new property, we'll just pretend it has some specified default value.

So now they didn't have to get all their data structures exactly right way in advance. Later on, when they added sub-Reddits - which allowed users to make their own categories (their own "Reddits"), these were just another 'thing' which made the whole development process a lot simper.

###7.6.4 Scaling

![web422.png-79.9kB][356]

So Reddit were at the point where they had a couple of app servers, running their own caches, and a couple of databases that were replicas of each other. They had also added a load balancer to improve the performance of their app servers.

The next thing that they added was the memcached layer. Now, instead of the app servers having their own in-memory cache, they would communicate via memcache. Now there was just the one cache shared among all of their app servers. With 20/20 hindsight, Steve now says that they should have added memcache from the beginning.

To improve the databases, they began by segmenting by type. Thus there would be one database for just links and another for just comments. This means that if you are only submitting a link, or if you are only submitting a comment, you only have to access one database. In fact, this is essentially the structure that Reddit has to this day.

Steve didn't include sharding from the beginning. Although he had it in mind when he re-wrote Thing db, it was left out in the rush to get into production. The lesson that he has learned from the experience is that when you are developing a large system, if you don't do the hard parts up-front, you may never get the chance.

he framework that Reddit used, at least since it has been using Python, is called web.py. The Google App Engine framework, webapp2, inherited many of its features (including the handler class with distinct get() and post() functions from web.py).

###7.6.5 Pre-computed Caching

![web423.png-88.2kB][357]

One of the other big architecture pieces that Reddit added to help them scale was the notion of a pre-compute cache. They would find themselves having to run the queries needed to generate the hot page for Reddit over-and-over again. They may have been able to cache it for a minute, but when that minute expired they had to recalculate it once again.

Alongside this were all the user pages. Every user had lists of the things that they had submitted and liked together with their top-things. Every subReddit had a new page and a hot page and so forth.

So, Reddit started to pre-compute everything. The way that they did this was to use a whole new database stack which were essentially replicas of the links database. These could lag behind the main database a little bit without causing a problem. When a vote came in, the app server would generate e series of tasks. These included recomputing the Reddit front page, recompute this user's likes page, recompute the user's top page and so forth. These tasks were held in a queue which fed a couple of machines called the "pre-compute servers".

The PC servers would take tasks from the queue and run the jobs against the new replica database. As a result, these databases ran really hot, although no real-time requests from the Internet ever touched these pre-compute machines. When the jobs completed, the result was stored in memcached. Now, almost every page you access on Reddit comes directly from the cache. There a very few things that you can do on Reddit that will directly manipulate the database.

Once they had reached that point, scaling became a lot easier. The main comments and links databases are now really the 'last-resort' primary data source. Any data you can access in real-time on Reddit is actually sourced from memcached. Every single listing is pre-computed and stored in memcached. This is also the reason that you can't go back beyond about 1000 links on any given listing. The upside is that it is now very fast.

###7.6.6  Interview With Neil

下面是Steve Huffman和 Neil Williams（Lead Engineer, Reddit）两个人详细介绍了reddit使用的工具和方法。有兴趣的话具体再看相关内容。

![web424.png-894.4kB][358]

![web425.png-684.7kB][359]

1.6.7 App Server Architecture
1.6.8 Database Architecture
1.6.9 Cache Architecture
1.6.10 Problems With Memcachedb
1.6.11 Locking And Memcache
1.6.12 Zookeeper
1.6.13 Improving Memcache
1.6.14 Pre-Compute Architecture
1.6.15 Mapreduce
1.6.16 Hadoop
1.6.17 Dealing With Search Indexing
1.6.18 Using The Queue
1.6.19 Lock Contention
1.6.20 Growing Reddit
1.6.21 Spam Prevention


  [1]: http://static.zybuluo.com/bramble/2hmz0be4jkgh3s7enix3eakq/wd1.png
  [2]: http://static.zybuluo.com/bramble/wnk4z6dhe018xt3c8629xfa1/wd2.png
  [3]: http://static.zybuluo.com/bramble/0or5emo0ejm9o76i6s1v0mq8/wd3.png
  [4]: http://static.zybuluo.com/bramble/q6wz1s2toh6167rtzfbvep4p/wd4.png
  [5]: http://static.zybuluo.com/bramble/orzu51sszoyeeaog17j023qx/wd5.png
  [6]: http://static.zybuluo.com/bramble/m60pbbw23yi61r0hzow3wbwm/wd6.png
  [7]: http://static.zybuluo.com/bramble/iljdzxmkurb0pqjte8mfis8x/wd7.png
  [8]: http://static.zybuluo.com/bramble/96d4p2idueirwbvgskm7hlyk/wd8.png
  [9]: http://static.zybuluo.com/bramble/oo8e6skkmbb4vzqwoh5ypxw5/wd9.png
  [10]: http://static.zybuluo.com/bramble/8rvyrd253fnvhuzhpzoxc7kr/wd10.png
  [11]: http://static.zybuluo.com/bramble/hymxuugtuppjn3t3wa7k1rys/wd11.png
  [12]: http://static.zybuluo.com/bramble/jau6s5x2ap9rx13cjgpiq1xa/wd12.png
  [13]: http://static.zybuluo.com/bramble/5tozch3c6lxh8z5b92d3gob7/wd13.png
  [14]: http://static.zybuluo.com/bramble/xsqq7xm6b6fhkqq8nf6a57sr/wd14.png
  [15]: http://static.zybuluo.com/bramble/jlxx5kjzo8k23i5dqum8b926/wd15.png
  [16]: http://static.zybuluo.com/bramble/y66am6u8sk1u495uz7q22hhv/wd16.png
  [17]: http://static.zybuluo.com/bramble/r0bget00m2k55je763vaaxmf/wd17.png
  [18]: http://static.zybuluo.com/bramble/gnlhzmpdpqj3rr38uai9ms66/wd18.png
  [19]: http://static.zybuluo.com/bramble/p2xr3ntyhdmmov8ofbyjscgc/wd19.png
  [20]: http://static.zybuluo.com/bramble/ioz07253bf7gh8nho0lpf4zw/wd20.png
  [21]: http://static.zybuluo.com/bramble/bw8g1133jm06nq44yb8vg25y/wd21.png
  [22]: http://static.zybuluo.com/bramble/8cqawzhtdbu2qgogyhpvhqt1/wd22.png
  [23]: http://static.zybuluo.com/bramble/ch1o39qdcz177pnjwiy6a330/wd23.png
  [24]: http://static.zybuluo.com/bramble/11xauxhe7wabkbshc4b008ns/wd24.png
  [25]: http://static.zybuluo.com/bramble/mr7dn2npmuf569ijqbo4j9sd/wd25.png
  [26]: http://static.zybuluo.com/bramble/ylj6wjm2n3othneshvgwfua7/wd26.png
  [27]: http://static.zybuluo.com/bramble/2m1idybo09m4wtxvnzqhk6r1/wd27.png
  [28]: http://static.zybuluo.com/bramble/g0ixtofilp4ildxme0y3cz9t/wd28.png
  [29]: http://static.zybuluo.com/bramble/lck2b6o5t98verzp4ixf6fnz/wd29.png
  [30]: http://static.zybuluo.com/bramble/3ltg01wz2mvdi1lsershs2cd/wd30.png
  [31]: http://static.zybuluo.com/bramble/y8rg8xzk2jsajyltxzr26n62/wd31.png
  [32]: http://static.zybuluo.com/bramble/5u7ankqm3nj0or46aj4bko3r/wd32.png
  [33]: http://static.zybuluo.com/bramble/m73j1s74fk257ax9lgi8oo6h/wd33.png
  [34]: http://static.zybuluo.com/bramble/vpooo5gcfsa9a093jx69xczy/wd34.png
  [35]: http://static.zybuluo.com/bramble/hzonetzvxjtwy8gr8h0hag3p/we35.png
  [36]: http://static.zybuluo.com/bramble/acvenb9a2lw3r58e4yx3a8bc/web37.png
  [37]: http://static.zybuluo.com/bramble/2eubzg8pe32przpppea5h7v6/web38.png
  [38]: http://static.zybuluo.com/bramble/mswyojn2csdpallg3vowtpql/web39.png
  [39]: http://static.zybuluo.com/bramble/rwir56zy9tegqzpt1qamd02r/web40.png
  [40]: http://static.zybuluo.com/bramble/vkmjd1mhtty5xinkgnxf8clf/web41.png
  [41]: http://static.zybuluo.com/bramble/izuvf3n7087xae2g3icofspa/web43.png
  [42]: http://static.zybuluo.com/bramble/v7wo40ygnz3cgb0xs6w94ffn/web42.png
  [43]: http://static.zybuluo.com/bramble/l4gi0qp2b52k6y7982hzrile/web44.png
  [44]: http://static.zybuluo.com/bramble/gtnptjlqg4wkiffe1mlt2o26/web45.png
  [45]: http://static.zybuluo.com/bramble/xkc8p1e2mssw7rh5gcp3vgyt/web46.png
  [46]: http://static.zybuluo.com/bramble/1de4il9ohzs5nmr9a5gontun/web47.png
  [47]: http://static.zybuluo.com/bramble/n8a8toq9puog87rkft1adr2i/web51.png
  [48]: http://static.zybuluo.com/bramble/o4nr0pez920dw4dchh3qjsdo/web49.png
  [49]: http://static.zybuluo.com/bramble/9paiuy5995xm5jz1vgnlw4o2/web50.png
  [50]: http://static.zybuluo.com/bramble/wbpor22qcp6spytrql4tjupm/web52.png
  [51]: http://static.zybuluo.com/bramble/ioks6387ftk5dtuzj1mz6twu/web53.png
  [52]: http://static.zybuluo.com/bramble/1stdvfh0rmlxx847ggnju38v/web54.png
  [53]: http://static.zybuluo.com/bramble/mylj9q687go75tg98lba6bbh/web55.png
  [54]: http://static.zybuluo.com/bramble/mhijvpngdb1fr6awz87tv5f8/web56.png
  [55]: http://static.zybuluo.com/bramble/6xd08ab7o5zfs32ojs24vet3/web57.png
  [56]: http://static.zybuluo.com/bramble/vqfn71owkqxps0066xoxc24o/web58.png
  [57]: http://static.zybuluo.com/bramble/bsxlkhn42g1gjug0jub3p82i/web59.png
  [58]: http://static.zybuluo.com/bramble/hh3ysr9kceobf0hsngddoaau/web60.png
  [59]: http://static.zybuluo.com/bramble/xtra3llk7vgtmvrgnmv9xs2v/web61.png
  [60]: http://static.zybuluo.com/bramble/b4de6i5sncxaueylcowm4ife/web62.png
  [61]: http://static.zybuluo.com/bramble/dpn0jjbcm09sscd9p461uue8/web63.png
  [62]: http://static.zybuluo.com/bramble/uair2bhy55dsqt5sgkmso8xw/web64.png
  [63]: http://static.zybuluo.com/bramble/qc93buc7zhk7dvfnwufdg06l/web65.png
  [64]: http://static.zybuluo.com/bramble/ji9g2x4rgfd7l95mci1hkxqw/web66.png
  [65]: http://static.zybuluo.com/bramble/yq409sqtqug78r0t2v5xo01h/web67.png
  [66]: http://static.zybuluo.com/bramble/7yw3uzjq9avk1hksu37pn6nx/web68.png
  [67]: http://static.zybuluo.com/bramble/vg39y3epz667ji460u0r7atn/web69.png
  [68]: http://static.zybuluo.com/bramble/vl5fdjkazxu4bff46fzwl5qw/web70.png
  [69]: http://static.zybuluo.com/bramble/hkclolsotl78ycvz5heu4dy4/web71.png
  [70]: http://static.zybuluo.com/bramble/vrmo0b0mywhvukxd0mxc990d/web72.png
  [71]: http://static.zybuluo.com/bramble/mm61ejujhnw8vhf58ywo99wf/web73.png
  [72]: http://static.zybuluo.com/bramble/z6de23194ujxsfo1n9lgd6st/web74.png
  [73]: http://static.zybuluo.com/bramble/umzpp54t360zoasfajynnqsc/web75.png
  [74]: http://static.zybuluo.com/bramble/8w54vnqmphas1lygx3a3zvuh/web76.png
  [75]: http://static.zybuluo.com/bramble/vgliu0gun53ywnwxi5sx36w8/web77.png
  [76]: http://static.zybuluo.com/bramble/uct0tkin7qtxy2a6svikfd8b/web78.png
  [77]: http://static.zybuluo.com/bramble/ip1o466ghw2jr81d3367ipye/web79.png
  [78]: http://static.zybuluo.com/bramble/z5z0ms79hpnc9f1rkpi1pbpe/web80.png
  [79]: http://static.zybuluo.com/bramble/v3vsk1nkkuaipwq2cijqu1nd/web81.png
  [80]: http://static.zybuluo.com/bramble/j03mujuplan3jrcxopcw7hab/web82.png
  [81]: http://static.zybuluo.com/bramble/ioexkc53etziqpcnhj7xexsj/webb82.png
  [82]: http://static.zybuluo.com/bramble/snbqwdfz35y76bqe5ni902a6/web83.png
  [83]: http://static.zybuluo.com/bramble/ma1aykrgpvqpksb1zfvqu1q5/web84.png
  [84]: http://static.zybuluo.com/bramble/inl5f69nz6sq2fd0rvgq8myi/web85.png
  [85]: http://static.zybuluo.com/bramble/4pgl7bazon401uot1vhh52zh/web86.png
  [86]: http://static.zybuluo.com/bramble/w1gl3l8fvjrclmnuu4p19lhz/web87.png
  [87]: http://static.zybuluo.com/bramble/0k3hwaet98w4140l672arlxf/web88.png
  [88]: http://static.zybuluo.com/bramble/5zz23ojkb1bybs6r86d6zxwn/web89.png
  [89]: http://static.zybuluo.com/bramble/4ovk00ll94wnqxhbyi8odwxe/web90.png
  [90]: http://static.zybuluo.com/bramble/a6e91g3u93q68q8e4tpjlc6a/web91.png
  [91]: http://static.zybuluo.com/bramble/fh604iv0jsa6eyzfdvkr1sa0/web92.png
  [92]: http://static.zybuluo.com/bramble/9np6s119lhuuypvv0kslougq/web93.png
  [93]: http://static.zybuluo.com/bramble/toa8bgfw5uopacn5nmhhpql5/web94.png
  [94]: http://static.zybuluo.com/bramble/kpjt4jefd4psc63hlrrq9zke/web95.png
  [95]: http://static.zybuluo.com/bramble/8a7ydfzu2nuww0c1dgrod5tn/web96.png
  [96]: http://static.zybuluo.com/bramble/4afw3rgwi2bw7jvcfu6r4mx4/web97.png
  [97]: http://static.zybuluo.com/bramble/9q1h1h04kmq7gupwx7y4wijs/web98.png
  [98]: http://static.zybuluo.com/bramble/jm43vt0t0s0c8d3zvhkf7r2g/web99.png
  [99]: http://static.zybuluo.com/bramble/46if94xa8vuk7cn4sq383eck/web100.png
  [100]: http://static.zybuluo.com/bramble/2ophsetpwt0444atrykkamol/web101.png
  [101]: http://static.zybuluo.com/bramble/kg31hg4blr87ni4o0phiaa4m/web102.png
  [102]: http://static.zybuluo.com/bramble/ycl9e8x8romhrhkh6tavai17/web104.png
  [103]: http://static.zybuluo.com/bramble/xer7dlr819uwtc3hi1k53zcl/web105.png
  [104]: http://static.zybuluo.com/bramble/m4m69r8pvx5plpx6xen5c3ch/web106.png
  [105]: http://static.zybuluo.com/bramble/18xgilzbxd9tku0pj1eg7h3b/web107.png
  [106]: http://static.zybuluo.com/bramble/d41u8bmyimtkb626vx65fej2/web108.png
  [107]: http://static.zybuluo.com/bramble/by54ol4hqkaav8bfc4q5v05z/web125.png
  [108]: http://static.zybuluo.com/bramble/7661cyx6ji5nvkergow86skf/web128.png
  [109]: http://static.zybuluo.com/bramble/tezozv6e1gou9mxerutgtwkl/web129.png
  [110]: http://static.zybuluo.com/bramble/p4pjhqovd416diuykjmfg55k/web130.png
  [111]: http://static.zybuluo.com/bramble/qqusz7lf42dfp76kywgkdjs8/web133.png
  [112]: http://static.zybuluo.com/bramble/fa5v3zaqo4xd8kqgfq84eq2p/web132.png
  [113]: http://static.zybuluo.com/bramble/ciw8gytb51i0lq88xyg46w5w/web134.png
  [114]: http://static.zybuluo.com/bramble/tgqr9p0y1icb44cgckvbrfzx/web135.png
  [115]: http://static.zybuluo.com/bramble/g9fpj674zep11flxi8ohqgbj/web136.png
  [116]: http://static.zybuluo.com/bramble/spyxz3prv2in1zwlnhtv4qao/web137.png
  [117]: http://static.zybuluo.com/bramble/ykvukikfyh0h7j9an7wcxens/web138.png
  [118]: http://static.zybuluo.com/bramble/7tbg99jk9ijj9qjbrqkau18r/web139.png
  [119]: http://static.zybuluo.com/bramble/3ghaaytx8akhxa82jm359va2/web140.png
  [120]: http://static.zybuluo.com/bramble/0kbivjk1x17zz0pby9pwynss/web141.png
  [121]: http://static.zybuluo.com/bramble/yz7rbfdybkok49ed88pkxxlb/web142.png
  [122]: http://static.zybuluo.com/bramble/ugnmdmb60vm2b288z2jwbs0x/web143.png
  [123]: http://static.zybuluo.com/bramble/mikf7qexex8jcxz3m8mk9lsm/web144.png
  [124]: http://static.zybuluo.com/bramble/8228loj261nt1jw7mz5yvzy4/web145.png
  [125]: http://static.zybuluo.com/bramble/6ra9w2x0vpawpxq76kxf1b4m/web146.png
  [126]: http://static.zybuluo.com/bramble/vatirrrtsb8c9b8bi2wpe4oh/web148.png
  [127]: http://static.zybuluo.com/bramble/ymlt01q8eue2au2igdymjm9g/web149.png
  [128]: http://static.zybuluo.com/bramble/nwu0mwwlcn1krb13wojm4uur/web150.png
  [129]: http://static.zybuluo.com/bramble/zv8jsijrshfxqp1ydslqkcmx/web151.png
  [130]: http://static.zybuluo.com/bramble/u2r2gsedtbjss1lfxzlff86t/web152.png
  [131]: http://static.zybuluo.com/bramble/pka40zito9l8zs6csy1twboz/web152.png
  [132]: http://static.zybuluo.com/bramble/crq3aowhf3j5d0wbsknpj72o/web153.png
  [133]: http://static.zybuluo.com/bramble/nbzpy69bay4s20pkpcchmxfm/web154.png
  [134]: http://static.zybuluo.com/bramble/fiei6zmfbdipdzvszq3dk0dn/web156.png
  [135]: http://static.zybuluo.com/bramble/1qfkup0ojxk0u52xuf1mokla/web157.png
  [136]: http://static.zybuluo.com/bramble/wa82legnnb58nlh0u3e7lzyv/web158.png
  [137]: http://static.zybuluo.com/bramble/xy7t0k4rq4cdhd1juijh2tgn/web160.png
  [138]: http://static.zybuluo.com/bramble/nh2t5dye94j57d6dqn6rk9rw/web161.png
  [139]: http://static.zybuluo.com/bramble/3aqe39992dmw43r7ivdiyxo3/web162.png
  [140]: http://static.zybuluo.com/bramble/ezkmctpouzp23n1ddhwww5cr/web164.png
  [141]: http://static.zybuluo.com/bramble/ea4zrbymtqfgjqpodwtlslk9/web166.png
  [142]: http://static.zybuluo.com/bramble/0erqx2l11b55gdjdim1gs1gb/web167.png
  [143]: http://static.zybuluo.com/bramble/2pxyuala2lzzgfis1zic50g9/web168.png
  [144]: http://static.zybuluo.com/bramble/cuxp7aejkqwb3hucmvb93106/web169.png
  [145]: http://static.zybuluo.com/bramble/6x9xdhnwfwqsytz5gxpeh91a/web170.png
  [146]: http://static.zybuluo.com/bramble/b1yzo2exiiuwtumzx3oid804/web171.png
  [147]: http://static.zybuluo.com/bramble/i62wgtc6q9nu4rjjifbn8r9y/web173.png
  [148]: http://static.zybuluo.com/bramble/eu3lgumsmffexwl063gk5tsf/web174.png
  [149]: http://static.zybuluo.com/bramble/e4yxyg6yysfalt7qandiuvmd/web175.png
  [150]: http://static.zybuluo.com/bramble/jo0etpw3hi7rb2e3tg04h4y5/web176.png
  [151]: http://static.zybuluo.com/bramble/pikcfe4uyzwo39hwnwdymjhw/web177.png
  [152]: http://static.zybuluo.com/bramble/w3n2a30b09x3bqthvsadut4k/web178.png
  [153]: http://static.zybuluo.com/bramble/4joijhapytqytqovlr6vg0j0/web179.png
  [154]: http://static.zybuluo.com/bramble/5fkhwtarsodp5vqa8k86kalq/web180.png
  [155]: http://static.zybuluo.com/bramble/uz67iw97a57g3eeoa3k68t1h/web181.png
  [156]: http://static.zybuluo.com/bramble/1bjzcb77cza5i638rp4xo81v/web182.png
  [157]: http://static.zybuluo.com/bramble/wgnnxto2umnjq486ar6ptrcy/web183.png
  [158]: http://static.zybuluo.com/bramble/njpmrd07y5qcejvsk1gkxlcj/web184.png
  [159]: http://static.zybuluo.com/bramble/1vek184toyvyqja9eas8cv25/web185.png
  [160]: http://static.zybuluo.com/bramble/9bisxbl5wze8dgesaxzvd0po/web186.png
  [161]: http://static.zybuluo.com/bramble/13fte1ny0hpetf4nr18dl0nb/web187.png
  [162]: http://static.zybuluo.com/bramble/nbuxrj5s726op6ncwbycs7g5/web188.png
  [163]: http://static.zybuluo.com/bramble/4y8zew6pmc9oixuadmigh9si/web189.png
  [164]: http://static.zybuluo.com/bramble/o1d5a2wumzfe4q7n1vppcoy8/web190.png
  [165]: http://static.zybuluo.com/bramble/vu71d6kr4bq5f6nt0h4o3ac0/web191.png
  [166]: http://static.zybuluo.com/bramble/nmnxicvur3umezg6m8t793nl/web192.png
  [167]: http://static.zybuluo.com/bramble/aifzbgr3p8s8si1vnneyxk5m/web193.png
  [168]: http://static.zybuluo.com/bramble/d2cwnzcx2d4dwxmjxiiykx02/web197.png
  [169]: http://static.zybuluo.com/bramble/qawlteh31kxzrv9fody0gz0k/web195.png
  [170]: http://static.zybuluo.com/bramble/8ldhkzibrr3aeh8rb5ihzrfh/web196.png
  [171]: http://static.zybuluo.com/bramble/nrfm80rk022n0fd9nt8a6tqn/web198.png
  [172]: http://static.zybuluo.com/bramble/egbxk90hq2928gs3fuzi2yv9/web199.png
  [173]: http://static.zybuluo.com/bramble/d89vt4r9qmuc6stqrk3ibno7/web200.png
  [174]: http://static.zybuluo.com/bramble/voxmk0bkz1cc1pl7vngjnpkv/web201.png
  [175]: http://static.zybuluo.com/bramble/eh1kg5hvin15id1qbfzyd8hi/web202.png
  [176]: http://static.zybuluo.com/bramble/595wq9ltpz01b89ur244yc8l/web203.png
  [177]: http://static.zybuluo.com/bramble/avtbszqjezkuysib0huhis6a/web204.png
  [178]: http://static.zybuluo.com/bramble/dvvj5reenfx7mw9ey5b3nt2b/web205.png
  [179]: http://static.zybuluo.com/bramble/e299lb83wuswv2cxv23rjbuo/web206.png
  [180]: http://static.zybuluo.com/bramble/45q48jupdsjloan5iu5ye6k2/web207.png
  [181]: http://static.zybuluo.com/bramble/e74ynneyuzb06818p3aihecs/web208.png
  [182]: http://static.zybuluo.com/bramble/jc4bwjpjh5n9ayineeloelk9/web209.png
  [183]: http://static.zybuluo.com/bramble/en4hio62omq3suj332nq5f4x/web210.png
  [184]: http://static.zybuluo.com/bramble/gaax7atbvzyzihs45as2eze5/web212.png
  [185]: http://static.zybuluo.com/bramble/f3ppntvgv2hw89gep3hanlo5/web214.png
  [186]: http://static.zybuluo.com/bramble/97qm6j3alo8fep6yrxoyvzki/web215.png
  [187]: http://static.zybuluo.com/bramble/2q6y2y1723ydj4ccp787c7dv/web216.png
  [188]: http://static.zybuluo.com/bramble/w30nwsx7a9ue43m02lk6ywbf/web217.png
  [189]: http://static.zybuluo.com/bramble/3p45lldg81mdvtmnnrpvj2e7/web220.png
  [190]: http://static.zybuluo.com/bramble/azv3feijchx2or2tl78lgv18/web221.png
  [191]: http://static.zybuluo.com/bramble/ggtm4j1v3tq3btr8t6ms3hkn/web222.png
  [192]: http://static.zybuluo.com/bramble/li145u20ijnuig25au03dsur/web223.png
  [193]: http://static.zybuluo.com/bramble/r77xx5fo7kgfg0fnfor8govb/web224.png
  [194]: http://static.zybuluo.com/bramble/cgacb5suyaqjkp8x0vko3v0c/web225.png
  [195]: http://static.zybuluo.com/bramble/40xwjowa7y3uadk813kggytg/web226.png
  [196]: http://static.zybuluo.com/bramble/e22dby5ldhd8yvfzdne2fztt/web227.png
  [197]: http://static.zybuluo.com/bramble/b9m77x7t4jonq07rk7jrgqtz/web228.png
  [198]: http://static.zybuluo.com/bramble/f62anq1ikgzhuaggg6khrd9t/web229.png
  [199]: http://static.zybuluo.com/bramble/7q7yfs7416lxd2vjrvkz7fi1/web230.png
  [200]: http://static.zybuluo.com/bramble/mkhjq017buahue3rwcnhxoja/web231.png
  [201]: http://static.zybuluo.com/bramble/sel8pthyia6z3ra248leotu6/web232.png
  [202]: http://static.zybuluo.com/bramble/f1f4vryle2nzwagiqow884b2/web233.png
  [203]: http://static.zybuluo.com/bramble/rivbi9ok7c5hgr3yk0sv48mm/web234.png
  [204]: http://static.zybuluo.com/bramble/yirjxx6cbuyyjrcfw4mo59f5/web235.png
  [205]: http://static.zybuluo.com/bramble/e46ecl55fmy4ri7q8z6j56qo/web237.png
  [206]: http://static.zybuluo.com/bramble/7d2gyr8oifykcjrhu80wn7g4/web238.png
  [207]: http://static.zybuluo.com/bramble/yny2dkvir7ik0ktzol7o5cb0/web239.png
  [208]: http://static.zybuluo.com/bramble/ktkbnmynfqbacve7o4pgyaze/web240.png
  [209]: http://static.zybuluo.com/bramble/bc1msfa473c3sgw9ekt81ik2/web241.png
  [210]: http://static.zybuluo.com/bramble/fab05xyl7y75ctj4dt89t3tq/web242.png
  [211]: http://static.zybuluo.com/bramble/a9dl2sle17ct6xuwkbpimnsu/web243.png
  [212]: http://static.zybuluo.com/bramble/rwgk8q3vw1kirlozyqig0p5m/web244.png
  [213]: http://static.zybuluo.com/bramble/m809xu5x1p9y4tse0fnv5hvl/web245.png
  [214]: http://static.zybuluo.com/bramble/s4f5fzjbus0oti6xymfo5lpp/web246.png
  [215]: http://static.zybuluo.com/bramble/npr3rzhxdrvaca34i3jrrrgu/web247.png
  [216]: http://static.zybuluo.com/bramble/b8l74lngdx46a498q3739f3w/web248.png
  [217]: http://static.zybuluo.com/bramble/ihvimftwzg7sv9tfxgcouqyv/web249
  [218]: http://static.zybuluo.com/bramble/3emgvwowjvtlqp8mo1gl5u32/web250.png
  [219]: http://static.zybuluo.com/bramble/hc13gkhqxyjqlk57ucrk14mq/web251.png
  [220]: http://static.zybuluo.com/bramble/zjlwgbgxofojnxoix5swf628/web252.png
  [221]: http://static.zybuluo.com/bramble/88lhijv6m1qutwkieltf9rsa/web253.png
  [222]: http://static.zybuluo.com/bramble/7z023cpi4t7i6fnydgruds1c/web255.png
  [223]: http://static.zybuluo.com/bramble/hby23j4eov4jlj4ofnp8okj1/web256.png
  [224]: http://static.zybuluo.com/bramble/cizt7uqg2v1134skz3andnp1/web257.png
  [225]: http://static.zybuluo.com/bramble/p1lmg8ui9zwy6lx2zlk265aj/web258.png
  [226]: http://static.zybuluo.com/bramble/gopi9everlyjs9jdehqqny84/web259.png
  [227]: http://static.zybuluo.com/bramble/koaq79rqa3i850bf1rdwaydc/web260.png
  [228]: http://static.zybuluo.com/bramble/xi9ld0qwkk32sh449j6xnn18/web262.png
  [229]: http://static.zybuluo.com/bramble/aikbrhi6egjaha0jb86dj53g/web263.png
  [230]: http://static.zybuluo.com/bramble/fdgneo666djbwcqyvivl0mok/web264.png
  [231]: http://static.zybuluo.com/bramble/kaaw9a5c9vg7ag5yv9q7c81x/web266.png
  [232]: http://static.zybuluo.com/bramble/wj3cl6vpdgki4lqywdt0ksfx/web267.png
  [233]: http://static.zybuluo.com/bramble/ygprjv43bd83sbwepi57wv3f/web268.png
  [234]: http://static.zybuluo.com/bramble/bbu8bt5lboj93n7u1qb6xfic/web269.png
  [235]: http://static.zybuluo.com/bramble/2meth9x0oggyd1d0zk3d08kc/web270.png
  [236]: http://static.zybuluo.com/bramble/m8d121tuabrycgfzwscncl9p/web271.png
  [237]: http://static.zybuluo.com/bramble/6dm6ywh7xmv5r3al7gjjc5yh/web273.png
  [238]: http://static.zybuluo.com/bramble/8lxvbmlgyu2hcio14mod6djz/web274.png
  [239]: http://static.zybuluo.com/bramble/rrdxhwk54mhvvmcwp6t1s9ka/web275.png
  [240]: http://static.zybuluo.com/bramble/25t8r02tip8yd01f9n6stlm9/web276.png
  [241]: http://static.zybuluo.com/bramble/ohfenti6snk7061ltrjg7c0k/web277.png
  [242]: http://static.zybuluo.com/bramble/psud72k1hhlgx0l8xrgqkwyx/web278.png
  [243]: http://static.zybuluo.com/bramble/1ehjhxhzh1udrgzdig9k0lpu/web279.png
  [244]: http://static.zybuluo.com/bramble/kd12cdgs0540nrvq7h1r45fi/web280.png
  [245]: http://static.zybuluo.com/bramble/rry0zy8tz49zmqn1wged8z0o/web283.png
  [246]: http://static.zybuluo.com/bramble/q9ub0658ihamo1yev3dkgk16/web284.png
  [247]: http://static.zybuluo.com/bramble/l6bkc274o75suegm3kcml1r8/web286.png
  [248]: http://static.zybuluo.com/bramble/hw0mld9pwprnztwcaxf8120g/web287.png
  [249]: http://static.zybuluo.com/bramble/8fgbk3wo77ia7d464tog3yls/web288.png
  [250]: http://static.zybuluo.com/bramble/p8gzgs4i6b4r6kdp5y6yissd/web289.png
  [251]: http://static.zybuluo.com/bramble/ym6mvqq03t3ef7o74mhfbpqt/web290.png
  [252]: http://static.zybuluo.com/bramble/4crq1hya33w1kjnz8mfhw7rl/web291.png
  [253]: http://static.zybuluo.com/bramble/hc5osy072m8f62ddfmkhpt1k/web292.png
  [254]: http://static.zybuluo.com/bramble/9vwb05748f8yra8aigub9mxd/web293.png
  [255]: http://static.zybuluo.com/bramble/bw6w5puan4yy2toz1xr3lbza/web295.png
  [256]: http://static.zybuluo.com/bramble/v75emlujxtwkxcnqoqi448ir/web294.png
  [257]: http://static.zybuluo.com/bramble/iy7rhjigakbxrnnb288ghr4i/web29.png
  [258]: http://static.zybuluo.com/bramble/1xbv1485d4o5anap3sen7e1g/web296.png
  [259]: http://static.zybuluo.com/bramble/2nl1et6he08v81qqar7oyyry/web297.png
  [260]: http://static.zybuluo.com/bramble/4j6ikqmr7p9zpf7kdrald4n0/web298.png
  [261]: http://static.zybuluo.com/bramble/vb96ja291q1o230nxk89vjfi/web299.png
  [262]: http://static.zybuluo.com/bramble/3wvsr5kvdwwzw2u3bea8i1gs/web300.png
  [263]: http://static.zybuluo.com/bramble/38slcyr70jgoz4393kf91n1a/web301.png
  [264]: http://static.zybuluo.com/bramble/xowrduhjjykpkahd3qqb90kz/web302.png
  [265]: http://static.zybuluo.com/bramble/1mrrpmq2e6c38b0hvk2e5syj/web303.png
  [266]: http://static.zybuluo.com/bramble/mjetfewh3qhf16p448rt71tm/web304.png
  [267]: http://static.zybuluo.com/bramble/va64cizzl2y49rckxixlmln6/web306.png
  [268]: http://static.zybuluo.com/bramble/nu0mkvqkvwgvxtl0t8d4giux/web308.png
  [269]: http://static.zybuluo.com/bramble/k5lrhixm3qm7fculbbap7utu/web307.png
  [270]: http://static.zybuluo.com/bramble/7ranmyaic8v60apbgpixdzlv/web309.png
  [271]: http://static.zybuluo.com/bramble/jn4mowa66u5iol2fppvyoeck/web310.png
  [272]: http://static.zybuluo.com/bramble/jxvulxmbeoz6b68lnu13q02e/web312.png
  [273]: http://static.zybuluo.com/bramble/cdh2sb6r8ecghs6o3etgijjf/web314.png
  [274]: http://static.zybuluo.com/bramble/wydjm2vjx4jh3hg94ehngse2/web318.png
  [275]: http://static.zybuluo.com/bramble/x7ebovq1u67b2jogh6o48e1c/web319.png
  [276]: http://static.zybuluo.com/bramble/p65pm96gvfk533mnhsnaxf87/web320.png
  [277]: http://static.zybuluo.com/bramble/ersbvnroektz75aeeklry1ua/web322.png
  [278]: http://static.zybuluo.com/bramble/2x7urezknv1qp4i42yd8p3q0/web323.png
  [279]: http://static.zybuluo.com/bramble/f8uaj7xzje2k31z4fs3nj53z/web324.png
  [280]: http://static.zybuluo.com/bramble/2o08z0aolnuclfhjcws5x6i1/web325.png
  [281]: http://static.zybuluo.com/bramble/dsgxln9kosfg1zbbce015es1/web326.png
  [282]: http://static.zybuluo.com/bramble/x1m36rlfs3lxaz1sgrio6fax/web328.png
  [283]: http://static.zybuluo.com/bramble/lavuxp1tzhl8617zypzxm6o2/web329.png
  [284]: http://static.zybuluo.com/bramble/i223odp8pnpcaza378nuwxdm/web330.png
  [285]: http://static.zybuluo.com/bramble/4wzxv5wij64xmm37igkdggu0/web331.png
  [286]: http://static.zybuluo.com/bramble/74jj62tachkh8nr04675cu31/web333.png
  [287]: http://static.zybuluo.com/bramble/vbmwbmb6yhtjs18tsbjxahne/web334.png
  [288]: http://static.zybuluo.com/bramble/avtjmgfzrod3y9x1qk4fz5pj/web335.png
  [289]: http://static.zybuluo.com/bramble/u270npp0isjhctsftsbrqme6/web336.png
  [290]: http://static.zybuluo.com/bramble/oqd6z5ffgfuzp4ansxj8y7bd/web337.png
  [291]: http://static.zybuluo.com/bramble/o1w0u7nmdtazit7k1f91xi8c/web338.png
  [292]: http://static.zybuluo.com/bramble/zby1jkia0q2jm0m262ibzm0f/web339.png
  [293]: http://static.zybuluo.com/bramble/ihttiymtw6rz8wfmqqk7qq2x/web340.png
  [294]: http://static.zybuluo.com/bramble/ocw37bo4729x4nrlou41i2gr/web342.png
  [295]: http://static.zybuluo.com/bramble/tf8i5nki4fk5zf3aix3b5wp2/web343.png
  [296]: http://static.zybuluo.com/bramble/ouejcu3358s6abakmuf76bgt/web344.png
  [297]: http://static.zybuluo.com/bramble/qtfc42k0hcvf2x8h1uylgeov/web344.png
  [298]: http://static.zybuluo.com/bramble/imyah7xkwnsc62o2dlbgo61e/web345.png
  [299]: http://static.zybuluo.com/bramble/lsx9bjlgsp0w0zw3ha8nbo8l/web346.png
  [300]: http://static.zybuluo.com/bramble/5dnxm1robkw4kxr1o8zvgg6x/web347.png
  [301]: http://static.zybuluo.com/bramble/xuet6pw3us1v657gcjv3dgq9/web349.png
  [302]: http://static.zybuluo.com/bramble/elc3zqpi87u902dco10hety4/web350.png
  [303]: http://static.zybuluo.com/bramble/o6hucvlvf105nrjb21w1732k/web351.png
  [304]: http://static.zybuluo.com/bramble/e6hss2oi2jxoqariej37y8g6/web354.png
  [305]: http://static.zybuluo.com/bramble/06i2fqa4j1iqvswtd27ububw/web356.png
  [306]: http://static.zybuluo.com/bramble/kc1ounchxttsfa4vdlvsj2gk/web358.png
  [307]: http://static.zybuluo.com/bramble/jf81g9d0q8wcgq3hyb3twrw1/web359.png
  [308]: http://static.zybuluo.com/bramble/ubly8ofjgv7awby7rki7sze8/web360.png
  [309]: http://static.zybuluo.com/bramble/um2elmlg21ergza41hm5uhss/web362.png
  [310]: http://static.zybuluo.com/bramble/cr6f12ec6z51fkj563btr4ew/web363.png
  [311]: http://static.zybuluo.com/bramble/ka2kalweh7mza9ug6f3ipks2/web365.png
  [312]: http://static.zybuluo.com/bramble/3po3gbzg89rn7y1zjp8exe01/web367.png
  [313]: http://static.zybuluo.com/bramble/8qpj1jgrkx8dkav2r2gsuvl6/web369.png
  [314]: http://static.zybuluo.com/bramble/torr9hxckwcxc5d7fgyw0y9l/web370.png
  [315]: http://static.zybuluo.com/bramble/xd12d2olkcu5pjhe71p313y0/web371.png
  [316]: http://static.zybuluo.com/bramble/220kh9e4h39kexmd2ylrhxkz/web375.png
  [317]: http://static.zybuluo.com/bramble/52txa6mixjtgdut2qgsnrj1n/web377.png
  [318]: http://static.zybuluo.com/bramble/vrrhwj7m82tx02c1ls37jhhl/web378.png
  [319]: http://static.zybuluo.com/bramble/p5au1lx02ftul8m8nzg3v7zv/web379.png
  [320]: http://static.zybuluo.com/bramble/g084hxbqdt7qaaie8aglyw0o/web380.png
  [321]: http://static.zybuluo.com/bramble/1786kd5klkwwjvtz7ypav825/web381.png
  [322]: http://static.zybuluo.com/bramble/1e2qmgtcc8skd33mc11l3ouo/web382.png
  [323]: http://static.zybuluo.com/bramble/kcl0elax29xuuwfm80wc6lzj/web383.png
  [324]: http://static.zybuluo.com/bramble/y8muz3bi6d3cgkheqoet2de6/web385.png
  [325]: http://static.zybuluo.com/bramble/yep6digga639u20n97ts3p9l/web386.png
  [326]: http://static.zybuluo.com/bramble/andresgett0ho6lruk3yiy08/web387.png
  [327]: http://static.zybuluo.com/bramble/zk7q3m9e03oku6ois2ht9qea/web388.png
  [328]: http://static.zybuluo.com/bramble/ziagpuvle9x43ftm3djmyr33/web389.png
  [329]: http://static.zybuluo.com/bramble/6bnkhtoytm4pf23tslovtu4j/web390.png
  [330]: http://static.zybuluo.com/bramble/bxpspq4tsvo6q1e7levbyly2/web392.png
  [331]: http://static.zybuluo.com/bramble/pl4rq0yjz4z4e1az9t89zerz/web391.png
  [332]: http://static.zybuluo.com/bramble/0yyl6r64llcukun3fk6qj8he/web393.png
  [333]: http://static.zybuluo.com/bramble/9f0yqj5dnm3yz5zhr3nkev8h/web394.png
  [334]: http://static.zybuluo.com/bramble/uyxqm8u7w6gcnzg73395pgxa/web396.png
  [335]: http://static.zybuluo.com/bramble/zrf7opflw53vj0ucw6ef3luv/web395.png
  [336]: http://static.zybuluo.com/bramble/6r442wga96b6huiyszp3r76y/web398.png
  [337]: http://static.zybuluo.com/bramble/v9jup75fkjbmvld0vema0fxn/web397.png
  [338]: http://static.zybuluo.com/bramble/htsh4pxl6mkck2w4bsgx98xo/web399.png
  [339]: http://static.zybuluo.com/bramble/4wu75s6snday0ji49x1izhs5/web400.png
  [340]: http://static.zybuluo.com/bramble/b5bqv67o9kl724g5ifsnfepz/web401.png
  [341]: http://static.zybuluo.com/bramble/6n0fii2pejchcj2buool8kvp/web402.png
  [342]: http://static.zybuluo.com/bramble/jo0bmb3h7h0a9pyswl8hvijp/web403.png
  [343]: http://static.zybuluo.com/bramble/m7zwae56tkxxvefb4jn06e92/web404.png
  [344]: http://static.zybuluo.com/bramble/sq705ih06psi2dk7642y48u9/web406.png
  [345]: http://static.zybuluo.com/bramble/z1k0d045yrdjvf8gn7hppvmc/web408.png
  [346]: http://static.zybuluo.com/bramble/yd4zubnzofnhn8drh8sntp7q/web407.png
  [347]: http://static.zybuluo.com/bramble/ocrrq86x6ui83uxtdqmeoike/web410.png
  [348]: http://static.zybuluo.com/bramble/yj8riznpdygh6w6pm4pakddm/web412.png
  [349]: http://static.zybuluo.com/bramble/dshru7m3dwzk9wpb8taqmgui/web413.png
  [350]: http://static.zybuluo.com/bramble/8vd84nuh1ns446vv9j9lc8k7/web414.png
  [351]: http://static.zybuluo.com/bramble/m5qbj9hspptg2smkwpejj1r1/web417.png
  [352]: http://static.zybuluo.com/bramble/38c9arpn8ny8qc9dh8dblb72/web418.png
  [353]: http://static.zybuluo.com/bramble/m2fan4pxwgqawcqa744xr1rq/web419.png
  [354]: http://static.zybuluo.com/bramble/lc58dzdlw1a8bh74ei3kp220/web420.png
  [355]: http://static.zybuluo.com/bramble/zuopwtm2nvxypv2iwniuug35/web421.png
  [356]: http://static.zybuluo.com/bramble/xzu1anjwa79ba0tf4sf9dz3q/web422.png
  [357]: http://static.zybuluo.com/bramble/d51nxkioyu53ldkipma7xmhz/web423.png
  [358]: http://static.zybuluo.com/bramble/e6fnvl6d4j1iswuen4ymi0uk/web424.png
  [359]: http://static.zybuluo.com/bramble/ozjlekahz53z92mrk7zd70ok/web425.png