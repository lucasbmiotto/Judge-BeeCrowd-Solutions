# Ex 1018
N = int(input())

V1 = N//100
V = N%100
V2 = V//50
V = V%50
V3 = V//20
V = V%20
V4 = V//10
V = V%10
V5 = V//5
V = V%5
V6 = V//2
V = V%2
V7 = V//1
V = V%1

print(N)
print("{} nota(s) de R$ 100,00".format(V1))
print("{} nota(s) de R$ 50,00".format(V2))
print("{} nota(s) de R$ 20,00".format(V3))
print("{} nota(s) de R$ 10,00".format(V4))
print("{} nota(s) de R$ 5,00".format(V5))
print("{} nota(s) de R$ 2,00".format(V6))
print("{} nota(s) de R$ 1,00".format(V7))