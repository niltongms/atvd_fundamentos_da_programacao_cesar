def escrever_votos():
    arquivo = open("votacao.txt", "w")  # abre o arquivo para escrita
    for i in range(10):
        while True:
            voto = input(f"Voto {i+1} - Digite 1 (Star Wars) ou 2 (Star Trek): ")
            if voto in ["1", "2"]:
                arquivo.write(voto + "\n")
                break
            else:
                print("Voto inválido. Tente novamente.")
    arquivo.close()  # fecha o arquivo após escrever

def apurar_resultado():
    votos_star_wars = 0
    votos_star_trek = 0

    arquivo = open("votacao.txt", "r")  # abre o arquivo para leitura
    for linha in arquivo:
        voto = linha.strip()
        if voto == "1":
            votos_star_wars += 1
        elif voto == "2":
            votos_star_trek += 1
    arquivo.close()  # fecha o arquivo após ler

    print("\nResultado da votação:")
    print(f"Star Wars: {votos_star_wars} votos")
    print(f"Star Trek: {votos_star_trek} votos")

    if votos_star_wars > votos_star_trek:
        print("Filme mais votado: Star Wars")
    elif votos_star_trek > votos_star_wars:
        print("Filme mais votado: Star Trek")
    else:
        print("Empate entre os filmes!")

# Execução do programa
escrever_votos()
apurar_resultado()
