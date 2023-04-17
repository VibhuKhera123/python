#every second character of a string using for loop4

x = input("Enter a string: ")
length= len(x)
for i in range(0,length,2):
    print(x[i],end=" ")
print("\n")