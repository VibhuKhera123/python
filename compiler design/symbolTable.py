# class SymbolTable:
#     def __init__(self):
#         self.symbol_table = {}
#         self.next_address = 1000  # Starting address

#     def insert(self, name, symbol_type):
#         if name in self.symbol_table:
#             print(f"Error: {name} is already defined.")
#         else:
#             address = self.next_address
#             self.next_address += 4  # Assuming each variable takes 4 bytes of memory
#             self.symbol_table[name] = {'type': symbol_type, 'address': address}

#     def lookup(self, name):
#         return self.symbol_table.get(name, None)

#     def display(self):
#         print("Symbol Table:")
#         for name, info in self.symbol_table.items():
#             print(f"Name: {name}, Type: {info['type']}, Address: {info['address']}")

# # Function to tokenize input and insert tokens into the symbol table with automatically inferred types
# def tokenize_and_insert(input_str, symbol_table):
#     tokens = input_str.split()
#     for token in tokens:
#         try:
#             # Attempt to evaluate the token as an expression
#             evaluated_value = eval(token)
#             symbol_type = type(evaluated_value).__name__
#         except:
#             # If the evaluation fails, assume it's a string
#             symbol_type = 'str'
#         symbol_table.insert(token, symbol_type)

# if __name__ == "__main__":
#     symbol_table = SymbolTable()

#     # Input string to tokenize
#     input_string = input("Enter a space-separated string to tokenize and store in the symbol table: ")

#     # Tokenize and insert tokens into the symbol table with automatically inferred types
#     tokenize_and_insert(input_string, symbol_table)

#     # Display the symbol table
#     symbol_table.display()


class SymbolTable:
    def __init__(self):
        self.symbol_table = {}

    def insert(self, name, symbol_type):
        if name in self.symbol_table:
            print(f"Error: {name} is already defined.")
        else:
            self.symbol_table[name] = {'type': symbol_type, 'address': None}

    def lookup(self, name):
        return self.symbol_table.get(name, None)

    def display(self):
        print("Symbol Table:")
        for name, info in self.symbol_table.items():
            address = id(name)  # Get the memory address of the variable name
            print(f"Name: {name}, Type: {info['type']}, Address: {address}")

# Function to tokenize input and insert tokens into the symbol table with automatically inferred types
def tokenize_and_insert(input_str, symbol_table):
    tokens = input_str.split()
    for token in tokens:
        try:
            # Attempt to evaluate the token as an expression
            evaluated_value = eval(token)
            symbol_type = type(evaluated_value).__name__
        except:
            # If the evaluation fails, assume it's a string
            symbol_type = 'str'
        symbol_table.insert(token, symbol_type)

if __name__ == "__main__":
    symbol_table = SymbolTable()
    input_string = input("Enter a space-separated string to tokenize and store in the symbol table: ")
    tokenize_and_insert(input_string, symbol_table)
    symbol_table.display()
