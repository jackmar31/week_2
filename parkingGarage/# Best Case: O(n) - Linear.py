# Best Case: O(n) - Linear
def swap(i,j, array):
    array[i],array[j] = array[j],array[i]
    
def bubbleSort(array):
    # initially define isSorted as False so we can
    # execute the while loop
    isSorted = False
    # while the list is not sorted, repeat the following:
    while not isSorted:
        # assume the list is sorted
        isSorted = True
        # crawl along the list from the beginning to the end 
        for num in range(len(array) - 1):
            # if the item on the left is greater 
            # than the item on the right
            if array[num] > array[num + 1]:
                # swap them so the greater item goes on the right
                swap(num, num + 1, array)
                # because we had to make the swap,
                # the list must not have been sorted
                isSorted = False
    return array

bubbleSort([22,55,88,44,1,100,34,66])