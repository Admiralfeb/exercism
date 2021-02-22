def is_armstrong_number(number):
    string_number = str(number)
    power = len(string_number)

    total = 0
    for value in string_number:
        total += int(value) ** power

    return total == number
