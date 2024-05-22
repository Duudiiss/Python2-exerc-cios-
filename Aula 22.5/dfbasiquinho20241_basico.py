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
dfGraus= pd.DataFrame(dicGraus)

print('\n----------1----------')
#Exibe o df
print(dfGraus)

print('\n----------2----------')
#Exibe os indices
print(dfGraus.index)
print('\nSó rotulos:')
print(dfGraus.index.values)
print(list(dfGraus.index))

print('\n----------3----------')
# Exibe as colunas
print(dfGraus.columns)
print('\nSó rotulos:')
print(dfGraus.columns.values)
print(list(dfGraus.columns))

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
dfGraus.info() #EXIBICAO

print('\n----------12---------')
#Resumos estatisticos das colunas numericas
print(dfGraus.describe())

######### Medidas (funcoes) e eixos #########
print('\n----------13---------')
print('\nMedia dos GRAUS') # => default: axis=0 ou axis='index'
print(dfGraus.mean())
print('\n')
print(dfGraus.mean(axis=0))
print('\n')
print(dfGraus.mean(axis='index'))

print('\n----------14---------')
print('\nMedia dos ALUNOS') # =>  axis=1 ou axis='columns'
print(dfGraus.mean(axis=1))
print('\n')
print(dfGraus.mean(axis='columns'))

######### Selecao de Elementos #########
print('\n----------15---------')
#Exibe dados da LELE
#Exibe dados de LELE e DUDU
print(dfGraus.loc['LELE'])
print(type(dfGraus.loc['LELE']))
# retorna uma series
print('\n')
print(dfGraus.loc[['LELE']])
print(type(dfGraus.loc[['LELE']]))
# retorna um DF
print('\n')
print(dfGraus.loc[['LELE','DUDU']])
print(type(dfGraus.loc[['LELE','DUDU']]))
# retorna um DF

print('\n----------16---------')
#Exibe coluna Grau1
#  retorna series
print(dfGraus['Grau1'])
print('\n')
# pode usar dfGraus.Grau1: retorna series
print(dfGraus.Grau1)
print('\n')    
#Exibe colunas Grau1 Grau2
# retorna DF
print(dfGraus[['Grau1','Grau2']])

print('\n----------17---------')
#Exibe o Grau1 da LELE
#Elemento (celula). Tambem para alteracao
print(dfGraus.loc['LELE','Grau1']) # usada tb para alterar

print('\n----------18---------')
print(dfGraus.loc['LELE']['Grau1'])
#Outras formas #CORRETO: dfGraus.loc['LELE'].loc['Grau1']
print(dfGraus['Grau1'].loc['LELE'])

print('\n----------19---------')
# O DF
print(dfGraus)

print('\n----------20---------')
# DF transposto, seus indices e suas colunas
print(dfGraus.T)
print('\nINDEX:', dfGraus.T.index)
print('\nCOLUMNS:', dfGraus.T.columns)


dfGraus.T.loc['Grau1','LELE']=10   #Alteracao do valor de uma celula

print('\n----------21---------')
print(dfGraus.T)

print('\n----------22---------')
print(dfGraus)

###############  VISUALIZACAO ###############
print('\n---------23----------')
#VISUALIZACAO: Barras => Todos os Graus juntos em um grafico unico
dfGraus.plot.bar(title='GRAUS JUNTOS', figsize=(6,4))
plt.show()

#VISUALIZACAO: Barras => Graus Separados
dfGraus.plot.bar(title='GRAUS SEPARADOS', subplots=True, figsize=(6,6))
plt.show()

###############  INCLUSOES ###############
print('\n---------24----------')
#INCLUSAO DE NOVA LINHA
srVava=pd.Series([9.4, 7.8], index=['Grau1','Grau2'])
print(srVava)
#Incluindo uma linha correspondente ao Vava
dfGraus.loc['VAVA']= srVava # poderia usar diretamente [9.4, 7.8]
print(dfGraus)
print('\n')
dfGraus.loc['KUKA']=0
print(dfGraus)
print('\n')
dfGraus.loc['TETE']=[3.6,9]
print(dfGraus)

print('\n---------25----------')
#INCLUSAO DE NOVA COLUNA
dicGrau3= {'LALA':9.5,'LELE':5.5,'LILI':6.2,'VAVA':8.2,'DUDU':2.7}
#Inclusao da coluna Grau3=
dfGraus['Grau3']=pd.Series(dicGrau3) 
print(dfGraus)


############## Descartando NaN #############
#Exibir sem linhas com NaN
print('\nSem linhas com NaN')
print(dfGraus.dropna(axis='index'))
#Exibir sem colunas com NaN
print('\nSem colunas com NaN')
print(dfGraus.dropna(axis='columns'))


print('\n---------26----------')
###############  Aplicacao de FUNCAO  ###############

#Maior nota
print('\nMaior Nota por grau')
print(dfGraus.max()) #axis=0 ou axis= 'index'

print('\nPor grau, um aluno q tirou a maior nota (maxima)')
print(dfGraus.idxmax())


print('Por grau: maior nota e 1 aluno de maior nota')
print(dfGraus.agg( ['max','idxmax'] ) )

print('---')
print('\nMaior Nota por aluno')
print(dfGraus.max(axis=1))

print('\nPor aluno: maior nota e 1 avaliacao em q tirou a maior nota')
print(dfGraus.agg(['max','idxmax'], axis=1  ))

####################################################
# Funcao recebe uma series e retorna a quant de 
# elementos com valor acima de 7
def qtdAcimaDe7(sr):
    sbool = sr>7
    return sbool.sum()

print('\nQuant de notas acima de 7 por Grau')
print(dfGraus.apply(qtdAcimaDe7, axis=0))

print('\nQuant de notas acima de 7 por Aluno')
print(dfGraus.apply(qtdAcimaDe7, axis=1))


###############  ORDENACAO  ###############
print('\n---------27----------')
#Um segundo DataFrame
dicOutros= {'NENE':{ 'Grau1':7.6, 'Grau3':2.8},
            'BUBA':{'Grau2':5.0},
            'GIGI':{'Grau1':5.4,'Grau2':8.6 },
            'TATA':{ 'Grau1':5.4, 'Grau2':7.8, 'Grau3':8.1}}
dfOutro= pd.DataFrame(dicOutros)
print(dfOutro,'\n')
dfOutro= dfOutro.T
print(dfOutro,'\n')

#Exibindo ordenado por ALUNO (index)
print('\nExibindo ordenado por ALUNO (index)  ')

print(dfOutro.sort_index())
#E se quiser deixar ordenado?
dfOutro.sort_index(inplace=True)
print('\n')
print(dfOutro)

#Exibindo ordenado pelos ROTULOS das colunas
print('\nExibindo ordenado pelos ROTULOS das colunas  ')
#exibe uma copia ordenada
# colunasOrdenadas= dfOutro.columns.sort_values()
# print('\n')
# print(colunasOrdenadas)
# print('\n')
# print(dfOutro[colunasOrdenadas])
#E se quiser deixar ordenado?
#Resposta: dfOutro = dfOutro[colunasOrdenadas]


print('\nOutra forma')
dfOutro.sort_index(axis=1,inplace=True)
print(dfOutro)

#Exibindo ordenado pelos valores do Grau1
print('\nExibindo ordenado pelos valores do Grau1  ')
print(dfOutro.sort_values(by='Grau1'))


#Exibindo ordenado pelos valores do [Grau1,Grau2]
print('\nExibindo ordenado pelos valores do [Grau1,Grau2]  ')
print(dfOutro.sort_values(by=['Grau1','Grau2' ]))

print('\nJuntando: concatenação')
dfJuntos= pd.concat([dfGraus,dfOutro ])
print(dfJuntos)

print('\n==== FILTROS ====')
print('\nDF com alunos que tiveram Grau1 > 5')
print(dfJuntos.loc[ dfJuntos['Grau1']>5])

print('\nDF com alunos que tiveram Grau1 > Grau2')
print(dfJuntos.loc[dfJuntos['Grau1'] > dfJuntos['Grau2']])

print('\n=== Preenchimento de Valores Ausentes===')
dfJuntos.fillna(0,inplace=True)
print(dfJuntos)

print('\n=== Inclusao de coluna a partir de medidas ===')

dfJuntos['MEDIA']= dfJuntos.mean(axis=1)
print(dfJuntos)