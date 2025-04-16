grupo = int(input("Quantas pessoas existem no grupo? "))
soma = 0
acima_70 =0

for i in range(grupo):
    peso = float(input("Peso: "))
    soma += peso
    if peso > 70:
        acima_70 +=1

media = peso/grupo

print("media de pesos:",media)
print("Pessoas acima de 70kg:",acima_70)