import BST as bst
import benchmark as bm
import datasets as ds
import matplotlib.pyplot as plt

randomDataset = ds.generate_random_dataset()
highRepetitionsDataset = ds.generate_random_high_repetitions_dataset()
worstCaseDataset = ds.generate_unbalanced_tree_dataset()

randomNormalInsertionTimes, randomNormalSearchTimes = bm.benchmark(randomDataset, "normal")
# randomBooleanInsertionTimes, randomBooleanSearchTimes = bm.benchmark(randomDataset, "boolean")
# randomListInsertionTimes, randomListSearchTimes = bm.benchmark(randomDataset, "list")
# randomRandomInsertionTimes, randomRandomSearchTimes = bm.benchmark(randomDataset, "random")
highRepetitionsNormalInsertionTimes, highRepetitionsNormalSearchTimes = bm.benchmark(highRepetitionsDataset, "normal")
# highRepetitionsBooleanInsertionTimes, highRepetitionsBooleanSearchTimes = bm.benchmark(highRepetitionsDataset, "boolean")
# highRepetitionsListInsertionTimes, highRepetitionsListSearchTimes = bm.benchmark(highRepetitionsDataset, "list")    
# highRepetitionsRandomInsertionTimes, highRepetitionsRandomSearchTimes = bm.benchmark(highRepetitionsDataset, "random")
worstNormalInsertionTimes, worstNormalSearchTimes = bm.benchmark(worstCaseDataset, "normal")
# worstBooleanInsertionTimes, worstBooleanSearchTimes = bm.benchmark(worstCaseDataset, "boolean")
# worstListInsertionTimes, worstListSearchTimes = bm.benchmark(worstCaseDataset, "list")
# worstRandomInsertionTimes, worstRandomSearchTimes = bm.benchmark(worstCaseDataset, "random")

plt.figure(num = 3, figsize=(7, 7))
plt.plot( [10, 100, 1000, 10000], randomNormalInsertionTimes, label='quicksort')
plt.plot( [10, 100, 1000, 10000], highRepetitionsNormalInsertionTimes, label='boolean')
plt.plot( [10, 100, 1000, 10000], worstNormalInsertionTimes, label='list')
plt.legend(loc="upper left")
plt.savefig('my_plot.png')
# plt.show()

print(randomNormalInsertionTimes)
# print(randomBooleanInsertionTimes)
# print(randomListInsertionTimes)
# print(randomRandomInsertionTimes) 
print(highRepetitionsNormalInsertionTimes)
# print(highRepetitionsBooleanInsertionTimes)
# print(highRepetitionsListInsertionTimes)
# print(highRepetitionsRandomInsertionTimes)
print(worstNormalInsertionTimes)
# print(worstBooleanInsertionTimes)
# print(worstListInsertionTimes)
# print(worstRandomInsertionTimes)





