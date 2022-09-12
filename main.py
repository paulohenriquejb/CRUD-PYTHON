from fileinput import close
import mysql.connector


def inserir():
    print("########## CADASTRANDO CLIENTE \n")
    nome1 = input('digite o nome do Cliente: ')
    endereco1 = input('digite o endereco do cliente: ')
    nome1 = nome1.upper()
    endereco1 = endereco1.upper()
    cursor.execute(f"INSERT INTO cadastro_clientes(nome, endereco) VALUES ('{nome1}', '{endereco1}') ")
    conexao.commit()
    print('\n \n cadastro concluido com sucesso')
    
def excluir():
    print(" ############ Excluindo cadastro ##############")
    print('Qual cliente deseja excluir') 
    codigoCliente = int(input('Digite o codigo: '))
    cursor.execute(f"DELETE FROM cadastro_clientes WHERE codigocli = {codigoCliente}")
    conexao.commit()
    print('Excluido com sucesso')

def atualizar():
    print(" ############ atualizando cadastro ##############")
    print('Qual cliente deseja atualizar') 
    codigoCliente1 = int(input('Digite o codigo de cliente: '))
    nome2 = input('Digite o nove nome: ')
    endereco2 = input('digite novo endereco')
    cursor.execute(f"UPDATE cadastro_clientes SET nome = '{nome2}', endereco = '{endereco2}' WHERE codigocli = {codigoCliente1} ")
    conexao.commit()



conexao = mysql.connector.connect(
    host='localhost',
    user='',
    password='',
    database='phtreinamentos'
   
    
)

cursor = conexao.cursor()
#myscursor.execute("CREATE DATABASE phtreinamentos")
#print('Sql executado com sucesso')

#myscursor.execute("CREATE TABLE cadastro_clientes (codigocli INTEGER AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(120), endereco VARCHAR(150))")
#print('tabela criada com sucesso')

print('############## SISTEMA BASICO DE VENDAS ######################')
print('1 - Clientes')
print('2 - Vendas')
escolha = int(input('Escolha uma das opções: '))
if escolha == 1 :
    print('1A - Cadastrar')
    print('2A - Atualizar')
    print('3A - Excluir ')
    escolha2 = input(' Digite a opção desejada: ')
while escolha2 != '1A' and escolha2 != "2A" and escolha2 != '3A' :
    print('1A - Cadastrar')
    print('2A - Atualizar')
    print('3A - Excluir ')
    escolha2 = input(' Escolha entre as opções a cima: ')
if escolha2 == '1A':
    inserir() 
elif escolha2 == '2A':
    atualizar()
elif escolha2 == '3A':
    excluir()


                  
cursor.close()
conexao.close()

