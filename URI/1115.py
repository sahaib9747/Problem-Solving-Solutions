display = ["primeiro", "quarto", "terceiro", "segundo"]
out = []
findOut = lambda x, y: [x > 0 and y > 0, x > 0 and y < 0,
                        x < 0 and y < 0, x < 0 and y > 0]

while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        break
    else:
        index = findOut(x,y)
        out.append(display[index.index(True)])
print(*out, sep='\n')