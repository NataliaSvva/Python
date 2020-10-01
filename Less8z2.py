class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")

div = DivisionByNull(15, 17)
print(DivisionByNull.divide_by_null(8, 0))
print(DivisionByNull.divide_by_null(25, 0.1))
print(div.divide_by_null(28, 0))