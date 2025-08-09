class Calculator:
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        return a + b
    

    @classmethod
    def multiply(cls, a, b):
        """Class method: accesses the class attribute and performs multiplication."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b