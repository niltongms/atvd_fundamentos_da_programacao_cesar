votos = [0, 0, 0, 0]

while True:
    voto = int(input("1-Windows, 2-Linux, 3-Mac, 4-Outro (0 para sair): "))

    if voto == 0:
        break
    elif 1 <= voto <= 4:
        votos[voto - 1] += 1
    else:
        print("Voto inválido!")

print("\nResultado da Enquete:")
print("Windows Server:", votos[0])
print("Linux:", votos[1])
print("Mac OS:", votos[2])
print("Outro:", votos[3])