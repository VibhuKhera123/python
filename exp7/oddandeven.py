if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    odd=[]
    even=[]
    for i in range (a,b):
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    print("Even element between ",a," and ",b," are ",even,"\nOdd elements between ",a," and ",b," are ",odd)