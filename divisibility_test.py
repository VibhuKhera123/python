num1 = eval(input("Enter first number: "))

if((num1%5 == 0) and (num1%10 == 0)):
    print("number is divisible by both")
elif(num1%5 == 0):
    print("number is divisible by 5")
elif(num1%10 == 0):
    print("number is divisible by 10")
else:
    print("number is not divisible")