# Ex 1051.py
sal = float(input())
imposto = 0

if sal <= 2000.00:
    print("Isento")
else:
    if sal > 4500.00:
        imposto += (sal - 4500.00) * 0.28
        sal = 4500.00
    if sal > 3000.00:
        imposto += (sal - 3000.00) * 0.18
        sal = 3000.00
    if sal > 2000.00:
        imposto += (sal - 2000.00) * 0.08

    print("R$ {:.2f}".format(imposto))
