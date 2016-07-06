# Linux Command Line Basics (closed)

标签（空格分隔）： Udacity

---

Lesson 1: Get Into the Shell
Lesson 2: Shell Commands
Lesson 3:The Linux Filesystem

[TOC]

#Lesson 1: Get Into the Shell

## 1.1 Log In and Break Stuff
log in:
cd **Udacity/Shell/**文件夹下：（有一个Vagrantfile的文件，有这个文件才能用vagrant up配置所需要的环境
```
vagrant up

vagrant ssh
```
ok, it's done. 现在可以试一试，在command line里随便输入一些东西。

你会发现大部分的命令都是无效的，但是出现`'`单引号的时候，shell会提示你继续输入，因为在没有见到第二个`'`之前，它认为现在输入的命令还没有写完。

除此之外用`exit`可以log out.

![lc1.png-138.9kB][1]

如果你输入`python`或其它什么奇怪的命令，进入了某个程序，可以用`quit`或Ctrl+C退出该程序，回到shell。

## 1.2 Commands That Work

![lm2.png-456kB][2]

![lm3.png-461.4kB][3]

运行后的结果，在**Udacity/Shell/**文件夹下多了一个things.zip的文件

##1.3 What can you do in the terminal?

![lm4.png-316.1kB][4]

##1.4 The Terminal Interface

![lm5.png-397.8kB][5]

##1.5 The Terminal vs The Shell

Terminal 只是一个终端而已，他负责接受input，但不会处理，所以把这些input传给shell来运行，shell把得到的结果返回给terminal，terminal再展示给我们。所以说terminal就是个窗口而已。

Different shells

Unix and Linux programmers over the years have written many different shell programs. You can read more about them on Wikipedia: the original Bourne shell or sh; the C shell or csh; the Korn shell or ksh; the Z shell or zsh; as well as the bash shell that this course uses.

Different systems may have different shells installed by default. Most Linux systems, and Mac OS X, default to bash for interactive shells. However, the most common default shell for scripting (shell programming) is classic sh. BSD Unix systems usually default to sh or ksh.

Almost everything in this course will work the same in any of these shell programs. The exception is one of the file matching (globbing) syntaxes at the end of Lesson 3.

## 1.6 Try More Commands

![lm6.png-363.4kB][6]

`host udacity.com` 给出了Udacity的IP地址，并告诉我们它的mail是Gmail负责的。

![lm7.png-525.1kB][7]

![lm8.png-621.3kB][8]

![lm9.png-199.4kB][9]

##1.7 Reading the Output of a Command

![lm10.png-442.4kB][10]

##1.8 Identify User Input

![lm11.png-406.1kB][11]

# Lesson 2: Shell Commands

## 2.1 Filenames and Contents

![lm12.png-366.7kB][12]

## 2.2 Command History
有三种方法来找到之前输入过的命令。
1. 用**↑**这个方向键, up arrow key.
2. use the commend `history`
3. Ctrl + R, 能用来搜索之前输入的命令，适合久远的命令。

## 2.3 Some Common Commands

用`unzip things.zip`来解压之前`curl`来的文件`things.zip`.

用`cat file_name.txt`，会return文档里的内容。

用**Tab**来自动补全。

用来分析文件的命令：
1. `wc bivalves.txt`, wc is a word count program. return the lines, words, bytes.
2. `diff gastropods.txt gastropods_draft.txt`, 返回两个文档不同的地方。这个在git教程里也讲到了。

![lm13.png-870.9kB][13]

## 2.4 Manual Pages

用`man` command 来查询文档

![lm14.png-211.2kB][14]

在synopsis里，像`[-e eye_string]`这样的表示有可选项的命令。必须在`-e`后添加一个`eye_string`来改变cowsay的眼睛形状。

![lm15.png-603kB][15]

##2.5 Using the Manual for Serious Purpose

比如在`unzip things.zip`的时候，发现`extracting .secret`的字样，但是用`ls`看不到。所以用`man ls`来查看用什么命令能看到隐藏文件。

答案是`ls -a`或`ls --all`.

## 2.6 Options to ls

![lm16.png-362.7kB][16]

从右到左，filename, modification time, file size(byte), 
![lm17.png-552.3kB][17]

## 2.7 Researching Commands

运行不确定的command前先google，别手贱……

比如`rm -rf/`：
`-r` is for recursive, and `-f` is for force.

Just to be clear: This command is not good for your system. Don't run it. Keep watching ...

## 2.8  Line Based Programs

一些交互式的命令，一旦运行后就会占据terminal，一直运行。比如`ping`,检测某个域名是否alive. 这个命令会一直返回echo。除非你用Ctrl+C终止进程。

![lm18.png-390.1kB][18]

但另外一些programs有不同的behavior。

![lm19.png-163.8kB][19]

比如输入`sort`,回车。这个命令会进入下一行，每输完一个单词回车后就会另起一行，无法停止。此时必须用**Ctrl+D**来告诉shell”输入完毕“，然后就会得到按字母排好序的单词。

![lm20.png-20.6kB][20]

## 2.9 Waiting for Input

输入`bc`可以进入一个basic calculator, 你可以输入数字，回车，但是怎样才能退出呢？
1. 输入`quit`
2. Ctrl + D

![lm21.png-315.6kB][21]

![lm22.png-229.3kB][22]

## 2.10 Full Screen Interactive Programs: less

其实在用`man` command的时候，就是用的less的语法。比如用Q退出，就是less的功能。
```
less thewind.txt
```
这个less就像是vim里的命令模式，只能看和编辑，不能输入。

[Cheatsheet of less's Keyboard](http://sheet.shiar.nl/less)

[Introduction to Regular Expressions](http://codular.com/regex)

## 2.11 Editing Files in nano

![lm23.png-504.8kB][23]

# Lesson 3:The Linux Filesystem

## 3.1 The Filesystem Tree

![lm24.png-213.4kB][24]

![lm25.png-316.3kB][25]

文件路径。Linux中用`/`（slash）来表示路径，和`https://`一样，和`1/2 = 0.5` 只有windows用backslash.

![lm26.png-222.2kB][26]

## 3.2 The Working Directory

用`pwd`显示 Present Working Directory。
用`cd`来改变Directory：
1. `cd /var/log` 给出整个path
2. `cd three`  进入当前Directory中的某个名为three的Directory
3. `cd ..` 返回上一级

![lm27.png-386.6kB][27]

可以下载一个叫**tree**的program，能显示文件目录的树状结构。

## 3.3 Absolute and Relative Paths

![lm28.png-1024.8kB][28]

`../mountain`:表示cwd(当前目录)的parent directory下的另一个directory mountain. 也就是说这个mountain和当前目录是同一层级的。
`.`:一个dot表示cwd。
`cd ~`: 回到home directory. 其中`～`代表home,我的home directory就是xu.

![lm29.png-457kB][29]

![lm30.png-34.5kB][30]

![lm31.png-72.4kB][31]


`cd without arguments is a shortcut to take you home.

As long as your home directory exists, you can always go home.

![lm32.png-431.8kB][32]

## 3.4 Tab Completion

在输入目录path的时候用**Tab**补全。

## 3.5 Moving and Copying Files

![lm33.png-194.6kB][33]

## 3.6 Making and Removing Directories

`mkdir notes`：在当前directory创建一个新的叫notes的directory
`mkdir /tmp/cache` : 给出absolute path, 创建叫cache的directory,和cwd无关。

![lm34.png-176.2kB][34]

`rmdir notes` ：只能移除空文件夹

`rm -rf junk` : 递归并强制删除

You might remember looking up `rm -rf` before. Well, it can be used for good as well as evil. Here, you don't need the -f option; just `rm -r` junk will do what you need.

## 3.7 mv and directories

![lm35.png-293kB][35]

![lm36.png-374.8kB][36]

## 3.8 Globbing （通配符）

![lm37.png-558.8kB][37]

`*`:代表多个character
`{css,html}` : css或html
`？` ：代表一个character
`[aeiou]` : 只要这五个字符中的一个出现即可
要注意，这些是大小写敏感的

![lm38.png-264.9kB][38]

![lm39.png-290.1kB][39]

## 3.9 Applying Globbing

![lm40.png-394.8kB][40]

![lm41.png-29.3kB][41]


  [1]: http://static.zybuluo.com/bramble/p425v19knlunyuphbr44r6s0/lc1.png
  [2]: http://static.zybuluo.com/bramble/8uh2gcj1pa6ulhzl3fc3gybe/lm2.png
  [3]: http://static.zybuluo.com/bramble/hxgoyyudzm244ogjiozoezfv/lm3.png
  [4]: http://static.zybuluo.com/bramble/kktpmzwd0pjwppho9jf1m1h6/lm4.png
  [5]: http://static.zybuluo.com/bramble/ao6x0xd999sbmk8p860eggg9/lm5.png
  [6]: http://static.zybuluo.com/bramble/2zd93irfc9phjjqrsyph3grx/lm6.png
  [7]: http://static.zybuluo.com/bramble/lu9gqylezb9x8lgipmgc58b3/lm7.png
  [8]: http://static.zybuluo.com/bramble/08eyfy7ql5s0rp4qlu65g02j/lm8.png
  [9]: http://static.zybuluo.com/bramble/qo2f66mx9hbixm9uo6mt5ptg/lm9.png
  [10]: http://static.zybuluo.com/bramble/b716hcqiuolkhtkitol8131p/lm10.png
  [11]: http://static.zybuluo.com/bramble/1grz77umh2risevl25dk96y0/lm11.png
  [12]: http://static.zybuluo.com/bramble/4ubz62bw3y9pm0h7n9oykl6v/lm12.png
  [13]: http://static.zybuluo.com/bramble/pv80m3gr77dd9kxgs2tat2vx/lm13.png
  [14]: http://static.zybuluo.com/bramble/swrud8apwwvutvsv5yt1s0hk/lm14.png
  [15]: http://static.zybuluo.com/bramble/inoupluettl9yic24ezusl0u/lm15.png
  [16]: http://static.zybuluo.com/bramble/6mnl9kjaq65t5zb2lp7ly7so/lm16.png
  [17]: http://static.zybuluo.com/bramble/zes22ylrdg7sy15s519vsd1h/lm17.png
  [18]: http://static.zybuluo.com/bramble/ecq61h1hqxvhpc3puc6jgst9/lm18.png
  [19]: http://static.zybuluo.com/bramble/jce944zqq9jinh3ludkkku3j/lm19.png
  [20]: http://static.zybuluo.com/bramble/9o9rfl8nwttg81qqzbiy1934/lm20.png
  [21]: http://static.zybuluo.com/bramble/auou36dbk36alx1li2542j0n/lm21.png
  [22]: http://static.zybuluo.com/bramble/xs4txowfoe49mqao6vwafh5k/lm22.png
  [23]: http://static.zybuluo.com/bramble/zfvhoyp84grndmiqcyvkmzqe/lm23.png
  [24]: http://static.zybuluo.com/bramble/dvjm21jhwo8bvmkgy4rhb9or/lm24.png
  [25]: http://static.zybuluo.com/bramble/ajcms4hxc5d1tekd20uhq5q7/lm25.png
  [26]: http://static.zybuluo.com/bramble/2uojwwz1ddcsbvy67wzvecdh/lm26.png
  [27]: http://static.zybuluo.com/bramble/y6legl6wrbig06d401biz1uh/lm27.png
  [28]: http://static.zybuluo.com/bramble/wxjt155wrsmw7yyp8gq5pg4u/lm28.png
  [29]: http://static.zybuluo.com/bramble/kmj9svl5ur8vghc3f4hjgy5g/lm29.png
  [30]: http://static.zybuluo.com/bramble/q737muklnl052gwvjv2hk2e2/lm30.png
  [31]: http://static.zybuluo.com/bramble/vt8nojj92vt4ydyrsz1f6ji2/lm31.png
  [32]: http://static.zybuluo.com/bramble/x4evuwu8i1yoaktbpk66pyly/lm32.png
  [33]: http://static.zybuluo.com/bramble/j04n0rl8f43fd07aycf0lfi5/lm33.png
  [34]: http://static.zybuluo.com/bramble/mkuk8hhfb61sctmr5h2owwgs/lm34.png
  [35]: http://static.zybuluo.com/bramble/p7cf0eq1okvcsa4v74x75spx/lm35.png
  [36]: http://static.zybuluo.com/bramble/0dvpo51v2jfpf9dcl0mchlcw/lm36.png
  [37]: http://static.zybuluo.com/bramble/p5htcnvc2tgw098xy0iqa6p9/lm37.png
  [38]: http://static.zybuluo.com/bramble/o0txcy6ss9wdard59tdjannj/lm38.png
  [39]: http://static.zybuluo.com/bramble/th6s4qdgq1pmvteod5o1nd4h/lm39.png
  [40]: http://static.zybuluo.com/bramble/ji58fvdu4ycf4shz64bo0xxy/lm40.png
  [41]: http://static.zybuluo.com/bramble/zpoxtglytonewsdme77uhepy/lm41.png