import re
def count_characters_identifiers_operators(input_string):
    # Count characters
    char_count = len(input_string)
    # Identify identifiers using regular expression
    identifier_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    identifiers = re.findall(identifier_pattern, input_string)
    identifier_count = len(identifiers)
    # Identify operators
    operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
    operator_count = sum(input_string.count(operator) for operator in operators)

    return char_count, identifier_count, operator_count

# Take input from the user
user_input = input("Enter a string: ")
# Call the function to count characters, identifiers, and operators
char_count, identifier_count, operator_count = count_characters_identifiers_operators(user_input)
# Display the results
print(f"Character Count: {char_count}")
print(f"Identifier Count: {identifier_count}")
print(f"Operator Count: {operator_count}")
