qtd_caixao = 0
code_caix = 0


while code_caix != -1:
    code_caix = int(input("Digite o código do Caixão: "))

    if code_caix != -1:
        qtd_caixao +=1
 

print("Temos", qtd_caixao,"caixões cadastrados")