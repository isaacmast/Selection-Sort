import random, timeit

'''
Determines the execution time of a selectionsort algorithm, given an 
array of random integers. I do not own some of this code. All rigths 
and original code of the wrapper and wrapped functions belong to 
Xiaonuo Gantan from Python Central. 
'''

def wrapper(func, *args, **kwargs):
    '''
    Wrapper function to wrap selectionsort function in to determine
    the execution time of the algorithm.
    '''
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def selectionsort(array):
    '''
    Selectionsort algorithm for sorting an array of integers
    Input: An array of integers, array
    Output: The sorted array of integers
    '''
    for i in range(len(array)):
        minPos = i
        for j in range(i, len(array)):
            if array[j] < array[minPos]:
                minPos = j
        temp = array[i]
        array[i] = array[minPos]
        array[minPos] = temp
    return array

arraySize = 10
array = random.sample(range(1, 100), arraySize)
wrapped = wrapper(selectionsort, array)
print selectionsort(array)
print
print timeit.timeit(wrapped, number = 1000)
