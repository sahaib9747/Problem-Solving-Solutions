salary = float(input())
salaryRange = [0 <= salary <= 400, 400.01 <= salary <= 800, 800.01 <= salary <= 1200, 1200.01 <= salary <= 2000,
               2000.01 <= salary]
salaryPercent = [15, 12, 10, 7, 4]
salaryIncrease = lambda x, y: x / 100 * y
index = salaryRange.index(True)
increaseAmount = salaryIncrease(salary, salaryPercent[index])
print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %s %s" % (increaseAmount + salary, increaseAmount, salaryPercent[index], '%'))