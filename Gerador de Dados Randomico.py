#Comentar tudo selecionado Shift + Alt + A
#Documentação do Fake: https://faker.readthedocs.io/en/master/#
# Desenvolvedor Peterson Mendonça de Oliveira
# Objetivo desse codigo é gerar dados randomicos para meu banco de dados Mysql

""" 
Standard Providers Fake
faker.providers
faker.providers.address
faker.providers.automotive
faker.providers.bank
faker.providers.barcode
faker.providers.color
faker.providers.company
faker.providers.credit_card
faker.providers.currency
faker.providers.date_time
faker.providers.file
faker.providers.geo
faker.providers.internet
faker.providers.isbn
faker.providers.job
faker.providers.lorem
faker.providers.misc
faker.providers.person
faker.providers.phone_number
faker.providers.profile
faker.providers.python
faker.providers.ssn
faker.providers.user_agent

"""

from faker import Faker
import csv
import random

fake_data = Faker('pt_BR')

"""     
    #Metodos pré-feitos de teste
    #Cria numero randomico
    cpf = fake_data.random_number(digits=11); print(cpf)

    #Cria um nome Falso
    name = fake_data.name(); print(name)

    #Cria um Endereço Falso
    addres = fake_data.address(); print(addres)

    #Cria um telefone
    phone = fake_data.msisdn(); print(phone)

    #Cria um email Falso
    email = fake_data.safe_email(); print(email)

    #Cria numero randomico
    cep = fake_data.random_number(digits=7); print(cep) 
"""

#INSERTS DE CLIENTES
""" 
#Cria arquivo de texto de nome arq01.txt
with open('Inserts_clientes.sql', 'w') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(1,100000):

        #Cria numero randomico
        cpf = fake_data.random_number(digits=11, fix_len=True); 

        #Cria um nome Falso
        name = fake_data.name(); 

        #Cria um telefone
        phone = fake_data.msisdn(); 

        #Cria numero randomico
        cep = fake_data.random_number(digits=7, fix_len=True); 

        #print('INSERT INTO clientes (cpf,nome, telefone, cep) VALUES ("{}", "{}", "{}", "{}");'.format(cpf,name,phone,cep)) 

        # Informação a ser passada para o arquivo de texto
        arquivo.write('INSERT INTO clientes (cpf,nome, telefone, cep) VALUES ("{}", "{}", "{}", "{}"\n);'.format(cpf,name,phone,cep))
"""


#INSERTS DE EDITORA
""" 
#Cria arquivo de texto de nome arq01.txt
with open('Inserts_editoras.sql', 'w') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(1,100000):

        #Cria nome de empresa randomico
        editora_nome = fake_data.company(); 

        #Cria um telefone
        phone = fake_data.msisdn(); 

        #Cria numero randomico
        cnpj = fake_data.random_number(digits=14, fix_len=True); 

        #Cria numero randomico
        cep = fake_data.random_number(digits=7, fix_len=True); 

        #print('INSERT INTO editoras (nome, telefone, cnpj, cep) VALUES ("{}", "{}", "{}", "{}");'.format(editora_nome,phone,cnpj,cep)) 

        # Informação a ser passada para o arquivo de texto
        arquivo.write('INSERT INTO editoras (nome, telefone, cnpj, cep) VALUES ("{}", "{}", "{}", "{}");\n'.format(editora_nome,phone,cnpj,cep))
 """

""" 
#INSERTS DE LIVROS

#Cria arquivo de texto de nome arq01.txt
#O motivo pelo qual está funcionando é porque a codificação é alterada para UTF-8 ao usar o arquivo, 
#então os caracteres em UTF-8 podem ser convertidos em texto, em vez de retornar um erro quando encontra um caractere UTF-8 
#que é não é compatível com a codificação atual.

with open('Inserts_livros.sql', 'w', encoding='utf-8') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(1, 100000):

        #Cria nome de empresa randomico - Usado como titulo
        titulo = fake_data.company(); 

        #Cria um nome Autor Falso
        autor = fake_data.name(); 

        #Cria numero genero
        genero = fake_data.currency_name(); 

        #Cria numero id de editora
        editora_id = random.randrange(1,100000); 

        #print('INSERT INTO livros (titulo, autor, genero, editora_id) VALUES ("{}", "{}", "{}", "{}");'.format(titulo,autor,genero,editora_id)) 

        # Informação a ser passada para o arquivo de texto
        arquivo.write('INSERT INTO livros (titulo, autor, genero, editora_id) VALUES ("{}", "{}", "{}", "{}");\n'.format(titulo,autor,genero,editora_id))
 """

#INSERTS DE CARRINHO_LOJA
""" 
#Cria arquivo de texto de nome arq01.txt
with open('carrinho_loja.sql', 'w') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(1,100000):

        #Cria numero livro_id
        livro_id = random.randrange(100000); 

        #Cria numero cliente_id
        cliente_id = random.randrange(100000); 

        #Cria numero randomico cnpj
        cnpj = fake_data.random_number(digits=14, fix_len=True); 

        #Cria nome de empresa randomico - Usado como titulo
        preco = random.uniform(0.0,800.00)

        #Cria numero id de editora
        quantidade = random.randrange(1000); 

        #print('INSERT INTO carrinho_loja (livro_id, cliente_id, cnpj, preco, quantidade) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(livro_id,cliente_id,cnpj,preco,quantidade)) 

        # Informação a ser passada para o arquivo de texto
        arquivo.write('INSERT INTO carrinho_loja (livro_id, cliente_id, cnpj, preco, quantidade) VALUES ("{}", "{}", "{}", "{}", "{}");\n'.format(livro_id,cliente_id,cnpj,preco,quantidade))

 """