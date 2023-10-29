# Nebojsa Kilibarda
# 1001934192
# 10/18/2023
# Python 3.10.2

class EmptyStackError(Exception):
    pass


class Evaluate:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []

    def push(self, value):
        self.top += 1
        self.array.append(value)

    def isEmpty(self):
        return True if self.top == -1 else False

    def pop(self):
        if self.isEmpty():
            raise EmptyStackError("Not enough operands.")
        else:
            self.top -= 1
            return self.array.pop()

    @staticmethod
    def performOperation(operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    def evaluateExpression(self, exp):
        try:
            for char in exp:
                if char.isdigit():
                    self.push(int(char))
                elif char in {'+', '-', '*', '/'}:
                    operand2 = self.pop()
                    operand1 = self.pop()
                    result = self.performOperation(char, operand1, operand2)
                    self.push(result)
            return self.pop()
        except EmptyStackError as e:
            print("Error:", e)
            return None


if __name__ == '__main__':
    with open('input_RPN.txt', 'r') as file:
        Lines = file.readlines()
        count = 0

        for line in Lines:
            count += 1
            expression = line.replace(" ", "")
            expression = expression.strip()
            # print(expression)
            obj = Evaluate(len(expression))
            print("%d" % (obj.evaluateExpression(expression)))


file.close()
