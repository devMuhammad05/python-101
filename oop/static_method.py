class Calculator:
    base_value = 100

    @staticmethod
    def add(value1, value2):
        return value1 + value2

    @staticmethod
    def subtract(value1, value2):
        return value1 - value2
    
    @classmethod
    def multiply_base(cls, multiplier):
        return cls.base_value * multiplier
    

# Using Static Method
print(Calculator.add(4, 5))

print(Calculator.subtract(4, 5))

print(Calculator.multiply_base(2))  

