# Ex 1020
VALOR = int(input())
ANOS = VALOR // 365
DIAS_RESTANTES = VALOR % 365
MESES = DIAS_RESTANTES // 30
DIAS = DIAS_RESTANTES % 30
print("{} ano(s)".format(ANOS))
print("{} mes(es)".format(MESES))
print("{} dia(s)".format(DIAS))
