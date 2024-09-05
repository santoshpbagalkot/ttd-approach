class Calculator:
    def add(self, numbers: str) -> int:
        numbers_copy = numbers.strip()
        if not numbers_copy:
            return 0
        # Split the string by commas, convert each part to int, and sum them up
        return sum(int(num) for num in numbers_copy.split(',') if num.strip())
