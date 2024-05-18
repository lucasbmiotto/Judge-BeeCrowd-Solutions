# Ex 1013
A, B, C = map(int, input().split())
MAIOR_AB = (A + B + abs(A - B)) // 2
MAIOR = (MAIOR_AB + C + abs(MAIOR_AB - C)) // 2
print(MAIOR, "eh o maior")
