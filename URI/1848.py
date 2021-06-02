import sys

"""
import json

x = '{"name name": "rihan"}'

y = json.loads(x)

n = json.dumps(y)
print(y)
print(type(y))
print(n)
print(type(n))
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4)

"""
# crow's eye's maximum combination could be this. so its constant
maxCom = {
    "---": 0,
    "--*": 1,
    "-*-": 2,
    "*--": 4,
    "-**": 3,
    "*-*": 5,
    "**-": 6,
    "***": 7
}

result = 0
userInput = sys.stdin.readlines()
i = 0
while i < len(userInput):
    if userInput[i].replace('\n', '') == "caw caw":
        print(result)
        result = 0
    else:
        result += maxCom[userInput[i].replace('\n', '')]
    i += 1
