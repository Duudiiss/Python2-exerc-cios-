# -*- coding: utf-8 -*-
"""

@author: Joisa

Exercicios de Revisao para o Teste2 - 2022/2


"""

'''
EXERCÍCIO DE TUPLA
Ex1) Uma transportadora faz entregas para empresas, transportando caixas contendo os produtos a serem entregues. 
Cada caixa tem identificação, dimensões em cm (comprimento, altura, largura) e peso em Kg. As dimensões são 
representadas por uma tupla de 3 elementos: (comprimento, altura, largura). A caixa é representada por uma tupla 
de 3 elementos: (identificação, dimensões, peso).

O valor cobrado por caixa depende do volume e do peso da caixa, de acordo com a descrição abaixo:
•	volume até 8000 cm3 (inclusive) e peso até 15kg (inclusive) => 30 reais
•	volume até 64000 cm3 (inclusive)  e peso até 30kg (inclusive) => 65 reais
•	volume até 216000 cm3 (inclusive) e peso até 50kg (inclusive)  => 100 reais

Caixas com volume acima de 216000 cm3 ou peso acima de 50kg são rejeitadas, ou seja, não são aceitas pela transportadora.

1.a) Escreva a função avaliaCaixa que:
- recebe uma tupla correspondente a uma caixa
- retorna uma tupla com:
 	(identificação ,'VALIDA', valor a ser pago), caso a caixa possa ser transportada
 	(identificação ,'INVALIDA'), caso a caixa não possa ser transportada.
    
        Saída esperada para as caixas:
('XS1111',(12,21,18),13.4) => ('XS1111', 'VALIDA', 30)
('XX1122',(42,41,45),13.4) => ('XX1122', 'VALIDA', 100)
('RV6677',(62,50,75),25.4) => ('RV6677', 'INVALIDA')

1.b) Escreva a função processaLoteDeCaixas que:
- recebe uma lista de caixas a serem transportadas
- retorna uma tupla de 3 elementos: o valor total a ser pago à transportadora, a lista com as caixas válidas e a lista com as caixas inválidas (rejeitadas)

Essa função usa obrigatoriamente a função avaliaCaixa do item anterior.
Para a lista de caixas lcx a seguir:
lcx=[  ('XS1111',(12,21,18),13.4), ('XX1122',(42,41,45),13.4) ,  ('PS1111',(12,21,18),25.4), 
      ('RV6677',(62,50,75),25.4),  ('MV4444',(30,25,30),21.5), ('RP6677',(32,45,45),55.4) ]
A saída esperada é:
(260.0, [('XS1111', (12, 21, 18), 13.4), ('XX1122', (42, 41, 45), 13.4), ('PS1111', (12, 21, 18), 25.4), 
          ('MV4444', (30, 25, 30), 21.5)], [('RV6677', (62, 50, 75), 25.4), ('RP6677', (32, 45, 45), 55.4)])

Escreva as funcoes pedidas e faca testes com os exemplos dados
'''
#Solucao do 1A:

    
#Solucao do 1B:

'''
Exercicio TUPLA/DIC
Ex2)

Em uma administradora de condomínios, um condomínio é representado por:
 	(nomeDoCondominio, CPFdoSindico, salarioSindico, despesaMensal, valorMensalEsperado, num de unidades, num de unidades_inadimplentes , bairro, 
    quantidade de empregados) em que:
 	  - nomeDoCondominio: string com o nome do condomínio
 	  - CPFdoSindico: string com o CPF do síndico
 	  - despesaMensal: valor da despesa do condomínio em um mês
 	  - valorMensalEsperado: valor total que o condomínio deve arrecadar em um mês, mediante  pagamento feito por todas as unidades
 	  - num de unidades: número de unidades do condomínio
 	  - num de unidades_inadimplentes: unidades que não pagaram conta(s) de condomínio

As informacoes dos condominios que comecaram a ser admistrados somente a partir do ano 2020 encontram-se 
na tupla de condominios a seguir:
ttCondominios=(('Condomínio VISCONDE', '057191184-71', 4164.75, 105610.56, 116494.84, 166, 25, 'Bangu', 6),
                ('Condomínio PRINCESA', '637634807-56', 3322.16, 187001.86, 233222.87, 134, 17, 'Centro', 1),
                ('Condomínio SOLAR', '748923456-05', 3055.0, 302781.28, 306556.84, 173, 17, 'Joatinga', 43),
                ('Condomínio ROSAS', '065970727-49', 1276.84, 11339.07, 12765.88, 31, 9, 'Bangu', 47),
                ('Condomínio JARDIM', '127953269-60', 1506.83, 110682.02, 150864.27, 48, 8, 'Leblon', 39),
                ('Condomínio IMPERADOR', '475118871-93', 5599.77, 71044.9, 75992.33, 28, 8, 'Joatinga', 47),
                ('Condomínio ALAMANDA', '115749372-38', 2408.44, 42109.16, 42408.33, 186, 42, 'Centro', 22),
                ('Condomínio VIOLETA', '447030779-35', 3620.82, 7340.92, 16200.64, 54, 5, 'Leblon', 46),
                ('Condomínio GERANIO', '998052813-65', 9777.69, 93324.52, 97776.62, 28, 3, 'Leblon', 41),
                ('Condomínio PEDRA', '757394517-39', 6278.59, 597623.84, 632783.78, 191, 80, 'Barra', 2),
                ('Condomínio TURQUESA', '021105794-45', 6982.39, 226243.09, 269824.97, 128, 35, 'Joatinga', 18),
                ('Condomínio ROCCA', '009173228-94', 4784.41, 42932.66, 47840.1, 26, 12, 'Santa Cruz', 11),
                ('Condomínio AMARELO', '524241695-96', 5447.25, 329434.67, 354471.42, 149, 49, 'Ipanema', 39),
                ('Condomínio CAMPOS', '915711983-44', 6798.22, 459950.99, 467984.22, 176, 58, 'Bangu', 7),
                ('Condomínio RIOS', '569898403-21', 3144.08, 209803.81, 231440.92, 176, 23, 'Leblon', 11),
                ('Condomínio SELVA', '360418037-34', 6533.89, 115232.99, 165336.03, 166, 17, 'Santa Cruz', 5),
                ('Condomínio SOLARIO', '630196508-33', 3359.7, 327700.75, 335590.29, 185, 20, 'Leblon', 50),
                ('Condomínio MADEIRA', '249274956-24', 1316.07, 10529.43, 13164.33, 6, 0, 'Copacabana', 22),
                ('Condomínio TORA', '851201254-65', 1101.4, 9915.54, 11017.69, 23, 9, 'Centro', 33),
                ('Condomínio MARES', '455006768-98', 7129.67, 257344.45, 271296.54, 157, 22, 'Barra', 34))

'''

# Ex2.A)
# Escreva uma função, denominada condominiosDeUmBairro,  que:
# 	o	receba uma tupla de condomínios (ou seja, uma tupla de tuplas) e um bairro,
# 	o	retorne uma tupla de 2 elementos:
# 	 a quantidade total de condomínios do bairro e uma tupla somente com as tuplas correspondentes aos condomínios do bairro recebido.
# '''

#Solucao do 2A:




# '''
# Ex2.B)
# Para o item B considere o dicionario com bairros e quantidade de condominios por bairro
# dessa administradora ate o ano de 2020 a seguir:
#     dicBairrosQtdCond={'Leblon': 12, 'Gavea': 12, 'Copacabana': 25, 
#                        'Ipanema': 12, 'Jardim Botanico':16, 'Botafogo':25, 'Barra':23}
    
# Escreva uma função, denominada atualizaDicPorBairro,  que:
# 	o	receba a tupla de condominios ja utilizada no item A e um dicionario como o acima, em que 
#         cada elemento/item eh:
#                           BAIRRO: qtd de condominios do bairro  (ate o ano de 2020)
# 	o	faca a atualizacao do dicionario a partir das informacoes da tupla

#Solucao do 2B:





'''
Ex3)
Considere um dicionario dicPessoa_IdadeSexo em que cada elemento e´:
    Pessoa: tupla com (idade,sexo) da pessoa
 
dicPessoa_IdadeSexo= {'TADEU' : (67,'M'), 'LINDA' : (73,'F')
                      'ROMEU' : (71,'M'), 'ALCEU' : (73,'M')
                      'DANDA' : (70,'F'), 'BENTO' : (74,'M'),
                      'KAKAU' : (73,'M'), 'ANTON' : (69,'M'),
                      'MOLLY' : (66,'F'), 'DUNGA' : (71,'M')
                      }    

    
Considere tambem o dicionario dicVacinasPrevistas em que cada item e´:
    (Idade,sexo) : dataDaVacina
    
dicVacinasPrevistas= {   (74,'F') : '22/03',   (74,'M') : '23/03',
                         (73,'F') : '25/03',   (73,'M') : '26/03',
                         (72,'F') : '29/03',   (72,'M') : '30/03',
                         (71,'F') : '31/03',   (71,'M') : '01/04',
                         (70,'F') : '02/03',   (70,'M') : '03/04'  }

Ex3) Escreva a funcao quandoVacina que recebe os dois dicionarios E O NOME DA PESSOA e 
    retorna a dataDeVacina da Pessoa. Caso a pessoa não esteja no dicionario, deve ser retornada 
    'Pessoa nao encontrada'. Caso ainda não haja previsao de vacina para essa pessoa 
    deve ser retornada 'Vacina nao prevista'.
'''

# Solucao do 3:





'''
EX4: 
Em uma academia da natacao com varias unidades um nadador eh representado como 
uma tupla: 
(Nome,Sexo,Idade,UNIDADE,TempoTreino1,TempoTreino2,TempoTreino3,TempoProva,Treinador)
    
Ex4.A:
Escreva uma funcao, denominada criaDicAbaixo, que:
- receba uma tupla de nadadores (ou seja, uma tupla de tuplas) e uma tupla (minutos,segundos)  
correspondente a um certo tempo 
- crie e retorne um dicionario apenas com os nadadores que tem tempo de prova 
inferior ao tempo recebido, em que cada elemento (item) do novo dicionario e
     TREINADOR: lista com as tuplas dos nadadores desse treinador 
                com tempo inferior ao tempo recebido
                
Por exemplo, para a tupla de nadadores dada e o tempo  (23,15), o dicionario 
retornado e´:                

{'EDU': [('Bibi', 'F', 20, 'Violetas', (24, 13), (23, 7), (22, 9), (21, 40), 'EDU'), 
         ('Tata', 'M', 20, 'Carvalho', (22, 24), (23, 18), (20, 15), (18, 50), 'EDU')], 
 'LEO': [('Kadu', 'M', 19, 'Carvalho', (22, 12), (21, 10), (20, 9), (19, 4), 'LEO'), 
         ('Guga', 'M', 29, 'Caravela', (24, 12), (23, 10), (22, 21), (22, 4), 'LEO'), 
         ('Lele', 'F', 19, 'Carvalho', (24, 32), (22, 10), (21, 9), (19, 4), 'LEO'), 
         ('Dina', 'F', 19, 'Carvalho', (24, 32), (22, 10), (21, 9), (19, 4), 'LEO')], 
 'VAL': [('Nena', 'F', 20, 'Violetas', (24, 13), (23, 7), (22, 29), (21, 42), 'VAL')]}
'''
# Sol do 4A




'''

Ex4.B) 
Escreva uma funcao, denominada criaDicTrEq_Qtd, que:
- receba uma tupla de nadadores 
- crie e retorne um dicionario em que cada elemento (item) do novo dicionario e
     (TREINADOR, UNIDADE) : quantidade de nadadores desse treinador nessa  
                            unidade
Por exemplo, para a tupla dada, o dicionario retornado e´:
{('LEO', 'Caravela'): 2, ('EDU', 'Violetas'): 2, ('VAL', 'Violetas'): 2, 
 ('LEO', 'Carvalho'): 3, ('RUI', 'Violetas'): 2, ('VAL', 'Caravela'): 2, 
 ('EDU', 'Carvalho'): 1}    
    
'''
# Sol do 4B





'''
Ex5) Escreva a funcao criaDicPorCor que:
    - recebe dicionario com  Pessoa: lista das cores favoritas
    - retorna dicionario com COR: lista das pessoas que gostam dessa cor
Obs: uma pessoa pode ter várias cores preferidas


Teste sua funcao chamando-a para o dicionario abaixo:
dicPessoaECores={  'LALA': ['ROSA','AMARELO'],
                   'MIMI': ['ROSA','PRETO'],
                   'GUGU': ['VERDE','AZUL','BRANCO'],
                   'LELE': ['VERMELHO'],
                   'LILI': ['ROSA','AZUL'],
                   'VAVA': ['AMARELO','ROXO'],
                   'DEDE': ['AMARELO','VERDE','AZUL']}
    
'''

#Solucao do 5:

    


'''
Ex6) Considere os dicionarios :
dicPaisFilhos =>    chave: Pessoa  valor: lista com os filhos dessa pessoa
dicAreaProfissional => chave: Pessoa  valor: AreaProfissional da pessoa


dicPaisFilhos = { 'Severina':['Elzira','Ernesto'],
               'Oto':['Elzira','Ernesto','Carla'],
               'Marta':['Carla'],
               'Elzira':['Marcia','Alvaro'],
               'Carlos':['Marcia','Alvaro'],
               'Marcia':['Rosinha','Lia'],
               'MarKio':['Rosinha','Lia'],
               'Alvaro':['Luis'],
               'Rita':['Luis','Sandro'],
               'Wilson':['Sandro'],
               'Rosinha':['Joana'],
               'Horácio':['Joana'],
               'Lia':[],
               'Joana':[],
               'Carla' : [],
               'Ernesto':['Karlos', 'Jorge','Ana'],
               'Miram':['Karlos', 'Jorge','Ana'],
               'Karlos':['Ricardo', 'Joice'],
               'Hanna': ['Ricardo'],
               'Mara':['Joice'],
               'Joice': [],
               'Jorge':['Marco', 'Francisca'],
               'Petra':['Marco', 'Francisca'],
               'Ana':[],
               'Ricardo':['Sara'],
               'Moira':['Sara'],
               'Sara':[],
               'Marco':[],
               'Francisca':[],
               'Luis':[],
               'Sandro':[]
               }

dicAreaProfissional = { 'Severina':'enfermagem',
               'Oto':'direito',
               'Marta':'engenharia',
               'Elzira':'ensino',
               'Carlos':'energia',
               'Marcia':'veterinaria',
               'MarKio':'medicina',
               'Alvaro':'ensino',
               'Rita':'vendas',
               'Wilson':'medicina',
               'Rosinha':'servicos',
               'Horácio':'dramaturgia',
               'Lia':'ensino',
               'Joana':'veterinaria',
               'Carla' : 'jornalismo',
               'Ernesto':'direito',
               'Miram':'ensino',
               'Karlos':'direito',
               'Hanna': 'medicina',
               'Mara':'ensino',
               'Joice': 'engenharia',
               'Jorge':'ensino',
               'Petra':'direito',
               'Ana':'ensino',
               'Ricardo':'jornalismo',
               'Moira':'vendas',
               'Sara':'vendas',
               'Marco':'direito',
               'Luis':'engenharia',
               'Sandro':'seguranca'
               }


6.A) Escreva uma funcao, denominada filhosComuns que:
- receba o dicionario de PaisFilhos, e os nomes de duas 
pessoas
- retorne a lista de filhos em comum dessas duas pessoas, 
ou seja, daqueles que sao filhos tanto de uma quanto da 
outra pessoa


6.B) Escreva um funcao, denominada filhosNaArea que:
- receba o dicionario de PaisFilhos, o dicionario de 
          AreaProfissional e o nome de uma pessoa  
- retorne True se a pessoa tem algum filho que trabalha 
                 em sua  area profissional  ou 
          False,  caso contrario
          
6.C) Escreva uma funcao, denominada ehNetoDe, que :
  receba o dicionario de PaisFilhos e os nomes de duas pessoas 
  retorne True se a segunda pessoa e´ neta da primeira ou
          False, caso contrario.

Utilize os dicionarios dados para testar suas funcoes
'''
#Sol do 6A




#Sol do 6B

    

#Sol do 6C




'''
6.D) (Proposicao extra no ex6):
Considerando que as chaves sempre estao nos dicionarios, 
escreva uma nova versao da funcao 6B que retorne a quantidade
de filhos com a mesma profissao do pai
'''
#Sol do 6D




'''
Ex7
Uma competição de luta entre robôs é realizada desde 2010, a cada um ou dois anos, e vários são os países 
que dela participam. São distribuídas medalhas de ouro, prata e bronze aos 3 primeiros colocados. Um dicionário 
é utilizado para guardar os resultados das últimas competições. Nesse dicionário cada elemento (item) é:
          ANO : { dicionário com as medalhas ouro, prata, bronze e seus países vencedores}
          
dicPorAno= { 
             2019: {'OURO': 'Japao', 'PRATA':'EUA', 'BRONZE':'Alemanha'},
             2018: {'OURO': 'Alemanha', 'PRATA': 'EUA', 'BRONZE':'Mexico'},
             2017: {'OURO': 'EUA', 'PRATA':'Franca', 'BRONZE': 'Alemanha'},
             2015: {'OURO': 'Mexico', 'PRATA':'Brazil', 'BRONZE': 'EUA'},
             2013: {'OURO': 'Canada', 'PRATA':'Japao', 'BRONZE':'China'},
             2012: {'OURO': 'Mexico', 'PRATA': 'Alemanha', 'BRONZE':'Brazil'},
             2010: {'OURO': 'Alemanha', 'PRATA':'Franca', 'BRONZE': 'Canada'}
      }
Obs: Lembre-se de que não há ordem em um dicionário

7.1) Escreva uma função, denominada vencedorMedalhaNoAno, que:
•	receba um dicionário como o descrito acima, um ano e  uma medalha,
•	exiba o país vencedor da medalha nesse ano
Obs: o ano recebido pode não estar no dicionário 

7.2) Escreva a funcao criaDicQtdMedPorPais que recebe um dicionário com os resultados por ano como descrito 
 no início da questão (dicPorAno) e constrói e retorna um dicionário com a quantidade de medalhas por país, 
 em que cada elemento do dicionário é:        
     PAÍS:  quantidade total de medalhas recebidas 
       
A saída esperada para o dicionário dicPorAno  é:
{'Japao': 2, 'EUA': 4, 'Alemanha': 5, 'Mexico': 3, 'Franca': 2, 'Brazil': 2, 'Canada': 2, 'China': 1}
Obs: Não pode construir o dicionário por enumeração.

'''

#Sol 7A




#Sol 7B


    

'''
Ex8)
Considere um dicionario de farmacias (dicionario de dicionarios) em que cada elemento é:
    
    FARMACIA: dicionario com remedios e respectivos precos dos remedios nessa farmacia
    
Exemplo:    
dFarma = { 'FARMYY': {'aspri':4.75, 'tuxis':16.38, 'corty':34.82, 'dig': 26.56, 'resfA': 11.45},
           'QDroga': {'aspri':3.75, 'tuxis':12.24, 'corty':42.57, 'dig': 28.45, 'resfA': 15.45},
           'DODOI':  {'aspri':6.75, 'tuxis':19.38, 'corty':24.82, 'dig': 18.56, 'resfA': 9.52},
           'RADAR':  {'aspri':5.75, 'tuxis':19.38, 'corty':30.85, 'dig': 23.56, 'resfA': 12.35},
           'MaisRem': {'aspri':4.45,'tuxis':17.65, 'corty':33.85, 'dig': 26.25, 'resfA': 10.45}
          }

Considere tambem a lista de remedios a serem comprados por uma pessoa como uma lista de tuplas 
de 2 elementos com (nomeDoRemedio, quantidade a ser comprada)

Ex8.A) Escreva a funcao totalNaFarmacia que recebe o dicionario de Farmacia - RemediosPrecos acima, a
lista de remedios a serem comprados e o nome de uma farmacia e exiba o valor total a ser pago
nessa farmacia

Ex8.B) Escreva a funcao pesquisaDePreco que recebe o dicionario de Farmacia - RemediosPrecos acima, a
lista de remedios a serem comprados, crie e retorne um dicionario em que cada elemento e´:
        FARMACIA: valor total da lista nessa farmacia

Para os itens A e B considere a lista:
lrem= [('aspri',4), ('tuxis',1), ('corty',2), ('resfA',2)]


OBS: teste suas funcoes criando outras listas de remedios

'''

#Solucao 8A
#Considerando que farmacia pode nao existir
#Considerando que pode haver um remedio na lista que nao esteja 
# na farmacia



#Solucao 8B
#Considerando que todos os remedios estao em todas as farmacias




#########################################
# Parte Principal
#########################################
#-------------------------------------------------------------
# PARA O EXERCICIO 1

lcx=[  ('XS1111',(12,21,18),13.4), ('XX1122',(42,41,45),13.4) ,  ('PS1111',(12,21,18),25.4), 
        ('RV6677',(62,50,75),25.4),  ('MV4444',(30,25,30),21.5), ('RP6677',(32,45,45),55.4) ]

print('\nTeste da 1')

#-------------------------------------------------------------
# PARA O EXERCICIO 2
tCondominios=(('Condomínio VISCONDE', '057191184-71', 4164.75, 105610.56, 116494.84, 166, 25, 'Bangu', 6),
               ('Condomínio PRINCESA', '637634807-56', 3322.16, 187001.86, 233222.87, 134, 17, 'Centro', 1),
               ('Condomínio SOLAR', '748923456-05', 3055.0, 302781.28, 306556.84, 173, 17, 'Joatinga', 43),
               ('Condomínio ROSAS', '065970727-49', 1276.84, 11339.07, 12765.88, 31, 9, 'Bangu', 47),
               ('Condomínio JARDIM', '127953269-60', 1506.83, 110682.02, 150864.27, 48, 8, 'Leblon', 39),
               ('Condomínio IMPERADOR', '475118871-93', 5599.77, 71044.9, 75992.33, 28, 8, 'Joatinga', 47),
               ('Condomínio ALAMANDA', '115749372-38', 2408.44, 42109.16, 42408.33, 186, 42, 'Centro', 22),
               ('Condomínio VIOLETA', '447030779-35', 3620.82, 7340.92, 16200.64, 54, 5, 'Leblon', 46),
               ('Condomínio GERANIO', '998052813-65', 9777.69, 93324.52, 97776.62, 28, 3, 'Leblon', 41),
               ('Condomínio PEDRA', '757394517-39', 6278.59, 597623.84, 632783.78, 191, 80, 'Barra', 2),
               ('Condomínio TURQUESA', '021105794-45', 6982.39, 226243.09, 269824.97, 128, 35, 'Joatinga', 18),
               ('Condomínio ROCCA', '009173228-94', 4784.41, 42932.66, 47840.1, 26, 12, 'Santa Cruz', 11),
               ('Condomínio AMARELO', '524241695-96', 5447.25, 329434.67, 354471.42, 149, 49, 'Ipanema', 39),
               ('Condomínio CAMPOS', '915711983-44', 6798.22, 459950.99, 467984.22, 176, 58, 'Bangu', 7),
               ('Condomínio RIOS', '569898403-21', 3144.08, 209803.81, 231440.92, 176, 23, 'Leblon', 11),
               ('Condomínio SELVA', '360418037-34', 6533.89, 115232.99, 165336.03, 166, 17, 'Santa Cruz', 5),
               ('Condomínio SOLARIO', '630196508-33', 3359.7, 327700.75, 335590.29, 185, 20, 'Leblon', 50),
               ('Condomínio MADEIRA', '249274956-24', 1316.07, 10529.43, 13164.33, 6, 0, 'Copacabana', 22),
               ('Condomínio TORA', '851201254-65', 1101.4, 9915.54, 11017.69, 23, 9, 'Centro', 33),
               ('Condomínio MARES', '455006768-98', 7129.67, 257344.45, 271296.54, 157, 22, 'Barra', 34))

dicBairrosQtdCond={'Leblon': 12, 'Gavea': 12, 'Copacabana': 25, 
                    'Ipanema': 12, 'Jardim Botanico':16, 'Botafogo':25, 'Barra':23}

print('\nTeste da 2')



#-------------------------------------------------------------
# PARA O EXERCICIO 3

dicPessoa_IdadeSexo= {'TADEU' : (67,'M'), 'LINDA' : (73,'F'),
                      'ROMEU' : (71,'M'), 'ALCEU' : (73,'M'),
                      'DANDA' : (70,'F'), 'BENTO' : (74,'M'),
                      'KAKAU' : (73,'M'), 'ANTON' : (69,'M'),
                      'MOLLY' : (66,'F'), 'DUNGA' : (71,'M')
                      }    

    

dicVacinasPrevistas= {   (74,'F') : '22/03',   (74,'M') : '23/03',
                          (73,'F') : '25/03',   (73,'M') : '26/03',
                          (72,'F') : '29/03',   (72,'M') : '30/03',
                          (71,'F') : '31/03',   (71,'M') : '01/04',
                          (70,'F') : '02/03',   (70,'M') : '03/04'  }

print('\nTeste da 3')




#-------------------------------------------------------------
# PARA O EXERCICIO 4

# Um nadador:
#(Nome,Sexo,Idade,UNIDADE,TempoTreino1,TempoTreino2,TempoTreino3,TempoProva,Treinador)

#Tupla de nadadores fornecida para testes:
tnadadores= (('Lala','F',33, 'Caravela', (25,12), (23,10), (26,9),(25,4),'LEO'),
              ('Bibi','F',20, 'Violetas', (24,13), (23,7), (22,9),(21,40),'EDU'),
              ('Gege','M',28, 'Violetas', (24,3), (25,10), (25,19),(26,20),'VAL'),
              ('Kadu','M',19, 'Carvalho', (22,12), (21,10), (20,9),(19,4),'LEO'),
              ('Leno','M',35, 'Violetas', (26,3), (27,10), (29,9),(30,10),'RUI'),
              ('Guga','M',29, 'Caravela', (24,12), (23,10), (22,21),(22,4),'LEO'),
              ('Nena','F',20, 'Violetas', (24,13), (23,7), (22,29),(21,42),'VAL'),
              ('Vava','M',28, 'Caravela', (24,3), (25,12), (25,19),(26,20),'VAL'),
              ('Lele','F',19, 'Carvalho', (24,32), (22,10), (21,9),(19,4),'LEO'),
              ('Buba','M',22, 'Violetas', (26,13), (27,10), (28,9),(24,10),'EDU'),
              ('Leda','F',24, 'Violetas', (30,33), (28,10), (33,15),(35,10),'RUI'),
              ('Tata','M',20, 'Carvalho', (22,24), (23,18), (20,15),(18,50),'EDU'),
              ('Dede','M',26, 'Caravela', (24,50), (26,10), (27,50),(28,20),'VAL'),
              ('Dina','F',19, 'Carvalho', (24,32), (22,10), (21,9),(19,4),'LEO'))


print('\nTeste da 4A')

print('\nTeste da 4B')


#-------------------------------------------------------------
# PARA O EXERCICIO 5
dicPessoaECores={  'LALA': ['ROSA','AMARELO'],
                   'MIMI': ['ROSA','PRETO'],
                   'GUGU': ['VERDE','AZUL','BRANCO'],
                   'LELE': ['VERMELHO'],
                   'LILI': ['ROSA','AZUL'],
                   'VAVA': ['AMARELO','ROXO'],
                   'DEDE': ['AMARELO','VERDE','AZUL']}
    
print('\nTeste da 5')



#-------------------------------------------------------------
# PARA O EXERCICIO 6
dicPaisFilhos = { 'Severina':['Elzira','Ernesto'],
               'Oto':['Elzira','Ernesto','Carla'],
               'Marta':['Carla'],
               'Elzira':['Marcia','Alvaro'],
               'Carlos':['Marcia','Alvaro'],
               'Marcia':['Rosinha','Lia'],
               'MarKio':['Rosinha','Lia'],
               'Alvaro':['Luis'],
               'Rita':['Luis','Sandro'],
               'Wilson':['Sandro'],
               'Rosinha':['Joana'],
               'Horácio':['Joana'],
               'Lia':[],
               'Joana':[],
               'Carla' : [],
               'Ernesto':['Karlos', 'Jorge','Ana'],
               'Miram':['Karlos', 'Jorge','Ana'],
               'Karlos':['Ricardo', 'Joice'],
               'Hanna': ['Ricardo'],
               'Mara':['Joice'],
               'Joice': [],
               'Jorge':['Marco', 'Francisca'],
               'Petra':['Marco', 'Francisca'],
               'Ana':[],
               'Ricardo':['Sara'],
               'Moira':['Sara'],
               'Sara':[],
               'Marco':[],
               'Francisca':[],
               'Luis':[],
               'Sandro':[]
               }

dicAreaProfissional = { 'Severina':'enfermagem',
               'Oto':'direito',
               'Marta':'engenharia',
               'Elzira':'ensino',
               'Carlos':'energia',
               'Marcia':'veterinaria',
               'MarKio':'medicina',
               'Alvaro':'ensino',
               'Rita':'vendas',
               'Wilson':'medicina',
               'Rosinha':'servicos',
               'Horácio':'dramaturgia',
               'Lia':'ensino',
               'Joana':'veterinaria',
               'Carla' : 'jornalismo',
               'Ernesto':'direito',
               'Miram':'ensino',
               'Karlos':'direito',
               'Hanna': 'medicina',
               'Mara':'ensino',
               'Joice': 'engenharia',
               'Jorge':'ensino',
               'Petra':'direito',
               'Ana':'ensino',
               'Ricardo':'jornalismo',
               'Moira':'vendas',
               'Sara':'vendas',
               'Marco':'direito',
               'Francisca':'vendas',
               'Luis':'engenharia',
               'Sandro':'seguranca'
               }

print('\nTeste da 6A')

print('\nTeste da 6B')



print('\nTeste da 6C')



#-------------------------------------------------------------
# PARA O EXERCICIO 7
dicPorAno= { 
             2019: {'OURO': 'Japao', 'PRATA':'EUA', 'BRONZE':'Alemanha'},
             2018: {'OURO': 'Alemanha', 'PRATA': 'EUA', 'BRONZE':'Mexico'},
             2017: {'OURO': 'EUA', 'PRATA':'Franca', 'BRONZE': 'Alemanha'},
             2015: {'OURO': 'Mexico', 'PRATA':'Brazil', 'BRONZE': 'EUA'},
             2013: {'OURO': 'Canada', 'PRATA':'Japao', 'BRONZE':'China'},
             2012: {'OURO': 'Mexico', 'PRATA': 'Alemanha', 'BRONZE':'Brazil'},
             2010: {'OURO': 'Alemanha', 'PRATA':'Franca', 'BRONZE': 'Canada'}
      }

print('\nTeste da 7A')

print('\nTeste da 7B')


#-------------------------------------------------------------
# PARA O EXERCICIO 8
dFarma = { 'FARMYY': {'aspri':4.75, 'tuxis':16.38, 'corty':34.82, 'dig': 26.56, 'resfA': 11.45},
            'QDroga': {'aspri':3.75, 'tuxis':12.24, 'corty':42.57, 'dig': 28.45, 'resfA': 15.45},
            'DODOI':  {'aspri':6.75, 'tuxis':19.38, 'corty':24.82, 'dig': 18.56, 'resfA': 9.52},
            'RADAR':  {'aspri':5.75, 'tuxis':19.38, 'corty':30.85, 'dig': 23.56, 'resfA': 12.35},
            'MaisRem': {'aspri':4.45,'tuxis':17.65, 'corty':33.85, 'dig': 26.25, 'resfA': 10.45}
          }

lrem= [('aspri',4), ('tuxis',1), ('corty',2), ('resfA',2)]

print('\nTeste da 8A')



print('\nTeste da 8B')


print('\n----------------- FIM ------------------')
