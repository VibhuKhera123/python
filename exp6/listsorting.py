def partition(a,fi,li):
    p = a[li]
    i = fi-1
    for j in range(fi,li):
        if(a[j]<=p):
            i+=1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[i+1]
    a[i+1] = a[li]
    a[li] = temp
    return i+1

def quickSort(a,fi,li):
    if(fi<li):
        pi = partition(a,fi,li)
        quickSort(a,fi,pi-1)
        quickSort(a,pi+1,li)

def main():
    li=[]
    n = int(input('Enter number of elements of the list: '))
    print('Enter the elements of the list: ')
    for i in range (0,n):
        a = int(input())
        li.append(a)
    print('List entered: ',li)
    for i in range(0,n):
        for j in range(0,i):
            if(len(str(li[j]))>len(str(li[i]))):
                temp = li[j]
                li[j] = li[i]
                li[i] = temp
    print("List after sorting on the basis of length: ",li)
    quickSort(li,0,n-1)

if __name__ == "__main__":
    main()
