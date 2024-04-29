# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:06:08 2021

@author: Joisa

Series: Introducao
Exemplos e exercicios basicos
Criacao, indices e valores, tamanho, acesso, exibicao,
inclusao, alteracao, 
Eliminacao de elementos : drop()/dropna() ,
Ordenacao 
    por valor: sort_values()
    por indices: sort_index()
Copia: copy()
    
OBS: os metodos drop(), dropna(), sort_values(), sort_index() 
retornam uma COPIA da series, sem alteracao da series original.
Para alterar a series original, deve-se usar dentro da chamada 
desses metodos o parametro (inplace= True) 


Voce deve preencher o codigo a seguir para obter o resultado 
desejado

"""
# NOME:
# TURMA:
# MAT:
# PROF: 
# Exercicio sobre series (introducao) nao pontuado



import pandas as pd
import matplotlib.pyplot as plt
'''
Criando uma series a partir de duas listas:
uma para valores e outra para indices
'''



lpessoas= ['tita','ludo','yuki','zeus','matt','deby','dave','babi', 'lulu']
lprof= ['medico','professor','advogado','filosofo','professor','medico','dentista','professor', 'fisioterapeuta']
lidades= [45,30,67,37,26,58,43,38,29]

#---------------------------------------------------------------
#---------------------------------------------------------------
#                    PARTE 1
srProfissoes= pd.Series(lprof,index = lpessoas)
print('\n Series:')
print(srProfissoes)

# Exiba o indice =>  .index
print('\n Indice:')
print(srProfissoes.index)
#So´rotulos dos indices: 2 formas
print(list(srProfissoes.index))
print(srProfissoes.index.values)


# Exiba os valores =>  .values
print('\n Valores:')
print(srProfissoes.values)


# Exiba numero de elementos (tamanho) =>  .size
print('\n Tamanho:')
print(srProfissoes.size)


# Profissao de um individuo => .loc[indice]
print('\n Profissao do matt:')
print(srProfissoes.loc['matt'])

# Profissoes de varios individuos => .loc[[lista de indices]]
print('\n Profissoes do yuki, deby e babi :')
print(srProfissoes.loc[ ['yuki','deby','babi'] ] )

# Profissoes dos 3 primeiros da series => .head()
print('\n Profissoes dos 3 primeiros:')
print(srProfissoes.head(3))


# Profissoes dos 6 ultimos da series => .tail()
print('\n Profissoes dos 6 ultimos:')
print(srProfissoes.tail(6))


# Alterar a profissao da lulu para 'chef' => .loc[] = ...
# Exibir a profissao da lulu antes e depois da alteracao
print('\n Alterando lulu')
print('ANTES:', srProfissoes.loc['lulu'])
srProfissoes.loc['lulu']= 'chef' #ATRIBUICAO
print('DEPOIS:', srProfissoes.loc['lulu'])

#Incluir um novo elemento: ruan, medico => .loc[] = ...
#Exibir a series depois da inclusao, assim como o seu tamanho
print('\n Incluindo ruan')
srProfissoes.loc['ruan']='medico'
print(srProfissoes)
print(srProfissoes.size)

#Apenas exibir a series SEM  yuki, dave => .drop([lista de indices])
print('\n Sem yuki, dave')
print(srProfissoes.drop(['yuki', 'dave']))

#Exibir a series srProfissoes 
print('\n Series:')
print(srProfissoes)


#Eliminar da srProfissoes yuki e lulu => .drop([lista de indices], inplace=True)
srProfissoes.drop(['yuki','lulu'], inplace=True)


#Exibir a series srProfissoes atualizada  e o tamanho
print('\n Series atualizada:')
print(srProfissoes)
print(srProfissoes.size)

#Apenas exibir a series  srProfissoes ordenada por profissao (valores) => .sort_values()
print('\n Exibicao da Series ordenada por profissao:')
print(srProfissoes.sort_values())

#Ordenar a series pelo nome das pessoas => .sort_index(inplace=True)
#Depois exibir a series alterada
print('\n Series srProfissoes alterada (ordenada por indice) :' )
srProfissoes.sort_index(inplace=True)
print(srProfissoes)


############ COMPLEMENTO ############ 
print('\nTabela de Frequencia das Profissoes')
sTabFreqProf= srProfissoes.value_counts()
print(sTabFreqProf)
print(type(sTabFreqProf))


print('\nTabela de Freq Percentual (Relativa) das Profissoes')
print(srProfissoes.value_counts(normalize=True)*100)

print('\nQuantas profissoes distintas ha´na series?')
print(srProfissoes.nunique())

print('\nQuais são profissoes distintas na series?')
print(srProfissoes.unique())


#---------------------------------------------------------------
#---------------------------------------------------------------
print('-----------------------------------------')
print('-----------------------------------------')
#                        PARTE 2
# A partir das listas lpessoas e lidades crie a series srIdades 
# em os valores devem ser as idades e os indices os nomes das pessoas
srIdades=pd.Series(lidades, index=lpessoas)
#Exiba devidamente identificados:
# a series
# os indices
# os valores
print('\n srIdades:')
print(srIdades)


print('\n Indice:')
print(srIdades.index)
#So´rotulos dos indices: 2 formas
print(list(srIdades.index))
print(srIdades.index.values)

# Exiba os valores =>  .values
print('\n Valores:')
print(srIdades.values)

# Exiba numero de elementos (tamanho) =>  .size
print('\n Tamanho:')
print(srIdades.size)

# a idade da tita
print('\nA idade da tita')
print(srIdades.loc['tita'])

# os 3 ultimos elementos
print('\nOs 3 ultimos elementos')
print(srIdades.tail(3))

# os 7 primeiros elementos da series, ordenados pela idade (nao alterar a series)
print('\n7 prim ordenados pela idade')
print(srIdades.head(7).sort_values())
# Se desejar em ordem decrescente:  .sort_values(ascending=False))

# os 3 primeiros mais novos
print('\n3 primeiros mais novos')
print(srIdades.sort_values().head(3))

# a series original sem a babi (nao alterar)
print('\nSem a babi (nao alterar)')
print(srIdades.drop('babi'))


############## COMPLEMENTO ##############
print('\n--Medidas--')
print('Maior Idade: (máxima) ', srIdades.max())
print('Pessoa com a maior Idade: ', srIdades.idxmax())
print('Menor Idade : (mínima)', srIdades.min())
print('Pessoa com a menor Idade: ', srIdades.idxmin())
print('Idade média ou média das idades: ', srIdades.mean())
print('Mediana das idades:',srIdades.median() )

# É possível agregar varias medidas => agg
print('\n É possível agregar varias medidas => agg ')
print(srIdades.agg(['max','idxmax','min','idxmin','mean']))



print('\nTabela de Freq das idades')
print(srIdades.value_counts())
#OBS: Pouco INTERESSANTE: melhor pensar em faixas (categorias) de idade

print('\nsrIdades')
print(srIdades)

print('\n Categorizando => pd.cut()')
print('\nPossibilidade 1: apenas 3 faixas')
srCat1= pd.cut(srIdades, bins=3 )
print(srCat1)

print('\nPossibilidade 2: fornecendo os extremos')
srCat2= pd.cut(srIdades, bins= [0,30,50,srIdades.max()])
print(srCat2)

print('\nPossib 3: fornecendo os extremos e associando rotulos as faixas')
srCat3= pd.cut(srIdades,
               bins= [0,30,50,srIdades.max()],
               labels=['JOVEM','ADULTO','MADURO'])
print(srCat3)

print('\nTab de Freq das categorias (faixas) de idade')
print(srCat3.value_counts())



'''
'''
#---------------------------------------------------------------
#---------------------------------------------------------------
print('-----------------------------------------')
print('-----------------------------------------')
#                      PARTE 3
# Trabalhando com uma series criada a partir de um arquivo excel:
# arquivo comprasabril.xlsx: com as compras feitas pelos clientes 
# em uma determinada loja no mes de abril
# O arquivo deve estar na mesma pasta que o .py
# Coluna 0 servira de indice (index_col=0)
# O arquivo tem linha de cabecalho (header=0)

# srClientes = pd.read_excel('comprasabril.xlsx', index_col=0, header=0,
#                             squeeze= True)

# PARA AS PROXIMAS VERSOES: 
srClientes = pd.read_excel('comprasabril.xlsx', index_col=0, 
                            header=0).squeeze().copy()
                          

print('\n srClientes')
print(srClientes)

# Observe a repeticao de indices
# Observe os valores com NaN

# Exiba devidamente identificados:
#  os Indices
#  os Valores
#

print('\n Indices')
print(srClientes.index)
print(srClientes.index.values)

print('\n Values')
print(srClientes.values)

print('\nTamanho')
print(srClientes.size)

print('\n Quant de elementos validos => .count()')
print(srClientes.count())

#
#  as compras da emma
#  as compras do vava e nena

print('\n Compras da emma')
print(srClientes.loc['emma'])

print('\n Compras do vava e nena')
print(srClientes.loc[['vava','nena' ]])

print('\nQuantos são os clientes distintos')
print(srClientes.index.nunique())

print('\nQuais são os clientes distintos')
print(srClientes.index.unique().values)

print('\nQuantas compras cada cliente fez')
print(srClientes.index.value_counts())


#  a series sem os elementos com valor NaN (sem alterar) => .dropna()
#  a series original ordenada pelas compras
#  o nome das pessoas que fizeram as 10 compras de mais alto valor 
#  (considerando as compras separadas mesmo)

print('\n series sem os elementos com valor NaN')
print(srClientes.dropna())

print('\n Eliminar da series os valores ausentes:')
srClientes.dropna(inplace=True)
print(srClientes)

print('\n Ordenada pelas compras')
print(srClientes.sort_values())

print('n Pessoas que fizeram as 10 compras de mais alto valor')

print(srClientes.sort_values(ascending=False).head(10).index.values)

srIdades.plot.pie(legend=True)
plt.show()