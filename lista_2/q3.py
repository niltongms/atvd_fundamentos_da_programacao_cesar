pessoas = 6
maior18 = 0
menor18 = 0
soma = 0

for i in range(pessoas):
    idade = int(input("Qual a idade da pessoa? "))
    soma += idade
    if idade >= 18:
        maior18 +=1
    else:
        menor18 +=1

print(maior18,"pessoas eram maiores de 18 anos")
print(menor18,"pessoas eram menores de 18 anos")
print("A media das idades foi: ", soma/pessoas)


