# Python sorting and graph alogrithms
![alt text](https://github.com/abhineetraj1/python-sort-lib/blob/main/sort.png?raw=true)
This repository contains Python implementation of graph and sorting algorithms

## Installation

This program requires Python 3 to run. You can download Python 3 from the official website - https://www.python.org/downloads/
Usage
## Sorting algorithms
### Quick Sort
*	Quick Sort is a divide-and-conquer algorithm that partitions an array into two parts, then recursively sorts each part. It selects a pivot element and rearranges the array so that all elements less than the pivot are moved to its left and all elements greater than the pivot are moved to its right. The pivot element is then placed in its final position, and the two subarrays to its left and right are recursively sorted.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.quicksort(array)

print(w)
```
### Merge Sort
*	Merge Sort is a divide-and-conquer algorithm that recursively splits an array into two halves until each subarray contains only one element. It then merges the two subarrays by comparing their elements, resulting in a sorted array.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.mergesort(array)

print(w)
```
*	Merge
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.mergesort(0,5)

print(w)
```

### Bubble Sort
*	Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.bubble_sort(array)

print(w)
```

### Selection Sort
*	Selection Sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. This process is repeated until the entire array is sorted.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.selection_sort(array)

print(w)
```

### Insertion Sort
*	Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It iterates through the array, comparing each element with the previous elements and inserting the current element into its correct position in the sorted part of the array.
*	Code
```
from sortlib import *

array=[1,2,3,4]
arr1 = [0.675, 0.876, 0.345, 0.9875, 0.0123, 0.599]

w = arr_sort.insertion_sort(array)
w1 = arr_sort.insertion_sort_bucket(arr1)

print(w1)
print(w)
```
### Shell Sort
*	Shell Sort is an efficient sorting algorithm that is a generalization of Insertion Sort. It sorts elements at a certain gap distance, then reduces the gap distance until it reaches 1, at which point the algorithm is identical to Insertion Sort.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.shell_sort(array)

print(w)
```

### Heap Sort
*    Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It starts by building a heap from the input data, then repeatedly extracts the minimum element from the heap and places it at the end of the sorted array.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.heap_sort(array)

print(w)
```

### Counting Sort
*    Counting Sort is an algorithm for sorting a collection of objects based on the keys that the objects possess. It operates by counting the number of objects that have each distinct key value, and using arithmetic on those counts to determine the positions of each key value in the output sequence.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.counting_sort(array)

print(w)
```

### Bucket Sort
*    Bucket Sort is a sorting algorithm that divides the input into several buckets. Each bucket is then sorted using another algorithm or by recursively applying the bucket sorting algorithm. The sorted buckets are then concatenated to obtain the final sorted output.
*	Code
```
from sortlib import *

array=[1,2,3,4]
w = arr_sort.bucket_sort(array)

print(w)
```

## Graph Alogrithms

### Bellman-Ford Algorithm

*	To use the Bellman-Ford Algorithm implementation, create a Graph object and add edges to it using the add_edge() method. Then, call the bellman_ford() method with the starting vertex as argument.
*	Code
```
from sortlib import*

sortlib.BGraph(vertices)
sortlib.add_edge(x,y,z)
sortlib.bellman_ford(start_index)
```
### Topological graph

*	A topological graph, also known as a planar graph, is a type of graph that can be drawn in the plane without any of its edges crossing each other. In other words, it is a graph that can be represented by a set of points in the plane (called vertices) and a set of curves connecting these points (called edges), such that no two edges intersect except at their endpoints.

*	Code
```
from sortlib import *

sortlib.TGraph(vertices)
sortlib.add_edge(x,y)
sortlib.topological_sort()
sortlib.topological_sort_util(x, visited, stack)
```

## Contributing

If you would like to contribute to this project, please create a pull request.
License

## Languages and tools used

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Author
*	[abhineetraj1](http://github.com/abhineetraj1)
