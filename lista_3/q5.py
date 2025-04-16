repteis = []
mamífero = []
aves = []
outros = []

for i in range(10): 
    nome = input("Escreva o nome do animal: ")
    cat = input("Em qual categoria ele se insere: 1 - Réptil, 2 - Mamífero, 3 - Ave, 4 – Outro: ")

    if cat == '1':
        repteis.append(nome)
    elif cat == '2':
        mamífero.append(nome)
    elif cat == '3': 
        aves.append(nome)
    elif cat =='4':
        outros.append(nome)
    else:
        print("Opção Inválida! Digite uma das opções indicadas")

print("Você digitou os seguintes reptéis: ", repteis, "Quantidade", len(repteis))
print("Você digitou os seguintes mamíferos: ", mamífero, "Quantidade", len(mamífero))
print("Você digitou as seguintes aves: ", aves, "Quantidade", len(aves))
print("E esses se encaixam em outras categorias: ", outros, "Quantidade", len(outros))


