# Lê a data de nascimento
dia = input("Digite o dia de nascimento (dd): ")
mes = input("Digite o mês de nascimento (mm): ")
ano = input("Digite o ano de nascimento (aaaa): ")

# Gera partes da senha
dia_invertido = dia[::-1]
mes_invertido = mes[::-1]

# Monta a senha
senha = mes + '$' + dia_invertido + '#' + dia + '!' + mes_invertido + '*' + ano

# Mostra a senha gerada
print("\nSenha gerada:", senha)

