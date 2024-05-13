# -*- coding: utf-8 -*-
"""
Created on Mon May 27 00:32:54 2019

@author: JOISA
Topicos: filtro
         replace(), update()
         operacao aritmetica com operador
         operacao aritmetica com metodo
         concatenacao
         concatenacao gerando MULTIIndice
         acessando MULTIIndice
"""
import pandas as pd

print('\nComplementos:')

"""
dsimp={'LALA':'Prod','LELE':'Comp','LILI':'Prod','LOLO':'Amb','JUJU':'Comp'}
sAl= pd.Series(dsimp)
print(sAl)

sCompAmb = sAl.loc[(sAl=='Comp') | (sAl=='Amb')]
print('\n')
print(sCompAmb)
"""


print('\n------------------------1-------------------------')
dprecos= {'laranja':0.6, 'pera':2.2, 'abacate':7.4, 'banana':0.8 ,
          'cafe':12.3, 'arroz':4.5, 'chocolate':7.8, 'leite':4.5, 'iogurte':3.4,
          'biscoito':3.5, 'queijo':15.6}
sprecos= pd.Series(dprecos)
print('\nsprecos:')
print(sprecos)

print('\n----------------------2---------------------------')
print('\nSeu preco unitario e´ acima de 2?:')
print(sprecos>2)

print('\n----------------------3---------------------------')
print('\nSelecionando produtos com precos acima de 2:')
print(sprecos.loc[sprecos>2])


print('\n----------------------4---------------------------')
print('\nPrecos abaixo de 2 OU acima de 10:')
sextremos = sprecos.loc[(sprecos<2) | (sprecos>10)]
print(sextremos)

print('\nPrecos acima de 7 e abaixo de 13 (dentro do intervalo):')
sss = sprecos.loc[(sprecos>7) & (sprecos<13)]
print(sss)

print('\n---------------------5--------------------------')
dfruta= {'laranja':18, 'pera':2, 'abacate':1, 'banana':12 }
sfruta= pd.Series(dfruta)
print('\nsfruta:')
print(sfruta)


print('\n--------------------6---------------------------')
dlat={'leite':6, 'iogurte':7, 'queijo':1}
slat= pd.Series(dlat)
print('\nslat (laticinios):')
print(slat)


print('\n--------------------7----------------------------')
print('\n-------------------- replace() -----------------')
srResult= sfruta.replace(to_replace=1, value=2)
print(srResult)

print('\n--------------------8----------------------------')
print('\n-------------------- update() ------------------')
dAlteracoes = {'banana':24, 'iogurte':10, 'manga':3}
srAlt = pd.Series(dAlteracoes)
srResult.update(srAlt) #NAO GERA COPIA.
print(srResult) #NAO INCLUIU manga


print('\n---------------------9---------------------------')
print('\n------------------------------------------------')
print('\nJuntando os dois: concatenacao')
scompras= pd.concat([sfruta,slat])
print(scompras)
print('\n----------------------10--------------------------')
print('\n------------------------------------------------')
print('\nSelecionando em sprecos so os desejados')
sprDesejados= sprecos.loc[sprecos.index.isin(scompras.index)]
print(sprDesejados,'\n')


#sprDes=sprecos.loc[scompras.index] #so se todos das compras estiverem nos precos
#print(sprDes)
print('\n-----------------------11-------------------------')
print('\nValor total das compras por produto:')
stotPorProd = scompras*sprDesejados
print(stotPorProd)
print('\nValor total das compras')
print(stotPorProd.sum())
print('\n-----------------------12-------------------------')
print('\nOutra forma:')
srTotPorProd = scompras*sprecos
print(srTotPorProd) # aqui resulta em valor NaN qdo ausente
print('\nTOTAL:',srTotPorProd.sum())

print('\nNao quero:')
srNaoQuero= srTotPorProd.loc[srTotPorProd.isnull()]
print(srNaoQuero)

print('\n---------------------13---------------------------')
stot2 = scompras.mul(sprecos,fill_value=0) 
print(stot2)
sindesejados= stot2.loc[stot2==0]
print('\nIndesejados')
print(sindesejados.index.values)

print('\n---------------------14---------------------------')
stot2.drop(sindesejados.index, inplace=True)
print(stot2)

print('\n---------------------15---------------------------')
print('\n----- Concatenacao gerando um multiindice ------')
sresult=pd.concat([sfruta,slat],keys=['FRUTA','LAT'])
print(sresult)
print('\nIndice')
print(sresult.index)
print("\n---------------sresult.loc['FRUTA']-------------")
print(sresult.loc['FRUTA'])
print("\n------------sresult.loc[('FRUTA','pera')]-------")
print(sresult.loc[('FRUTA','pera')])
print("\n------------sresult.loc[[('FRUTA','pera')]]-------")
print(sresult.loc[[('FRUTA','pera')]])
print("\n--------------sresult.xs('LAT',level=0)---------")
print(sresult.xs('LAT',level=0))
print("\n-------------sresult.xs('iogurte',level=1)------")
print(sresult.xs('iogurte',level=1))


