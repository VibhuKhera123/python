def convert_predicate_to_propositional_logic(predicate):
    # Split the predicate into parts
    parts = predicate.split('(')
    predicate_name = parts[0]
    arguments = parts[1].split(')')[0].split(',')
    
    # Convert predicate name to propositional logic symbol
    proposition = predicate_name.lower()
    
    # Add arguments to the proposition
    for arg in arguments:
        proposition += f' {arg.lower()}'
    
    return proposition

# Get user input for predicate
predicate = input("Enter a predicate: ")

# Convert predicate to propositional logic
propositional_logic = convert_predicate_to_propositional_logic(predicate)

print(f"Propositional logic: {propositional_logic}")
