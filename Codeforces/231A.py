tcase = int(input())  # total test case

can_solved = 0
for i in range(tcase):
    inp = sum(list(map(int, input().split())))

    if inp >= 2:
        can_solved += 1

print(can_solved)
