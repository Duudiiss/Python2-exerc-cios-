# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:30:58 2024

@author: PC-PROF
"""

import pandas as pd
import matplotlib.pyplot as plt

df1= pd.read_excel('exemplo2024.xlsx',
                   sheet_name= 'notas',
                   index_col=0,
                   header=0)

print('-----------------')
print('\n1) df1')
print(df1)
print('\nInformacoes')
df1.info()


df2= pd.read_excel('exemplo2024.xlsx',
                   sheet_name= 'bio',
                   index_col=0,
                   header=0)



print('-----------------')
print('\n2) df2')
print(df2)
print('\nInformacoes')
df2.info()

print('-----------------')
print('\n3) Lidando com valores ausentes')
print(df1.fillna(0)) # não altera

print('\nPreenchendo valores ausentes (por coluna)')



df1.fillna(value={'Grau1':0,'Grau2': df1['Grau2'].mean()},
           inplace=True)

#df1['Grau2'].mean() ou  df1.Grau2.mean()

print(df1)

print('-----------------')
print('\n4) Renomeando colunas')
df1.rename(columns={'Grau1':'G1', 'Grau2':'G2'},
           inplace=True)
print(df1)

print('\n5) Mudando valores de colunas')
df1['G1'].replace({0.0: 0.5},inplace=True)
print(df1)

print('\n6) Incluindo coluna Media (media ponderada)')
# Peso de G1 é 1 e Peso de G2 é 2
df1['Media']= (df1.G1 + 2*df1.G2)/3 
print(df1)


print('\n7) Trabalhando com df2')
print(df2)

print('\n7A)Maior idade, menor idade:')
print(df2['IDADE'].agg(['max','min']))

print('\n7B)Tabela de Freq de sexo:')
print(df2.SEXO.value_counts() )

print('\n8)df12: juntando os dfs')
df12= pd.concat( [df1,df2],axis=1, 
                join='inner' )
print(df12)

print('\n9A- Elementos com G1 maior do que G2 ')
print(df12.loc[ df12.G1>df12.G2])

print('\n10) Graficos')
# df12.plot.bar(title='df12')
# plt.show()

df12[['G1','G2','Media']].plot.bar(title='Graus e media')
plt.show()

print('\n11) Visualização gráfica IDADE X Media')
df12.plot.scatter(x='IDADE',y='Media')
plt.show()
