one, two, third = map(int, input().split())  # take temperature
emoji = [":)", ":(", ":(", ":)", ":)", ":(", ":)", ":("]
conChecker = [
    one > two <= third,
    one < two >= third,
    one < two < third and (two - one) > (third - two),
    one < two < third and (two - one) <= (third - two),
    one > two > third and (one - two) > (two - third),
    one > two > third and (two - third) >= (one - two),
    one == two < third,
    True
]
print(emoji[conChecker.index(True)])
