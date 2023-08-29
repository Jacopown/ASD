import BST as bst
from time import perf_counter_ns as timer
import random

def createTree(dataset, insertionType):
    tree = bst.Tree(dataset[0])
    for i in dataset[1:-1]:
        tree.insert(i, insertionType)
    return tree

def benchmark(dataset, insertionType):
    insertionTimes = []
    searchTimes = []
    for i in range(0,len(dataset)):
        totalInsertionTime = 0
        maxInsertionTime = 0
        totalSearchTime = 0
        maxSearchTime = 0
        for j in range(0, len(dataset[i])):
            T = createTree(dataset[i][j], insertionType)
            start = timer()
            T.insert(dataset[i][j][-1], insertionType)
            end = timer()
            insertionTime = end-start
            if insertionTime > maxInsertionTime: maxInsertionTime = insertionTime
            totalInsertionTime += insertionTime
            start = timer()
            x = random.choice(dataset[i][j])
            T.search(x)
            end = timer()
            searchTime = end-start
            if searchTime > maxSearchTime: maxSearchTime = searchTime
            totalSearchTime += searchTime
        insertionTimes.append((totalInsertionTime-maxInsertionTime)/(len(dataset[i])-1))
        searchTimes.append((totalSearchTime-maxSearchTime)/(len(dataset[i])-1))
    return insertionTimes, searchTimes
