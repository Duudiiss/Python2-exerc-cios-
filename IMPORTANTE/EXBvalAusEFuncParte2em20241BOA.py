# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:53:13 2020

@author: JOISA

TRATANDO VALORES COM NaN

FUNCAO SOBRE VALORES DE UMA SERIES: series.apply(funcao)
FUNCAO SOBRE INDICES => criando grupos => series.groupby( by= funcao)
FUNCAO SOBRE GRUPOS ( a partir do agrupamento)=> agrup.apply(funcao)

"""
import pandas as pd

print('----------0-----------')
print('\n Tratando NaN')
lv=[120, None, 130, 200, None, 180, 330, 300, None, 190]
lind=list('abcdefghij')

srExemplo= pd.Series(lv, index=lind)
print('\nSeries srExemplo - serao criadas 5 copias')
print(srExemplo)



print('\nTamanho da series: ', srExemplo.size)
print('\nNumero de elementos validos: ',  srExemplo.count())


srCop1= srExemplo.copy()
srCop2= srExemplo.copy()
srCop3= srExemplo.copy()
srCop4= srExemplo.copy()
#srCop5= srExemplo.copy()

print('----------1-----------')
#ATENCAO: uma series pode TER UM NOME!!!
print('\nNome da series:', srExemplo.name )
srExemplo.name='exemplo'
print('\nNome da series:', srExemplo.name )
print('\nSeries srExemplo com seu nome:')
print(srExemplo)

print('-----------2----------')
print('\nDescartando')
srCop1.dropna(inplace=True) # altera srCop1 
print(srCop1)
print('-----------3----------')

print('\nPreenchendo srCop2 com 0 no lugar de NaN =>fillna()')
srCop2.fillna(value=0,inplace=True)
print(srCop2)
print('-----------4----------')

print('\nPreenchendo srCop3 com a MEDIA no lugar de NaN =>fillna()')
srCop3.fillna(value=srCop3.mean(),inplace=True)
print(srCop3)

print('----------5-----------')
#PAUSA: funcoes
##########################################################
#            Falando de funcoes e series: 1              #
##########################################################
# Funcao sobre valores de uma series

# #Ex1
# def aumentaDe11(v):
#     return v+11

# print('\nAumentando de 11')
# soutra1= srExemplo.apply(aumentaDe11)
# print(soutra1)

# #Ex2
# def aumentaDeAcordo(v):
#     if v < 200:
#         return v+5
#     else:
#         return v+1000
    
# print('\nAumentando de acordo (< ou nao q 200)')    
# soutra2= srExemplo.apply(aumentaDeAcordo)
# print(soutra2)

# #Ex3
# def aumentaDeAcordoIncrementosRec(v, incpouco, incmuito):
#     if v < 200:
#         return v+ incpouco
#     else:
#         return v+ incmuito
# print('\nAumentando de acordo (< ou nao q 200) com inc recebidos')      
# soutra3= srExemplo.apply(aumentaDeAcordoIncrementosRec, args=(1,5000))
# print(soutra3)

#FIM DA PAUSA

print('----------6-----------')

#AGRUPANDO POR UMA FUNCAO QUE ATUA SOBRE INDICES
def classe(x):
    if x in 'aeiou':
        return 'VOG'
    else:
        return 'CONS'
    
agVC= srCop4.groupby(by=classe)
print(agVC.groups,'\n')

#APENAS PARA EXIBICAO
for (grupo, srDoGrupo) in agVC:
    print('\nGrupo:',grupo)
    print('Elementos:')
    print(srDoGrupo)
    
    
print('\nMedia de cada grupo:')
print(agVC.mean())
   
# # #SELECIONANDO 1 grupo especifico
# # sCons= agVC.get_group('CONS')
# # print('\n Grupo das consoantes')
# # print(sCons)

print('----------7-----------') 
print('Aplicando uma função ao agrupamento com apply')

# Lembrando que cada grupo de um agrupamento eh na verdade uma series
# Ao usar o apply a partir de um agrupamento, a funcao sera chamada para
# cada grupo do agrupamento 

print('Quantos NaN por Grupo?')

def contaNull(sgr):
    return sgr.isnull().sum()

sresp= agVC.apply(contaNull)
print(sresp)

print('----------8-----------')
print('\n Funcao amplitude')

def amplitude(sg):
    return sg.max() - sg.min()
    
print('\nAgrupamento e apply')
resp1= agVC.apply(amplitude)
print(resp1)

print('\nAgrupamento e apply')
resp2= agVC.transform(amplitude)
print(resp2)

  

print('----------9-----------')
print('\nVS2: "Preenchendo" srCop4  de acordo com a MINIMA dos grupos: VOGAIS ou CONSOANTES')

print('\nPrimeiro criar a series com os indices e valores de substituicao')
srMinGrupo= agVC.transform('min')
print(srMinGrupo)
print('\n Com NaN:')
print(srCop4)
print('\n Com NaN substituido pelo minimo do grupo:')
srCop4.fillna(srMinGrupo,inplace=True)
print(srCop4)


