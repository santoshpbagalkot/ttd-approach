class Calculator:
    def add(self, numbers: str) -> int:
        numbers_copy = numbers.strip()
        if not numbers_copy:
            return 0
        numbers_array = numbers_copy.split(',')
        if len(numbers_array) == 1:
            return int(numbers_array[0])
        else:
            return (int(numbers_array[0]) + int(numbers_array[1]))
