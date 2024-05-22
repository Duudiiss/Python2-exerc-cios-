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
dfGraus = pd.DataFrame(dicGraus)

print('\n----------1----------')
#Exibe o df
print(dfGraus)


print('\n----------2----------')
#Exibe os indices
print(dfGraus.index)
print('\nSó rotulos:')
print(list(dfGraus.index))
print(dfGraus.index.values)

print('\n----------3----------')
# Exibe as colunas
print(dfGraus.columns)
print('\nSó rotulos:')
print(list(dfGraus.columns))
print(dfGraus.columns.values)


print('\n----------4----------')
#Exibe os valores
print(dfGraus.values)


print('\n----------5----------')
#Exibe quantidade de valores
print(dfGraus.size)

print('\n----------6----------')
# Exibe numLinhas e numColunas
print(dfGraus.shape)

print('\n----------7----------')
#Exibe num linhas
print(dfGraus.shape[0])

print('\n----------8----------')
#Exibe num colunas
print(dfGraus.shape[1])

print('\n----------9----------')
#Exibe 2 prim elementos
print(dfGraus.head(2))

print('\n----------10---------')
#Exibe 2 ult elementos
print(dfGraus.tail(2))

print('\n----------11---------')
#Exibe as informacoes do df
dfGraus.info()

print('\n----------12---------')
#Resumos estatisticos das colunas numericas
print(dfGraus.describe())

######### Medidas (funcoes) e eixos #########
print('\n----------13---------')
print('\nMedia dos GRAUS') # => default: axis=0 ou axis='index'
print(dfGraus.mean())
# print('--')
# print(dfGraus.mean(axis=0))
# print('--')
# print(dfGraus.mean('index'))

print('\n----------14---------')
print('\nMedia dos ALUNOS') # =>  axis=1 ou axis='columns'
print(dfGraus.mean(axis=1))
# print('--')
# print(dfGraus.mean(axis='columns'))

######### Selecao de Elementos #########
print('\n----------15---------')
#Exibe dados da LELE
print('\ndados da LELE')
print(dfGraus.loc['LELE'])
print('--')
print(dfGraus.loc[ ['LELE'] ] )
#Exibe dados de LELE e DUDU
print('\ndados da LELE e DUDU')
print(dfGraus.loc[ ['LELE','DUDU'] ] )

print('\n----------16---------')
#Exibe coluna Grau1
#  retorna series
print('\ncoluna Grau1:\n')
print(dfGraus['Grau1'])
#ATENCAO: coluna existente pode ser acessada
# diretamente com df.NomeDaColuna
print('\n')
print(dfGraus.Grau1)

print('\n----------17---------')
#Exibe o Grau1 da LELE

print(dfGraus.loc['LELE']['Grau1'])
print('\n----------18---------')
#Abaixo uma segunda forma de acessar
# Essa forma tb permite alteração do 
# valor da célula
print(dfGraus.loc['LELE', 'Grau1' ])

print('\n----------19---------')
# O DF


print('\n----------20---------')
# DF transposto, seus indices e suas colunas
print('DF transposto')
print(dfGraus.T)
print('\nIndices do transposto')
print(dfGraus.T.index)
print('\nColunas do transposto')
print(dfGraus.T.columns)

#Alteracao do valor de uma celula

print('\n----------21---------')

print('\n----------22---------')


###############  VISUALIZACAO ###############
print('\n---------23----------')
#VISUALIZACAO: Barras => Todos os Graus juntos em um grafico unico
dfGraus.plot.bar(title='Graus')
plt.show()

#VISUALIZACAO: Barras => Graus Separados
dfGraus.plot.bar(title='Graus',
                 subplots=True,
                 figsize=[6,5])
plt.show()

###############  INCLUSOES ###############
print('\n---------24----------')
#INCLUSAO DE NOVA LINHA
srVava=pd.Series([9.4, 7.8], index=['Grau1','Grau2'])
print(srVava)
#Incluindo uma linha correspondente ao Vava
dfGraus.loc['VAVA']= srVava # poderia usar diretamente [9.4, 7.8]
print(dfGraus)

dfGraus.loc['KUKA']=0
print(dfGraus)

dfGraus.loc['TETE']=[3.6,9]
print(dfGraus)

print('\n---------25----------')
# INCLUSAO DE NOVA COLUNA
dicGrau3= {'LALA':9.5,'LELE':5.5,'LILI':6.2,'VAVA':8.2,'DUDU':2.7}
#Inclusao da coluna Grau3=
dfGraus['Grau3']=pd.Series(dicGrau3) 
print(dfGraus)


############## Descartando NaN #############
# Exibir sem linhas com NaN
print('\nSem linhas com NaN')
print(dfGraus.dropna(axis='index'))
# Exibir sem colunas com NaN
print('\nSem colunas com NaN')
print(dfGraus.dropna(axis='columns'))

###############  Aplicacao de FUNCAO  ###############

#Maior nota
print('\nMaior Nota por grau')
print(dfGraus.max())


print('\nMaior Nota por aluno')
print(dfGraus.max(axis=1))

#########################################################
def qtdAcimaDe7(series):
    qtd = series>7
    return qtd.sum()
                        
            
series = pd.Series([1,2,3,4,8,7,6,9,10], index=list('abcdefghi'))
print(qtdAcimaDe7(series))
# print(series.loc[:]>7)