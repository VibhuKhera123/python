class OperatorPrecedenceParser:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    def display_precedence_table(self):
        print("Operator Precedence Table:")
        operators = list(self.operators.keys())
        operators.sort()
        print("  |", end="")
        for op in operators:
            print(f" {op} ", end="|")
        print()
        print("--+" + "+".join(["---" for _ in operators]))
        for row_op in operators:
            print(f"{row_op} |", end="")
            for col_op in operators:
                if self.operators[row_op] > self.operators[col_op]:
                    print(" > ", end="|")
                elif self.operators[row_op] < self.operators[col_op]:
                    print(" < ", end="|")
                else:
                    print(" = ", end="|")
            print()
    def parse(self, expression):
        tokens = expression.replace(" ", "")
        stack = []
        output = []
        for token in tokens:
            if token.isalnum():
                output.append(token)
            elif token in self.operators:
                while stack and stack[-1] in self.operators and self.operators[stack[-1]] >= self.operators[token]:
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
        while stack:
            output.append(stack.pop())
        return output 
    def evaluate_postfix(self, postfix_expression):
        stack = []
        for token in postfix_expression:
            if token.isalnum():
                stack.append(int(token))
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression")
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        raise ValueError("Division by zero")
                    stack.append(operand1 / operand2)
        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")
        return stack.pop()
def main():
    parser = OperatorPrecedenceParser()

    expression = input("Enter an infix expression: ")
    postfix_expression = parser.parse(expression)
    result = parser.evaluate_postfix(postfix_expression)

    print("Postfix expression:", postfix_expression)
    print("Result:", result)

    parser.display_precedence_table()
if __name__ == "__main__":
    main()
