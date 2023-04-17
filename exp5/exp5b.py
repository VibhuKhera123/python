#temperature conversion

n = int(input('Enter the number of inputs: '))
li = []
for i in range(0,n):
    x = eval(input('Enter the temperature in fernite: '))
    li.append(x)
celcius = [format((x-32)*5/9,".2f") for x in li]
print(li)
print(celcius)