class ShiftReduceParser:
    def __init__(self):
        self.operators = {'+', '*'}
        self.precedence = {'+': 1, '*': 2}

    def parse(self, input_expression):
        output_queue = []
        operator_stack = []

        tokens = input_expression.split()

        for token in tokens:
            if token.isnumeric():
                output_queue.append(token)
            elif token in self.operators:
                while (operator_stack and
                       operator_stack[-1] in self.operators and
                       self.precedence[token] <= self.precedence[operator_stack[-1]]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()

        while operator_stack:
            output_queue.append(operator_stack.pop())

        if len(output_queue) == 1:
            print("Parse successful!")
        else:
            print("Parse failed!")

if __name__ == "__main__":
    parser = ShiftReduceParser()

    # Example input: 2 + 3 * 4
    input_expression = input("Enter an arithmetic expression: ")

    parser.parse(input_expression)
