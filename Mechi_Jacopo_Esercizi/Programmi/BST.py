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
        height = 0  # Inizializza l'altezza a 0
        y = None
        x = self.root
        while x != None:
            height += 1  # Incrementa l'altezza ad ogni passaggio
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
        return height  # Restituisci l'altezza raggiunta dall'albero dopo l'inserimento

    def booleanInsert(self, z):
        height = 0  # Inizializza l'altezza a 0
        y = None
        x = self.root
        while x != None:
            height += 1  # Incrementa l'altezza ad ogni passaggio
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
        return height  # Restituisci l'altezza raggiunta dall'albero dopo l'inserimento

    def listInsert(self, z):
        height = 0  # Inizializza l'altezza a 0
        y = None
        x = self.root
        while x != None:
            height += 1  # Incrementa l'altezza ad ogni passaggio
            y = x
            if z.key ==  x.key:
                z.duplicate = x
                if x != self.root:
                    z.p = x.p
                if x.left != None:
                    x.left.p = z
                if x.right != None:
                    x.right.p = z
                return height
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
        return height  # Restituisci l'altezza raggiunta dall'albero dopo l'inserimento

    def insert(self, z, insertType):
        if insertType == "normal":
            height = self.normalInsert(Node(z))
        elif insertType == "boolean":
            height = self.booleanInsert(Node(z))
        elif insertType == "list":
            height = self.listInsert(Node(z))
        else:
            raise ValueError('insertType deve essere "normal", "boolean" o "list"')
        return height

    def search(self, k):
        x = self.root
        height = 0  # Inizializza l'altezza a 0
        while x != None and k != x.key:
            height += 1  # Incrementa l'altezza ad ogni passo
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x, height  # Restituisci sia il nodo trovato che l'altezza
