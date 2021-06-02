import string
lCase = string.ascii_lowercase

uCase = string.ascii_uppercase

digit = string.digits

testCase = int(input())

display = ["Uppercase Character", "Lowercase Character", "Numerical Digit", "Special Character"]
for i in range(testCase):
    case = input()
    conCheck = [case in uCase, case in lCase, case in digit, True]
    print(display[conCheck.index(True)])