# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 03:33:23 2020

@author: Joisa

Agrupamentos por 1 ou 2 agrupadores
"""

import pandas as pd

pd.set_option("display.max_rows", 999) 
pd.set_option("display.max_columns", 999) 
pd.set_option("display.precision", 2) 
pd.set_option("float_format", '{:.2f}'.format) 

lsexo =['F','F','M','M','O','M','F','M','F','F','M','O','M','M']

lolho= ['castanho','azul','castanho','castanho','azul',
       'castanho','castanho','verde','castanho','castanho',
       'castanho','verde','azul','castanho']

lalt= [1.71, 1.63, 1.82, 1.69, 1.67, 1.67, 1.63,
       1.59, 1.79, 1.61, 1.68, 1.67,1.50, 1.72]

lnomes=[ 'Teka', 'Lili', 'Duda', 'Buba',  'Didi', 'Zeze', 'Nina',
         'Beto', 'Lala', 'Gugu','Vava', 'Gege','Kaka', 'Dede']
        
srAlt= pd.Series(lalt, index= lnomes)
srSexo =  pd.Series(lsexo, index= lnomes)   
srOlho =   pd.Series(lolho, index= lnomes)   

print(srAlt.size,srSexo.size,srOlho.size ) 

# PERGUNTAS

print('====================1===================')

print('\nQual a maior e menor altura por sexo? \
Apresente tambem 1 nome de altura max e 1 de min por sexo\n')

agSx= srAlt.groupby(by= srSexo)

print(agSx)
print('--')
print(agSx.groups)


print('====================2===================')



#APENAS PARA EXIBICAO -> NUNCA PARA MEDIDAS
print('\nsrAlt agrupada por sexo')
for g, els in agSx:
    print('\nGRUPO: ', g)
    print('Elementos do grupo:')
    print(els)

print('====================3===================')

#Obtendo os elementos de um grupo específico
print('\nGrupo F')
sF= agSx.get_group('F')
print(sF)

print('====================4===================')

#Para saber a altura maxima por grupo
print('\nAlt max por grupo')
print(agSx.max())

print('====================5===================')

print(agSx.agg(['max','idxmax','min','idxmin']))

print('====================6===================')

print('\nQual o numero de individuos e a altura media por cor do olho?')
agOlho= srAlt.groupby(by= srOlho)
print(agOlho.agg(['count','mean']))

print('====================7===================')

print('\nQual a quantidade de individuos e a altura maxima por sexo e Cor Do Olho?')
agSxOlho= srAlt.groupby(by= [srSexo,srOlho])
print('====================1===================')


#APENAS PARA EXIBICAO -> NUNCA PARA MEDIDAS
print('\nsrAlt agrupada por sexo,olho')
for g, els in agSxOlho:
    print('\nGRUPO: ', g)
    print('Elementos do grupo:')
    print(els)
    
print('--')
print(agSxOlho.agg(['count','max']))

print('====================8===================')

print('\nQual a altura minima das mulheres de olhos castanhos?')
print(agSxOlho.min().loc[('F','castanho')])

print('====================9===================')

#para entender melhor...
sz= agSxOlho.min()
print(sz)
print('--')
print('\nindice')
print(sz.index)
print('--')
print(type(sz))
print('====================10===================')

#TRABALHANDO COM OS NIVEIS (LEVELS) do INDEX
print(sz.xs('F', level=0))
print('--')
print(sz.xs('azul', level=1))

