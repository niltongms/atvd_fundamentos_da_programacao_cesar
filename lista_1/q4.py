temp = float(input("Insira a temperatura que deseja converter"))
grau = input("Digite C se a quer converter de Fahrenheit para Celsius ou F se quer converter de Celsius para Fahrenheit")
convert = 0

if grau == "F":
    convert = ((temp * 9)/5) + 32
    print("Convertendo",temp,"de Fahrenheit para Celsius temos:", convert,"graus celsius")
elif grau == "C":
    convert = ((temp - 32) * 5)/9
    print("Convertendo",temp,"de Celsius para Fahrenheit temos:", convert,"graus Fahrenheit")

