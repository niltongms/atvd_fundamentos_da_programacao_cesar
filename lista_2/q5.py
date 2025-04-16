tabuada = int(input("Digite o número que você quer ver a tabuada: "))
comeco = int(input("Digite onde começa"))
termino = int(input("Digite onde termina"))

for i in range(comeco, termino + 1):
    print(f"{tabuada} x {i} = {tabuada * i}")
