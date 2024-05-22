# Ex 1047
hora1, minuto1, hora2, minuto2 = map(int, input().split())

inicio_minutos = hora1 * 60 + minuto1
fim_minutos = hora2 * 60 + minuto2

if inicio_minutos >= fim_minutos:
    fim_minutos += 24 * 60

duracao_minutos = fim_minutos - inicio_minutos
duracao_horas = duracao_minutos // 60
duracao_minutos = duracao_minutos % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_horas, duracao_minutos))