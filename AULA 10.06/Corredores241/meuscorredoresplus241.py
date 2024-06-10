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

print('\n2-index renomeado')
dfCorredores.index.name='num'
print(dfCorredores)

print('\n3- Nome do(s) vencedor(es) da corrida e melhor tempo')
melhorTempo = dfCorredores.corrida.min()
dfVenc= dfCorredores.loc[dfCorredores.corrida==melhorTempo]
print(dfVenc.nome.values)
print('Melhor tempo:',melhorTempo)


print('\n4- Nomes dos corredores com melhor desempenho na corrida do que no melhor treino')
dfTreino = dfCorredores[['treino1','treino2','treino3']]

srtempoMelhorTreino = dfTreino.min(axis=1)
#print(srtempoMelhorTreino,'\n')

dfMelhorDesempenho = dfCorredores.loc[dfCorredores.corrida < srtempoMelhorTreino]
print(dfMelhorDesempenho)
print(dfMelhorDesempenho.nome.values)

print('\n5-Dataframe so com os que tiveram desempenho na corrida pior ou igual a media dos treinos')
srMediaTreinos= dfTreino.mean(axis=1)
dfPiores = dfCorredores.loc[dfCorredores.corrida>=srMediaTreinos]
print(dfPiores)

print('\n6-Nome dos corredores que tiveram a maior diferenca entre o seu melhor treino e a corrida')
print('(para mais ou para menos)')
difTreinoCorrida = abs(dfCorredores.corrida - srtempoMelhorTreino)
print(difTreinoCorrida)
maiorDif = difTreinoCorrida.max()
print(maiorDif)
dfMaiorDif= dfCorredores.loc[difTreinoCorrida==maiorDif]
print(dfMaiorDif)
print(dfMaiorDif.nome.values)

print('\n7-Grafico Corrida X Media do treino')
dfCorredores['MdTreino']=srMediaTreinos
dfCorredores.plot.scatter(x='MdTreino', y='corrida')
plt.show()


print('\n8-Grafico Melhor treino X corrida')
dfCorredores['MelhorTreino']=srtempoMelhorTreino
dfCorredores.plot.scatter(x='MelhorTreino', y='corrida')
plt.show()


print('\n9-Grafico de barras de treinos e corridas')

dfCorredores.plot.bar(title='Corredores', figsize=(9,6))
plt.show()

################################################################
#Considerando agora o resultado final das corridas em 2017 e 2016
print('\nConsiderando agora o resultado final das corridas em 2017 e 2016')

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
dfCorridas=pd.concat([sCorrida16,sCorrida17,sCorrida18],axis=1,join='inner')
print(dfCorridas)

#Trabalhando com o dfCorridas, crie e exiba uma series informando se o 
# com o passar dos anos  o desempenho do o corredor melhorou, piorou ou 
# ficou indefinido
print('\n11-Desempenho geral nas 3 corridas')
def analise(l):
    if l.corrida2016 < l.corrida2017 and l.corrida2017 < l.corrida2018:
        return 'PIOROU'
    elif l.corrida2016 > l.corrida2017 and l.corrida2017 > l.corrida2018:
        return 'MELHOROU'
    else:
        return 'indefinido'

srDesempGeral= dfCorridas.apply(analise,axis=1)
print(srDesempGeral)

print('\n12-Exibir graficamente os resultados das 3 corridas')
dfCorridas.plot.bar(title='CORRIDAS 2016,2017,2018', figsize=(8,6))
plt.show()

print('\n13-Exibir graficamente quantos melhoraram e quantos pioraram percentualmente')
srTabFreq=srDesempGeral.value_counts()
srTabFreq.plot.pie(title='Desempenho geral',autopct='%.1f')
plt.show()

print('\n14-Exibir numericamente quantos melhoraram e quantos pioraram percentualmente')
srTabFreqRel= srTabFreq*100/srTabFreq.sum()
print(srTabFreqRel)

################################################################
# dfInfo criado a partir da planilha info do arq 

print('\n15- DataFrame dfInfo')
dfInfo = pd.read_excel('corredoresplus.xlsx', sheet_name='info',
                             index_col=0,header =0)
print(dfInfo)

print('\n16- Exiba a tabela de frequencia dos estados ')
print(dfInfo.ESTADO.value_counts())

print('\n17- Exiba graficamente o percentual de corredores do RJ ')
sboolrj= dfInfo.ESTADO=='RJ'
sboolrj.replace({True:'DoRJ', False: 'ForaDoRJ'},inplace=True)
sboolrj.value_counts().plot.pie(title='Corredores do Rio',
                                autopct='%.1f')
plt.show()

print('\n18- Exiba a tabela de frequencia no cruzamento EQUIPE/ESTADO')
print(pd.crosstab(index=dfInfo.EQUIPE, columns= dfInfo.ESTADO))

print('\n19- Exiba as idades min,max e a quantidade de anos da atividade media por EQUIPE/ESTADO')
agEE= dfInfo.groupby(['EQUIPE','ESTADO'])
print(agEE.agg({'IDADE':['min','max'], 'QtdAnosAtiv':'mean'}))


# Necessario agora criar um df  juntando colunas de interesse de 2 DFs
print('\n20- Graficamente(dispersao): Relacao entre idade e tempo na corrida de 2018')
dfIdadeCorrida= pd.concat([dfCorridas['corrida2018'],dfInfo['IDADE'] ],axis=1)
dfIdadeCorrida.plot.scatter(x='IDADE', y= 'corrida2018')
plt.show()



