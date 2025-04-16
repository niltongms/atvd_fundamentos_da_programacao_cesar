nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
freq = float(input("Qual a frequência, em porcentagem, do aluno: "))

media = (nota1 + nota2)/2

if media >= 7 and freq >=75:
    print("O aluno foi aprovado com média", media)

elif media <7 and freq >=75:
    print("O aluno foi reprovado por média")

elif media >=7 and freq <75:
    print("O aluno foi reprovado por faltas")

else:
    print("O aluno foi reprovado por faltas e por média")

