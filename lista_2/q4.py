
for i in range (6):
    cod = int(input("Digite o código do produto: "))
    valor = float(input("Digite o valor unitário do produto:"))
    qtd = int(input("Digite a quantidade de produtos"))

    if qtd <= 2:
        print("O desconto foi de 40%")
        valor = valor * (40/100)
        print("O novo valor unitário é: ", valor)
    elif qtd > 2 and qtd <= 5:
        print("O desconto foi de 30%")
        valor = valor * (30/100)
        print("O novo valor unitário é: ", valor)
    elif qtd > 5 and qtd <= 9:
        print("O desconto foi de 20%")
        valor = valor * (20/100)
        print("O novo valor unitário é: ", valor)
    else:
        print("O desconto foi de 10%")
        valor = valor * (10/100)
        print("O novo valor unitário é: ", valor)
