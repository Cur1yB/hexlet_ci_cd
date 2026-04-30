class Calculator:
    def __init__(self):
        self.OPERATORS = {
            "*": self.mult,
            "+": self.add,
            "-": self.sub,
            "/": self.div,
        }

    def __call__(self, expression: str):
        left, operator, right = expression.split(" ")
        return self.OPERATORS[operator](int(left), int(right))

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b


calc = Calculator()

print(calc("77 / 22"))
