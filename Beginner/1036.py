# Ex 1036
import math

A, B, C = map(float, input().split())

if A == 0:
    print("Impossivel calcular")
else:
    delta = B ** 2 - 4 * A * C

    if delta < 0:
        print("Impossivel calcular")
    elif delta == 0:
        X = -B / (2 * A)
        print("R1 = {:.5f}".format(X))
    else:
        raiz = math.sqrt(delta)
        X1 = (-B + raiz) / (2 * A)
        X2 = (-B - raiz) / (2 * A)
        print("R1 = {:.5f}".format(X1))
        print("R2 = {:.5f}".format(X2))