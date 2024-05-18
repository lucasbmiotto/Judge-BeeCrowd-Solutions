# Ex 1019
VALOR = int(input())
SEGUNDO = VALOR % 60
MINUTO = (VALOR // 60) % 60
HORA = VALOR // 3600
print("{}:{}:{}".format(HORA, MINUTO, SEGUNDO))
