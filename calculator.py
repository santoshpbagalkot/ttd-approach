import re

class Calculator:

    # Regular expression to split by comma or newline
    default_delimiter_pattern = r'[,\n]'
    dymanic_delimiter_pattern = r'^//(.{1})\n'

    def remove_pattern(self, pattern, text):
        """
        Utility to remove the delimiter pattern from the parent string to allow split on the captured delimiter
        """
        return re.sub(pattern, '', text)


    def add(self, numbers: str) -> int:
        numbers_copy = numbers.strip()
        if not numbers_copy:
            return 0
        match = re.match(Calculator.dymanic_delimiter_pattern, numbers_copy)
        if match:
            # If we are supplied with a delimiter already, extract it to split the string on the same
            delimiter = match.group(1) # Extract the delimiter from the () group
            numbers_copy = self.remove_pattern(Calculator.dymanic_delimiter_pattern, numbers_copy)
            numbers_copy = numbers_copy.split(delimiter)
        else:
            # If we are not supplied with a delimiter pattern use the default , or \n
            numbers_copy = re.split(Calculator.default_delimiter_pattern, numbers_copy)
        # Split the string by commas, convert each part to int, and sum them up
        # Negative numbers if found must be tracked and an exception must be raised.
        detected_negative_numbers = []
        for num in numbers_copy:
            int_casted_number = int(num)
            if int_casted_number < 0:
                detected_negative_numbers.append(num)
        if len(detected_negative_numbers) > 0:
            error_message = "negative numbers not allowed "+(" ".join(detected_negative_numbers)) + "."
            raise ValueError(error_message)
        return sum(int(num) for num in numbers_copy if num.strip())
