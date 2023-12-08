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
            address = id(name)
            print(f"Name: {name}, Type: {info['type']}, Address: {address}")
def tokenize_and_insert(input_str, symbol_table):
    tokens = input_str.split()
    for token in tokens:
        try:
            evaluated_value = eval(token)
            symbol_type = type(evaluated_value).__name__
        except:
            symbol_type = 'str'
        symbol_table.insert(token, symbol_type)
if __name__ == "__main__":
    symbol_table = SymbolTable()
    input_string = input("Enter a space-separated string to tokenize and store in the symbol table: ")
    tokenize_and_insert(input_string, symbol_table)
    symbol_table.display()
