# Heaps, Priority queues and Heapsort

# Heaps
Heap data structures are complete binary trees that makes it apt to be implemented as arrays.
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
In the worst case the heapyify function will traverse through from root to bottom leaf node across the levels in the heap. For a heap with number of nodes = n, total levels in the trees = $logn$.
Runtime will be in the order of $O(logn)$

**Building the heap** : A heap is built by calling the max_heapify on elements as they are entered into the array in a bottom up fashion i.e starting from the leaf nodes. At each step the *MaxHEap Property* is to be maintained. Since we insert the leaf nodes first, and all leaf nodes fullfil the *MaxHeap Property* by default. Hence the max_heapify procedure is called for the internal nodes instead. As per the peroperty of complete binary tree, $N_i = (N-1)/2$

    build_max_heap(arr):
        N = len(arr)
        for i in range(N/2, 0, -1):
            max_heapify(arr, i)
            
*Runtime analysis of build_max_heap* \
<ins>Upper bound analysis</ins> : The procedure calls max_heapify n/2 times which takes $logn$ in itself to run. Hence, the upper bound is $O(nlogn)$.\

<ins>Assympototically tight analysis</ins> : If we observe carefully the max_heapify takes O(logn) or O(h). The height of the tree is changing for each node. h=0 for all leaf nodes, h = 1 for all nodes one level up, h = 2 for all nodes before and so on. Given the number of leaf nodes in a tree is $(N+1)/2$, the runtime can be expanded as follows 

$= \frac{N+1}{2}*0 + \frac{N+1}{2^2}*1 + \frac{N+1}{2^3}*2 + ... + 1$\
$= \sum\limits_{0}^{logn} \frac{N+1}{2^i} * (i-1)$\
$= (N+1)\sum\limits_{0}^{logn} \frac{i-1}{2^i}$\
substituiting $x = \frac{1}{2}$\
$= (N+1)\sum\limits_{0}^{logn} (i-1)*x^i$\
$= (N+1) \frac{d}{dx}\sum\limits_{0}^{logn} x^{i-1}$\
The upper bound can be defined if $logn \to \infty$\
$\leq (N+1) \frac{d}{dx}[\sum\limits_{0}^{\infty} x^{i-1}]$\
Since the sum of geometric series till $\infty$ is equal to $\frac{1}{1-r}$
$\leq (N+1) \frac{d}{dx}(\frac{1}{1-x})$\
$\leq (N+1) \frac{1}{(1-x)^2}$\
Substituiting $x = \frac{1}{2}$ The runtime comes to 
**$O(N)$**

# Priority Queueus
A priority queue is a data structure to maintain $n$ elements with a priorirty assigned to each of them. \
Max priority queue is used in a job scheduler which selelcts the highest priorty jobs in the queue of remaining tasks.\
Min prioirity queue is used in an event driven simulator with each items priority being it's time of occurance.\

A heap can be used to implement a priority queue.\

## Priority queuue operations

Max Element : Retrive maximum element from the queue

    def max_element(arr):
        return arr[0] 
*Runtime analysis of max_element*: The opertion runs at constant time. $O(1)$

Delete Max Element : Remove the maximum element from the priority queue

    def delete_max(arr):
        N = len(arr)
        if N<1:
            return -1
        arr[0], arr[N-1] = arr[N-1], arr[0] // swap the first element with the last element
        arr.pop() // remove the last element
        max_heapify(arr, 0)
        return 1
*Runtime analysis of delelte_max*: The swap operation is a constant time operation and max_heapify requires $O(logn)$ making delete_max to be $O(logn)$

Increase key of an element : Increase the priority associated with an element.

        def increase_key(arr, i, key):
            arr[i] = key
            while(i>0 and arr[i//2] < arr[i]):
                arr[i//2], arr[i] = arr[i], arr[i//2]
                i = i//2
*Runtime analysis of increase_key*: This operation traverses the tree from node to the root, in the worst case the node will be a leaf. Which makes the runtime of the procedure to be $O(logn)$

Insert element into the priority queue: 

    def insert(arr, key):
        arr.append(key)
        i = len(arr)-1
        while(i>0 and arr[i//2] < arr[i]):
                arr[i//2], arr[i] = arr[i], arr[i//2]
                i = i//2
or

    def insert(arr, key):
        arr.append(sys.minint)
        increase_key(arr, len(arr)-1, key)

*Runtime analysis of insert* : after adding the value to the array which takes constant time in python, the 
# Heap sort

##### Ref: CLRS
