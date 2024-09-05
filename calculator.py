import re

class Calculator:

    # Regular expression to split by comma or newline
    pattern = r'[,\n]'

    def add(self, numbers: str) -> int:
        numbers_copy = numbers.strip()
        if not numbers_copy:
            return 0
        # Split the string by commas, convert each part to int, and sum them up
        numbers_copy = re.split(Calculator.pattern, numbers_copy)
        return sum(int(num) for num in numbers_copy if num.strip())
