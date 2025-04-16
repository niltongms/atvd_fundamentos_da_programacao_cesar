numeros = []
qdd = []

for i in range (10):
    n = float(input(f"Digite aqui seu {i+1}º número: "))
    numeros.append(n)
    qdd.append(n ** 2)


print("O vetor original é: ", numeros)
print("O vetor com os quadrados de cada elemento é: ", qdd)

