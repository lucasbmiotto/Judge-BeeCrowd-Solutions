# Ex 1044
N1, N2 = map(int, input().split())

if N1 % N2 == 0 or N2 % N1 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")