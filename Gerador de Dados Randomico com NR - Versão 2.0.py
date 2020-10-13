# Comentar tudo selecionado Shift + Alt + A
# Documentação do Fake: https://faker.readthedocs.io/en/master/#
# Desenvolvedor Peterson Mendonça de Oliveira
# Versão 1.0 - Gerador de Dados para Banco Relacional
# Versão 2.0 - Inserção e Geração de Dados para Banco Relacional e Não-Relacional
# Objetivo desse codigo é gerar dados randomicos para meu banco de dados Mysql

# Ferramentas da Biblioteca
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


from itertools import count
from faker import Faker
import csv
import random
import pymysql
import time
import pymongo

fake_data = Faker('pt_BR')

######################################################### VERSÃO 1.0 #########################################################

# BANCO RELACIONAL

"""
    drop database loja;

    create database if not exists loja;

    use loja;

    create table if not exists clientes(
        id bigint unsigned primary key not null auto_increment,
        cpf varchar (255) not null,
        nome varchar (255) not null,
        telefone varchar (255) not null,
        cep varchar (255) not null
    );

    create table if not exists editoras(
        id bigint unsigned primary key not null auto_increment,
        nome varchar (255) not null,
        telefone varchar (255) not null,
        cnpj varchar (255) not null,
        cep varchar (255) not null
    );

    create table if not exists livros(
        id bigint unsigned primary key not null auto_increment,
        titulo varchar (255) not null,
        autor varchar (255) not null,
        genero varchar (255) not null,
        editora_id bigint unsigned not null,
        constraint editora_id foreign key (editora_id) references editoras(id)
    );

    create table if not exists carrinho_loja(
        id bigint unsigned primary key not null auto_increment,
        livro_id bigint unsigned not null,
        cliente_id bigint unsigned not null,
        cnpj varchar (255) not null,
        preco double (8,2) not null,
        quantidade int (10) not null,
        constraint livro_id foreign key (livro_id) references livros(id),
        constraint cliente_id foreign key (cliente_id) references clientes(id)
    );
"""

# BANCO NÃO-RELACIONAL
"""
db.clientes.insert({ 
	cpf: "45137449809",
	nome: "Peterson Mendonça",
	telefone: "34249871",
	cep: "13487013",
	pedidos:
		{
		preco: 39.90,
		quantidade: 40,
		livros:
			{
			titulo: "A volta dos que não foram 2",
			autor: "Jack Black",
			genero: "Aventura",
			editora:
				{
				nome: "The Time 2",
				telefone: "97865421",
				cnpj: "56842521384985",
				cep: "13254287"
				}
			}
		}
})
"""


# GERADOR DE DADOS PARA O BANCO RELACIONAL

#INSERTS DE CLIENTES
'''  
with open('Inserts_clientes.sql', 'w') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(0,20000):

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
        arquivo.write('INSERT INTO clientes (cpf,nome, telefone, cep) VALUES ("{}", "{}", "{}", "{}");\n'.format(cpf,name,phone,cep))
 '''

#INSERTS DE EDITORA
'''  
with open('Inserts_editoras.sql', 'w') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(0,20000):

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
 '''
 
#INSERTS DE LIVROS
''' 
with open('Inserts_livros.sql', 'w', encoding='utf-8') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(0,20000):

        #Cria nome de empresa randomico - Usado como titulo
        titulo = fake_data.company(); 

        #Cria um nome Autor Falso
        autor = fake_data.name(); 

        #Cria numero genero
        genero = fake_data.currency_name(); 

        #Cria numero id de editora
        editora_id = random.randrange(1,20000); 

        #print('INSERT INTO livros (titulo, autor, genero, editora_id) VALUES ("{}", "{}", "{}", "{}");'.format(titulo,autor,genero,editora_id)) 

        # Informação a ser passada para o arquivo de texto
        arquivo.write('INSERT INTO livros (titulo, autor, genero, editora_id) VALUES ("{}", "{}", "{}", "{}");\n'.format(titulo,autor,genero,editora_id))
 '''

#INSERTS DE CARRINHO_LOJA
''' 
with open('carrinho_loja.sql', 'w') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(0,20000):

        #Cria numero livro_id
        livro_id = random.randrange(1,20000); 

        #Cria numero cliente_id
        cliente_id = random.randrange(1,20000); 

        #Cria numero randomico cnpj
        cnpj = fake_data.random_number(digits=14, fix_len=True); 

        #Cria nome de empresa randomico - Usado como titulo
        preco = random.uniform(0.0,800.00)

        #Cria numero id de editora
        quantidade = random.randrange(10000); 

        #print('INSERT INTO carrinho_loja (livro_id, cliente_id, cnpj, preco, quantidade) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(livro_id,cliente_id,cnpj,preco,quantidade)) 

        # Informação a ser passada para o arquivo de texto
        arquivo.write('INSERT INTO carrinho_loja (livro_id, cliente_id, cnpj, preco, quantidade) VALUES ("{}", "{}", "{}", "{}", "{}");\n'.format(livro_id,cliente_id,cnpj,preco,quantidade))
 '''



# GERADOR DE DADOS PARA O BANCO NÃO-RELACIONAL
''' 
with open('Inserts_clientes_Nrelacional.txt', 'w', encoding='utf-8') as arquivo:

    # Grande geração de lista \ Tabela Cliente
    for _ in range(0,2000000):
        resu = 0

        cpf_cli = fake_data.random_number(digits=11, fix_len=True)

        nome = fake_data.name()

        telefone = fake_data.msisdn()

        cep = fake_data.random_number(digits=7, fix_len=True)

        preco1 = random.uniform(0.0,800)
        preco = round(preco1,2)

        quantidade = random.randrange(2000)

        titulo = fake_data.company()

        autor = fake_data.name()

        genero = fake_data.currency_name()
        
        nome2 = fake_data.company()

        telefone2 = fake_data.msisdn()

        cnpj = fake_data.random_number(digits=14, fix_len=True); 

        cep2 = fake_data.random_number(digits=7, fix_len=True)

        part1 = ('db.clientes.insert({')
        part2 = ('cpf: "{}", '.format(cpf_cli))
        part3 = ('nome: "{}", '.format(nome))
        part4 = ('telefone: "{}", '.format(telefone))
        part5 = ('cep: "{}", '.format(cep))
        part6 = ('pedidos: { ')
        part7 = ('preco: {}, '.format(preco))
        part8 = ('quantidade: {}, '.format(quantidade))
        part9 = ('livros: { ')
        part10 = ('titulo: "{}", '.format(titulo))
        part11 = ('autor: "{}", '.format(autor))
        part12 = ('genero: "{}", '.format(genero))
        part13 = ('editora: { ')
        part14 = ('nome: "{}", '.format(nome2))
        part15 = ('telefone: "{}", '.format(telefone2))
        part16 = ('cnpj: "{}", '.format(cnpj))
        part17 = ('cep: "{}"'.format(cep2))
        part18 = (' } } } })\n')

        resu = part1+part2+part3+part4+part5+part6+part7+part8+part9+part10+part11+part12+part13+part14+part15+part16+part17+part18

        #print(resu)

        # Informação a ser passada para o arquivo de texto
        arquivo.write(resu)
 '''




######################################################### VERSÃO 2.0 #########################################################



# INSERÇÃO E GERAÇÃO DE DADOS DIRETO NO MYSQL

# Conexão com o Banco de dados MYSQL
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'undertaker1234'
)

cursor = conexao.cursor()

''' 
# Execulta um show table no mysql
#cursor.execute("SHOW DATABASES")

#for x in cursor:
#    print(x)


# Ira criar um banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS loja7")

# Ira acessar o banco criado
cursor.execute("USE loja7")

# Ira criar as tabelas
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, cpf VARCHAR (255) NOT NULL, nome VARCHAR (255) NOT NULL, telefone VARCHAR (255) NOT NULL, cep VARCHAR (255) NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS editoras (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, nome VARCHAR (255) NOT NULL, telefone VARCHAR (255) NOT NULL, cnpj VARCHAR (255) NOT NULL, cep VARCHAR (255) NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS livros (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, titulo VARCHAR (255) NOT NULL, autor VARCHAR (255) NOT NULL, genero VARCHAR (255) NOT NULL, editora_id BIGINT NOT NULL, CONSTRAINT editora_id FOREIGN KEY (editora_id) REFERENCES editoras(id))")
cursor.execute("CREATE TABLE IF NOT EXISTS carrinho_loja (id BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, livro_id BIGINT NOT NULL, cliente_id BIGINT NOT NULL, cnpj VARCHAR (255) NOT NULL, preco double (8,2) NOT NULL, quantidade int (10) NOT NULL, CONSTRAINT livro_id FOREIGN KEY (livro_id) REFERENCES livros(id), CONSTRAINT cliente_id FOREIGN KEY (cliente_id) REFERENCES clientes(id))")
 
#INSERTS DE CLIENTES

for _ in range(0,25350):

    #Cria numero randomico
    cpf = fake_data.random_number(digits=11, fix_len=True); 

    #Cria um nome Falso
    name = fake_data.name(); 

    #Cria um telefone
    phone = fake_data.msisdn(); 

    #Cria numero randomico
    cep = fake_data.random_number(digits=7, fix_len=True); 

    # Ira inserir os dados no Mysql
    cursor.execute('INSERT INTO clientes (cpf,nome, telefone, cep) VALUES ("{}", "{}", "{}", "{}");\n'.format(cpf,name,phone,cep))


#INSERTS DE EDITORA

for _ in range(0,25350):

    #Cria nome de empresa randomico
    editora_nome = fake_data.company(); 

    #Cria um telefone
    phone = fake_data.msisdn(); 

    #Cria numero randomico
    cnpj = fake_data.random_number(digits=14, fix_len=True); 

    #Cria numero randomico
    cep = fake_data.random_number(digits=7, fix_len=True); 

    # Ira inserir os dados no Mysql
    cursor.execute('INSERT INTO editoras (nome, telefone, cnpj, cep) VALUES ("{}", "{}", "{}", "{}");\n'.format(editora_nome,phone,cnpj,cep))

 
#INSERTS DE LIVROS

for _ in range(0,25350):

    #Cria nome de empresa randomico - Usado como titulo
    titulo = fake_data.company(); 

    #Cria um nome Autor Falso
    autor = fake_data.name(); 

    #Cria numero genero
    genero = fake_data.currency_name(); 

    #Cria numero id de editora
    editora_id = random.randrange(1,25350); 

    # Informação a ser passada para o arquivo de texto
    cursor.execute('INSERT INTO livros (titulo, autor, genero, editora_id) VALUES ("{}", "{}", "{}", "{}");\n'.format(titulo,autor,genero,editora_id))


#INSERTS DE CARRINHO_LOJA

for _ in range(0,25350):

    #Cria numero livro_id
    livro_id = random.randrange(1,25350); 

    #Cria numero cliente_id
    cliente_id = random.randrange(1,25350); 

    #Cria numero randomico cnpj
    cnpj = fake_data.random_number(digits=14, fix_len=True); 

    #Cria nome de empresa randomico - Usado como titulo
    preco = random.uniform(0.0,800.00)

    #Cria numero id de editora
    quantidade = random.randrange(10000); 

    cursor.execute('INSERT INTO carrinho_loja (livro_id, cliente_id, cnpj, preco, quantidade) VALUES ("{}", "{}", "{}", "{}", "{}");\n'.format(livro_id,cliente_id,cnpj,preco,quantidade))


# Grava todas as alterações das tabelas
conexao.commit()

 '''

# MEDIR TEMPO DE BUSCA MYSQL
""" 
cursor.execute("USE loja7")

inicio = time.time()

busca = cursor.execute("select clientes.cpf, clientes.nome, clientes.telefone, clientes.cep, editoras.nome, editoras.telefone, editoras.cnpj, editoras.cep, livros.titulo, livros.autor, livros.genero, carrinho_loja.id, carrinho_loja.livro_id, carrinho_loja.cliente_id, carrinho_loja.cnpj, carrinho_loja.preco, carrinho_loja.quantidade from carrinho_loja inner join clientes on carrinho_loja.cliente_id = clientes.id inner join livros on carrinho_loja.livro_id = livros.id inner join editoras on editoras.id = livros.editora_id;")

fim = time.time()

#for x in cursor:
#    print(x)

print("Tempo: ",fim - inicio)

 """





# INSERÇÃO E GERAÇÃO DE DADOS DIRETO NO MONGODB

# Efetua a conexão no banco de dados
client = pymongo.MongoClient('localhost', 27017)

# Verifica os bancos de Dados existentes
#print(client.list_database_names())

""" 
# Criar / Usar dados no MongoDB
db = client.loja6

nun = 0

# Grande geração de lista \ Tabela Cliente
for _ in range(0,13000000):
    
    nun = nun + 1

    cpf_cli = str(fake_data.random_number(digits=11, fix_len=True))
    
    nome_cli = fake_data.name()

    telefone_cli = fake_data.msisdn()

    cep_cli = str(fake_data.random_number(digits=7, fix_len=True))

    preco1 = random.uniform(0.0,800)
    preco = round(preco1,2)

    quantidade = str(random.randrange(1,2000))

    titulo = fake_data.company()

    autor = fake_data.name()

    genero = fake_data.currency_name()
        
    nome2 = fake_data.company()

    telefone2 = fake_data.msisdn()

    cnpj = str(fake_data.random_number(digits=14, fix_len=True))

    cep2 = str(fake_data.random_number(digits=7, fix_len=True))

# Inserção dos dados no bando de dados
    db.clientes.insert_many(
        [
            { 
            "_id": nun,
            "cpf": cpf_cli,
            "nome": nome_cli,
            "telefone": telefone_cli,
            "cep": cep_cli,
            "pedidos":
                {
                "preco": preco,
                "quantidade": quantidade,
                "livros":
                    {
                    "titulo": titulo,
                    "autor": autor,
                    "genero": genero,
                    "editora":
                        {
                        "nome": nome2,
                        "telefone": telefone2,
                        "cnpj": cnpj,
                        "cep": cep2
                        }
                    }
                }
            }
        ]
    )

 """

# MEDIR TEMPO DE BUSCA MONGODB

# Opção com retorno do texto selecionado
""" 
db = client.loja6

SomaTempo = 0

for i in range(13000000):
    
    inicio = time.time()

    clientes = db.clientes.find()

    fim = time.time()
    
    SomaTempo = SomaTempo + (fim - inicio)    

print("Tempo: ",SomaTempo)
 """