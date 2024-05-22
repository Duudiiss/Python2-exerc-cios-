# -*- coding: utf-8 -*-
"""
Created on 2022/1

@author: JOISA

Criacao de DF (dataframe) a partir de dic de dic

index/columns/values/shape/size

selecao de linha/coluna/elemento

medida (pelos diferentes eixos)

DF transposto

Inclusao de colunas e de linhas,

Uso de funcoes:
    - no eixo index (axis=0/default) => "geraria uma nova linha"
    - no eixo columns (axis=1)  => "geraria uma nova coluna"
    
Ordenacao

Preenchimento de valores ausentes

Concatenacao de DataFrames

Renomeando colunas
"""

import pandas as pd
import matplotlib.pyplot as plt

dicGraus={ 'Grau1': {'LALA':5.5,'LELE':2.4,'LILI':3.7,'DUDU':7.9},
           'Grau2': {'LALA':9.5,'LELE':6.5,'LILI':6.4,'DUDU':9.1}
        }

print('\n-------AULA1---------')
df = pd.DataFrame(dicGraus)

print('\n----------1----------')
#Exibe o df
print(df)

print('\n----------2----------')
#Exibe os indices
print(df.index)
print('\nSó rotulos:')
print(list(df.index))

print('\n----------3----------')
# Exibe as colunas
print(df.columns)
print('\nSó rotulos:')
print(list(df.columns))

print('\n----------4----------')
#Exibe os valores
print(df.values)


print('\n----------5----------')
#Exibe quantidade de valores
print(df. size)

print('\n----------6----------')
# Exibe numLinhas e numColunas
print(df.shape)

print('\n----------7----------')
#Exibe num linhas
print(df.shape[0])

print('\n----------8----------')
#Exibe num colunas
print(df.shape[1])

print('\n----------9----------')
#Exibe 2 prim elementos
print(df.head(2))

print('\n----------10---------')
#Exibe 2 ult elementos
print(df.tail(2))

print('\n----------11---------')
#Exibe as informacoes do df
df.info()

print('\n----------12---------')
#Resumos estatisticos das colunas numericas
print(df.describe())

######### Medidas (funcoes) e eixos #########
print('\n----------13---------')
print('\nMedia dos GRAUS') # => default: axis=0 ou axis='index'
print(df.mean())

print('\n----------14---------')
print('\nMedia dos ALUNOS') # =>  axis=1 ou axis='columns'
print(df.mean(axis=1))

######### Selecao de Elementos #########
print('\n----------15---------')
#Exibe dados da LELE
print(df.loc['LELE'])

#Exibe dados de LELE e DUDU
print(df.loc[['LELE','DUDU']])

print('\n----------16---------')
#Exibe coluna Grau1
#  retorna series
print(df['Grau1'])
#ouuu
print(df.Grau1)

print('\n----------17---------')
#Exibe o Grau1 da LELE
print(df['Grau1'].loc['LELE'])

print('\n----------18---------')
print(df.loc['LELE','Grau1'])


print('\n----------19---------')
# O DF


print('\n----------20---------')
# DF transposto, seus indices e suas colunas
print(df.T)

#Alteracao do valor de uma celula

print('\n----------21---------')

print('\n----------22---------')


###############  VISUALIZACAO ###############
print('\n---------23----------')
#VISUALIZACAO: Barras => Todos os Graus juntos em um grafico unico
df.plot.bar(title = 'Graus')
plt.show()
#VISUALIZACAO: Barras => Graus Separados
df.plot.bar(title = 'Graus', subplots = True)
plt.show()


###############  INCLUSOES ###############
print('\n---------24----------')
# #INCLUSAO DE NOVA LINHA
# srVava=pd.Series([9.4, 7.8], index=['Grau1','Grau2'])
# print(srVava)
# #Incluindo uma linha correspondente ao Vava
# dfGraus.loc['VAVA']= srVava # poderia usar diretamente [9.4, 7.8]
# print(dfGraus)

# dfGraus.loc['KUKA']=0
# print(dfGraus)

# dfGraus.loc['TETE']=[3.6,9]
# print(dfGraus)

print('\n---------25----------')
#INCLUSAO DE NOVA COLUNA
# dicGrau3= {'LALA':9.5,'LELE':5.5,'LILI':6.2,'VAVA':8.2,'DUDU':2.7}
# #Inclusao da coluna Grau3=
# dfGraus['Grau3']=pd.Series(dicGrau3) 
# print(dfGraus)


############## Descartando NaN #############
#Exibir sem linhas com NaN
# print('\nSem linhas com NaN')
# print(dfGraus.dropna(axis='index'))
#Exibir sem colunas com NaN
# print('\nSem colunas com NaN')
# print(dfGraus.dropna(axis='columns'))

###############  Aplicacao de FUNCAO  ###############

#Maior nota
print('\nMaior Nota por grau')



print('\nMaior Nota por aluno')


