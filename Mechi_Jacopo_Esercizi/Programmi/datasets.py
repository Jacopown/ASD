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

def generate_worst_dataset(tests = 4, times = 100, dim = [10, 100, 1000, 10000]):
    if tests != len(dim):
        raise ValueError('La dimenzione del array dim deve combaciare con il numero di test da eseguire indicati dalla variabile tests')
    dim = np.sort(dim)
    worst_dataset = []
    for i in range(tests):
        test = np.array([[j for j in range(dim[i])] for _ in range(times)])
        worst_dataset.append(test)
    return worst_dataset
