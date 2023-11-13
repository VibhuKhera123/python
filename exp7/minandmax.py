def minelement(list):
    x = len(list)
    min = list[0]
    for i in range(0,x):
        if(list[i]<min):
            min = list[i]
    return min

def maxelement(list):
    x = len(list)
    max = list[0]
    for i in range(0,x):
        if(list[i]>max):
            max = list[i]
    return max

if __name__ == "__main__":
    list = []
    n = int(input("Enter the number of elements: "))
    print("Enter the elements: ")
    for i in range(0,n):
        a=int(input())
        list.append(a)
    print("Maximum element: ",maxelement(list),"\nMinimum element: ",minelement(list))
