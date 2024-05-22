# Ex 1046
A, B = map(int, input().split())

if A < B:
    duracao = B - A
elif A > B:
    duracao = 24 - A + B
else:
    duracao = 24

print("O JOGO DUROU {} HORA(S)".format(duracao))
