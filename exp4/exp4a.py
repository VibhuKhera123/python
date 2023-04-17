#calculator
#to print even number from 1 to 10 and their sum
#wap to display multiplication tables from 1 to 5
#reverse of a number
#calculate the factorial of a number using recurssion
#wap to triverse every second character of a string using for loop



x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

print("Enter your option:\n1)Addition(+)\n2)Subtraction(-)\n3)Multiplication(*)\n4)Division(/)")
opr = input("Choose the operation: ")
if(opr == "+"):
    print("Sum is: ",x+y)
elif(opr == "-"):
    print("Difference is: ",x-y)
elif(opr == "*"):
    print("product is: ",x*y)
elif(opr == "/"):
    print("division: ",x/y)
else:
    print("invalid input")

