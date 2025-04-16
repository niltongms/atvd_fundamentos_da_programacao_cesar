
C = []
R = []
S = []
total = []

for i in range(12):
    coelho = float(input(f"Quantas coelhos foram usados de cobaia no experimento do {i+1}º mês:? "))
    rato = float(input(f"Quantas ratos foram usados de cobaia no experimento do {i+1}º mês:?"))
    sapo = float(input(f"Quantas sapos foram usados de cobaia no experimento do {i+1}º mês:? "))
    total_mes = (coelho + rato + sapo)


    total.append(total_mes)
    C.append(coelho)
    R.append(rato)
    S.append(sapo)

soma_coelho = sum(C)
soma_rato = sum(R)
soma_sapo = sum(S)

print(f"O total de cobaias utilizadas no ano foi: {sum(total):.0f}")
print(f"O total de coelhos foi: {soma_coelho:.0f}")
print(f"O total de ratos foi: {soma_rato:.0f}")
print(f"O total de sapos foi: {soma_sapo:.0f}")

print(f"Percentual de coelhos: {(soma_coelho/sum(total)) * 100:.2f}%")
print(f"Percentual de ratos: {(soma_rato/sum(total)) * 100:.2f}%")
print(f"Percentual de sapos: {(soma_sapo/sum(total)) * 100:.2f}%")