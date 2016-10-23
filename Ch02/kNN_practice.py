from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1],[1.0, 1.0],[0.0],[0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, label

def classify0(inX, dataSet, labels, k):
    #The shape attribute for numpy arrays returns the dimensions of the array. If Y has n rows and m columns, then Y.shape is (n,m). So Y.shape[0] is n.
    dataSetSize = dataSet.shape[0]
    
    #tile把inX复制为(4,1)的矩阵形式，减去dataSet即点（0，0）到group里四个点的距离
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # 插值的平方
    sqDiffMat = diffMat**2
    #axis=1，插值
    sqDistances = sqDissMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems()