#display odd number from a list using list comprihension

li = [21,24,26,29,31,45]
newList = [x for x in li if x%2!=0]
print(newList)