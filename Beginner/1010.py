# Ex 1010
C1, P1, V1 = input().split()
C1 = int(C1)
P1 = int(P1)
V1 = float(V1)

C2, P2, V2 = input().split()
C2 = int(C2)
P2 = int(P2)
V2 = float(V2)

total = (P1 * V1) + (P2 * V2)

print("VALOR A PAGAR: R$ {:.2f}".format(total))
