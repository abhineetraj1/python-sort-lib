from collections import defaultdict

class arr_sort:
    #Quick Sort is a divide-and-conquer algorithm that partitions an array into two parts, then recursively sorts each part.
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    #Merge Sort is a divide-and-conquer algorithm that recursively splits an array into two halves until each subarray contains only one element.
    def mergesort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = mergesort(left)
        right = mergesort(right)
        return merge(left, right)
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    #Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    #Selection Sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part.
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    #Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.
    def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    #Shell Sort is an efficient sorting algorithm that is a generalization of Insertion Sort.
    def shell_sort(arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j-gap] > temp:
                    arr[j] = arr[j-gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr
    #Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.
    def heap_sort(arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr
    #Counting Sort is an algorithm for sorting a collection of objects based on the keys that the objects possess.
    def counting_sort(arr):
        n = len(arr)
        count = [0] * (max(arr)+1)
        output = [0] * n
        for i in range(n):
            count[arr[i]] += 1
        for i in range(1, max(arr)+1):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            output[count[arr[i]]-1] = arr[i]
            count[arr[i]] -= 1
        for i in range(n):
            arr[i] = output[i]
        return arr
    #Bucket Sort is a sorting algorithm that divides the input into several buckets.
    def bucket_sort(arr):
        bucket = []
        for i in range(len(arr)):
            bucket.append([])
        for j in arr:
            index = int(10*j)
            bucket[index].append(j)
        for i in range(len(arr)):
            bucket[i] = insertion_sort(bucket[i])
        k = 0
        for i in range(len(arr)):
            for j in range(len(bucket[i])):
                arr[k] = bucket[i][j]
                k += 1
        return arr
    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            temp = bucket[i]
            j = i-1
            while j >= 0 and temp < bucket[j]:
                bucket[j+1] = bucket[j]
                j -= 1
            bucket[j+1] = temp
        return bucket
    #A topological graph, also known as a planar graph, is a type of graph that can be drawn in the plane without any of its edges crossing each other. In other words, it is a graph that can be represented by a set of points in the plane (called vertices) and a set of curves connecting these points (called edges), such that no two edges intersect except at their endpoints.
    class TGraph:
        def __init__(self, vertices):
            self.graph = defaultdict(list)
            self.V = vertices
        def add_edge(self, u, v):
            self.graph[u].append(v)
        def topological_sort(self):
            visited = [False] * self.V
            stack = []
            for i in range(self.V):
                if not visited[i]:
                    self.topological_sort_util(i, visited, stack)
            return stack[::-1]
        def topological_sort_util(self, v, visited, stack):
            visited[v] = True
            for i in self.graph[v]:
                if not visited[i]:
                    self.topological_sort_util(i, visited, stack)
            stack.append(v)
    #To use the Bellman-Ford Algorithm implementation, create a Graph object and add edges to it using the add_edge() method. Then, call the bellman_ford() method with the starting vertex as argument.
    class BGraph:
        def __init__(self, vertices):
            self.V = vertices
            self.graph = []
        def add_edge(self, u, v, w):
            self.graph.append([u, v, w])
        def bellman_ford(self, start):
            dist = [float("inf")] * self.V
            dist[start] = 0
            for i in range(self.V - 1):
                for u, v, w in self.graph:
                    if dist[u] != float("inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    print("Negative cycle detected")
                    return
            print("Vertex \t Distance from Source")
            for i in range(self.V):
                print(f"{i}\t{dist[i]}")

# Made by Abhineet Raj (https://github.com/abhineetraj1)
