pontos = 0
horas = int(input("Quantas horas de atividade física você fez esse mês?"))

if horas <= 10:
    pontos = horas * 2
elif horas >10 and horas <= 20:
    pontos = horas * 5
else:
    pontos = horas * 10


print("Você fez", pontos,"pontos esse mês")