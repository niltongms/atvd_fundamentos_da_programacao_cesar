numeros = []

while True:
    n = int(input("Digite um número (-1 para parar): "))
    if n == -1:
        break
    numeros.append(n)

# a) Quantos números foram digitados
print("na) Você digitou", len(numeros),"números.")

# b) Lista ordenada de forma decrescente
print("b) Lista em ordem decrescente:", sorted(numeros, reverse=True))

# c) Se o número 5 está na lista
if 5 in numeros:
    print("c) O número 5 está na lista.")
else:
    print("c) O número 5 NÃO está na lista.")
