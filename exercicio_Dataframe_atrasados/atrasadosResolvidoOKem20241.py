# -*- coding: utf-8 -*-
"""
Joisa

Ex de Atrasos
"""
'''
Considere o arquivo atrasos2022.xlsx com os minutos de atraso dos funcionários 
de uma empresa nos 30 dias de um determinado mês.

1-	Crie a series srAtrasos a partir da planilha minutosDeAtraso do 
arquivo atrasos2022.xlsx.
1A) Exibindo a srAtrasos.
1B) Apresente a visualização gráfica da srAtrasos (barras))
1C) Apresente o percentual de valores ausentes.
1D) Substitua os valores ausentes pela mediana dos (tempos de) atraso

2-	Qual o maior atraso de um funcionário? Qual (ou quais) funcionário(s)?
3-	Crie uma nova series com os funcionários que tiveram atrasos maiores 
do que 20 minutos. Exiba a nova series.
4-	Crie uma series (srFaixas) com 3 faixas de atrasos: de 0 a 15(inc), 
de 15 a 25(inc), acima de 25. Exiba a series.
5-	Faça a tabela de frequência da srFaixas. 
5.A) Exiba-a numericamente.
5.B) Exiba-a graficamente.
6-	Para cada funcionário exiba o total de atrasos em minuto
(Crie um agrupamento por índices=> groupby(level=0) )
7-	Para cada funcionário exiba a sua quantidade de atrasos, seu maior atraso 
e seu menor atraso (Crie um agrupamento por índices=> groupby(level=0) )
8- Em quantos dias do mes a LALA atrasou?


9-	Crie a series srSexo a partir da partir da planilha sexo do 
arquivo atrasos2022.xlsx,  exibindo a srSexo ordenada crescentemente 
por nome.

10) POR SEXO: exiba  maior atraso, menor atraso e atraso médio.

11- Crie a series srIdade a partir da partir da planilha idade do 
arquivo atrasos2022.xlsx. Considere as seguintes categorias de idade:
 ate 25 anos(inc): jovem, de 25 até 40(inc): adulto, de 40 até 65(inc):maduro, 
 acima de 65: idoso. 
Apresente por SEXO e CATEGORIA DE IDADE: maior  tempo de atraso e qtd de atrasos


'''

import pandas as pd
import matplotlib.pyplot as plt


pd.set_option("display.max_rows", 999) 
pd.set_option("display.max_columns", 999) 
pd.set_option("display.precision", 2) 
pd.set_option("float_format", '{:.2f}'.format) # define as casas decimais do float

#-------Somente srAtrasos---------------
srAtrasos = pd.read_excel('atrasos2022.xlsx', sheet_name= 'minutosDeAtraso', 
                          index_col=0, header=0).squeeze('columns').copy()



print('1A) Exibindo a srAtrasos.')
print(srAtrasos)

print('1B) Apresente a visualização gráfica da srAtrasos (barras))')
srAtrasos.plot.bar(title='srAtrasos', figsize=(6,4))
plt.show()

print('1C) Apresente o percentual de valores ausentes.')
print(srAtrasos.isnull().sum()/srAtrasos.size *100)

print('1D) Substitua os valores ausentes pela mediana dos (tempos de) atraso')
srAtrasos.fillna(value= srAtrasos.median(),inplace=True)
print(srAtrasos)


print('2.a - Maior atraso')
maiorAtraso= srAtrasos.max()
print(maiorAtraso)

print('2.b - Nomes dos funcionarios com maior atraso')
print(list(srAtrasos.loc[srAtrasos==maiorAtraso].index))


print('3- Com mais de 20 minutos')
srMaisQ20 = srAtrasos.loc[srAtrasos>20]
print(srMaisQ20)


print('4- Faixas de atraso')
srFaixas= pd.cut(srAtrasos, bins=[0,15,25,srAtrasos.max()])
print(srFaixas)

print('5- Tabela de Frequencias das Faixas de atraso')
stTabFreq= srFaixas.value_counts()
print('\n5.A) Exiba-a numericamente.')
print(stTabFreq)

print('\n5.B) Exiba-a graficamente.')
stTabFreq.plot.pie(title="Tab Freq Faixas de Atraso", autopct='%.1f')
plt.show()

print('6- Por funcionario: total de minutos de atraso')
# Agrupar por level=0 (indice: o funcionario) e usar a medida!!!
print('\nUsando groupby(level=0).sum()')
print(srAtrasos.groupby(level=0).sum())

print('7- Por funcionario: quant de atrasos, atrasos max e min')
agrupadorPorIndice= pd.Grouper(level=0)
agPorFunc= srAtrasos.groupby(by=agrupadorPorIndice)
# Nesse caso podemos usar direto agPorFunc= srAtrasos.groupby(level=0)
print(agPorFunc.agg(['count','max','min']))

print('8- Em quantos dias do mes a LALA atrasou?')
print(srAtrasos.loc['LALA'].size)
print(agPorFunc.get_group('LALA').count())


#-------Considerando tambem srSexo---------------

srSexo= pd.read_excel('atrasos2022.xlsx', sheet_name= 'sexo', 
                          index_col=0, header=0).squeeze('columns').copy()

print('9- Series srSexo ordenada por nome')
print(srSexo.sort_index())

#Extra
print('\n9B- Sexo (Genero) mais frequente:')
print(srSexo.mode())
#ATENCAO COM mode() !!! -> retorna uma series
print(srSexo.mode().values) # so´ para os valores mais frequentes
print(srSexo.mode().loc[0])  # para pegar 1 dos valores mais frequentes

print('\n10- Por sexo:maior atraso, menor atraso, atraso medio')
print(srAtrasos.groupby(srSexo).agg(['max', 'min','mean']))


#-------Considerando tambem srIdade---------------
srIdade= pd.read_excel('atrasos2022.xlsx', sheet_name= 'idade', 
                          index_col=0, header=0).squeeze('columns').copy()
print('\n11- por SEXO e CATEGORIA DE IDADE: maior atraso e qtd de atrasos')
 
srCatId= pd.cut(srIdade, bins=[0,25,40,65, srIdade.max()],
                labels= ['jovem','adulto','maduro','idoso'])



# A linha 148 funciona em algumas versões, em outras causa erro:
# srAtrasos tem repetição de índice
# srCatId não tem
# Todos os índices de srAtrasos estão em srCatId
# Mas em algumas versões ocorre erro ao tentar fazer o agrupamento:
agSxCatId= srAtrasos.groupby([srSexo,srCatId]) # DEPENDE DA VERSÃO


# print('\n########################')
# # No caso de erro: é necessário construir uma nova series 
# # de categorias com as categorias de cada atraso
# # Observe a series resultante:
# srCatIdDeCadaAtraso = srCatId.loc[srAtrasos.index]
# print(srCatIdDeCadaAtraso)
# print('\n')

# #E depois faz o agrupamento
# agSxCatId= srAtrasos.groupby([srSexo,srCatIdDeCadaAtraso]) 


print(agSxCatId.agg(['max', 'count']))
print('\n')
print('\n--------------------------------')

srAux= srCatId.loc[srAtrasos.index]
print(srAux)
print(srAux.size)

print('\n--------------------------------')

srAux= srCatId.loc[srCatId.index.isin(srAtrasos.index)]
print(srAux)
print(srAux.size)


