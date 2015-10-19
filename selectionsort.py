import random, timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def selectionsort(array):
    for i in range(len(array)):
        minPos = i
        for j in range(i, len(array)):
            if array[j] < array[minPos]:
                minPos = j
        temp = array[i]
        array[i] = array[minPos]
        array[minPos] = temp

arraySize = 50
array = random.sample(range(1, 100), arraySize)
wrapped = wrapper(selectionsort, array)
print timeit.timeit(wrapped, number = 1000)
