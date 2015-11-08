import random, string, timeit

'''
Determines the execution time of a selectionsort algorithm, given an 
array of random strings. All rigths and original code of the wrapper 
and wrapped functions belong to Xiaonuo Gantan from Python Central at 
"pythoncentral.io/time-a-python-function/". 
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

#Assign variables
array = []
ARRAYLENGTH = 2000
STRINGLENGTH = 10

#Generate array, length ARRAYLENGTH, of random strings, 
#length STRINGLENGTH
for i in range(0, ARRAYLENGTH):
	array.append(''.join(random.choice(string.lowercase) for i in range(STRINGLENGTH)))

#Wrap algorithm to determine execution time
wrapped = wrapper(selectionsort, array)

#Determine basic operation execution count
print selectionsort(array)

#Determine execution time of algorithm
print (timeit.timeit(wrapped, number = 1000)) / 1000
