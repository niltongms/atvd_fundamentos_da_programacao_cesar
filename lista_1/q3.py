m2 = float(input("Qual o tamanho do terreno em metros quadrados? "))

if m2 < 100:
    print("TERRENO POPULAR")
elif m2 >= 100 and m2 <=500:
    print("TERRENO MASTER")
else:
    print("TERRENO VIP")