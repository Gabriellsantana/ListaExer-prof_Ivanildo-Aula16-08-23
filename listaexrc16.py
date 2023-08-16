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

