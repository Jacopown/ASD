import random

class Node:
    def __init__(self, key = None):
        self.key = key
        self.elements = 0
        self.b = True
        self.left = None
        self.right = None
        self.p = None

class Tree:
    def __init__(self, key = None):
        if key is None:
            self.root = None
        else:
            self.root = Node(key)

def normalTreeInsert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def booleanTreeInsert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key ==  x.key:
            x.b = not x.b
            if x.b:
                x = x.left
            else:
                x = x.right
        elif z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key == y.key:
        if x.b:
            y.left = z
        else:
            y.right = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def listTreeInsert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key ==  x.key:
            x.elements += 1
            return
        elif z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def randomTreeInsert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key ==  x.key:
            n = random.randint(0, 1)
            if n == 0:
                x = x.left
            else:
                x = x.right
        elif z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key == y.key:
        n = random.randint(0, 1)
        if n == 0:
            y.left = z
        else:
            y.right = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

