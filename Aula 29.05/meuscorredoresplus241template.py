# -*- coding: utf-8 -*-
"""
JOISA
DataFrame Corredores
"""

import pandas as pd
import matplotlib.pyplot as plt

print('\n1- DataFrame dfCorredores')
dfCorredores = pd.read_excel('corredoresplus.xlsx',index_col=0,header =0)
print(dfCorredores)

#renomeie o índice apenas como num
print('\n2-index renomeado')


print('\n3- Nome do(s) vencedor(es) da corrida e melhor tempo')



print('\n4- Nomes dos corredores com melhor desempenho na corrida do que no melhor treino')



print('\n5-Dataframe so com os que tiveram desempenho na corrida pior ou igual a media dos treinos')



print('\n6-Nome dos corredores que tiveram a maior diferenca entre o seu melhor treino e a corrida')
print('(para mais ou para menos)')



print('\n7-Grafico Media do treino X corrida')#inclua a coluna Media


print('\n8-Grafico Melhor treino X corrida') #inclua a coluna MelhorTreino


print('\n9-Grafico de barras de treinos e corridas')


#Considerando agora o resultado final das corridas em 2017 e 2016

sCorrida17=pd.read_excel('corridasantigas.xlsx',sheet_name='corrida2017',
                         index_col=0, header=None).squeeze()
sCorrida17.name='corrida2017'
print('\nCorrida em 2017')
print(sCorrida17)

sCorrida16=pd.read_excel('corridasantigas.xlsx',sheet_name='corrida2016',
                         index_col=0, header=None).squeeze()
sCorrida16.name='corrida2016'
print('\nCorrida em 2016')
print(sCorrida16)

sCorrida18= pd.Series(dfCorredores.corrida.values,index=dfCorredores.nome)
sCorrida18.name= 'corrida2018'
print(sCorrida18)

#Crie o dfCorridas concatenando as corridas de 2016, 2017 e 2018. Exiba
print('\n10- dfCorridas')


#Trabalhando com o dfCorridas, crie e exiba uma series srDesemp informando se o 
# com o passar dos anos  o desempenho do o corredor melhorou, piorou ou 
# ficou indefinido. Exiba o desempenho dos corredores
print('\n11-Desempenho geral nas 3 corridas')



print('\n12-Exibir graficamente os resultados das 3 corridas')



print('\n13-Exibir graficamente quantos melhoraram e quantos pioraram percentualmente')



print('\n14-Exibir numericamente quantos melhoraram e quantos pioraram percentualmente')


################################################################
# dfInfo criado a partir da planilha info do arq 

print('\n15- DataFrame dfInfo')
dfInfo = pd.read_excel('corredoresplus.xlsx', sheet_name='info',
                             index_col=0,header =0)
print(dfInfo)

print('\n16- Exiba a tabela de frequencia dos estados ')

print('\n17- Exiba graficamente o percentual de corredores do RJ ')


print('\n18- Exiba a tabela de frequencia no cruzamento EQUIPE/ESTADO')


print('\n19- Exiba as idades min,max e a quantidade de anos da atividade media por EQUIPE/ESTADO')

# Necessario agora criar um df  juntando colunas de interesse de 2 DFs
print('\n20- Graficamente(dispersao): Relacao entre idade e tempo na corrida de 2018')

