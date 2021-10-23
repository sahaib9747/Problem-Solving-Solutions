if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])

    names = [i[0] for i in lst]
    grades = [i[1] for i in lst] 

    grades = set(grades)
    lowest = max(grades)
    if len(grades) > 2:
        grades.remove(min(grades))
        lowest = min(grades)

    lst = [i[0] for i in lst if lowest in i]
    print(*sorted(set(lst)), sep='\n')
