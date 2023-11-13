def calculate_first_and_follow(grammar, start_symbol):
    first_sets = {}
    follow_sets = {}

    for non_terminal in grammar.keys():
        first_sets[non_terminal] = set()
        follow_sets[non_terminal] = set()

    follow_sets[start_symbol] = {'$'}

    for non_terminal in grammar.keys():
        first(grammar, non_terminal, first_sets)

    for non_terminal in grammar.keys():
        follow(grammar, non_terminal, start_symbol, follow_sets, first_sets)

    return first_sets, follow_sets

def first(grammar, symbol, first_sets):
    # if symbol in first_sets:
    #     return first_sets[symbol]

    first_set = set()

    if symbol in grammar:
        for production in grammar[symbol]:
            for char in production:
                if char not in grammar:
                    first_set.add(char)
                    break
                elif char != symbol:
                    char_first = first(grammar, char, first_sets)
                    first_set.update(char_first - {'ε'})
                    if 'ε' not in char_first:
                        break
                else:
                    continue
            else:
                first_set.add('ε')

    first_sets[symbol].update(first_set)
    return first_set


def follow(grammar, symbol, start_symbol, follow_sets, first_sets):
    if symbol in grammar:
        for non_terminal, productions in grammar.items():
            for production in productions:
                if symbol in production:
                    index = production.index(symbol)
                    if index == len(production) - 1:
                        if non_terminal != symbol:
                            follow_sets[symbol].update(follow_sets[non_terminal])
                    else:
                        next_symbol = production[index + 1]
                        if next_symbol in grammar:
                            next_first = first_sets[next_symbol]
                            follow_sets[symbol].update(next_first - {'ε'})
                            if 'ε' in next_first:
                                follow_sets[symbol].update(follow_sets[non_terminal])

# Example usage:
grammar = {
    'S': ['AB', 'b'],
    'A': ['ε', 'c'],
    'B': ['d']
}

start_symbol = 'S'

first_sets, follow_sets = calculate_first_and_follow(grammar, start_symbol)

print('First sets:')
for non_terminal, first_set in first_sets.items():
    print(f'{non_terminal}: {first_set}')

print('Follow sets:')
for non_terminal, follow_set in follow_sets.items():
    print(f'{non_terminal}: {follow_set}')
