# Ex 1040
N1, N2, N3, N4 = map(float, input().split())
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    nota_exame = float(input())
    print("Aluno em exame.")
    print("Nota do exame: {:.1f}".format(nota_exame))

    media2 = (media + nota_exame) / 2
    
    if media2 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print("Media final: {:.1f}".format(media2))