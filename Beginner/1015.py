# Ex 1015
import math

X1, Y1 = map(float, input().split())
X2, Y2 = map(float, input().split())
DISTANCIA = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
print("{:.4f}".format(DISTANCIA))