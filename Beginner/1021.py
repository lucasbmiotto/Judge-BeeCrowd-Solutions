# Ex 1021
N = float(input())
N = int(N * 100)

V1 = N // 10000
V = N % 10000
V2 = V // 5000
V = V % 5000
V3 = V // 2000
V = V % 2000
V4 = V // 1000
V = V % 1000
V5 = V // 500
V = V % 500
V6 = V // 200
V = V % 200
V7 = V // 100
V = V % 100

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(V1))
print("{} nota(s) de R$ 50.00".format(V2))
print("{} nota(s) de R$ 20.00".format(V3))
print("{} nota(s) de R$ 10.00".format(V4))
print("{} nota(s) de R$ 5.00".format(V5))
print("{} nota(s) de R$ 2.00".format(V6))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(V7))

V8 = V // 50
V = V % 50
V9 = V // 25
V = V % 25
V10 = V // 10
V = V % 10
V11 = V // 5
V = V % 5
V12 = V // 1

print("{} moeda(s) de R$ 0.50".format(V8))
print("{} moeda(s) de R$ 0.25".format(V9))
print("{} moeda(s) de R$ 0.10".format(V10))
print("{} moeda(s) de R$ 0.05".format(V11))
print("{} moeda(s) de R$ 0.01".format(V12))