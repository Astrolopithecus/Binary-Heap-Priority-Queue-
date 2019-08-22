#Implementing a min heap using a list
class BinHeap:
    def __init__(self):
        self._heap = [0]
        self.currentSize = 0

    def insert(self, data):
        self._heap.append(data)
        self.currentSize +=1
        self.percUp(self.currentSize)
    
    def percUp(self, index):
        while(index // 2 > 0):
            if (self._heap[index] < self._heap[index // 2]):
                #Need to move up, swap
                self._heap[index], self._heap[index // 2] = self._heap[index // 2] , self._heap[index]
                index = index // 2
            else:
                break
    def pop(self):
        if (self.currentSize == 0): #Heap is empty, return None
            return None
        retVal = self._heap[1] #save the root value to return
        #set the value of the last leaf at the root
        self._heap[1] = self._heap[self.currentSize]
        self._heap.pop() # remove the last leaf
        self.currentSize -= 1
        # Call percDown to position self._heap[1] at the right place
        self.percDown(1)
        return retVal


    def percDown(self,index):
        while (index*2 <= self.currentSize): # This node has a child node
            #Check if the child nodes are larger than the current index, if so swap with
            # the min child
            minChildIndex = self.getMinChildIndex(index)
            if (self._heap[index] > self._heap[minChildIndex]):
                #need to swap with the minChildIndex
                self._heap[index], self._heap[minChildIndex] = self._heap[minChildIndex], self._heap[index]
                index = minChildIndex
            else:
                #current node is less than min child, it is in the right place
                break
    def getMinChildIndex(self, index):
        assert(index*2 <= self.currentSize)
        if (index*2 + 1 <= self.currentSize and self._heap[index*2+1] < self._heap[index*2]):
            #right child exists and is smaller than left child. return right child index
            return index*2 + 1
        else:
            #had Only left child , or right Child is greater than left child
            return index*2

    def __str__(self):
        return self._strRecursive(1,0)
    def _strRecursive(self, nodeIndex, level):
        '''Recursive function to return an ASCII version of
        90 degree rotated view of the tree
        '''
        s = ""
        if (nodeIndex < len(self._heap)): #node is a valid index
            s += self._strRecursive(nodeIndex*2+1, level+1)
            s += "| "*level
            s += str(self._heap[nodeIndex]) + "\n"
            s += self._strRecursive(nodeIndex*2, level+1)
        return s

    def buildHeap(self, lyst):
        # build a heap from given lyst
        self._heap = [0]+lyst[:]
        self.currentSize = len(lyst)
        index = len(lyst) // 2 # start at the parent of the first leaf node
        while (index > 0):
            #print("percing down",self._heap[index])
            self.percDown(index)
            index -= 1
            #print(self)
# Function to sort the given lyst in-place using a min heap
def heapSort(lyst):
    #Create an empty heap
    heap = BinHeap()
    #Call buildHeap to load the elements of lyst in the heap
    heap.buildHeap(lyst)
    #Pop items and store them back in lyst to get the sorted
    # version of lyst
    for k in range(len(lyst)):
        lyst[k] = heap.pop()
        
def main():
    lyst = [74,12,3,38,41,99,18,62,11,55,90]
    print("Before sorting...")
    print(lyst)
    print("After sorting...")
    heapSort(lyst)
    print(lyst)
    
if __name__ == "__main__":
    main()
