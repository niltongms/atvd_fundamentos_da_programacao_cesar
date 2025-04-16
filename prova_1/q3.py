salario = float(input("Digite aqui o seu salário: "))

if salario < 1500:
    print("Faixa salarial 1")
elif salario >= 1500 and salario < 3000:
    print("Faixa Salarial 2")
elif salario >= 3000 and salario < 5000:
    print("Faixa Salarial 3")
else:
    print("Faixa Salarial 4")