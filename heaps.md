# Heaps, Priority queues and Heapsort

# Heaps
Heaps data structures are complete binary trees that makes it apt to be implemented as arrays.
![heap as binary tree and array implementation](max-heap.jpg)
Image source: Introduction to algorithms. Cormen Et, al

## Aranging heap elements in the array
For a given index i in a 0 indexed array, it's parent and children nodes can be retrieved as follows

- Parent(i) = i//2
- leftChild(i) = 2*i + 1
- rightChild(i) = 2*i + 2

## Types of binary heaps
All the nodes in the heap should satisfy the heap property specified by the following types of heap

##### Max heap
- **MaxHeap Property** : For a given node its value is less than or equal to it's parent.
  <p style="text-align: center;"> arr[Parent(i)] >= arr[i] </p>
- For a given node all nodes in the subtree have values at most it's value
- The largest value in the heap is situated at the root
- Max heap is generally used in HeapSort applications
##### Min heap
- **MinHeap Property** : For a give node its value is greater than or equal to it's parent.
  <p style="text-align: center;"> arr[Parent(i)] <= arr[i] </p>
- For a given node all nodes in the subtree have values at min it's value
- The smallest value in the heap is present at the root
- Min heap is generally used in priority queue applications

## Heap operations
### Maintaining the heap property
**max_heapify** : In a max heap, function to main the MaxHeap Property. If the given node has value less than it's children then the procedure identifies the child node with largest value and swaps the value of the given node. The max_heapify is then recursively called on the sub trees with the swapped value. max_heapify percolates the values from top to bottom.

    max_heapify(arr, i):
        l_i = 2*i+1
        r_i = 2*i+2
        largest = i

        if l_i <= len(arr)-1 and arr[l_i] > arr[largest]:
            largest = l_i
        elif r_i <= len(arr)-1 and arr[r_i] > arr[largest]:
            largest = r_i            

        if largest != i:
            swap(arr[i], arr[largest])
            max_heapify(arr, largest)

*Runtime analysis of max_heapify* \
In the worst case the heapyify function will traverse through from root to bottom leaf node across the levels in the heap. For a heap with number of nodes = n, total levels in the trees = logn.
Runtime will be in the order of O(logn)

**Building the heap** : 

# Priority Queueus

# Heap sort
