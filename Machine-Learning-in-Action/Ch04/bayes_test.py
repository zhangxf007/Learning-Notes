# -*- coding: utf-8 -*-

from numpy import *
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]   #1 is the bad word, 0 is normal word
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec

'''
input:
trainMatrix: 所有docList里已经变味词向量的矩阵
trainCategory： 对应词向量的标签

output：
p1Vect: 每个word是spam（类别为1）的概率vector
p0Vect: 每个word是ham（类别为0）的概率vector
pAbusive： 先验概率，spam在所有docs中的概率
'''
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix) # there are 6 setences in postingList
    numWords = len(trainMatrix[0]) # 32, there are totally 32 different words in our dic
    pAbusive = sum(trainCategory) / float(numTrainDocs) # 3/6, 3 abusive setences, 6 total setences
    #initialize four param
    p0Num = ones(numWords) # [0, 0, ...., 0], 32 zeros
    p1Num = ones(numWords) # numerator is 分子
    p0Denom = 2.0       # denominator is 分母
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i]) #
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as : ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)


'''
input:
1. vocabList: 所有词的一个list，没有重复的，字典
2. inputSet: 存放有一份邮件词组的一个list，e.g. ['this', 'is', 'a', 'mail']

output:
a word vector(list): 把inputSet里的每一个词和vocabList里作对比，计算每个词出现的频率
e.g. [0, 0, 0, 1, 0, 2.....]
'''


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

'''
docList 存放有50份电子邮件，每一封是一个list[]。docList的总体架构是[["mail1"], ["mail2"].....]
然后我们用这个docList来构建一个没有重复单词的词汇表list: vocabList

'''
def spamTest():
    docList=[]
    classList = []
    fullText = []
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList) # create vocabulary

    trainingSet = range(50)
    testSet = [] # create test set
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])

    trainMat = []
    trainClasses = []
    for docIndex in trainingSet: # train the classifier (get probiblity) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:    #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error", docList[docIndex]
    print 'the error rate is: ', float(errorCount)/len(testSet)
'''
input:
vocabList: 词汇表，无重复单词
fullText: 所有单词汇总的list，有重复单词

output：

数据类型是dict, 单词本身是key, 单词出现的次数是value
返回出现频率最高的三十个单词。

我用counter class 更简洁地实现了这个功能，而且只用到了fullText
'''


def calcMostFreq(vocabList,fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]


'''
operator.itemgetter函数
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号），下面看例子。
a = [1,2,3]
>>> b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
>>> b(a)
2
>>> b=operator.itemgetter(1,0)   //定义函数b，获取对象的第1个域和第0个的值
>>> b(a)
(2, 1)
要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。

key为函数，指定取待排序元素的哪一项进行排序，函数用上面的例子来说明，代码如下：
sorted(students, key=lambda student : student[2])
key指定的lambda函数功能是去元素student的第三个域（即：student[2]），
因此sorted排序时，会以students所有元素的第三个域来进行排序。

有了上面的operator.itemgetter函数，也可以用该函数来实现，例如要通过student的第三个域排序，可以这么写：
sorted(students, key=operator.itemgetter(2))
sorted函数也可以进行多级排序，例如要根据第二个域和第三个域进行排序，可以这么写：
sorted(students, key=operator.itemgetter(1,2)) 即先跟句第二个域排序，再根据第三个域排序。
（4）reverse参数就不用多说了，是一个bool变量，表示升序还是降序排列，默认为false（升序排列），定义为True时将按降序排列。

'''

# counter class enhanced version for calcMostFreq
def calcMostFreq_counter(fullText):
    from collections import Counter
    word_dict = Counter(fullText)
    return word_dict.most_common(30)

def localWords(feed0, feed1):
    import feedparser
    docList = []
    classList = []
    fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList) # create vocabulary
    top30Words = calcMostFreq_counter(fullText)
    for pairW in top30Words:    # remove top 30 words
        if pairW[0] in vocabList:
            vocabList.remove(pairW[0])
    trainingSet = range(2*minLen)
    testSet = []    #create test set
    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:    #train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:    #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount)/len(testSet)
    return vocabList, p0V, p1V

def getTopWords(ny, sf):
    import operator
    vocabList, p0V, p1V = localWords(ny, sf)
    topNY = []
    topSF = []
    for i in range(len(p0V)):
        if p0V[i] > -6.0:
            topSF.append((vocabList[i], p0V[i]))
        if p1V[i] > -6.0:
            topNY.append((vocabList[i], p1V[i]))
    sortedSF = sorted(topSF, key = lambda pair:pair[1], reverse = True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key = lambda pair:pair[1], reverse = True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    for item in sortedNY:
        print item[0]
