#Write a class for square of a number and double a number
class Square:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        return self.num ** 2
    
    def double(self):
        return self.num * 2

class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2