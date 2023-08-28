import random

class Node:
    def __init__(self, key):
        self.key = key
        self.duplicate = None
        self.b = True
        self.left = None
        self.right = None
        self.p = None

class Tree:
    def __init__(self, key):
        self.root = Node(key)

    def normalInsert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def booleanInsert(self, z):
        y = None
        x = self.root
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
            self.root = z
        elif z.key == y.key:
            if y.b:
                y.left = z
            else:
                y.right = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def listInsert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key ==  x.key:
                z.duplicate = x
                if x != self.root:
                    z.p = x.p
                if x.left != None:
                    x.left.p = z
                if x.right != None:
                    x.right.p = z
                return
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def randomInsert(self, z):
        y = None
        x = self.root
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
            self.root = z
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

    def insert(self, z, insertType):
        if insertType == "normal":
            self.normalInsert(Node(z))
        elif insertType == "boolean":
            self.booleanInsert(Node(z))
        elif insertType == "list":
            self.listInsert(Node(z))
        elif insertType == "random":
            self.randomInsert(Node(z))
        else:
            raise ValueError('insertType deve essere "normal", "boolean", "list" o "random"')

    def search(self, x, k):
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def _print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left is not None or node.right is not None:
                self._print_tree(node.left, level + 1, "L--- ")
                self._print_tree(node.right, level + 1, "R--- ")

    def print_tree(self):
        self._print_tree(self.root)




