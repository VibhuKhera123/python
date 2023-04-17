def binary_search(arr, x):
    """
    Perform binary search on a sorted list of integers.

    Args:
        arr (list[int]): A sorted list of integers.
        x (int): The value to search for in the list.

    Returns:
        int: The index of the element in the list, or -1 if it's not found.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

if __name__ == "__main__":
    a = []
    n=int(input('Enter the number of elements: '))
    print("Enter the elements: ")
    for i in range(0,n):
        x=int(input())
        a.append(x)
    key = int(input('Enement to be searched: '))
    index = binary_search(a,key)
    if(index == -1):
        print("element not found!")
    else:
        print(key,' found at ',index)