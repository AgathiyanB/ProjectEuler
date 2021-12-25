class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.buffer = None
    def reciprocal(self):
        self.buffer = self.numerator
        self.numerator = self.denominator
        self.denominator = self.buffer
        self.buffer = None
    def add(self,value):
        self.numerator += self.denominator*value

root_two = Fraction(3,2) #technically first iteration
count = 0
for iteration in range(2,1001):
    root_two.add(1)
    root_two.reciprocal()
    root_two.add(1)
    if len(str(root_two.numerator)) > len(str(root_two.denominator)):
        count += 1
print(count)
