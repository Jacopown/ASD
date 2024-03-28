import BST as bst
from time import perf_counter_ns as timer
import random
import time

def createTree(dataset, insertionType):
    tree = bst.Tree(dataset[0])
    for i in dataset[1:-1]:
        tree.insert(i, insertionType)
    return tree

def benchmark(dataset, insertionType):
    insertionTimes = []
    searchTimes = []
    for i in range(0,len(dataset)):
        time.sleep(0.1)
        totalInsertionTime = 0
        totalSearchTime = 0
        for j in range(0, len(dataset[i])):
            T = createTree(dataset[i][j], insertionType)
            start = timer()
            T.insert(dataset[i][j][-1], insertionType)
            end = timer()
            insertionTime = end-start
            totalInsertionTime += insertionTime
            start = timer()
            x = random.choice(dataset[i][j])
            T.search(x)
            end = timer()
            searchTime = end-start
            totalSearchTime += searchTime
        insertionTimes.append(totalInsertionTime/(len(dataset[i])))
        searchTimes.append(totalSearchTime/(len(dataset[i])))
    return insertionTimes, searchTimes

def benchmark_nodes(dataset, insertionType):
    insertionHeights = []
    searchHeights = []
    for i in range(len(dataset)):
        time.sleep(0.1)
        totalInsertionHeight = 0
        totalSearchHeight = 0
        for j in range(len(dataset[i])):
            T = createTree(dataset[i][j], insertionType)
            insertionHeight = T.insert(dataset[i][j][-1], insertionType) 
            totalInsertionHeight += insertionHeight
            x = random.choice(dataset[i][j])
            node_found, searchHeight = T.search(x)  # Ottiene il nodo e l'altezza durante la ricerca
            totalSearchHeight += searchHeight
        insertionHeights.append(totalInsertionHeight / len(dataset[i]))
        searchHeights.append(totalSearchHeight / len(dataset[i]))
    return insertionHeights, searchHeights

