import numpy as np
import random

def generate_random_dataset(tests = 4, times = 100, dim = [10, 100, 1000, 10000]):
    if tests != len(dim):
        raise ValueError('La dimenzione del array dim deve combaciare con il numero di test da eseguire indicati dalla variabile tests')
    dim = np.sort(dim)
    random_dataset = []
    for i in range(tests):
        test = np.array([[random.randint(0, dim[i]) for _ in range(dim[i])] for _ in range(times)])
        random_dataset.append(test)
    return random_dataset

def generate_random_high_repetitions_dataset(tests = 4, times = 100, dim = [10, 100, 1000, 10000]):
    if tests != len(dim):
        raise ValueError('La dimenzione del array dim deve combaciare con il numero di test da eseguire indicati dalla variabile tests')
    dim = np.sort(dim)
    random_dataset = []
    for i in range(tests):
        test = np.array([[random.randint(0, dim[i]/2) for _ in range(dim[i])] for _ in range(times)])
        random_dataset.append(test)
    return random_dataset

def generate_unbalanced_tree_dataset(tests = 4, terms = 100, dim = [10, 100, 1000, 10000]):
    dataset = generate_random_high_repetitions_dataset(tests, terms, dim)
    for i in dataset:
        for j in i:
            j.sort()
    return dataset
