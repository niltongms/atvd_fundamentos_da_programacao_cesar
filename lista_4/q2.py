def filtrar(lista, lim_inf, lim_sup):
    return [n for n in lista if lim_inf <= n <= lim_sup]

# Lê 10 números
numeros = []
for i in range(10):
    numeros.append(int(input("Digite um número: ")))

# Lê os limites
lim_inf = int(input("Limite inferior: "))
lim_sup = int(input("Limite superior: "))

# Chama a função e mostra o resultado
filtrados = filtrar(numeros, lim_inf, lim_sup)
print("Números no intervalo:", filtrados)
