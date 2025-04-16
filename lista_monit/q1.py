temp_media = []
temp_20 = []
temp_acima_media = []


for i in range(12):
    temp_mes = float(input(f"Digite a temperátura média do {i+1}º mês: "))
    temp_media.append(temp_mes)
    media = sum(temp_media)/12

    if temp_mes < 20:
        temp_20.append(temp_mes)
    elif temp_mes > media:
        temp_acima_media.append(temp_mes)

print (f"A média anual de temperatura foi: {media}")
print(f"As temperaturas acima da média anual foram: {temp_acima_media}")
print(f"{len(temp_20)} temperaturas foram abaixo de 20º")
print(f"A maior temperatura foi {max(temp_media)}º e a menor temperatura foi {min(temp_media)}º")
