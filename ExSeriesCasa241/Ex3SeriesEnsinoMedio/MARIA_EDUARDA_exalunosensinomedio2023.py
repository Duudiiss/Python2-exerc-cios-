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
                         header=0).squeeze().copy()

'''
CONHECENDO A SERIES srAno:
Exiba seu tamanho, os 6 primeiros alunos, os 6 ultimos, e quantos sao 
os elementos validos.
'''
print(srAno.head(6)) #primeiros
print(srAno.tail(6)) #ultimos
'''
Exiba qual ano o aluno de nome Edu Macieira esta cursando
'''
print(srAno.loc['Edu Macieira'])
'''
Exiba quais sao os anos dos alunos Kaka Machado, Buba Porto e Lala Pontes   
'''
print(srAno.loc[['Lala Pontes', 'Kaka Machado', 'Buba Porto']])
'''
Exiba a series ordenada pelo nome
'''
print(srAno.sort_index())
'''
Ordene a series pelo ano e exiba a resultante
'''
print(srAno.sort_values())
'''
Crie e exiba a tabela de frequencia dos anos, ou seja, a series srTFreqAno que 
tem ano e quantidade de alunos nesse ano
'''
srTFreqAno = srAno.value_counts()
'''
Crie e exiba a tabela de frequencia PERCENTUAL dos anos, ou seja, a series 
srTFreqAnoPerc 
'''
srTFreqAnoPerc = srAno.value_counts(normalize = True).mul(100).round(1).astype(str) + '%'
'''
Exiba a series srAno, sem os valores com NaN
'''
print(srAno.count())

print('--- Trabalhando com a series srAltura ----')
srAltura = pd.read_excel('alunosensinomedio.xlsx', usecols=(0,2), index_col=0,
                         header=0).squeeze().copy()

'''
CONHECENDO A SERIES srAltura:
Exiba seu tamanho, os 6 primeiros alunos, os 6 ultimos, e quantos sao 
os elementos validos.
'''
print(srAltura.head(6)) #primeiros
print(srAltura.tail(6)) #ultimos
'''
Descarte da propria series os Elementos com NaN.
Exiba a series ordenada por nome
'''
srAltura.dropna(inplace=True)
print(srAltura)
'''
Exiba a maior altura e exiba o nome de um aluno com essa altura
'''
print(srAltura.max())
print(srAltura.idxmax())
'''
Qual a media das alturas dos alunos?
'''
print(srAltura.mean())
'''
Crie a series srFxAlt com 4 categorias (faixas) de altura: ate 1.60 (inclusive), 
de 1.60 ate 1.72 (inclusive), de 1.72 ate 1.85(inclusive) e acima de 1.85.
Exiba a series srFxAlt
'''
srFxAlt = pd.cut(srAltura, bins=[srAltura.min(),1.60,1.72,1.85, srAltura.max()])
print(srFxAlt)
'''
Crie e exiba srTabFax : tabela de frequencia dos faixas de altura,  que 
tem as faixas de alturas e a quantidade de alunos de cada faixa
'''
srTabFax = srFxAlt.value_counts()
print(srTabFax)
'''
Consultando os videos e slides disponibilizados, apresente os seguintes 
graficos
'''

'''
Grafico1: grafico de barras verticais da srAltura
'''
# srAltura.plot.bar(title=" grafico de barras ALTURAS", color='r', width = 0.5)
'''
Grafico2: Grafico de pizza da srAltura (Tem sentido?)
'''
# srAltura.plot.pie(title="grafico de pizza ALTURAS", colors= ['c','m','r','b','k','g','y'], legend = True, figsize=(10,10), autopct= '%.1f')
'''
Grafico3: Grafico de barras verticais da tabela de frequencia das 
faixas de alturas (srTabFax)
'''
# srTabFax.plot.barh(title="Gastos com o Pai", color='g', width = 0.8)
'''
Grafico4: Grafico de pizza da tabela de frequencia das 
faixas de alturas (srTabFax)
'''
# srTabFax.plot.pie(title="grafico de pizza ALTURAS", colors= ['c','m','r','b','k','g','y'], legend = True, figsize=(10,10))

#############filtros#################
#retorna series com valores booleanos
srBoolAlturaMior = srAltura>1.80
print(srBoolAlturaMior)

# alunos com altura acima
srAc180 = srAltura.loc[srAltura>1.80]
print(srAc180)

# series com valores em uma faixa
seriesBool= (srAltura>=1.60) & (srAltura<=1.75)
srAcfaixa = srAltura.loc[(srAltura>=1.60) & (srAltura<=1.75)]
print(seriesBool)
print(srAcfaixa)

# abaixo de 1.70
srBool170 = srAltura<1.70
'''se pedir .sum() de series booleanas ele te da a quantidade de valores true naquela series'''
print(srBool170.sum())
