timeA = input("Escreva o nome do time da casa: ")
golA = int(input("Quantos gols o time da casa fez? "))
timeB = input("Escreva o nome do time visitante: ")
golB = int(input("Quantos gols o time da fora fez? "))

if golA == golB:
    print("EMPATE")

elif golA > golB:
    print(timeA,"FOI O VENCEDOR")

else:
    print(timeB,"FOI O VENCEDOR")