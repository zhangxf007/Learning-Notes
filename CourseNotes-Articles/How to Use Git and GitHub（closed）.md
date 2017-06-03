# How to Use Git and GitHub（closed）

标签（空格分隔）： Udacity

---

Course Syllabus
Lesson 1: Navigating a Commit History
Lesson 2: Creating and Modifying a Repository
Lesson 3: Using GitHub to Collaborate

[TOC]

# Lesson 1: Navigating a Commit History
## 1.1 Finding Diffs Between Larger Files
![git1.png-268.6kB][67]

in windows
![git2.png-389.8kB][68]

in Linux and Mac
![git3.png-492.9kB][69]

## 1.2 Reflections
![git4.png-454.1kB][70]

##1.3 Properties of a VCS for Code
VCS：Version Control System
![git5.png-509.8kB][71]

##1.4 Manual Commits in Git
这个**Commit**的概念在git中很重要
![git6.png-229.2kB][72]

##1.5 Creating a Concept Map
![git7.png-306.2kB][73]

##1.6 Using Git to View History
使用`git log`来查看history。每一个commit都有一个ID, Author, a data and a message assicioated with it.
![git8.png-664.4kB][74]

用两个commit的ID来代替文件名，通过`git diff commit_1_ID commit_2_ID`来查看两个commit之间的差别。这个效果和之前在shell里看到的效果是一样的，而且git中还有高亮。
![git9.png-436.1kB][75]

## 1.7 Concept Map: diff
![git10.png-362.5kB][76]

##1.8  One Commit per Change Instructions
### 1.8.1 How Often to Commit
A good rule of thumb is to make one commit per *logical* change. For example, if you fixed a typo, then fixed a bug in a separate part of the file, you should use one commit for each change since they are logically separate. If you do this, each commit will have one purpose that can be easily understood. Git allows you to write a short message explaining what was changed in each commit, and that message will be more useful if each commit has a single logical change.

### 1.8.2 Commit Size Quiz
![git11.png-131.4kB][77]

### 1.8.3 One Commit per Logical Change Solution

**You commit all the changes required to add a new feature, which you’ve been working on for a week. You haven’t committed since you started working on it.**

This commit seems too big. It's easier to understand what each commit does if each only does one thing and is fairly small. Going a week without committing is not the best idea.

**You found three typos in your README. You fix and commit the first.**

This commit seems too small. It would be better to fix all three typos, then commit. That way, your history won't get too cluttered with typo fixes. Plus, you don’t need to worry about introducing bugs to a README, so bundling changes together is more likely to be a good idea.

**You commit all the changes required to add a new feature, which you’ve been working on for an hour.**

This is probably a good size for a commit. All the work is on a single feature, so the commit will have a clear logical purpose. After an hour, the diff will probably have a fair amount of content in it, but not too much to understand.

On the other hand, sometimes after working for an hour you’ll have run into more than one natural committing point, in which case you would want to break the feature up into smaller commits. Because of this, “too big” could also be a reasonable answer here.

**You fix two small bugs in different functions and commit them both at once.**

This commit is probably too big. It would have been better to commit after the first bug fix, since the two bug fixes aren't related to each other.

---
**Judgment Call**

Choosing when to commit is a judgment call, and it's not always cut-and-dried. When choosing whether to commit, just keep in mind that each commit should have one clear, logical purpose, and you should never do too much work without committing.

## 1.9 Tracking Across Multiple Files

![git12.png-340.3kB][78]

### 1.9.1 Git Commits Across Multiple Files

![git13.png-229.9kB][79]

if you have a project to work on, you'll often have multiple files that you want to tract together. Git calls such collection of files a **repository**.

when you save a version in git, in other words, when you make a commit, you will save a version of every file in your repository.

![git14.png-456.2kB][80]

在shell中实际操作一下.下面的命令可以检查which files have changed in each commit.
```
git log --stat
```
![git15.png-480.5kB][81]

`game.js | 5 +++--`表示有5处change，3处addition,2处deletion。
图中高亮的部分就是一个commit有三个文件同时changed.
通过`git diff ID1 ID2`能看到两个commit之间三个文件的变化情况。
![git16.png-587.3kB][82]

## 1.10 Cloning and Exploring The Repo 

![git17.png-396kB][83]

用`git clone`得到本地的repo后，就不用再联网了

![git18.png-290kB][84]

- Cloning a Repository
To clone a repository, run `git clone` followed by a space and the repository URL.
- Exiting `git log`
To stop viewing `git log` output, press `q` (which stands for quit).
- Getting Colored Output
To get colored diff output, run `git config --global color.ui auto`
- Using git log and git diff
As a reminder, running `git log` will show a list of the recent commits with information about them, including commit IDs. Running `git diff` followed by two commit IDs will compare the two versions of the code in those commits. 
- Entering commit IDs
If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.

## 1.11 Concept Map: repository, clone, log

![git19.png-352.2kB][85]

![git20.png-358.7kB][86]

##1.12 Git Errors and Warnings 

**Git Errors and Warnings Solution**

**Should not be doing an octopus**
Octopus is a strategy Git uses to combine many different versions of code together. This message can appear if you try to use this strategy in an inappropriate situation.

**You are in 'detached HEAD' state**
HEAD is what Git calls the commit you are currently on. You can “detach” the HEAD by switching to a previous commit, which we’ll see in the next video. Despite what it sounds like, it’s actually not a bad thing to detach the HEAD. Git just warns you so that you’ll realize you’re doing it.

**Panic! (the 'impossible' happened)** 
This is a real error message, but it’s not output by Git. Instead it’s output by GHC, the compiler for a programming language called Haskell. It’s reserved for particularly surprising errors!

## 1.13 Checking Out Old Versions of Code

**Most Recent Commit**

The commit ID of the most recent commit is `3884eab839af1e82c44267484cf2945a766081f3`. You can use this commit ID to return to the latest commit after checking out an older commit.

**Format of `git checkout`**

The command Caroline types to checkout the "Revert controls" commit is git checkout `b0678b161fcf74467ed3a63110557e3d6229cfa6`.

**Entering commit IDs**

If it is easier, you may enter the first four or more characters of the commit ID rather than pasting the entire ID.

git checkout讲解：
we can also temporarily change our files back to how they were at the time of any commit. This is called a git checkout, and it's sort of like restoring a previous version. In git, checking out a commit means resetting all of your files to how they were at the time that commit was made.

为什么用git checkout:
One reason might be, if a bug was introduced, but you're not sure which commit introduced it. You can test wether a commit has the bug by checking out that commit and running the code.

示意图
![git21.png-338kB][87]

打开**/home/xu/Udacity/version-control/asteroids/index.html**，在网页里可以进行游戏，但是发现飞船的子弹是无限连续射出的，一定是有了bug。所以我们通过`git checkout`回到写有`Revert controls`的那个commit ID。

![git22.png-102.4kB][88]

回到那个ID后，发现有`detached HEAD state`的信息。

I get this strange warning we mentioned before. You are in detached head state. Like we mentioned, head is what git calls the commit that you're currently working on, and you've detached it here by checking out an older commit.

![git23.png-683.5kB][89]

再次打开`index.html`,发现子弹是一个一个发射，虽然正常了，但是飞船颜色也没用了。用`git log`查看，发现之前的所有ID都没有了，想回到之前的commit只要直到ID就可以了，问题是那个ID，已经没了。现在我们直接用提前记好的ID，之后的可能有办法解决这个问题。

我们要找到子弹的bug,how?
I want to check out each of these commits one at a time until I find the one with the bug. 然后发现是25ede这个ID下有了bug.If we want to know exactly how the bug got introduced, we can use git diff to compare this commits and the previous one.

## 1.14 Git Workspace

这一节就是设置git的一些高亮，比如修改文件后，会有`*`号提示等等一些便于使用git的设置。不过用zsh+oh my zsh，使用git 插件后（选好主题），这些配置都自动设置好了，所以没必要自己再去改配置。


# Problem Set 1

## 1 Old File Plus Diff Quiz

左侧是原始文件，中间是原始文件和另一个文件的比较结果，根据结果，重建出另一个文件。

![git24.png-35.2kB][90]

## 2 Tracking Versions Using Git Quiz

![git25.png-82.4kB][91]

**Using `git diff` to compare the two versions would show the same changes as `diff -u` did in the previous exercise.**

This is true.` diff -u` and `git diff` show very similar outputs. Even if the exact format was slightly different, the actual changes indicated would be the same. 

## 3 Git Command Review Quiz

**Compare two commits, printing each line that is present in one commit but not the other.**

`git diff` will do this. It takes two arguments - the two commit ids to compare. 


**Make a copy of an entire Git repository, including the history, onto your own computer.**

`git clone` will do this. It takes one argument - the url of the repository to copy. 


**Temporarily reset all files in a directory to their state at the time of a specific commit.**

`git checkout` will do this. It takes one argument - the commit ID to restore. 


**Show the commits made in this repository, starting with the most recent.**

`git log` will do this. It doesn't take any arguments.

## 4 Behavior of git clone Quiz

![git26.png-78.3kB][92]

**If someone else gives you the location of their directory or repository, you can copy or clone it to your own computer.**

This is true for both copying a directory and cloning a repository.

As you saw in the previous lesson, if you have a URL to a repository, you can copy it to your computer using `git clone`.

For copying a directory, you weren't expected to know this, but it is possible to copy a directory from one computer to another using the command `scp`, which stands for "secure copy". The name was chosen because the `scp` command lets you securely copy a directory from one computer to another. 


**The history of changes to the directory or repository is copied.**

This is true for cloning a repository, but not for copying a directory. The main reason to use `git clone` rather than copying the directory is because `git clone` will also copy the commit history of the repository. However, copying can be done on any directory, whereas `git clone` only works on a Git repository. 


**If you make changes to the copied directory or cloned repository, the original will not change.**

This is true for both copying a directory and cloning a repository. In both cases, you're making a copy that you can alter without changing the original. 


**The state of every file in the directory or repository is copied.**

This is true for both copying a directory and cloning a repository. In both cases, all the files are copied.

## 4 Behavior of git log Quiz

![git27.png-106.9kB][93]

`git log` lists the most recent commit first, as you can verify by checking the commit dates. The middle commit probably contains the code for the mute button, since the commit message indicates that the mute button was added in that commit. The top commit also probably contain the mute button, since that commit is more recent and nothing suggests the mute button has been removed. The bottom commit probably does not contain the mute button, since that commit was created before the commit that added the mute button.

## 5 Behavior of git diff Quiz

`git diff`是有顺序的.`git diff A B`，其实A是old file, B是new file, 这样才会显示B比A多了什么，少了什么。 顺序很重要。

![git27.png-106.9kB][94]

The middle commit, `06d72e`, is the first commit with the mute button, so comparing that commit and the previous commit, `3d4d45`, would show the changes that add the mute button.

In order for the changes adding the mute button to be shown as additions, the commit with the mute button needs to be the second argument to `git diff`. That is because `git diff` considers the first argument as the "original", and the second argument as the "new" version, so additions are lines present in the second argument but not the first.

Thus, the last command listed, `git diff 3d4d45 06d72e`, is correct, and would show the mute button lines as additions. Reversing the arguments and running `git diff 06d72e 3d4d45` would instead show the mute button lines as deletions.

##6 Behavior of git checkout Quiz

![git29.png-73.8kB][95]

**Checking out an earlier commit will change the state of at least one file.**

This is sometimes true. Git doesn't allow you to save a new commit if no files have been updated, so you might think this is always true. However, it's possible to do the following:

- Save a commit (call this commit 1).
- Update some files and save another commit (call this commit 2).
- Change all the files back to their state during commit 1, then save again (call this commit 3).

就是说当commit 2引入了bug后，我们checkout到commit 1，在修正bug后提交，这个时候创建的是commit 3。
This sometimes happens if commit 2 contained a bug, and it's important to fix the bug quickly. The easiest thing to do might be to remove all the changes introduced by commit 2 to fix the bug, then figure out how to safely reintroduce the changes later.

At this point, commit 3 is the latest commit, so if you checkout commit 1, none of the files will be changed. 


**Checking out an earlier commit will change the state of more than one file.**

Checking out an earlier commit will change the state of every file in the repository.

Both of these are sometimes true. Since each commit tracks the state of all files in the repository, it is possible that checking out an earlier commit will change the state of multiple files, or even all the files in the repository. However, it is possible to save a new commit after changing only one file, so it is possible only one file will change. 


**After checking out a commit, the state of all the files in the repository will be from the same point in time.**

This is always true. A commit saves a snapshot of all files in the repository at the time the commit was made, so checking out an earlier commit will result in all the files being reverted to their state at the time the commit was made. That is, the files will be in a consistent state.

##7 Cloning a New Repository
clone一个新的游戏 Repository，叫**Pappu Pakia**.用这个来做练习，找bug之类的。

### 7.1 Identifying a Bug

- Buggy behavior

If you started playing Pappu Pakia, you should have noticed some pretty strange behavior! The game seems empty of any obstacles, so it's pretty boring. Also, the bird (called a "pappu"), seems to flicker in various locations across the screen.

- Solution

The commit that introduced this bug has the ID 547f4171a82ec6429d002c1acef357aec41d3f17. One way to find this out would have been to run git log, which should have shown that the most recent 4 commits, and their commit ids, were:
```
commit fa4c6bade4970c282b3870ad16f1bde8164663a9
changing flattr link

commit 708bcce690e5faa5739bd471507c102ea16b77f7
pressing down arrow wont cause scroll down anymore

commit 547f4171a82ec6429d002c1acef357aec41d3f17
refactoring collision detection

commit 71d52709ddc4066e7a79a1d0a412e43429a0cdeb
removing old readme
(This output has been shortened to be easier to read.)
```
Then you could use git checkout to examine old commits and see which ones have the bug. You already know the most recent commit, "changing flattr link" has the bug, so you could run git checkout `708bcce690e5faa5739bd471507c102ea16b77f7` to test the second-most-recent commit . You should find that this commit also has the bug. Next, you'll find the commit "refactoring collision detection" also has the bug, but the commit "removing old readme" does not. That means the commit "refactoring collision detection" with commit ID `547f4171a82ec6429d002c1acef357aec41d3f17`, is the one that introduced the bug.

### 7.2 Fixing the Bug

To find the lines introduced by the buggy commit, you can use `git diff`. You'll need the ID of the buggy commit, which you just found to be `547f4171a82ec6429d002c1acef357aec41d3f17`. Then you'll need the ID of the previous commit, which will be the commit **below** it in `git log`. (That's because git log lists the most recent commit first.) That turns out to be `71d52709ddc4066e7a79a1d0a412e43429a0cdeb`.

Thus, by running `git diff 71d52709ddc4066e7a79a1d0a412e43429a0cdeb 547f4171a82ec6429d002c1acef357aec41d3f17`, you can find out that the lines changed by the buggy commit were:
```
-    return !(
-      bounds1.end_x < bounds2.start_x ||
-      bounds2.end_x < bounds1.start_x ||
-      bounds1.end_y < bounds2.start_y ||
-      bounds2.end_y < bounds1.start_y
-    );
-
+    if (bounds1.end_x < bounds2.start_x) {
+        return true;
+    }
+    if (bounds2.end_x < bounds1.start_x) {
+        return true;
+    }
+    if (bounds1.end_y < bounds2.start_y) {
+        return true;
+    }
+    if (bounds2.end_y < bounds1.start_y) {
+        return true;
+    }
+    return false;
```
This change represents an "or" expression being separated out into several "if" statements. The number of functions did not change, and no variables were renamed.

- File changed

Near the top of the `git diff` output, you can see the lines
```
--- a/js/utils.js
+++ b/js/utils.js
```
This indicates that the file changed was `js/utils.js`, that is, the file `utils.js` within the `js` directory.

What caused the bug

Based on the change that was made, a reasonable guess is that the bug is some sort of logic error - maybe the new version does not return true and false at the correct times.

It turns out that this is correct. The new code has `true` and `false` reversed! Even if you weren't sure exactly why the bug was there, congratulations! You tracked down exactly where the bug was introduced, and knew which lines introduced it, without knowing the code base. All you had to know was how to use Git.

### 7.3 Identifying a Second Bug

** There is a second bug**

Now you should have a version of the code that works much better - your pappu is not flickering across the screen, and there are plenty of obstacles to avoid. However, there is another, harder to see, bug in the code.

During the game, a cluster of berries appears reasonably often. When the pappu hits those berries, it should split into three pappu clones, but instead, nothing seems to happen.

**Finding the bug**

This time, instead of checking out old versions of the code, just run git log and look at the 10 most recent commits. Based only on the commit messages, which commit do you think is most likely to have introduced this bug? You can't be sure just by reading the messages, but pick the one you think is most likely.

** Identifying a Second Bug Solution**

One reasonable guess is that the commit with message "speeding clones up", that is, commit `003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a`, is likely to be the one causing the bug. The bug is related to clones, and this commit changed the behavior of clones, so it seems plausible that this commit caused the bug.

Of course, the most likely-looking commit won't always be the culprit, so you'll always have to take a closer look at the suspicious commit to see if it actually caused the bug. In this case, the commit "speeding up clones" did in fact cause the bug.

Using this strategy of examining the most likely looking commits doesn't always work, but it often does, and it can save a lot of debugging time. This is one of the reasons it's so useful to make one commit per logical change and give each commit a good message - to make it possible to take shortcuts like this!

### 7.4 Fixing the Second Bug

**Changes introduced**

As before, you can use `git diff` to find the lines introduced by the buggy commit. Again, you'll need the ID of the buggy commit, which is `003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a`, and the ID of the previous commit, which is `746f762e38b5bbb7d0b837464ef6ec3f8ee5bf91`.

Thus, by running `git diff 746f762e38b5bbb7d0b837464ef6ec3f8ee5bf91 003c8c197cd3b1e5b28b58f53ee14d7ebaa9bb3a`, you can find out that the change made by the buggy commit was:
```
-      clone.x += utils.randomNumber(5, 10);
-      clone.y += utils.randomNumber(-20, 20);
+      clone.x += utils.randomNumber(500, 1000);
+      clone.y += utils.randomNumber(-2000, 2000);
```
That is, **the `x` and `y` coordinate of each clone is changed by a larger random amount**. This will have the effect of making the clones move more quickly, or speed up, since their positions change more quickly.

**File changed**

Near the top of the `git diff` output, you can see the lines:
```
--- a/js/pappu.js
+++ b/js/pappu.js
```

This indicates that the file changed was `js/pappu.js`, that is, the file `pappu.js` in the directory `js`.

What caused the bug

Based on the change that was made, one possible bug is that the clones move too quickly - so quickly they have left the screen before you see them. This turns out to be correct. If you change the code to have numbers bigger than the original numbers, but smaller than the new numbers, the clones will move more quickly, but still be visible. Some lines of code that work well are:
```
clone.x += utils.randomNumber(20, 40);
clone.y += utils.randomNumber(-30, 30);
```

Again, even if you weren't sure exactly why the bug was there, congratulations! You tracked down which lines introduced a bug without knowing the code base, just by using Git.

# Lesson 2: Creating and Modifying a Repository

## 2.1 What Makes a Repository a Repository?

通过`git clone`得到metadata后，有些hidden directory是看不到的。比如`.git`.必须用`ls -a`才能看到隐藏文件.而这个隐藏的`.git` is the thing that *Makes a Repository a Repository*

![git30.png-225.1kB][96]


##2.2 Initializing a Repository

通过`git init`来初始化。比如在`recipes` directory下初始化，那么这个repository的名字就是`recipes`。这个文件夹下的所有文件都会包括在repository里。

![git31.png-290.8kB][97]

**Git repositories and directories**

Each Git repository is tied to a specific directory - the directory where you ran `git init`. Only files from that directory (and subdirectories inside that directory) will be contained in that repository, and you can have different repositories in different directories.

Note: it's often the case that a Git repository in some directory will only contain, or track, **some** of the files in that directory, rather than **all** of them. You'll see how this works later this lesson.

**QUIZ**
`git init`不会有commit ID,这个必须自己手动，而且要写**commit message**.

![git32.png-222.2kB][98]

### 2.2.1 Examining the New Repository

用`git log`返回错误，因为`git init`之后，没有commit.但我们可以用`git status`查看现在的repository 状态。**status** shows which files have changed since the last commit. 

![git34.png-343.8kB][99]

## 2.3 Staging Area

利用staging area做一个缓冲区，可以一下子commit多个files。通过`git add`把working directory 里的files *add* to the staging area. 

![git35.png-319kB][100]

![git36.png-285.5kB][101]

![git37.png-444.3kB][102]

## 2.4 Concept Map: init, add, staging area

![git38.png-319.9kB][103]

## 2.5 **Writing Good Commit Messages**

**How to write a commit message**

You're about to make your first commit to your reflections repository. When you do this, you'll need to write a commit message describing your changes. If you followed the instructions in the "Setting Up Your Workspace" video for your platform near the end of Lesson 1, the editor you chose will appear as soon as you run `git commit` and allow you to write a commit message. If you get an error message, you should try revisiting the instructions in Lesson 1 and make sure your text editor is set up properly.

You can also specify a commit message via the command line by running `git commit -m "Commit message"` instead of just `git commit`. It's still a good idea to get an editor set up, since this will make it easier to write long commit messages that fully describe the change.

简单一句话：不要用`git commit`！要用这个：`git commit -m "Commit message"`

**Commit message style**

While commit message style varies from person to person, [this style guide](http://udacity.github.io/git-styleguide/) describes some common best practices when writing commit messages.
这个guide写的很好，到了自己写message的时候，一定要好好参考。

全部commit后，用`git status`检查，显示nothing to commit, working directory clean。

## 2.6* git diff Revisited(重点)

之前的git diff都是比较commit ID之间的，但是有时候我们也想比较working directory, staging area, and Repository之间的变化。比如刚刚take a break，回来的时候忘记modify了哪些部分。


先回顾一下之前用git diff找*asteroids*里bug的流程。(step 1 and step 2)
1. 打开directory asteroids 的时候，发现当前的ID是之前的一个ID，不是最新的`3884eab839`。而且`game.js`也被modify了。发现必须得commit or discard the modification of `game.js`，才能`checkout`回到`3884eab839`。于是用`git checkout game.js` discard the modification, and then `git checkout 3884eab839`回到初始状态。现在这个状态是最开始clone完的状态，有bug。
2. 我们已经知道了有bug的ID是`25ede836` with the message "a couple missing ends with the ipad verison", the previous one is `df035382`。用`git diff df035382 25ede836`找到不同的地方。![git39.png-118.4kB][104] 记住删除信息所在位置，用sublime打开`game.js`，加上删去的那一行。用`git status`检查，看到`modified: game.js`.
3. `st index.html` 打开后随便找一行collapse the line onto the previous one.
4. 好了。我们现在有两个文件处于modified。一个是`games.js`，这个文件之前有bug，子弹可以连续射出。通过比较bug的ID和previous one, 我们发现the bug one 少了一行，我们加上。再把index里面的随便一行更改一下位置。每个modified file都有一个`*`标记，表示虽然更改了，但是没有commit。（我用的注意是最右侧有一个雷电的标识表示有文件modify了）。

现在来看一下working directory, staging area, and Repository的状态。
1. The **repository** contains several commits. And each commit contains several files. 比如现在图中的the most recent commit contain the `game.js` and `index.html`，这些是ID `3884eab839` 下的文件，也就是说有bug的文件。修改的文件还在working directory.
2. The **staging area** is a copy of the most recent commit until I add changes to it. So it has those same files.
3. The **working directory** also has the same files in it, but I've made some updates to `game.js` and `index.html`，which I'll represet using these stars.

![git40.png-250.8kB][105]

We know that we can use `git diff` to compare two commits by entering their commit ID's. 但是staging area and working directory are not commits, so they don't have ID's. 
- 那么我们该怎么比较staging area and working directory里的modification呢？

Solution： use `git diff` to compare working directory and staging area, `git diff`不加arguments. This will show any changes you've made that you haven't added to the staging area yet.

![git43.png-393kB][106] (注意两个diff的用法)


试验一下，现在有`game.js` and `index.html`处于modification状态，run `git diff`，结果会把staging area 里的文件当做old file, wroking directory里的文件当做new file:

![git41.png-101.3kB][107]

- add `game.js` to the staging area and run `git diff` again

This time we only see the changes to `index.html`，因为现在working directory and staging area里的`game.js`是一样的了。(since the `game.js` is the same in the staing area and workign directory).Add a star to `game*` in the staging area.

现在我们可以用`git diff --staged`查看staging area and Repository之间的changes。因为现在只有`game.js`不同，所以只会显示the changes of `games.js`

![git44.png-476.5kB][108]

run `git diff --staged`:

![git45.png-54.4kB][109]

- `git commit -m "Add delay back to bullets"`, then `git diff`

git commit 之后，创建了新的commit ID `943a54d`，此时只有`index.html`处于modefied状态，the `game.js` is all same in three stage.

![git46.png-103.5kB][110]

- 但如果我不想要`index.html`里的changes怎么办？

use `git reset --hard`, which discards any changes in either the working directory or the staging area. 但是用的时候一定小心。虽然在git里大部分的操作都是reversible，你可以随时resotre previous commits,但是！！！But you've never committed the changes in your working directory or staging area. So if you run this command, you can't get those changes back.

![git47.png-523.9kB][111]

**QUIZ**
注意第二行，`git diff --staged` 比较的是staing area and commit1

![git48.png-393.9kB][112]

## 2.7 Commit the Bug Fix

**Leave 'detached HEAD' state**

Right now, your HEAD should still be 'detached' from Lesson 1 when you checked out an old commit. To fix that, run the command `git checkout master`. You'll learn more about what this command does later this lesson.

**Fix the delay bug**

Now, if you were following along with Caroline, you may have already fixed the bug in the Asteroids repository. If not, go ahead and make the change and add it to the staging area now.

In `game.js` find the statement `if (this.delayBeforeBullet <= 0) {` (should be on line 423). On the next line, insert `this.delayBeforeBullet = 10;`

**Instructor Notes**

You may notice that our commit id is different from yours, even though we made the same change, while the commit ids up to this point have all been the same. That’s because if there is any difference between two commits, including the author or the time it was created, the commits will have different ids. 

## 2.8 Branches

比起那些不易理解的commit ID,创建branch可以更方便人类理解。比如一个program要做一个中文版，那就创建一个branch，起名叫"chinese". 在git中默认的最主要的branch是**master**.

master branch has quilty, so it should be stable. 当我们做一些experiment 或是 add new feature的时候，会创建一个新的branch. Branches are also good when not only collaborating publicly, but they really good to collaborate with yourself.

![git50.png-313.6kB][113]

### 2.8.1  Making a Branch

`git branch` show the current branch, `git branch easy-mode` create a new branch with the argument name. `* master`表示当前所在的branch是master，`git checkout easy-mode` switch to the easy-mode branch, 

找到`game.js`中关于fragement的代码，把`3`改为`2`，这样游戏里击中陨石后就会变为两半而不是三部分。

We consider this one logical change since it changes the behavior of the game.

`git add game.js`, `git commit -m "Make asteroids split into 2 smaller pieces instead of 3`

![git51.png-452.7kB][114]

`git status`显示：
```
On branch easy-mode
nothing to commit, working directory clean
```

### 2.8.2 Branches for Collaboration
通常一个project的workflow是这样的，一开始有*master*，然后分为两个branch，一个*bug-fix*, 一个*feature*.这样可以同时进行debug和add feature的工作。

![git52.png-326.3kB][115]

Then once a feature or bug-fix is complete, the author can either update master to the tip of new branch, 

![git53.png-323.6kB][116]

or combine the feature branch with the current master, using git merge feature.

![git54.png-209.7kB][117]

**实战**

We add a new feature to the game, a new game mechanic.  you can collect coins by touching them with your ship. 

现在老师A已经创建了branch `coin`, 她告诉老师B可以test it. She can get some feedback before adding it into the main branch.

测试发现能通过touch coin得分，但是spaceship没有颜色,`git log`后发现在branch coin里没有添加颜色的commit Id。`git checkout master`,`git log`发现在master里有添加颜色的commit.

Git can help you visualize the branch structure via the command:
```
git log --graph --oneline master coins
```
`--oneline` means making the output shorter and easier to see.
`master coins` means telling the Git which branch I want to visualize

output分为三部分，从下到上分别是：
1. These commits existed before the coins branch was created.
2. These are commits that Sarah added to the coins branch.
3. And these are commits that were added to master after the coins branch was created.

![git56.png-780.6kB][118]

**Quiz**

![git57.png-162.9kB][119]

![git58.png-312.4kB][120]

### 2.8.3 Reachability

每一个commit都有自己的parent, 只有一个没有，the initial one. Using arrow to represent parent. 

但是有些commit之间是unreachable的

![git59.png-408.2kB][121]

**quiz**,简图，a and b are branch name.

![git60.png-326.1kB][122]

![git61.png-370.8kB][123]

### 2.8.4 Detached HEAD Revisited

To understancd the entire detached head message. Remember, to get this message, we checkout a commit, not a branch. Remember the head just means current commit.

![git62.png-414.3kB][124]

Running `git checkout -b new_branche_name` is equivalent to running two commands.
First, its just like running `git branch new_branch_name` and then, running `git checkout` on that new branch.

![git63.png-473.5kB][125]

比如我一直master这条直线上的某个branch做开发，添加了一个new feature, 我想要把这个feature独立出来，就用`git checkout -b new_branche_name`把这个new feature 从master主线上独立出来，head也会teach到这个new branch上，图中最下面的*new_branch_name* 就是new branch, 对于其他branch,这个new branch是unreachable的，不论怎么玩都没关系。

![git64.png-464.8kB][126]

### 2.8.5 Combining Simple Files(Mering files)

How to conbine braches into single version?

之前讲到了branch coin添加了吃coin的feature，但是spaceship没有颜色，而branch master的spaceship有颜色，但没有吃coin的feature,我们要combine these two branch into a new branch.

![git65.png-405.8kB][127]

**An example quiz**

Jack和Rachel都有B和D，所以我们希望在final version里有这个连feature.但是其他三个都是只有一个人添加了的feature,我们不确定这个feature在final version 里是否是必须的，所以不确定。

![git66.png-365.4kB][128]

那么怎么来确定需要哪个feature呢？如果我们知道original里有哪些feature的话呢？
**quiz two**
A：Rachel 有A，没做什么修改，但Jack明确地删除了A，说明不需要A。
C：Original和Jake都没有C，但是Rachel added it. 说明it should be in the final.
E: same with C.

![git67.png-370.8kB][129]

### 2.8.6 Merging Coins into Master

现在branch coins(这个coin只是一个commit ID的易于理解的名称，一个branch tip,现在这个branch coins 的head teach在ships on conis这个commit上），而master在color这个commit上。我们要把master当做主线，把coins添加到里面去。

利用三个commit，git能实现merge的功能。图中蓝色画圈的三个。
*revert controls* 是Jack和Rechel开始分道扬镳的commit,
*ships on coins* 是Jack added coins feature
*color* 是Rechel在master 主线上的更改，包括添加了color等feature.

这个combined version is also a commit. 而这个new commit会store the information of its parent, 其parent就是*color*和*ships on coins*. 这样的merge能保存两条线上所有的commit.

![git69.png-437.3kB][130]

一旦我们成果merge,就不在需要coins这个branch了，因为我们可以用合并后的master直接回溯到之前的commit.So once we're down with the merge, we can delete the coins branch. 注意我们删除的是label,而不是commit.(Note that when we talk about deleting braches, we mean deleting the label. The commmits will still be there in the history.) However, if no branches can reach the commit, deleting a branch does effectively discard its commits.

So if you deleted the coins branch without merging it in first, you would essentially be abandoning these commits since they would all become unreachable.

![git70.png-573.2kB][131]

**quiz**
merge后，`git log`能看到哪些commits？

只有右下角哪个easy是unreachable.

![git71.png-436kB][132]

### 2.8.7 Merging on the Command Line(实操)

**Comparing a commit to its parent**

The command Caroline mentions to compare a commit to its parent is `git show commit_id`.也就是说不用非得找到两个commit ID一起提交，只要找到一个有bug的ID，就能看到它和它parent之间的差别。

**Checking out the coins branch**

If you haven't already checked out the coins branch, you'll need to do so now with the command `git checkout coins` before you'll be able to refer to it. Once you've done that, decide whether you should keep it checked out or check out a different branch before completing the merge.

**A note about`git merge`**

下面一大堆就是想说，在`git merge`之前，一定要想checkout切换到要merge的branch上，不然会把current branch也merge掉。比如，`git checkout branch1` and then type `git merge branch2`. The only reason to type `git merge branch1 branch2` is if it helps you keep better mental track of which branches you are merging.

`git merge` will also include the currently checked-out branch in the merged version. So if you have branch1 checked out, and you run `git merge branch2 branch3`, the merged version will **combine branch1 as well as branch2 and branch3**. That’s because the branch1 label will update after you make the merge commit, so it’s unlikely that you didn’t want the changes from branch1 included in the merge. For this reason, you should always checkout one of the two branches you’re planning on merging before doing the merge. Which one you should check out depends on which branch label you want to point to the new commit.

Since the checked-out branch is always included in the merge, you may have guessed that when you are merging two branches, you don't need to specify both of them as arguments to `git merge` on the command line. If you want to merge branch2 into branch1, you can simply `git checkout branch1` and then type `git merge branch2`. The only reason to type `git merge branch1 branch2` is if it helps you keep better mental track of which branches you are merging.

Also, since the two branches are merged, the order in which they are typed into the command line does not matter. The key is to remember that `git merge` always merges all the specified branches into the currently checked out branch, creating a new commit for that branch.

**Merge conflict**

如果出现这个confilict,到时候在查看[这个网站](https://www.udacity.com/course/viewer#!/c-ud775/l-2969618657/e-2989238628/m-2960548799)，看教程
If you get a message like this
```
Auto-merging game.js
CONFLICT (content): Merge conflict in game.js
Automatic merge failed; fix conflicts and then commit the result.
```

必须先checkout到master, 再merge coins. merge后，会有up arrow,提示你可以`git push`，把local推送到远端服务器。如果想要Undo this merge, 用命令`git reset --hard commit_sha` 。`commit_ID`是merge前的一个commit ID. 
![git72.png-115.1kB][133]

merge后，会有不同的author，不同的branch线，组合在一起，用`git log`很难找到某个commit的parent。这个时候我们用本小结一开是介绍的`git show commit_ID`来查看某ID和其parent的区别。

merge成功后就可以delete the branch coins, 用`git branch -d coins`。
用`git log --graph --oneline`查看commit信息。

###2.8.8 Merge Conflicts

orinical里**B**是原版，但Jake里的**B'**是修改过的，而Rachel里的**B''**也是修改过的。如果merge的话，最后的文件里究竟是哪个**B**

![git73.png-265.3kB][134]

结果是不确定
![git74.png-385.7kB][135]

###2.8.9 Conflict Detection

how Git know whether there is a merge conflict?

举例来说，有两个文件。第一个文件`foo.py`,第二个文件名字不同，实现方法不同，但功能一样。

![git75.png-229.8kB][136]

Consider the following two examples. In both cases, we start with two identical copies of the same file. In the first case, two different contributors add new functions to the bottom of the files. These are different functions that don't interact with each other and have nothing to do with one another. However, in the second case, two different contributors add different implementations of the same function with different names.

Git无法分辨第二个例子里哪个文件应该保留。
In the first case, you pretty clearly want both functions to be included, but in the second situation, you probably only want one version of the function, probably whichever one is either more memory efficient or
faster, depending on what you're going for. But Git can't really tell these two options apart.

所以Git不会管那么多闲事，它会把有confilct的文件提醒给contributor,让这些人自己去决定选择哪个文件。
Git just assumes that if you're merging together two commits that have changes in the same general area, the authors will want to know about it and have the chance to figure out for themselves which change to keep. This decision to ask the user whenever there's any ambiguity at all does sometimes lead to situations where it seems really obvious to you, as an expert on the content, how to resolve the conflict. But Git brings it to your attention anyway. While this may be annoying, it's significantly better than if Git tried to guess too often, which could lead to weird conglomerate changes that don't really make any sense and probably wouldn't compile or run.

###2.8.10 Update Easy Mode

**Motivation**

Master has updated since the easy-mode branch was created. In this case, it has the addition of coins, which you might like to include in the easy-mode branch. In general, it’s very common that if you make a branch, either an experimental branch or to work on a new feature, you want to periodically merge master into that branch. This is because master usually contains the official version of the code, and it’s common to want experimental changes to include all of the changes to master.

**Previous version of the diagram**

Here’s what the history looks like right now. 

![git76.png-106kB][137]

**Draw an updated diagram**

If you merge master into the easy-mode branch, what will the history look like afterward? Take a minute to draw the new history using whatever method you like best. You might want to use pencil and paper, or create a text file with stars and dashes similar to the output of `git log --graph`, or maybe use an online diagramming tool like **gliffy** or **yUML**. Once you’re finished, watch the solution to compare your diagram to Sarah’s.


**Solution**

![git77.png-394.4kB][138]

### 2.8.11 Resolving Merge Conflicts

merge *master* 和 *easy-mode*的时候，出现了merge conflict, 因为两个branch都对`game.js`做了更改。

![git78.png-367.9kB][139]

打开`game.js`，GIT会把有问题的部分标记出来。一些special lines会把内容分为三个部分。

The top section, marked **HEAD** is my code. The bottom section, marked **master** is the code that's in master right now. And the middle section is the original version that both branches modified,
which git called the **common ancestor**.

the HEAD and common ancestor
![git79.png-617.8kB][140]

the master
![git80.png-556.6kB][141]


**如果解决？**

Now when I'm trying to resolve a merge conflict, the first thing I do is try to understand what changes both branches have made. The difference between the middle section and the top, shows the changes that I made in the easy-mode branch. If I'd forgotten what those changes were, I can spend a few minutes comparing and recall that the difference was changing this three to a two.

The difference between the middle and the bottom shows the changes that were made in master.

这样的conflict在merge的时候很常见，发现后可以直接和另一个contributor交谈看怎么解决问题，但是我们最好先自己看一下这些difference. it looks like Sarah replaced this entire section of code with a call to a function called breakIntoFragments. Now that probably means that she created this function and moved this code into that function. Which is a pretty common way to make code more readable by breaking it up into understandable parts.

Now it might look like this function existed in both versions. Since it's not inside the special merge conflict lines. But actually, that's just because this change didn't create a conflict. Now after I've spent a few minutes comparing this function to the code that was removed by Sarah below.
I could see that she didn't make any changes to the code, other than to move it.

Now, how should I reserve this merge conflict?

For example, if I wanted to undo my changes, I could just delete my version and the original version, as well as these special lines to leave only Sarah's code. Instead, you should create a version of the code that incorporates both of our changes.

### 2.8.12 Resolving Merge Conflicts Quiz

conflict file
```
Asteroid = function() {  
  this.breakIntoFragments = function () { 
    for (var i = 0; i < 3; i++) {
      var roid = $.extend(true, {}, this);
      roid.vel.x = Math.random() * 6 - 3; 
      roid.vel.y = Math.random() * 6 - 3; 
      if (Math.random() > 0.5) {
        roid.points.reverse();
      }    
      roid.vel.rot = Math.random() * 2 - 1; 
      roid.move(roid.scale * 3); // give them a little push
      Game.sprites.push(roid);
    }    
  };

  this.collision = function (other) {
    SFX.explosion();
    if (other.name == "bullet") Game.score += 120 / this.scale;
    this.scale /= 3;
    if (this.scale > 0.5) {
<<<<<<< HEAD 
      // break into fragments
      for (var i = 0; i < 2; i++) {
        var roid = $.extend(true, {}, this);
        roid.vel.x = Math.random() * 6 - 3; 
        roid.vel.y = Math.random() * 6 - 3; 
        if (Math.random() > 0.5) {
          roid.points.reverse();
        }    
        roid.vel.rot = Math.random() * 2 - 1; 
        roid.move(roid.scale * 3); // give them a little push
        Game.sprites.push(roid);
      }
||||||| merged common ancestors
      // break into fragments
      for (var i = 0; i < 3; i++) {
        var roid = $.extend(true, {}, this);
        roid.vel.x = Math.random() * 6 - 3;
        roid.vel.y = Math.random() * 6 - 3;
        if (Math.random() > 0.5) {
          roid.points.reverse();
        }
        roid.vel.rot = Math.random() * 2 - 1;
        roid.move(roid.scale * 3); // give them a little push
        Game.sprites.push(roid);
      }
=======
      this.breakIntoFragments();
>>>>>>> master
    }
  };
};
```

**solution**
In this case I want to keep Sarah's change of moving this code to the function.
So I'll need to make my change to the function.
So, I'll scroll back up to the function and change this 3 to a 2 (line 4).

Now I'll delete my version since I already have the change from it and the original version since I don't need that version any more and I'll delete git's special lines.

I'll also clean up a little bit by removing these blank lines. Now I'm left with the call to the breakIntoFragments function, which breaks each asteroid into two fragments, rather than three.

changed file:
```
Asteroid = function() {  
  this.breakIntoFragments = function () { 
    for (var i = 0; i < 2; i++) {   //change 3 to 2
      var roid = $.extend(true, {}, this);
      roid.vel.x = Math.random() * 6 - 3; 
      roid.vel.y = Math.random() * 6 - 3; 
      if (Math.random() > 0.5) {
        roid.points.reverse();
      }    
      roid.vel.rot = Math.random() * 2 - 1; 
      roid.move(roid.scale * 3); // give them a little push
      Game.sprites.push(roid);
    }    
  };

  this.collision = function (other) {
    SFX.explosion();
    if (other.name == "bullet") Game.score += 120 / this.scale;
    this.scale /= 3;
    if (this.scale > 0.5) {
      // break into fragments
      for (var i = 0; i < 2; i++) {
        var roid = $.extend(true, {}, this);
        roid.vel.x = Math.random() * 6 - 3; 
        roid.vel.y = Math.random() * 6 - 3; 
        if (Math.random() > 0.5) {
          roid.points.reverse();
        }    
        roid.vel.rot = Math.random() * 2 - 1; 
        roid.move(roid.scale * 3); // give them a little push
        Game.sprites.push(roid);
      }
      this.breakIntoFragments();
    }
  };
};
```


### 2.8.13 Committing the Conflict Resolution

我想保留branch easy-mode, 所以merge master into easy-mode. 先checkout easy-mode, 再merge. 发现有conflict，我们按照上一节的教程，修改好`game.js`。

![git82.png-64.2kB][142]

更改完成后，`git status`, 显示 fix conflict. `git add game.js`后，再`git status`, 显示 you are still merging.

![git83.png-439.9kB][143]

`git commit -m "fix merge confict, merge master into easy-mode"`, 不知道怎么设置能像教程里那样自动弹出写message的editor界面，所以只好自己写message，要尽量写的详细些。

`git log --graph --oneline`：

![git85.png-65.1kB][144]

![git86.png-192.7kB][145]

**quiz**
`git log -n 1`只输出一个commit，更改数字`1`可以得到不同数量的commit
![git88.png-86.6kB][146]

output:

![git89.png-57.2kB][147]

## 2.9 Concept Map: branch, merge

You know that merging and branching both have to do with commits, but what kind of relationships does each of these ideas have with the commit.

Branches are really just labels that refer to commits, so we have this new kind of relationship, through first year relationship. So this has to be branch. Let's make sure this really makes sense.

Does diff really have an operates on relationship with branch?

Well, yes.You can diff two commits or you can diff two branches, which is basically just diff into two commits. But they're sort of different ideas, similarly you can run log on a branch or on a commit.

So let's check this one, does merge operate on commits?

Well, yeah, merge takes two commits and sort of smushes them together into a new commit.

![git90.png-478.9kB][148]

# Lesson 3: Using GitHub to Collaborate

##3.1 Creating a GitHub Account

**Set up Password Caching**

Every time you send changes to GitHub via the command line, you'll need to type your password to prove that you have permission to modify the repository. This can get annoying quickly, so many people like to set up password caching, which will let you type your password once and have it auto-filled on that computer in the future. To do this, follow the instructions [here](https://help.github.com/articles/caching-your-github-password-in-git/). If you're using Windows and you followed our Git installation instructions earlier, you're using msysgit, so you can follow the instructions for msysgit.

##3.2 Keeping Repositories in Sync

在向github推送前，一定要先把working directory and staing area里的文件commit掉， 通过commit history记录下来。

![web110.png-108.7kB][149]

github repo里没有working directory and staing area, 因为github repo 是在远程的，并不能直接连接，所以没有。github不会像其他service一样sync with cloud，比如CMD markdown就是，我现在敲击的每一句话都会立刻与云端同步。而且正因为能自动同步到云端，when you use Github, you need to choose when and how to get two version.

So, since syncing doesn't happen automatically, how do we sync between the local copy of a repository and the one hosted on GitHub?

你可能回答lesson oneli里用过的`git clone`.但这个命令只能从github server clone, 并不能把本地的repo clone 到github server上。

git has a concept of a **remote repository**. This lets you store the location of a repository that you will want to send and receive new commits to and from. Git users often refer to these remote repositories simply as remotes.
我们在之后的课程里再详细讲这个**remote repository**。

假设我们现在已经有了remote repo指向github上的repo(见图中arrow), you can **pull** data and **push** data. 我们不是一个一个的commit推送，而是选定一个branch, `git push`后，就能把这个branch下的所有commit同步到remote repo。

![web111.png-176.9kB][150]

但是想象一些，如果branch里有上百个commit，每次push都要把所有commit推送的话是件很低效的事。

![web113.png-171.6kB][151]

git的做法很聪明，只提交“有用的”branch。比如下图中local有4个branch, github里只有一个branch. 现在我要推送local 里的a, 即`e53`，github会找到这个`e53`的所有parent和children。并只推送github中没有的branch. 而`664`因为unreachable,所以不会被推送。所以结果只有`fd2` and `e53`被推送。

![web114.png-145.8kB][152]

##3.3 Adding a Remote

我们打算把local 的 reflection 推送到github. 先cd到reflection directory。

记住，remote repo的stardard name 是`origin`. 用`git remote add origin url_address`,url_address可以在创建好的github repo里找到,初始化不带。

```
git remote add origin https://github.com/user_name/reflections.git
```
![web116.png-75.9kB][153]

我自己尝试推送的时候得到了error
```
[XX@XXXX] ~/Udacity/version-control/reflections  
❯ git push
fatal: Not a git repository (or any parent up to mount point /home)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
```
发现这个reflections derectory根本没有初始化。

初始化以及准备工作： `git init`, `git add xxx.txt`,`git commit -m "add xxx.txt`.

好了，创建remote： `git remote add origin https://github.com/user_name/reflections.git`。
`git remote`能查看remote branch. `git remote -v`能查看更多的信息。

`git push` takes two arguments, the remote I want to send changes to, and the name of local branch that I'd like to push. 所以把branch master push到 remote origin. 
```
git push origin master
```
![web119.png-95.1kB][154]

命令行提示输入github的用户名和密码，输入后推送完成，可以在github官网上看到相应的文件了。
推送后，github默认会创建相同的branch name，即github上的branch也叫master。

## 3.4 Editing Files on GitHub

点击commit button，可查看commit history. 点击new fiel创建一个新文件。填写文件名，文件内容，commit message等相关信息。

![web120.png-31.3kB][155]

我们在github直接创建一个文件，比如collebrate的时候别人也会上传一些commit,而我们的本地主机没有相关文件。下一节练习如何得到最新的version。

## 3.5 Pulling Changes

这是我们现在的状态
![web121.png-144.8kB][156]

利用`git pull`来获得最新的commit
![web122.png-166.8kB][157]

在terminal端的操.`git pull`后还是要two argus, 一个是remote name, 一个是本地的branch name.
```
git pull origin master
```
pull之后，branch也会checkout到最新的commit状态。

![web123.png-65.2kB][158]

run `git log`就能看到在github端提交的commit了。

## 3.6 Concept Map: GitHub, Push, Pull, Remote

We’ve introduced a few new concepts since we last revisited our concept map.

- GitHub
- git push
- git pull
- remote

GitHub is a service that lets users interact with Git. But I chose to represent it as Git being a part of GitHub.

A remote in your local repository is basically a reference to another repository, so we can say that remote refers to repositories. Also when you clone a repository, a remote gets set up for you automatically, so we can say that clone operators on remotes.

When you push or pull, you have to specify what branch you want to push or pull. So, it definitely operates on branches. Pull takes a branch from a remote and brings it to your local repository. And push does the opposite, taking a branch and pushing it to a remote. So these do both operate on a remote as well.

![web124.png-355.8kB][159]

##3.7 Forking a Repository
左上是原始的repo，通过fork,会在自己的github账户中创建一个相同的repo。而Caroline和Sarah可以对右上的repo做出各种修改，制作自己喜欢的recipe，个人定制化。

![git91.png-682.4kB][160]

**quiz**
![git92.png-130.3kB][161]
左上，Branches happen on a single repository. Of course, you can push and pull branches, but when you create one, you're creating it on one single repository

右上，右下，Cloning involves taking an existing repository and making one just like it. The original repository could either be remote, like in this case, so here we cloned from GitHub to local. Or you could even clone a local repository into another spot on your computer. We haven't really talked about this, so this one was probably a little tricky.

左下，This one looks a lot like a clone too, but remember, we are cloning our repository from GitHub onto GitHub. You do that using GitHub's built-in fork feature. Forking is only used within the context of GitHub, taking an existing GitHub repository and making a copy of it, whereas clone works on any two repositories.

### 3.7.1 Fork the Recipes Repository
找到想要fork的repo,点击github页面右上的fork，这样你的账户里就有一样的repo了。跳转页面到你账户里的repo，找到右下的https赋值。在本地`git clone https//XXX`就能得到local repo. 如果是通过这种方式，我们就不用自己添加remote了，git会自动添加remote. 不信的话运行`git remote -v`查看详情。

我想让Larry和我一起collaborate这个repo,在右下的setting里添加collaborator,输入对方的github name.

###3.7.2 Push Changes to the Recipes Repository
**Add a new recipe to the repository**
On your own computer, add a new recipe for a food that you like and commit it on the master branch.

**Push your changes**
Push the master branch to your fork.

**Where was your commit?**

Before you ran `git push`, your change should have only existed locally via `git log`. Commits will not automatically be shared to remotes - you have to manually push your branch if you want to share changes.

After you ran `git push`, your change should have existed locally and on your fork. It should not have existed on Larry's repository, which is the repository you forked. The reason you forked in the first place is because you don't have permission to change Larry's repository!

##3.8 Collaborations Cause Conflict
如果local和github上的repo都有了改变，那么不论是pull还是push,都会有confilict.
![git94.png-78.6kB][162]

其实我们想merge local and remote branches. 

###3.8.1 Change the Chili Recipe Quiz

最上面的commit是另一个人提交的。
![git97.png-120kB][163]

因为两个人都对同一个文件的同一行做出了改动，github会高亮标识，提示有confilct

![git98.png-158.6kB][164]

##3.9 Updating Local Copies of Remote Branches
我对一个Chili Recipe里做了改动后（包括add, commit),本地的master已经最新了，但是remote branch还没有更新。而remote branch的name就是**origin/master**,通过`git push`后，才能让branch master和origin/master同步。不信的话先别push,`git diff origin/master master` (`git diff old_one new_one`), 可以看到二者之间的差别。

图中本地的origin/master和github的master都是未更新状态，只有local的master有改动，是latest.（注：origin和origin/master是一个branch）
![git100.png-84.9kB][165]

push后，全部更到最新。
![git101.png-121.3kB][166]

如果现在local和github repo都改变了
![git102.png-115.6kB][167]

我们可以通过`git fetch`只更新local, 即让origin/master和github repo(remote)同步，而让local的master被保留。

![git104.png-127.8kB][168]

也就是说，local现在有两个branch,一个是master，一个是和remote github端同步了的origin/master. 比如说现在我要上飞机，但我本地已经有了最新的version，这个时候我可以merge这两个branch。但我也可以不着急merge二者，继续在master做我的修改。

![git105.png-128.9kB][169]

但如果merge了的话，其实相当于用了`git pull`。因为pull的流程也是先更新(fetch)本地的remote branch **origin/master**,然后再把**origin/master**和local的**master** 合并(merge).
所以说，`git pull` = `git fetch` + `git merge`

![git106.png-445.4kB][170]

### 3.9.1 Merging the Changes Together
**实操：command line**
现在的状态是github remote段写了两个commit，local段写了一个commit.

可以用`git branch -a`看到remote branch. 用`git fetch origin`把本地的**origin/master**更到和github remote端一样新。`git log orgin`可以查看origin/master的所有commit,现在这个branch的commit已经完全和github端一样了，`git log`查看的是local的master。

![git110.png-64.1kB][171]

`git status`可以看到当前的状态，提示说origin/master和local的master有不同的commit进度
![git111.png-32.8kB][172]

`git merge master origin/master`,理所当然得得到了conflict提示，因为两个branch的commit history不一样
![git112.png-18.8kB][173]

好了，打开有问题的文件，fix the conflict.
原文件
![git113.png-29.1kB][174]

我要保留github 段做出的修改
![git115.png-22.7kB][175]

修改完后，`git add xxxx` and `git commit`这一次没有加message，但是竟然跳出了nano的编辑界面，自动写好了message. Ctrl+X, 选yes, alt+D选择DOS-format,即可保存message。果然还是自动的填写的信息更准确方便。

![git114.png-13.9kB][176]

通过commit之后，这次merge也就算成功了。当然，也可以直接`git pull`.
`git push origin master`，顺序不能错，必须是`git push remote_branch local_branch`. push后就能在github看到所有的commit了。

###3.9.2 Fast-Forward Merges

既然`git pull` = `git fetch` + `git merge`，那为什么在上一节的例子里，直接用`git pull`的时候没有generated merge commit like `git fetch + git merge` did.

因为启动了fast-forward merges. This kind of merge occurs when you merge two commits, where one is ancestor of the other. （一个commit是另一个commit的祖先，这里的commit也可以理解为branch）

![git117.png-89.9kB][177]

如果想把上图中的a和b合并，其实没有必要创建一个新的commit。想想也知道新的commit也会有二者共同的commit history, 那么创建一个新的commit就没有必要了。

![git118.png-93kB][178]

只需把commit label 更到最新即可。So instead of adding a new commit, all we would do is update the lable to point b(latest). 

![git119.png-66kB][179]

We're taking a label from the history of a branch somewhere in its ancestry, and moving that label forward to the tip of the branch.

**quiz**
![git120.png-131kB][180]

###3.9.3 Making a Pull Request 

其实这里的pull并不是`git pull`里的意思，而是我打算在github段合并两个branch,这个合并的申请叫做 pull request, github非要这么设定，只能顺势而为了。

现在做一个example，展示整个workflow。
1. 我先在本地修改了`cask-recipe.txt`里的配方，添加了一种更健康的oil.
2. 创建一个branch,叫different oil.`git branch different-oil`+ `git checkout different-oil` 或者用一个命令`git checkout -b different-oil`.
3. `git add cask-recipe.txt` + `git commit` + `git push origin different-oil`. 这样就把branch different-oil 推送到了github端。接下在就能在github端查看了。![git121.png-127.6kB][181]
4. 切换到branch different-oil，查看commit ![git122.png-141.5kB][182]
5. 我们向pull request, 点击pull request button（如果绿色的那个button没出现的话就在branch different-oil里点pull request button,如图） ![git123.png-102.5kB][183]
6. github默认会认为你想要和原版的Larry的master合并，但是我们只是想把branch different-oil和master合并而已。点击右侧的edit，选择要合并的branch。再点击右下的**create pull request**. 这样我们就发出了请求。
7. 现在在pull request里可以看到我们做出的所有commit，修改。其他的人可以在主页面右侧的list里有pull request，可以点击查看。![git124.png-82.5kB][184]
8. 好了，接下来是另一个contributor的视角了,也就是Sarah.因为Sarah watching Caroline's fork of the recipes repository, 所有Sarah got an email notifying that Caroline made a pull request. 点击邮件里的地址，查看pull request.
9. Caroline想让sarah同意合并maser和different-oil。因为master是最主要的branch，所以必须保证没有错误。Sarah查看了Caroline做出的修改，但是添加的那个oil有拼写错误。所以Sarah在下面的写一个comment,提醒Caroline发现的问题。也可以在上面出错的地方写一个inline comment![git126.png-155.6kB][185]
10. 如果检查后一切正常，可以点击**merge pull request** button. 这个button只有在没有conflict的时候才会 ![git127.png-130.3kB][186]
11. 在有conflict的情况下，先让Caroline fix the conflict。让Caroline合并master和different-oil，成功后说明没有什么问题，之后再同一merge.

**quiz**

![git129.png-550kB][187]

###3.9.4  Updating a Pull Request

1. 上一节里Sarah发现了pull request 里有spell error，所以写了个comment。接着Caroline收到了邮件，里面写着comment的内容。
2. Caroline在local检查了下文件，发现全是写错了，于是fix，然后commit the fix。![git130.png-67.3kB][188]  ![git131.png-179.7kB][189]
3. `git push origin different-oil`,这样github端也能看到修改了。![git132.png-62.5kB][190]
4. push branch自动出现在pull request界面，在Sarah的comment下面，能看到Caroline的commit：*Fix type in caola*.![git133.png-120kB][191]
5. 现在commit显示为2，file changed显示1，可以点击file changed查看修改。  ![git136.png-99kB][192]

###3.9.5 Conflicting Changes

前一节我们学会了如何pull request，这一节我们take a look at what happens when someone else makes changes that confilct with your pull request. 

Sarah也made a pull request,
![git137.png-119.3kB][193]

It looks like she increased the amount of oil to put in the cake so that it would be more moist. Since our changes affect the same line, git will mark them as a merge so one of us will have to resolve the conflict.
二人修改的是同一行，所以git认定是一个merge conflict，二人中的一个得负责fix it.
![git138.png-350.7kB][194]

点击左上的**conversatoin** button，先点击绿色的**merge pull request**, 再点击绿色的**Confirm merge**, 即先confirm Sarah的changes，然后再去resolve merging conflict。
![git139.png-393.8kB][195]

Confirm后就可以删除sarah创建的*more-oil* branch 了。
![git140.png-257kB][196]

回到pull request 界面，发现无法merge的消息提醒。This is because performing a merge between the master branch and my branch would now cause merge conflicts. 之前的Sarah的修改已经提前改变了master里的`cake-recipes.txt`里的oil那一行,而Caraline在自己的branch里也是修改的同一行，所以无法合并master，有confilit. 
![git141.png-88.4kB][197]

解决方法：Rather than having you resolve the merge conflicts from the browser GitHub requires you to merge the changes on your own computer and send update the pull request with the merged version.
也就是说github不让你通过browser更改，必须要在local fix conflict, merge suffessfullly, then git push to update the merged version.

**图解**

初始状态：左图是local version，master在中间，Craline做出的changes全在新的branch **different-oil**里。右图是github version. 可以看到中间是master,但是从master开始，向右有两个branch就有差异了。一个右上角Sarah做出修改的branch *more-oil*,一个是右下角Craline做出的changes的branch different-oil。
![git142.png-493.4kB][198]

我们把master和Sarah的**more-oil** branch合并。这其实本来是个fast forward merge, 也就是说master的lable会移动到**more-oil**上，并不会创建一个新的commit。但是github的merge机制不一样，只要是github页面上的merge button，点击后merge后就一定会有一个commit。（it turns out that even if you could of had a fast forward merge, merging with the button on GitHub will always make a commit anyway even if no extra information is given by making that merge commit.） 合并后**master** label 到了新的commit上。现在就可以删除**more-oil**这个branch了，因为一旦合并它的使命也就完成了。所以在图中把右上角的**more-oil**这个branch name 移去。现在Craaline想要把自己的branch和master合并，但因为两个人都对同一line做除了改动，所以有conlict. 现在Caraline必须在local fix this conflict.
![git143.png-476.6kB][199]

Now if Caroline wants to update her pull request to include my changes. If merging these two branches wouldn't cause a conflict, I could actually just pull in her request now. But since we changed the same lines, she's going to have to pull these changes over into her local version. So she'll need to pull master.
要想在local修改，就要用`git pull`更新本地到最新版本。
![git144.png-561.1kB][200]

好了，现在Caraline可以直接fix conflict，merge master and different-oil, git push, 这样github段的master就能更新了。但是！！！这么做的话其他人没有机会看到Caraline做出的修改，也没有机会提醒修改是否合理。尤其是在collaboration的环境下，必须要让别人review，所以要通过github的pull request功能来提交，这样其他人就能得到通知，来查看修改是否正确了。

具体的做法： Caroline will need to make the fix to her branch. Fix the typo for canola, and then merge in master into her different oil branch. And then push her branch up to GitHub which will update the pull request so that I can look at that before merging it back into master.
也就是说把所有改动放在**different-oil**里，然后合并**master**到**different-oil**, 再push **different-oil**，github那边会自动更新 pull request. 注意，别把**different-oil**合并到**master**，然后推送**master**，这会直接覆盖，别人没有机会在merge前review。

![git145.png-600.1kB][201]

###3.9.6 Updating Your Local Repository

上一节讲了各种原理，这一节讲在terminal端的具体命令操作。

用`git pull origin master`更新local. 也可以用`git fetch` + `git merge origin master`.

![git146.png-91.3kB][202]

先checkout到**different-oil**，再`git merge master different-oil`.这样才能把master merge到branch。如我们所料，得到了merge conflict提示。 
![git147.png-92.2kB][203]

---
下面是stackoverflow上的回答：
How to merge the master branch into the feature branch? Easy:
```
git checkout feature1
git merge master
```
---

I'll resolve the conflict keeping both of our changes, so now there's three quarters of the cup of canola oil, and then I'll commit the merge. 
修改了`cake-recipes.txt`后，commit.
![git148.png-178.7kB][204]

Now I'll run git log, and I can see that this branch contains both of our changes. 
这下两个人的修改commit就都能看到.

![git149.png-521kB][205]

之后run `git push origin different-oil`。As you saw before, pushing the branch updates the pull request. 
push后就能更新github端的pull request了

![git150.png-406.6kB][206]

在点击绿色的**Merge pull request**前，先写个comment通知Sarah让她来review.因为updata the pull request的消息是不会email给Sarah的。

![git151.png-117kB][207]

**quiz**

![git152.png-73.8kB][208]

After running `git log -n 1`, you should have seen output something like this:
```
commit bc368511c6406028c77e2631f77c4d22a5da16d0
Merge: 79fff84 23d1775
Author: cbuckey 
Date:   Tue Sep 30 18:50:28 2014 -0400

    Merge pull request #1 from cbuckey-uda/different-oil

    Change vegetable oil to canola oil
```

Notice that the commit message:

- Indicates that a pull request was merged
- Gives the number of the pull request (#1 here)
- Gives the branch the pull request was merged from (cbuckey-uda/different-oil here).
- Contains the title of the pull request.

GitHub automatically creates a commit message like this whenever a pull request is merged to make it easy to see pull requests in the commit history. Even when the merge is a fast-forward merge, GitHub still creates this commit.

## 3.10  CM: Fork, Fetch, Pull Request 

![git154.png-539.1kB][209]

![git156.png-514.3kB][210]

Forking is like cloning but with some extra steps and you can only do it on GitHub itself. It also takes a repository and makes another repository, so it does operate on repositories.

We know that fetching is a part of pull, but does it operate on remotes and branches? It clearly operates on remotes, because you're fetching data from the remote repository. The connection to branch is a little less clear. You can definitely, fetch a particular branch. When you fetch, the branch doesn't necessarily get updated. But remember that, we have references to the remote versions of our branches, and those are the things that get updated. So, it does operate on branches, as well.

you would think fast-forward merge would be related to merges.But the way that I think, about fast-forward merges is basically, that they change where a branch points. So, it's take a branch label from one commit to another commit. So in my mind, it just operates on a branch.

When you make a pull request, you're asking to have a particular branch be merged in, with the main branch or some other branch. It doesn't necessarily, have to be a master. And pull requests are purely GitHub idea. They don't exist in git proper. So, mergers are part of pull requests. Pull requests, work on branches. You merge two branches together. And it's something that's part of GitHub, so it all fits.

##3.11 Reflect: When to use a separate branch

You just saw that the workflow when making changes in a separate branch is more complicated than working directly in master, especially when you need to stay up-to-date with changes others are making. Rather than simply pulling and pushing, you need to pull changes into your local master branch, merge the local master into your branch (different-oil, in our case), then push your branch to the remote before finally merging your branch into master, either locally or on GitHub.

Given that, please add the following question and your thoughts on it to your reflections file:

**When would you want to make changes in a separate branch rather than directly in master? What benefits does each approach have?**

因为通过创建不同的branch来添加新的feature更易于和别人合作，每个人都更易于理解project的branch结构，user friendly. 通过pull request来merge，也能让别人review。

##3.12 Modifying the Adventure Repository (实操练习)

以下是指南部分，主要是fork[这个repo](https://github.com/udacity/create-your-own-adventure),来进行练习。
**Fork the repository and clone your fork**

Now that you've learned how to fork a repository, push changes to your fork, and make a pull request, you’re ready to contribute to the create-your-own-adventure story that you saw at the beginning of the lesson. To do this, first you should fork this repository. Then clone your fork, and make a branch to make your changes in.

Note: You could make your changes directly to the master branch in your fork, but when contributing to a public repository, it’s standard practice to make the changes in a non-master branch within the fork. This way, you can easily keep your master branch up-to-date with master of the original repository, and merge changes from master into your branch when you are ready.

**Make a change to the story**

Next, you should actually make a change to the story. For instructions on how to do so, please read the README in the create-your-own-adventure repository.

**Make a pull request**

Next, you should make a pull request containing your changes to the original repository. To do this, click the "pull request" button from your branch like you did before, but this time, leave the original repository as the base.

**Ask for your pull request to be merged**

You don't have permission to modify this repository, so you'll need someone at Udacity to merge your pull request. Our helpful bot Casey may be able to merge your pull request automatically. To have your pull request automatically merged, you'll need to follow the guidelines in the README of the repository, and in addition you won't be able to delete or modify lines. That restriction on deletions is because Casey doesn't want to merge a request that accidentally deletes part of the story, and she can't tell the difference between an accidental deletion and an intentional modification. To request auto-merging, leave a comment on the pull request containing "@casey-collab". For example "Please review this, @casey-collab". Make sure to leave the comment on the "Conversation" tab of the pull request, not the "Files changed" tab.

There are some valid pull requests that Casey won't be able to merge. For example, she won't accept a pull request that fixes a typo, since that modifies a line. If you'd like to make a pull request Casey can't merge, feel free to do so, and someone from Udacity will merge the pull request if we have time. However, we can't guarantee a response to these pull requests.

**If needed, update your pull request**

If someone merges your pull request or leaves a comment, GitHub will email you and let you know. If you're asked to make some changes, push those changes to your fork to update the pull request. Make sure you let the reviewer know that they should take another look!

If your pull request would result in a merge conflict, and you're not sure how to resolve it, see the next video for instructions.

---
根据上面的指南，完成了整个练习。review一下整个流程：
1. github(original): fork repo **create-your-own-adventure**.在我的repo里得到github (my fork): **create-your-own-adventure**
2. local(terminal): git clone github (my fork): **create-your-own-adventure**。在本地得到了整个repo
3. local(terminal): 在`/create-your-own-adventure/chinese/`里添加了folder **little_prince**,在floder里添加了file:**this_is_a_story_about_a_boy.md**.这个path: `create-your-own-adventure/Chinese/little_prince/this_is_a_story_about_a_boy.md`. `git checkout -b little-prince`,创建新的branch. `git add xxx`+`git commit -m "xxxxx"`, 最后`git push origin little-prince` 
4. github(my fork): 有了新的branch,点击**comment&pull request**绿色button.这一次合并请求的对象是github(original)里的那个master, 被合并的是github(my fork)下little-prince这个branch. 点击绿色的**commit pull request**后
5. github(original)：打开Pull request(有80+ge), 移动到**Conversation**这个label下，只有在这里留言才能提醒original repo的owner去处理我的合并请求。在comment里留言`@casey-collab`.这个是一个bot，查看你的提交是否符合规范
6. local(terminal)：好了，看来不符合。@casey-collab 给我反馈说md文件里的一行太长，超120个字符，让我用回车隔开。还有一个问题是在`chinese/language.md`里应该添加一行链接到我的文件，不然如果别人直接看`language.md`的话，是看不到的我的文件的。所以我在`大话西游.md`里添加了一行`[little_prince](little_prince/this_is_a_story_about_a_boy.md)`。（我想吐槽一句，能不能别用`大话西游.md`表示`language.md`，看了好久没反应过来)
7. local(terminal)：修改完了。 `git add 两个文件_分别add`,'git commit'(注释用自带的，自己写的不好），`git push origin little-prince`.
8. github(original)：Pull request, 移动到**Conversation**这个label下,再给`@casey-collab`写个comment告诉他我改好了。`@casey-collab`告诉我好了，没问题了。会自动merge pull request. 这个时候有提示，可以删除little-prince这个branch了。
9. local(terminal): `git checkout master`, `git merge little-prince`, `git push origin master`. 
10. github(original)：好了，这样在主目录里就能看到自己添加的文件了。而github(my fork)里也会有最新的commit和文件。Over

## 3.13 Keeping a Fork Up-To-Date(Merge Conflicts in Pull Request)

有时候pull request会因为merge confilcts无法通过。比如，你fork了一个repo，你在fork repo上做了changes,但是此时original repo也有别人做了修改，所以pull request会有merge conflicts, 而且你是没有权限修改origianl repo的。在github端使无法解决这个conflict，必须得在local解决。下面说得更具体些：

初始状态
![git157.png-113.2kB][211]

然后在local做了些changes，并把这些push到了fork repo. 
![git157.png-113.2kB][212]

与此同时有人更新了original repo。所有现在问题出现了，你想把自己的fork repo和original repo 合并，但因为现在两个repo都有了变化，所以pull request会有merge confilct。（If there are merge conflicts between their change and your change, then your pull request will not be able to be automatically merged.）
![git159.png-110.4kB][213]

Since there's no way to resolve merge conflicts on the GitHub site, you'll need to resolve the conflicts within the clone on your computer.
因为不能在github端解决conflict, 所以必须要把conflict clone到local来解决。也就是说，一个是local的已经有了changes的branch，这个branch和fork repo是一致的，另一个是已经更新过的latest origial repo，我们想把后者clone到local,在local合并并解决conflict后再push就能解决问题了。那么如果把original repo clone到local呢？ 我们可以通过adding remote（这里的remote就是original repo）的方式来做到这点。（To do that, you'll need to get the conflicting changes from the original repository into your local repository, which you can do by adding a remote.）

但是别忘了我们已经添加了一个remote叫origin，这个origin指向fork repo,我们需要另一个remote指向original repo。通常，这个指向original repo的remote起名为upstream。（Recall that you already have a remote set up called origin that points to your fork. But you'll still need to add a remote that points to the original repository. And many people namethis remote upstream.）

在本地fetch创建新的branch后，这个新的remote 的正式表示是 upstream/master。这样就可以在本地把upstream/master和local branch合并了。（Adding and fetching the upstream remote will add branches like upstream/master into your local repository, so that you can merge the upstream branch with your local branch.）
![git160.png-331.6kB][214]

现在我们举例来说。original repo里添加了名为**Sprikler**的branch，而我在本地做出的changes也全放到了名为**stop drop roll**的branch里。
![git161.png-136.3kB][215]

在local,因为我们把changes都放在新的branch **stop drop roll**里了，所以我们想把master更新到original repo的最新版。`git merge upstream/master master`.(Since I created my change in a separate branch, I want to make my master branch the same as the master in the original repository. So, I'll run git pull upstream/master to update my master branch to the latest commit from the original repository.)
![git161.png-136.3kB][216]

![git162.png-43.8kB][217]

然后我们把master和**stop drop roll** branch（也就是我们在本地change过的branch）合并成change branch。
![git163.png-45.5kB][218]

然后把master和change branch都推送到fork repo。（Then I'll merge the master branch into my changed branch, and I'll push both the changed branch and the master branch to my fork. I didn't need to push the master branch, but I thought it might be nice.）
![git164.png-163.5kB][219]

**quiz**
![git165.png-101kB][220]

**实操**
1. 复制original repo 的https, 作为remote添加到local。![git167.png-51.2kB][221]
2. 切换到master,然后用`git pull upstream master`更新master![git168.png-39.8kB][222]
3. 此时用`git log`就能看到最新的commit了![git169.png-244.3kB][223]
4. 切换到**stop-drop-roll** branch，也就是我们在local做出了changes的branch。然后和master合并,这样就得到了merge conflict.（记住，想要把A合并到B里，就先checkout到B，在进行merge）![git170.png-41.8kB][224]
5. 得到conflict后打开文件，fix the conflict![git173.png-191.3kB][225]
6. `git add xxxx`,`git commit`,`git push origin stop-drop-roll`，记住最后是把**stop-drop-roll** push 到 origin,也就是fork repo,而不是original repo. 因为你没有权限直接推送给主仓库。![git175.png-57.8kB][226]
7. 然后checkout到master，把master也推送到fork repo![git178.png-50.8kB][227]
8. 好了，解决了conflict，回到全球同性交友网站，发现可爱的绿色button，说明我们能merge pull request了。![git179.png-133.2kB][228]


  [1]: http://static.zybuluo.com/bramble/y5jh5bqna4ryry9c2nwzhpko/git1.png
  [2]: http://static.zybuluo.com/bramble/ikpnucnw46btmtsh3uzd122z/git2.png
  [3]: http://static.zybuluo.com/bramble/n7pg6z6k6keu3hzodz84f220/git3.png
  [4]: http://static.zybuluo.com/bramble/6i2a5jqwdt7keg4pbkattjdb/git4.png
  [5]: http://static.zybuluo.com/bramble/i9quu0kkpi7ktfe4pg7h4fbr/git5.png
  [6]: http://static.zybuluo.com/bramble/p1ja4hn4vyhkg6ohqjs2u0zr/git6.png
  [7]: http://static.zybuluo.com/bramble/adf4udit4h3azszamrbkiymd/git7.png
  [8]: http://static.zybuluo.com/bramble/ipxyl4qqr5ssv3fye6lg00wa/git8.png
  [9]: http://static.zybuluo.com/bramble/qhobdp713os2e6rlchsibabw/git9.png
  [10]: http://static.zybuluo.com/bramble/5izpnylqkpucsqr6bngvumd0/git10.png
  [11]: http://static.zybuluo.com/bramble/ek2hw1yxezbkuciim82nix9e/git11.png
  [12]: http://static.zybuluo.com/bramble/ozu9bfl6byre3muxe2m7axpe/git12.png
  [13]: http://static.zybuluo.com/bramble/4pmi9booqckbxt97x07ggx7i/git13.png
  [14]: http://static.zybuluo.com/bramble/k3q82taiwf4z0qfhewk2njse/git14.png
  [15]: http://static.zybuluo.com/bramble/82psf3zqra5mbb1o8j8ufj8w/git15.png
  [16]: http://static.zybuluo.com/bramble/y5n4078mwuul1x8h8lf68s8h/git16.png
  [17]: http://static.zybuluo.com/bramble/7dslc9z51hdkpvrh0n0p9g2b/git17.png
  [18]: http://static.zybuluo.com/bramble/p00p74q5zhdkzh1vyu38syac/git18.png
  [19]: http://static.zybuluo.com/bramble/sq1cop6b9pf1ase5ftq1ur3i/git19.png
  [20]: http://static.zybuluo.com/bramble/wu0gxbvvzagzgn4j6cw4d2ox/git20.png
  [21]: http://static.zybuluo.com/bramble/n4zb3b9887e1488k60ymaows/git21.png
  [22]: http://static.zybuluo.com/bramble/dqu2zbswowxgot9kv4f9n9u8/git22.png
  [23]: http://static.zybuluo.com/bramble/je60ujhoqxfqoxx7v9vgnfrz/git23.png
  [24]: http://static.zybuluo.com/bramble/4eneueu93dpj74svofcltsq1/git24.png
  [25]: http://static.zybuluo.com/bramble/4ho0knpyjedj353ggen33giw/git25.png
  [26]: http://static.zybuluo.com/bramble/arurf0m8ldlcan9lm78rhd6g/git26.png
  [27]: http://static.zybuluo.com/bramble/hkapu62jnmq8mg8egygbyq7j/git27.png
  [28]: http://static.zybuluo.com/bramble/kk6b2ehyfuv16gbf6yk620rx/git27.png
  [29]: http://static.zybuluo.com/bramble/t2h15li8bi11l1uj1v7r1hrm/git29.png
  [30]: http://static.zybuluo.com/bramble/b5ablxsav02ibeccjnq8t24g/git30.png
  [31]: http://static.zybuluo.com/bramble/kt2oj0x2cyl615omx21e4lhk/git31.png
  [32]: http://static.zybuluo.com/bramble/du0e9e5lpymj47yq7is71chk/git32.png
  [33]: http://static.zybuluo.com/bramble/0zhy52fqmjs7djxoy2zfv0z5/git34.png
  [34]: http://static.zybuluo.com/bramble/oqcjvd811caqhmkzznyvvica/git35.png
  [35]: http://static.zybuluo.com/bramble/z7o7lkhww0rsgdxm6isxjx6n/git36.png
  [36]: http://static.zybuluo.com/bramble/f5szdod7iour3e9scwxfwxlw/git37.png
  [37]: http://static.zybuluo.com/bramble/ayksedcvd6lwa1woiiqounwi/git38.png
  [38]: http://static.zybuluo.com/bramble/2sdhrcu4akp87r6s2n8ni9a0/git39.png
  [39]: http://static.zybuluo.com/bramble/tk15pwtshnq1kjneuh7rnsrb/git40.png
  [40]: http://static.zybuluo.com/bramble/7bo3o9d1etdvdv95rtgxa8y5/git43.png
  [41]: http://static.zybuluo.com/bramble/1n6elxr8klaemzne6cx8fak1/git41.png
  [42]: http://static.zybuluo.com/bramble/2rodkcydugeobuo6l0dd0d5v/git44.png
  [43]: http://static.zybuluo.com/bramble/y1sqsbfc5a7wh8vwrvwj2wmg/git45.png
  [44]: http://static.zybuluo.com/bramble/6jvw1069shi29ha5tnr2za3u/git46.png
  [45]: http://static.zybuluo.com/bramble/nohgcziqcktxegu7yctaklcq/git47.png
  [46]: http://static.zybuluo.com/bramble/exa76odvhsnyo4zub6sp3y18/git48.png
  [47]: http://static.zybuluo.com/bramble/6xx8wnggm42rkwnkbebyzp55/git50.png
  [48]: http://static.zybuluo.com/bramble/lym02n5wcx0rs0t4zvky67sk/git51.png
  [49]: http://static.zybuluo.com/bramble/1kybf26tkqah36v0ub9s9w4g/git52.png
  [50]: http://static.zybuluo.com/bramble/bgjp15xv9p0lpea1oitt09vm/git53.png
  [51]: http://static.zybuluo.com/bramble/mg92uqdxwvvp1t94fctwdq9w/git54.png
  [52]: http://static.zybuluo.com/bramble/1ds7gbk3oixzw6gfug9b8f83/git56.png
  [53]: http://static.zybuluo.com/bramble/i448mawaw74gwl7dvcqie7wd/git57.png
  [54]: http://static.zybuluo.com/bramble/n07efp5qbyu3ovk9r81wnnvy/git58.png
  [55]: http://static.zybuluo.com/bramble/0nlciyw8rnpr7oc8nvaogsxd/git59.png
  [56]: http://static.zybuluo.com/bramble/hjh280183w0s6gf2wk0d3a77/git60.png
  [57]: http://static.zybuluo.com/bramble/39jeuzi6j6decytgvi01xwch/git61.png
  [58]: http://static.zybuluo.com/bramble/1l21cna8vwsrqqwp2pj5oazy/git62.png
  [59]: http://static.zybuluo.com/bramble/lqrbtv8e612hvtoi7e2tyitd/git63.png
  [60]: http://static.zybuluo.com/bramble/ehfhyr5tc082o2kkxxhu485s/git64.png
  [61]: http://static.zybuluo.com/bramble/s4q5dotuvrr6nfl81sqx4o0a/git65.png
  [62]: http://static.zybuluo.com/bramble/ieh1d0v0zmmze8n76zhm05tg/git66.png
  [63]: http://static.zybuluo.com/bramble/6xrrauk78rjpsqrbfllc2jz4/git67.png
  [64]: http://static.zybuluo.com/bramble/jgn8epe0gruc46oireyu3m22/git69.png
  [65]: http://static.zybuluo.com/bramble/nhfeo5pmmh3sath348qp92me/git70.png
  [66]: http://static.zybuluo.com/bramble/w38uauo9vbxlcy3odzooibz0/git71.png
  [67]: http://static.zybuluo.com/bramble/y5jh5bqna4ryry9c2nwzhpko/git1.png
  [68]: http://static.zybuluo.com/bramble/ikpnucnw46btmtsh3uzd122z/git2.png
  [69]: http://static.zybuluo.com/bramble/n7pg6z6k6keu3hzodz84f220/git3.png
  [70]: http://static.zybuluo.com/bramble/6i2a5jqwdt7keg4pbkattjdb/git4.png
  [71]: http://static.zybuluo.com/bramble/i9quu0kkpi7ktfe4pg7h4fbr/git5.png
  [72]: http://static.zybuluo.com/bramble/p1ja4hn4vyhkg6ohqjs2u0zr/git6.png
  [73]: http://static.zybuluo.com/bramble/adf4udit4h3azszamrbkiymd/git7.png
  [74]: http://static.zybuluo.com/bramble/ipxyl4qqr5ssv3fye6lg00wa/git8.png
  [75]: http://static.zybuluo.com/bramble/qhobdp713os2e6rlchsibabw/git9.png
  [76]: http://static.zybuluo.com/bramble/5izpnylqkpucsqr6bngvumd0/git10.png
  [77]: http://static.zybuluo.com/bramble/ek2hw1yxezbkuciim82nix9e/git11.png
  [78]: http://static.zybuluo.com/bramble/ozu9bfl6byre3muxe2m7axpe/git12.png
  [79]: http://static.zybuluo.com/bramble/4pmi9booqckbxt97x07ggx7i/git13.png
  [80]: http://static.zybuluo.com/bramble/k3q82taiwf4z0qfhewk2njse/git14.png
  [81]: http://static.zybuluo.com/bramble/82psf3zqra5mbb1o8j8ufj8w/git15.png
  [82]: http://static.zybuluo.com/bramble/y5n4078mwuul1x8h8lf68s8h/git16.png
  [83]: http://static.zybuluo.com/bramble/7dslc9z51hdkpvrh0n0p9g2b/git17.png
  [84]: http://static.zybuluo.com/bramble/p00p74q5zhdkzh1vyu38syac/git18.png
  [85]: http://static.zybuluo.com/bramble/sq1cop6b9pf1ase5ftq1ur3i/git19.png
  [86]: http://static.zybuluo.com/bramble/wu0gxbvvzagzgn4j6cw4d2ox/git20.png
  [87]: http://static.zybuluo.com/bramble/n4zb3b9887e1488k60ymaows/git21.png
  [88]: http://static.zybuluo.com/bramble/dqu2zbswowxgot9kv4f9n9u8/git22.png
  [89]: http://static.zybuluo.com/bramble/je60ujhoqxfqoxx7v9vgnfrz/git23.png
  [90]: http://static.zybuluo.com/bramble/4eneueu93dpj74svofcltsq1/git24.png
  [91]: http://static.zybuluo.com/bramble/4ho0knpyjedj353ggen33giw/git25.png
  [92]: http://static.zybuluo.com/bramble/arurf0m8ldlcan9lm78rhd6g/git26.png
  [93]: http://static.zybuluo.com/bramble/hkapu62jnmq8mg8egygbyq7j/git27.png
  [94]: http://static.zybuluo.com/bramble/kk6b2ehyfuv16gbf6yk620rx/git27.png
  [95]: http://static.zybuluo.com/bramble/t2h15li8bi11l1uj1v7r1hrm/git29.png
  [96]: http://static.zybuluo.com/bramble/b5ablxsav02ibeccjnq8t24g/git30.png
  [97]: http://static.zybuluo.com/bramble/kt2oj0x2cyl615omx21e4lhk/git31.png
  [98]: http://static.zybuluo.com/bramble/du0e9e5lpymj47yq7is71chk/git32.png
  [99]: http://static.zybuluo.com/bramble/0zhy52fqmjs7djxoy2zfv0z5/git34.png
  [100]: http://static.zybuluo.com/bramble/oqcjvd811caqhmkzznyvvica/git35.png
  [101]: http://static.zybuluo.com/bramble/z7o7lkhww0rsgdxm6isxjx6n/git36.png
  [102]: http://static.zybuluo.com/bramble/f5szdod7iour3e9scwxfwxlw/git37.png
  [103]: http://static.zybuluo.com/bramble/ayksedcvd6lwa1woiiqounwi/git38.png
  [104]: http://static.zybuluo.com/bramble/2sdhrcu4akp87r6s2n8ni9a0/git39.png
  [105]: http://static.zybuluo.com/bramble/tk15pwtshnq1kjneuh7rnsrb/git40.png
  [106]: http://static.zybuluo.com/bramble/7bo3o9d1etdvdv95rtgxa8y5/git43.png
  [107]: http://static.zybuluo.com/bramble/1n6elxr8klaemzne6cx8fak1/git41.png
  [108]: http://static.zybuluo.com/bramble/2rodkcydugeobuo6l0dd0d5v/git44.png
  [109]: http://static.zybuluo.com/bramble/y1sqsbfc5a7wh8vwrvwj2wmg/git45.png
  [110]: http://static.zybuluo.com/bramble/6jvw1069shi29ha5tnr2za3u/git46.png
  [111]: http://static.zybuluo.com/bramble/nohgcziqcktxegu7yctaklcq/git47.png
  [112]: http://static.zybuluo.com/bramble/exa76odvhsnyo4zub6sp3y18/git48.png
  [113]: http://static.zybuluo.com/bramble/6xx8wnggm42rkwnkbebyzp55/git50.png
  [114]: http://static.zybuluo.com/bramble/lym02n5wcx0rs0t4zvky67sk/git51.png
  [115]: http://static.zybuluo.com/bramble/1kybf26tkqah36v0ub9s9w4g/git52.png
  [116]: http://static.zybuluo.com/bramble/bgjp15xv9p0lpea1oitt09vm/git53.png
  [117]: http://static.zybuluo.com/bramble/mg92uqdxwvvp1t94fctwdq9w/git54.png
  [118]: http://static.zybuluo.com/bramble/1ds7gbk3oixzw6gfug9b8f83/git56.png
  [119]: http://static.zybuluo.com/bramble/i448mawaw74gwl7dvcqie7wd/git57.png
  [120]: http://static.zybuluo.com/bramble/n07efp5qbyu3ovk9r81wnnvy/git58.png
  [121]: http://static.zybuluo.com/bramble/0nlciyw8rnpr7oc8nvaogsxd/git59.png
  [122]: http://static.zybuluo.com/bramble/hjh280183w0s6gf2wk0d3a77/git60.png
  [123]: http://static.zybuluo.com/bramble/39jeuzi6j6decytgvi01xwch/git61.png
  [124]: http://static.zybuluo.com/bramble/1l21cna8vwsrqqwp2pj5oazy/git62.png
  [125]: http://static.zybuluo.com/bramble/lqrbtv8e612hvtoi7e2tyitd/git63.png
  [126]: http://static.zybuluo.com/bramble/ehfhyr5tc082o2kkxxhu485s/git64.png
  [127]: http://static.zybuluo.com/bramble/s4q5dotuvrr6nfl81sqx4o0a/git65.png
  [128]: http://static.zybuluo.com/bramble/ieh1d0v0zmmze8n76zhm05tg/git66.png
  [129]: http://static.zybuluo.com/bramble/6xrrauk78rjpsqrbfllc2jz4/git67.png
  [130]: http://static.zybuluo.com/bramble/jgn8epe0gruc46oireyu3m22/git69.png
  [131]: http://static.zybuluo.com/bramble/nhfeo5pmmh3sath348qp92me/git70.png
  [132]: http://static.zybuluo.com/bramble/w38uauo9vbxlcy3odzooibz0/git71.png
  [133]: http://static.zybuluo.com/bramble/1tbg2838i5jvdy3w7spcr9yv/git72.png
  [134]: http://static.zybuluo.com/bramble/07o0h02rhnhkm7tfbxmpx4qu/git73.png
  [135]: http://static.zybuluo.com/bramble/4qd1bwq1n59wg0wvujhml7k5/git74.png
  [136]: http://static.zybuluo.com/bramble/kt7cfed129n2rln0kx7iqaef/git75.png
  [137]: http://static.zybuluo.com/bramble/g91qbjovttmykgvqyspirtfe/git76.png
  [138]: http://static.zybuluo.com/bramble/6b3icm1n2qcsdq7uiqb57241/git77.png
  [139]: http://static.zybuluo.com/bramble/oaucnsrl5bt1hu2pcndf8otl/git78.png
  [140]: http://static.zybuluo.com/bramble/aubxjedg1lrohc4f9heyzr9a/git79.png
  [141]: http://static.zybuluo.com/bramble/rgempvv2s4swijvjd7wn8eba/git80.png
  [142]: http://static.zybuluo.com/bramble/5cvieyx2bm85768jtcr35y0e/git82.png
  [143]: http://static.zybuluo.com/bramble/d3ika71vlxyzqyvlxfrxxhjc/git83.png
  [144]: http://static.zybuluo.com/bramble/5z2nggimdmshtg2v5fs6435m/git85.png
  [145]: http://static.zybuluo.com/bramble/uiu7pfl64khrbzl6ix7x19j3/git86.png
  [146]: http://static.zybuluo.com/bramble/q7tug590kl8oldwsfvee0kdn/git88.png
  [147]: http://static.zybuluo.com/bramble/w0ndjh1zk0lovav8djmmylah/git89.png
  [148]: http://static.zybuluo.com/bramble/svicqfc1gs6vj9hbf9e2lycu/git90.png
  [149]: http://static.zybuluo.com/bramble/7jms6asif4ewif7ljxdj8k59/web110.png
  [150]: http://static.zybuluo.com/bramble/17dc63jnzqgovw4nox45cl3o/web111.png
  [151]: http://static.zybuluo.com/bramble/xnhls9rlsff0dyeu2xo2crv6/web113.png
  [152]: http://static.zybuluo.com/bramble/a93ibel3ecdhme7wltlfa2nw/web114.png
  [153]: http://static.zybuluo.com/bramble/vdjy02gvfqzar0yulhw66n31/web116.png
  [154]: http://static.zybuluo.com/bramble/nk2ep2u9z0yylxzbhgrmurra/web119.png
  [155]: http://static.zybuluo.com/bramble/8ntgqglpwh48ipdqklfnh6u1/web120.png
  [156]: http://static.zybuluo.com/bramble/wkh6m8qwvrp8dw2v46nj28rm/web121.png
  [157]: http://static.zybuluo.com/bramble/dcif5lv90qsmhncmyv7vgqh3/web122.png
  [158]: http://static.zybuluo.com/bramble/8ohvcskwfwsypztrme8uyixr/web123.png
  [159]: http://static.zybuluo.com/bramble/p7z3kkit98507bq6c12gfnut/web124.png
  [160]: http://static.zybuluo.com/bramble/e5xb30zw67oupbpahus9ehyd/git91.png
  [161]: http://static.zybuluo.com/bramble/avg6m1gyfg62yrvj5e16z2ql/git92.png
  [162]: http://static.zybuluo.com/bramble/1qs18lfqka1or1djo997has2/git94.png
  [163]: http://static.zybuluo.com/bramble/h2qtzwteei1bet9iblyogb1i/git97.png
  [164]: http://static.zybuluo.com/bramble/ergmhemubv7hmhg5etx0tdjo/git98.png
  [165]: http://static.zybuluo.com/bramble/0fb9a1jw8d0pkv7l9swedpc4/git100.png
  [166]: http://static.zybuluo.com/bramble/lyxfgxxhwexqdo24qt10y1np/git101.png
  [167]: http://static.zybuluo.com/bramble/ewj56gwl7km259mtdn9amhyj/git102.png
  [168]: http://static.zybuluo.com/bramble/spbhaba57jso3ifwqhcshj1c/git104.png
  [169]: http://static.zybuluo.com/bramble/310chwekvba8q36wzrcjxifn/git105.png
  [170]: http://static.zybuluo.com/bramble/rvtzb07wrmeaifqfhuhjb9dh/git106.png
  [171]: http://static.zybuluo.com/bramble/n4gq8ogtyufrrz940w1jab82/git110.png
  [172]: http://static.zybuluo.com/bramble/me15mi73pgb5kwqyfkoty93g/git111.png
  [173]: http://static.zybuluo.com/bramble/hvqxq0av3q09shn1chuh5lq4/git112.png
  [174]: http://static.zybuluo.com/bramble/xfbcf7yx9eggb8cofu6mrszd/git113.png
  [175]: http://static.zybuluo.com/bramble/if10detn3mtgkonmm9agoh9e/git115.png
  [176]: http://static.zybuluo.com/bramble/oo1a9mwfz7n2zuvefp6dmr1t/git114.png
  [177]: http://static.zybuluo.com/bramble/kiqjoh3kydttub9dkjws4gcy/git117.png
  [178]: http://static.zybuluo.com/bramble/e3hp8slo84l4on0xqe56dpb8/git118.png
  [179]: http://static.zybuluo.com/bramble/9ot5g1fbsaat9zm4wuptk4ek/git119.png
  [180]: http://static.zybuluo.com/bramble/w6chgmfjumn2tbyhpnqj3nx9/git120.png
  [181]: http://static.zybuluo.com/bramble/ecm40gjwwod09054bs5vqenv/git121.png
  [182]: http://static.zybuluo.com/bramble/1612of5326n58vov468wz73p/git122.png
  [183]: http://static.zybuluo.com/bramble/exd9wu3pi20pviheoamsiu0q/git123.png
  [184]: http://static.zybuluo.com/bramble/u995vg574qnnm568ru1yrjlf/git124.png
  [185]: http://static.zybuluo.com/bramble/6oayar6k5v2thgnjo4ajksaz/git126.png
  [186]: http://static.zybuluo.com/bramble/vms5semxh2tgdqvbk7i8m7jj/git127g
  [187]: http://static.zybuluo.com/bramble/xos4ggmsxb8sut10lx6mz8zh/git129.png
  [188]: http://static.zybuluo.com/bramble/ecbprpl1mvs8w87bi66xwkcn/git130.png
  [189]: http://static.zybuluo.com/bramble/v39k08v5oad9h7lezx01gqiv/git131.png
  [190]: http://static.zybuluo.com/bramble/n024s4d8oo5n1q8i560udtgd/git132.png
  [191]: http://static.zybuluo.com/bramble/wvhbiv02jy0zjlew28bx04ya/git133.png
  [192]: http://static.zybuluo.com/bramble/24zdfhklwgp9awkvt7pj2mci/git136.png
  [193]: http://static.zybuluo.com/bramble/8zmwp7ll1kgv7j4siwcp21y1/git137.png
  [194]: http://static.zybuluo.com/bramble/xzcdq0r6idbr59f9po1v584z/git138.png
  [195]: http://static.zybuluo.com/bramble/vgfaf8pc81pbu9ee850snot2/git139.png
  [196]: http://static.zybuluo.com/bramble/oa38uidie9htu9986u9e6q4a/git140.png
  [197]: http://static.zybuluo.com/bramble/64r0mc2k9o0tskxqnjgfgm7s/git141.png
  [198]: http://static.zybuluo.com/bramble/yxgy87f4twkeyp5x9f02swdi/git142.png
  [199]: http://static.zybuluo.com/bramble/yzavl817n7zlnq1j9sexy8m3/git143.png
  [200]: http://static.zybuluo.com/bramble/il3t1j75qanfqlqs6yxeb4zw/git144.png
  [201]: http://static.zybuluo.com/bramble/h6v34pv0l5egzev636i0qfiu/git145.png
  [202]: http://static.zybuluo.com/bramble/y97mlaibhj2zjy9xaifm16t5/git146.png
  [203]: http://static.zybuluo.com/bramble/kcgy35aj4e7xf1xi4sli9nw4/git147.png
  [204]: http://static.zybuluo.com/bramble/98gsqw0g3m6t6kkkbsiv6mrz/git148.png
  [205]: http://static.zybuluo.com/bramble/s3dg3cqwogxovrski8morzjl/git149.png
  [206]: http://static.zybuluo.com/bramble/f5e5t5sw0gg8voq0l6qtme7o/git150.png
  [207]: http://static.zybuluo.com/bramble/t23pwazhpglq6yepnw8t5wio/git151.png
  [208]: http://static.zybuluo.com/bramble/sqy9f52ymez9j1pvee2448bv/git152.png
  [209]: http://static.zybuluo.com/bramble/a6li9rr2wod8cv29n6lc5x4w/git154.png
  [210]: http://static.zybuluo.com/bramble/jr8pvnx8c9na4lc1kmp0jxss/git156.png
  [211]: http://static.zybuluo.com/bramble/anvaiwc5w6p8kydm0y8oyzif/git157.png
  [212]: http://static.zybuluo.com/bramble/6xukg0122yrozmyj8tnvk8m7/git157.png
  [213]: http://static.zybuluo.com/bramble/69ptjckqmx7rt0b342f0gvj6/git159.png
  [214]: http://static.zybuluo.com/bramble/rtofxlz93xbjki4r2itdvai7/git160.png
  [215]: http://static.zybuluo.com/bramble/jlvmsh3tzqys0vw64h63idil/git161.png
  [216]: http://static.zybuluo.com/bramble/ujluxtepgim8oxauu7f55hac/git161.png
  [217]: http://static.zybuluo.com/bramble/84f3bommw9n532t1nn0ol4kt/git162.png
  [218]: http://static.zybuluo.com/bramble/avj2kvicpueugzayxeysuuq6/git163.png
  [219]: http://static.zybuluo.com/bramble/mazd4yfm92nomsboy9qhshuu/git164.png
  [220]: http://static.zybuluo.com/bramble/biaxvb3mxlkfdxd7yiy81671/git165.png
  [221]: http://static.zybuluo.com/bramble/xodax8xuty7kr5bhjrm6c7ug/git167.png
  [222]: http://static.zybuluo.com/bramble/mbt51qswuu0pvt5za0f9f45f/git168.png
  [223]: http://static.zybuluo.com/bramble/u55zlghx42e6civpdye46d9a/git169.png
  [224]: http://static.zybuluo.com/bramble/j3s5u2scdk5jihgtfoj71xqp/git170.png
  [225]: http://static.zybuluo.com/bramble/zi7idkbr2co5cgmy1j9lbpta/git173.png
  [226]: http://static.zybuluo.com/bramble/q9fbawir51yuzgyybvvqhxco/git175.png
  [227]: http://static.zybuluo.com/bramble/edse40bhw3w73gn8ft1p2e8r/git178.png
  [228]: http://static.zybuluo.com/bramble/0g6bub3benjl99hami49fb7r/git179.png