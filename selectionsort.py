import random, string, timeit

'''
Determines the execution time of a selectionsort algorithm, given an 
array of random strings. I do not own some of this code. All rigths 
and original code of the wrapper and wrapped functions belong to 
Xiaonuo Gantan from Python Central at 
pythoncentral.io/time-a-python-function/. 
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
    Selectionsort algorithm for sorting an array of strings
    Input: An array of strings, array
    Output: The sorted array of strings
    '''
	count = 0
    for i in range(len(array)):
		minPos = i
		for j in range(i, len(array)):
			count += 1
			if array[j] < array[minPos]:
				minPos = j
		temp = array[i]
		array[i] = array[minPos]
		array[minPos] = temp
	return count

array = []
ARRAYLENGTH = 1000
STRINGLENGTH = 10
for i in range(0, ARRAYLENGTH):
	array.append(''.join(random.choice(string.lowercase) for i in range(STRINGLENGTH)))
wrapped = wrapper(selectionsort, array)
print selectionsort(array)
print timeit.timeit(wrapped, number = 1000)
