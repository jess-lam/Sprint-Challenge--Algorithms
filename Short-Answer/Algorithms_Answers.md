#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because as the input increases, the run time will increase at the same rate


b) O(n log n) because the for loop is O(n): as the input increases, the run time grows at the same rate.
  The while loop inside the for loop is O(log n) because the run time grows at a slightly slower rate as the input increases. Therefore, O(n log n).


c) O(n) because this function runs n times as bunnyEars decrements by 1 until it reaches 0, which means the as the input increases, the run time increases at the same rate.

## Exercise II

I would start from the middle of number of floors and if the egg doesn't break at that floor, then that becomes our new end an we don't have to look below that. The you would get the middle of the new list of floors, test if the egg breaks, and repeat the process of elimination. This would probably involve a Binary Search so the run time would be O(n).


def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)

        else:
            return binary_search(arr, target, start, mid - 1)
    else:
        return -1
