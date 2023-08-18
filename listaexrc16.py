'''
1 Crie um dicionário d e coloque nele seus dados: nome, idade,
telefone,endereço. Usando o dicionário d criado anteriormente, imprima
seu nome.
'''

lista = {"nome":"gabriel","idade":18 ,"tel":71992742146 , "end":"Rua Antonio Rubens 80"}
print(lista["nome"])

'''

2 Crie um dicionário d e coloque nele os dados fornecidos pelo usuário:
nome, idade, telefone,endereço. Também usando d, imprima todos os
itens do dicionário no formato chave : valor, ordenado pela chave
'''
lista2 = {}
lista2['nome'] = input("Informe seu nome:")
lista2["idade"] = int(input("Informe sua idade:"))
lista2["tel"] = int(input("Informe seu tel:"))
lista2["endereco"] = input("Informe seu enfreço:")
print(lista2)
'''
3 Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
chave (cpf), nome, idade, telefone. O programa deve ler um número
indeterminado de dados, criar a agenda e imprimir todos os itens do
dicionário no formato chave: nome-idadefone.
'''
agenda = {}
for i in range(5):
 agenda["cpf"] = input("digite seu cpf")
 agenda["nome"] = input("digite seu nome")
 agenda["tel"] = input("digite seu tel")
 i =i+1
print(agenda)

4) Crie um programa que cadastre informações de várias pessoas (nome,
idade e cpf) e depois coloque em um dicionário. Depois remova todas as
pessoas menores de 18 anos do dicionário e coloque em outro dicionário.
'''
lista4 ={}
for i in range(5):
 lista4["cpf"] = input("digite seu cpf")
 lista4["nome"] = input("digite seu nome")
 lista4["tel"] = input("digite seu tel")
 i =i+1
print(lista4)


'''
5 Considere um sistema onde os dados são armazenados em dicionários.
Nesse sistema existe um dicionario principal e o dicionário de backup.
Cada vez que o dicionário principal atinge tamanho 5, ele imprime os
dados na tela e apaga o seu conteúdo. Crie um programa que insira dados
em um dicionário, realizando o backup a cada dado e excluindo os dados
do dicionário principal quando ele atingir tamanho 5.
'''
def realizar_backup(dicionario_principal, dicionario_backup):
    dicionario_backup.update(dicionario_principal)
    dicionario_principal.clear()

def main():
    dicionario_principal = {}
    dicionario_backup = {}
    contador = 1

    while True:
        nome = input("Digite o nome : ")
        idade = int(input("Digite a idade da pessoa: "))
        cpf = input("Digite o CPF : ")
        pessoa = {'nome': nome, 'idade': idade, 'cpf': cpf}
        dicionario_principal[cpf] = pessoa

        if len(dicionario_principal) >= 5:
            print(f"\nRealizando backup {contador}")
            realizar_backup(dicionario_principal, dicionario_backup)
            contador += 1

        print("\nDicionário Principal:")
        for cpf, pessoa in dicionario_principal.items():
            print(f"CPF: {cpf}, Pessoa: {pessoa}")

        print("\nDicionário de Backup:")
        for cpf, pessoa in dicionario_backup.items():
            print(f"CPF: {cpf}, Pessoa: {pessoa}")

if __name__ == "__main__":
    main()


'''
6) Escreva uma função que conta a quantidade de vogais em um texto e
armazena tal quantidade em um dicionário, onde a chave é a vogal
considerada.

'''
def cacavogais():
 a = 0
 j = 0
 string = str(input("Digite um nome: "))
 for a in string:
  if a.lower() in string:
   j += 1
 print("A string digitada foi: {}".format(string))
 print("A quantidade de vogais que possui é {}".format(j))

cacavogais()

'''
7) Escreva um programa que lê duas notas de vários alunos e armazena tais
notas em um dicionário, onde a chave é o nome do aluno. A entrada de
dados deve terminar quando for lida uma string vazia como nome.
Escreva uma função que retorna a média do aluno, dado seu nome.
'''
nota= {}
nome ={}
while nome != "":
 nome["Nome"] = input("Digite seu nome: ")
 nota[nome["Nome"]] =input("digite sua primeira nota: ")
 nota[nome["Nome"]] =input("digite sua segunda nota: ")
 print(nota)

'''
8)Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Escreva um programa que leia todos os tempos em segundos e os guarde
em um dicionário, onde a chave é o nome do corredor. Ao final diga de
quem foi a melhor volta da prova e em que volta; e ainda a classificação
final em ordem (1o o campeão). O campeão é o que tem a menor média
de tempos.

'''

def calcular_media_tempos(tempos):
    return sum(tempos) / len(tempos)

def main():
    corredores = {
        "Corredor 1": [],
        "Corredor 2": [],
        "Corredor 3": [],
        "Corredor 4": [],
        "Corredor 5": [],
        "Corredor 6": []
    }

    for corredor in corredores:
        print(f"Digite os tempos das 10 voltas para {corredor}:")
        for volta in range(1, 11):
            tempo = float(input(f"Volta {volta}: "))
            corredores[corredor].append(tempo)

    resultados = {}

    for corredor, tempos in corredores.items():
        media_tempo = calcular_media_tempos(tempos)
        resultados[corredor] = media_tempo

    classificacao_final = sorted(resultados.items(), key=lambda x: x[1])

    print("\nClassificação Final:")
    for posicao, (corredor, media_tempo) in enumerate(classificacao_final, start=1):
        print(f"{posicao}º lugar: {corredor} - Média de Tempos: {media_tempo:.2f} segundos")

    melhor_corredor = classificacao_final[0][0]
    melhor_tempo = min(corredores[melhor_corredor])
    volta_melhor_tempo = corredores[melhor_corredor].index(melhor_tempo) + 1

    print(f"\nMelhor volta da prova:")
    print(f"Corredor: {melhor_corredor}")
    print(f"Volta: {volta_melhor_tempo}")
    print(f"Tempo: {melhor_tempo:.2f} segundos")

if __name__ == "__main__":
    main()


