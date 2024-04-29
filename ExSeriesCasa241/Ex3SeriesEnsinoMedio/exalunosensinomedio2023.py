# -*- coding: utf-8 -*-

# Exercicio sobre Series a ser entregue ate as 12h de segunda dia 26/10

# NOME:
# MAT:
# TURMA:
# PROF:


"""
Created on Fri Oct 23 06:25:44 2020

@author: Joisa

"""

'''
A partir do arquivo alunosensinomedio.xlsx serao criadas duas series: 
a srAno com o ano dos alunos, usando as colunas 3 e 0(indice) e 
a srAltura com as alturas dos alunos, usando as colunas 2 e 0 (indice)

ATENCAO: todas as respostas que voce exibir na console devem ser precedidas 
por uma mensagem identificando apriadamente o que esta sendo exibido, como 
feito nos exemplos de aula 
'''
import pandas as pd
import matplotlib.pyplot as plt

print('--- Trabalhando com a series srAno ----')
srAno = pd.read_excel('alunosensinomedio.xlsx', usecols=(0,3), index_col=0,
                         header=0).squeeze()

'''
CONHECENDO A SERIES srAno:
Exiba seu tamanho, os 6 primeiros alunos, os 6 ultimos, e quantos sao 
os elementos validos.
'''

'''
Exiba qual ano o aluno de nome Edu Macieira esta cursando
'''

'''
Exiba quais sao os anos dos alunos Kaka Machado, Buba Porto e Lala Pontes   
'''

'''
Exiba a series ordenada pelo nome
'''

'''
Ordene a series pelo ano e exiba a resultante
'''

'''
Crie e exiba a tabela de frequencia dos anos, ou seja, a series srTFreqAno que 
tem ano e quantidade de alunos nesse ano
'''

'''
Crie e exiba a tabela de frequencia PERCENTUAL dos anos, ou seja, a series 
srTFreqAnoPerc 
'''


'''
Exiba a series srAno, sem os valores com NaN
'''


print('--- Trabalhando com a series srAltura ----')
srAltura = pd.read_excel('alunosensinomedio.xlsx', usecols=(0,2), index_col=0,
                         header=0).squeeze()

'''
CONHECENDO A SERIES srAltura:
Exiba seu tamanho, os 6 primeiros alunos, os 6 ultimos, e quantos sao 
os elementos validos.
'''

'''
Descarte da propria series os alementos com NaN.
Exiba a series ordenada por nome
'''

'''
Exiba a maior altura e exiba o nome de um aluno com essa altura
'''

'''
Qual a media das alturas dos alunos?
'''

'''
Crie a series srFxAlt com 4 categorias (faixas) de altura: ate 1.60 (inclusive), 
de 1.60 ate 1.72 (inclusive), de 1.72 ate 1.85(inclusive) e acima de 1.85.
Exiba a series srFxAlt
'''


'''
Crie e exiba srTabFax : tabela de frequencia dos faixas de altura,  que 
tem as faixas de alturas e a quantidade de alunos de cada faixa
'''

'''
Consultando os videos e slides disponibilizados, apresente os seguintes 
graficos
'''

'''
Grafico1: grafico de barras verticais da srAltura
'''

'''
Grafico2: Grafico de pizza da srAltura (Tem sentido?)
'''

'''
Grafico3: Grafico de barras verticais da tabela de frequencia das 
faixas de alturas (srTabFax)
'''

'''
Grafico4: Grafico de pizza da tabela de frequencia das 
faixas de alturas (srTabFax)
'''


