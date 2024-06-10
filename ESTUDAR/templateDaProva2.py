# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:41:21 2018

@author: Paula
"""

import pandas as pd
import matplotlib.pyplot as plt

print('*******************************************')
print('---------------- Questao 1 ----------------')
print('*******************************************')
sLig = pd.read_excel('C:\\Users\\meduarda\\Desktop\\prova_Racas\\ligacoes.xlsx',index_col=0,header=0).squeeze().copy()


print('---------------- item a) ------------------')
print('\nTempo total das ligacoes:')
print(sLig.sum())

print('\nMediana das ligacoes:')
print(sLig.median())

print('---------------- item b) ------------------')
print('\nDestino das ligacoes com tempo abaixo da mediana:')
print(sLig[sLig < sLig.median()].index)

print('---------------- item c) ------------------')
print('\nTabela de frequencia das faixas:')
print(sLig.value_counts(bins = [0,180,300,587]))

print('---------------- item d) ------------------')
print('\nEstatisticas por destino da ligacao:')
print('\tGraficamente (barras), tempo total das ligacoes:')
sTempoDestino = sLig.groupby(level=0).sum()
sTempoDestino.plot.bar()
# plt.show()
print('\tTempo medio das ligacoes:')
print(sLig.groupby(level=0).mean())

print('---------------- item e) ------------------')
print('\nGrafico de pizza com o percentual de ligaçoes para fora do Brasil:')

freq = sLig.groupby(sLig.index.str.contains('\+55'))
sfreq = freq.agg('count')/sLig.count()*100
print(sfreq.index)
sfreq.plot.pie(figsize=(6,6),autopct='%.2f')
# plt.show()

print('---------------- item f) ------------------')
print('\nA forma de ligacao com maior tempo total das ligaçoes e a com maior quantidade de ligacoes:')
def forma(destino):
    if 'W' in destino:
        return 'W'
    return 'O'

srForma = sLig.groupby(forma)
dfDuracao = srForma.agg(['sum','count'])
print(dfDuracao)
print(dfDuracao.idxmax())

print('\n*******************************************')
print('---------------- Questao 2 ----------------')
print('*******************************************')
dfFinan = pd.read_excel('C:\\Users\\meduarda\\Desktop\\prova_Racas\\RacasCaninasSimplificada.xlsx',sheet_name='dadosFinan',index_col=0,header=0)
dfBio = pd.read_excel('C:\\Users\\meduarda\\Desktop\\prova_Racas\\RacasCaninasSimplificada.xlsx',sheet_name='dadosBio',index_col=0,header=0)
dfCarac = pd.read_excel('C:\\Users\\meduarda\\Desktop\\prova_Racas\\RacasCaninasSimplificada.xlsx',sheet_name='caracteristicas',index_col=0,header=0)
sCategoria = pd.read_excel('C:\\Users\\meduarda\\Desktop\\prova_Racas\\RacasCaninasSimplificada.xlsx',sheet_name='categoria',index_col=0,header=0).squeeze()

print('---------------- Parte I ------------------')
print('---------------- item 1. ------------------')
print('\nb.Tabela de frequencia de racas por categoria:')
print(sCategoria.value_counts())

print('---------------- item 2. ------------------')
print('\nb.i. Quantidade de racas, preco min medio, preco max medio, por pais de origem, ',end='')
print('ordenado decrescentemente por quantidade:')
grPaisesRaca = dfFinan.groupby('ORIGEM')

dfOrigem = grPaisesRaca.agg({'PRMIN': 'mean', 'PRMAX': 'mean', 'ORIGEM': 'count'})
print(dfOrigem)

print('\nb.ii. Menor preco minimo e uma raca com este valor, por pais de origem')
print(grPaisesRaca.agg({'PRMIN': ['min','idxmin']}).min())

print('---------------- item 3. ------------------')
print('\nb.Racas cujas medidas sao iguais no macho e na femea:')
dfIgual = dfBio.loc[(dfBio['ALTMACHO'] == dfBio['ALTFEMEA'])&(dfBio['PESOMACHO'] == dfBio['PESOFEMEA'])]
print(list(dfIgual.index))

print('---------------- item 4. ------------------')
sRank = dfCarac['RANKINTELIGENCIA']
dfCarac.drop('RANKINTELIGENCIA', axis=1, inplace=True)
dfCarac.fillna(1, inplace=True)
dfCarac['RANKINTELIGENCIA']=sRank

print('\nb.Graficamente a relacao entre posicao no rank inteligencia e facilidade de treinamento:')
dfCarac.plot.scatter('RANKINTELIGENCIA', 'TREINAMENTO')
plt.show()
print('---------------- Parte II ------------------')
print('---------------- item 5. ------------------')
print('\nCategoria e caracteristicas das 10 primeiras racas no rank inteligencia:')
dfCatCarac = pd.concat([dfCarac, sCategoria], axis=1, join='inner')
print(dfCatCarac.sort_values(by='RANKINTELIGENCIA'))

print('---------------- item 6. ------------------')
print('\nTabela de frequencia da relacao entre categoria e caracteristicas: protecao e apego ao dono:')
dfRelacao = pd.crosstab(index= dfCatCarac['CATEGORIA'], columns=[dfCatCarac['PROTECAO'], dfCatCarac['APEGODONO']])
print(dfRelacao)

print('---------------- Parte III ------------------')
print('---------------- item 7. ------------------')
print('\nDataFrame dfRacas - 3 ultimas linhas:')
dfRacas = pd.concat([dfFinan,dfBio,dfCarac,sCategoria],axis=1,join='inner')
print(dfRacas.tail(3))
print('---------------- item 8. ------------------')
faixaPrec= pd.cut(dfRacas['PRMIN'], bins=[0,2500,4000,dfRacas['PRMIN'].max()], labels=['NORMAL','ELEVADO','CARO'])
dfRacas['CATEGORIA']= faixaPrec
print('\nb.Nota media da caracteristica apego ao dono por faixa de preco:')
gruped = dfRacas.groupby(by='CATEGORIA')
print(gruped['APEGODONO'].mean())

#INTERESSANTE
print('\nc.Tabela de frequencia das faixas de preco X sociabilidade:')
def classif(l):
    if l['APEGODONO'] >=4 and l['AMIZADE']>=4 and l['BRINCALHAO']>=4:
        return 'AMOROSO'
    if l['AMIZADE']>=4 and l['BRINCALHAO']>=4:
        return 'SOCIAVEL'
    return 'INDETERMINADO'


    
dfRacas['SOCIAL'] = dfRacas[['APEGODONO','AMIZADE','BRINCALHAO']].apply(classif,axis=1)


print('\n*******************************************')
print('---------------- Questao 3 ----------------')
print('*******************************************')


dfEst1=pd.read_excel('est1.xlsx',index_col=0,header=None)
dfEst1.rename(columns={1:'est1'},inplace=True)
dfEst2=pd.read_excel('est2.xlsx',index_col=0,header=None)
dfEst2.rename(columns={1:'est2'},inplace=True)
dfProf=pd.read_excel('profissional.xlsx',index_col=0,header=None)
dfProf.rename(columns={1:'prof'},inplace=True)

dfAval=pd.concat([dfEst1,dfEst2,dfProf],axis=1)
print(dfAval,'\n') # so para ajudar a enxergar

print('a)Notas finais da gema e classificacao considerando os 3 avaliadores:')
    
def notaFinal(col):
    return col.loc['Cor']*0.5+col.loc['Pureza']*0.3+col.loc['Lapidacao']*0.2

srNota=dfAval.apply(notaFinal,axis=0)

print(srNota,'\n') # so para ajudar a enxergar

#pd.cut
def classificacao(nota):
    if nota>8:
        return 'excelente'
    if nota>6:
        return 'boa'
    if nota>4:
        return 'media'
    return 'fraca'

srClassif=srNota.apply(classificacao)
print(srClassif) # so para ajudar a enxergar

print('\nRESPOSTA do item a:') 
dfRes=pd.concat([srNota,srClassif],axis=1)
#se as series tivessem name nao precisaria renomear as columns
dfRes.rename(columns={0:'NotaGema',1:'classif'},inplace=True) 
print(dfRes,'\n')
dfRes=dfRes.T  # apenas para exibir  a resposta como o esperado
print(dfRes)

print('\nb)Estagiario com maior diferenca na nota atribuida:')

srDif1=abs(dfAval.prof-dfAval.est1)
srDif2=abs(dfAval.prof-dfAval.est2)
srDif1.name ='Est1'
srDif2.name ='Est2'

dfDiferencas = pd.concat([srDif1,srDif2], axis=1)

print('\n*************************')
print(dfDiferencas) # para compreensao
print('\n*************************')

dfDiferencas['EstMaiorDif']= dfDiferencas.idxmax(axis=1)

print('\n*************************')
print(dfDiferencas) # para compreensao
print('\n*************************')


iguais= dfDiferencas.loc[(dfDiferencas.Est1==0)&(dfDiferencas.Est2==0)]

dResp= pd.concat([dfAval,dfDiferencas.EstMaiorDif],axis=1)
print(dResp.drop(iguais.index))



