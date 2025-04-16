numeros = []


for i in range (10):
    n = float(input("Digite seu número aqui: "))

    numeros.append(n)


   
negativos = 0
soma_pos = 0

for n in numeros:
    if n < 0:
        negativos += 1
    else:
        soma_pos += n

print("Você digitou", negativos,"números negativos")
print("A soma dos números positivos foi: ", soma_pos)
    

