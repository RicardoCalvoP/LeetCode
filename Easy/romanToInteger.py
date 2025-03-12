import os


def romanToInt(s):
    # Convert the string to uppercase
    s = s.upper()
    num = 0
    # Dictionary of roman numerals
    roman_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    i = 0
    while i < len(s):
        # If the current letter is less than the next letter, subtract the current letter from the next letter
        # and skip the next letter in the loop
        if i + 1 < len(s) and roman_nums[s[i]] < roman_nums[s[i + 1]]:
            num += roman_nums[s[i + 1]] - roman_nums[s[i]]
            i += 2
        # If the current letter is greater than or equal to the next letter, add the current letter to the number
        else:
            num += roman_nums[s[i]]
            i += 1
    print(num)


os.system('cls')


romanToInt('IV')
romanToInt('XXXV')
