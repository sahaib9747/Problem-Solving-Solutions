#use graph to understand
output = ["Q1", "Q3", "Q2", "Q4", "Origem", "Eixo X", "Eixo Y"]
x, y = map(float, input().split())
conChecker = [x > 0 and y > 0, x < 0 and y < 0, x < 0 and y > 0, x > 0 and y < 0,
              x == y == 0, (x > 0 or x < 0) and y == 0, (y > 0 or y < 0) and x == 0]
print(output[conChecker.index(True, 0)])