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

