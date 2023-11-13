def reverse_string(s):
  reversed_string = ""
  for i in range(len(s) - 1, -1, -1):
    reversed_string += s[i]
  return reversed_string

def main():
    inputString = input("Enter a string: ")
    print("The reverse of the string is: ", reverse_string(inputString))
if "__name__" == "__main__":
  main()