import time

start = time.process_time()

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        return self.a / self.b

mycal = Calculator(2,4)

print(mycal.get_product())

end = time.process_time()
print(f"CPU Time Used: {end-start} seconds")