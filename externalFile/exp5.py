def main():
  string = input("Enter a string: ")
  print("The length of the string is:", len(string))
  upper_string = string.upper()
  print("The uppercase version of the string is:", upper_string)
  lower_string = string.lower()
  print("The lowercase version of the string is:", lower_string)
  reversed_string = string[::-1]
  print("The reversed version of the string is:", reversed_string)
  if string.startswith("hello"):
    print("The string starts with 'hello'")
  else:
    print("The string does not start with 'hello'")
  if string.endswith("world"):
    print("The string ends with 'world'")
  else:
    print("The string does not end with 'world'")
  index = string.index("i")
  print("The index of the character 'e' in the string is:", index)
  count = string.count("e")
  print("The number of occurrences of the character 'l' in the string is:", count)
  replaced_string = string.replace("hello", "goodbye")
  print("The string with the character 'hello' replaced with 'goodbye' is:", replaced_string)
  list_of_strings = string.split()
  print("The list of strings created by splitting the string is:", list_of_strings)
  joined_string = " ".join(list_of_strings)
  print("The string created by joining the list of strings is:", joined_string)
  print('\a')
if __name__ == "__main__":
  main()
