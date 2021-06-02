tCase = int(input())
while tCase:
    userData = input()
    vowels = 'AEIOUaeiou'
    vowel, cons = "".join(list(filter(lambda char: char in vowels, userData))), \
                  "".join(list(filter(lambda char: char not in vowels and char.isalpha(), userData)))
    print(vowel + '\n' + cons)
    tCase -= 1