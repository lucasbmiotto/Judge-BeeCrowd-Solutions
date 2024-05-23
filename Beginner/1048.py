# Ex 1048
sal = float(input())

if sal > 0 and sal <= 400.00:
    percentual = 15
elif sal <= 800.00:
    percentual = 12
elif sal <= 1200.00:
    percentual = 10
elif sal <= 2000.00:
    percentual = 7
else:
    percentual = 4

reajuste = sal * (percentual / 100)
novo_sal = sal + reajuste

print("Novo salario: {:.2f}".format(novo_sal))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))