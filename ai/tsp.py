ary = [[0] * 10 for _ in range(10)]
n = 0
cost = 0

def takeInput():
    global n, completed
    print("Enter the number of cities: ")
    n = int(input())
    completed = [0] * n
    print("\nEnter the Cost Matrix")
    for i in range(n):
        print("\nEnter Elements of Row: ", i+1)
        for j in range(n):
            ary[i][j] = int(input())
    print("\n\nThe cost list is:")
    for i in range(n):
        print()
        for j in range(n):
            print("\t", ary[i][j], end="")
            
def mincost(city):
    global cost
    completed[city] = 1
    print(city+1, "--->", end="")
    ncity = least(city)
    if ncity == 999:
        ncity = 0
        print(ncity+1)
        cost += ary[city][ncity]
        return
    mincost(ncity)
    
def least(c):
    global cost
    nc = 999
    min = 999
    kmin = 0
    for i in range(n):
        if ary[c][i] != 0 and completed[i] == 0:
            if ary[c][i] < min:
                min = ary[c][i]
                kmin = ary[c][i]
                nc = i
    if min != 999:
        cost += kmin
    return nc

takeInput()
print("\n\nThe Path is:")
mincost(0) #passing 0 because starting vertex
print("\n\nMinimum cost is ", cost)
