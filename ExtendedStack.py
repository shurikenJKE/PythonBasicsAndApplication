class ExtendedStack(list):
    # Операция умножения
    def sum(self):
        self.append(self.pop() + self.pop())
    # Операция вычитания
    def sub(self):
        self.append(self.pop() - self.pop())
    # Операция умножения
    def mul(self):
        self.append(self.pop() * self.pop())
    # Операция целочисленного деления
    def div(self):
        self.append(self.pop() // self.pop())