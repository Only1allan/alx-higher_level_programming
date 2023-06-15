#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {'M': 1000,
                    'D': 500,
                    'C': 100,
                    'L': 50,
                    'X': 10,
                    'V': 5,
                    'I': 1
                    }
    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_values[char]
        if value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value
    return result
