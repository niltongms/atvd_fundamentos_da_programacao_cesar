def imprimir_sequencias():
    while True:
        x = int(input("Digite um número (0 para sair): "))
        if x == 0:
            break
        for i in range(1, x + 1):
            print(i, end=" ")
        print()  # quebra de linha após cada sequência

# Chamada da função
imprimir_sequencias()
