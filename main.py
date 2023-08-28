import benchmark as bm
import datasets as ds
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

# Dataset generation
dim = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
randomDataset = ds.generate_random_dataset(len(dim), 500, dim)
highRepetitionsDataset = ds.generate_random_high_repetitions_dataset(len(dim), 500, dim)
worstCaseDataset = ds.generate_unbalanced_tree_dataset(len(dim), 500, dim)

# Benchmarks
randomNormalInsertionTimes, randomNormalSearchTimes = bm.benchmark(randomDataset, "normal")
randomBooleanInsertionTimes, randomBooleanSearchTimes = bm.benchmark(randomDataset, "boolean")
randomListInsertionTimes, randomListSearchTimes = bm.benchmark(randomDataset, "list")
highRepetitionsNormalInsertionTimes, highRepetitionsNormalSearchTimes = bm.benchmark(highRepetitionsDataset, "normal")
highRepetitionsBooleanInsertionTimes, highRepetitionsBooleanSearchTimes = bm.benchmark(highRepetitionsDataset, "boolean")
highRepetitionsListInsertionTimes, highRepetitionsListSearchTimes = bm.benchmark(highRepetitionsDataset, "list")    
worstNormalInsertionTimes, worstNormalSearchTimes = bm.benchmark(worstCaseDataset, "normal")
worstBooleanInsertionTimes, worstBooleanSearchTimes = bm.benchmark(worstCaseDataset, "boolean")
worstListInsertionTimes, worstListSearchTimes = bm.benchmark(worstCaseDataset, "list")

# Plots and tables
plt.figure(num = 1, figsize=(7, 7))
plt.plot( dim, randomNormalInsertionTimes, label='Normal RD')
plt.plot( dim, highRepetitionsNormalInsertionTimes, label='Normal HRD')
plt.plot( dim, randomBooleanInsertionTimes, label='Boolean RD')
plt.plot( dim, highRepetitionsBooleanInsertionTimes, label='Boolean HRD')
plt.plot( dim, randomListInsertionTimes, label='List RD')
plt.plot( dim, highRepetitionsListInsertionTimes, label='List HRD')
plt.plot( dim, np.array([math.log(dim[i],2)*170 for i in range(0, len(dim))]), label='h = lg(n)')
plt.title('RD and HRD insertion times')
plt.xlabel('Number of nodes n')
plt.ylabel('Time in ns')
plt.legend(loc="upper left")
plt.savefig('Chiavi duplicate in alberi binari di ricerca/Resources/ABR_Resources/RDeHRDinsertion.png')

plt.figure(num = 2, figsize=(7, 7))
plt.plot( dim, worstNormalInsertionTimes, label='Normal WCD')
plt.plot( dim, worstBooleanInsertionTimes, label='Boolean WCD')
plt.plot( dim, worstListInsertionTimes, label='List WCD')
plt.plot( dim, np.array([dim[i]*30 for i in range(0, len(dim))]), label='n')
plt.title('Worst case insertion times')
plt.xlabel('Number of nodes n')
plt.ylabel('Time in ns')
plt.legend(loc="upper left")
plt.savefig('Chiavi duplicate in alberi binari di ricerca/Resources/ABR_Resources/WDinsertion.png')

plt.figure(num = 3, figsize=(7, 7))
plt.plot( dim, randomNormalSearchTimes, label='Normal RD')
plt.plot( dim, highRepetitionsNormalSearchTimes, label='Normal HRD')
plt.plot( dim, randomBooleanSearchTimes, label='Boolean RD')
plt.plot( dim, highRepetitionsBooleanSearchTimes, label='Boolean HRD')
plt.plot( dim, randomListSearchTimes, label='List RD')
plt.plot( dim, highRepetitionsListSearchTimes, label='List HRD')
plt.plot( dim, np.array([math.log(dim[i],2)*170 for i in range(0, len(dim))]), label='h = lg(n)')
plt.title('RD and HRD search times')
plt.xlabel('Number of nodes n')
plt.ylabel('Time in ns')
plt.legend(loc="upper left")
plt.savefig('Chiavi duplicate in alberi binari di ricerca/Resources/ABR_Resources/RDeHRDsearch.png')

plt.figure(num = 4, figsize=(7, 7))
plt.plot( dim, worstNormalSearchTimes, label='Normal WCD')
plt.plot( dim, worstBooleanSearchTimes, label='Boolean WCD')
plt.plot( dim, worstListSearchTimes, label='List WCD')
plt.plot( dim, np.array([dim[i]*30 for i in range(0, len(dim))]), label='n')
plt.title('Worst case search times')
plt.xlabel('Number of nodes n')
plt.ylabel('Time in ns')
plt.legend(loc="upper left")
plt.savefig('Chiavi duplicate in alberi binari di ricerca/Resources/ABR_Resources/WDsearch.png')
# data = {'dataset dimension' : dim, 'random': randomNormalInsertionTimes, 'high repetitions': highRepetitionsNormalInsertionTimes, 'worst case': worstNormalInsertionTimes}
# df = pd.DataFrame(data)  
# print(df)  

# print(randomNormalInsertionTimes)
# print(randomBooleanInsertionTimes)
# print(randomListInsertionTimes)
# print(randomRandomInsertionTimes) 
# print(highRepetitionsNormalInsertionTimes)
# print(highRepetitionsBooleanInsertionTimes)
# print(highRepetitionsListInsertionTimes)
# print(highRepetitionsRandomInsertionTimes)
# print(worstNormalInsertionTimes)
# print(worstBooleanInsertionTimes)
# print(worstListInsertionTimes)
# print(worstRandomInsertionTimes)





