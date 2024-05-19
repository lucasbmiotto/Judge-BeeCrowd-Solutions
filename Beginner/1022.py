# Ex 1022
def mdc(A, B):
    while B:
        A, B = B, A % B
    return A

def simplificar(numero, den):
    divisor_comum = mdc(numero, den)
    return numero // divisor_comum, den // divisor_comum

num_casos = int(input())
for _ in range(num_casos):
    num1, _, den1, op, num2, _, den2 = input().split()
    num1, den1, num2, den2 = map(int, (num1, den1, num2, den2))
    if op == '+':
        num = num1 * den2 + num2 * den1
        den = den1 * den2
    elif op == '-':
        num = num1 * den2 - num2 * den1
        den = den1 * den2
    elif op == '*':
        num = num1 * num2
        den = den1 * den2
    elif op == '/':
        num = num1 * den2
        den = num2 * den1
    
    num_simp, den_simp = simplificar(num, den)
    print("{}/{} = {}/{}".format(num,den,num_simp,den_simp))
