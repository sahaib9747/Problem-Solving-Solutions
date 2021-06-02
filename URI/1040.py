avCalculator = lambda n1, n2, n3, n4: (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
reAvCalculator = lambda more, previousAv: (more + previousAv) / 2
conChecker = lambda result = 0, finalResult = 0: ([result >= 7.0, result < 5.00, result >= 5.00 and result < 6.9, finalResult >= 5.0, finalResult <= 4.9])

if __name__ == '__main__':
    n1, n2, n3, n4 = map(float, input().split())
    result = avCalculator(n1, n2, n3, n4)
    display = ["Aluno aprovado.", "Aluno reprovado.", "Aluno em exame."]
    checker = conChecker(result)
    if checker[2]:
        more = float(input())
    print("Media: %.1f\n%s" % (result, display[checker.index(True)]))
    if checker[2]:
        finalResult = reAvCalculator(more, result)
        checker = conChecker(0, finalResult)
        print("Nota do exame: %.1f\n%s\nMedia final: %.1f" % (more, display[checker.index(True,3) - 3], finalResult))