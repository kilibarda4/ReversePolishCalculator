# Nebojsa Kilibarda
# 1001934192
# 10/18/2023
# Python 3.10.2

# The added operation is %
# The program takes an algebraic statement, converts it to Postfix
# And prints the postfix version along with the result of calculation

class EmptyStackError(Exception):
    pass


operators = "+-*/%"


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

    def peek(self):
        if not self.isEmpty():
            return self.array[-1]

    def getPrecedence(self, c):
        result = 0
        for char in operators:
            result += 1

            if char == c:
                if c in '-/':
                    result -= 1
                break

        return result

    def toPostfix(self, exp):
        result = ""
        for char in exp:
            if char.isdigit():
                result += char

            elif char in operators:
                while True:
                    topChar = self.peek()

                    if self.isEmpty() or topChar == '(':
                        self.push(char)
                        break
                    else:
                        pC = self.getPrecedence(char)
                        pTc = self.getPrecedence(topChar)

                        if pC > pTc:
                            self.push(char)
                            break
                        else:
                            result += self.pop()

            elif char == '(':
                self.push(char)

            elif char == ')':
                nextChar = self.pop()
                while nextChar != '(':
                    result += nextChar
                    nextChar = self.pop()

        while not self.isEmpty():
            cpop = self.pop()
            result += cpop
        return result

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
        elif operator == '%':
            return operand1 % operand2

    def evaluateExpression(self, exp):
        try:
            for char in exp:
                if char.isdigit():
                    self.push(int(char))
                elif char in {'+', '-', '*', '/', '%'}:
                    operand2 = self.pop()
                    operand1 = self.pop()
                    result = self.performOperation(char, operand1, operand2)
                    self.push(result)
            return self.pop()
        except EmptyStackError as e:
            print("Error:", e)
            return None


if __name__ == '__main__':
    with open('input_RPN_EC.txt', 'r') as file:
        Lines = file.readlines()
        count = 0

        for line in Lines:
            count += 1
            expression = line.strip()
            obj = Evaluate(len(expression))
            postfixExp = obj.toPostfix(expression)
            print(postfixExp)
            print("%d" % (obj.evaluateExpression(postfixExp)))


file.close()
