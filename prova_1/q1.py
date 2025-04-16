A = []
B = []
C = []
D = []


for i in range(10):
    nome = input("Qual o nome do aluno? ")
    al = input("Em qual turma deseja se matricular: A, B, C ou D: ")

    if al == 'A':
        A.append(nome)
    elif al == 'B':
        B.append(nome)
    elif al == 'C':
        C.append(nome)
    elif al == 'D':
        D.append(nome)
    else:
        print("Escolha um opção válida")


print(f"Foram inscritos {len(A)} alunos na turma A e a turma arrecadou R$ {len(A)*75.00} de mensalidade")
print(f"Foram inscritos {len(B)} alunos na turma B e a turma arrecadou R$ {len(B)*58.00} de mensalidade")
print(f"Foram inscritos {len(C)} alunos na turma C e a turma arrecadou R$ {len(C)*44.00} de mensalidade")
print(f"Foram inscritos {len(D)} alunos na turma D e a turma arrecadou R$ {len(D)*50.00} de mensalidade")
