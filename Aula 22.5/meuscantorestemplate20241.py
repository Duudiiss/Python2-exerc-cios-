# -*- coding: utf-8 -*-
"""
NOME:
MAT:
TURMA:
PROF:

Dataframe  - Concurso Meus Cantores
autor: Joisa
"""

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows",100)
pd.set_option("display.max_columns",100)
"""
Os votos dos diferentes candidatos do concurso MiorVoiz estão
armazenados no arquivo votoscantores.xlsx.
Há duas planilhas:
    nacional: com os votos recebidos por cada candidato, por região
    exterior: com os votos recebidos pelos candidatos no exterior
"""
'''
1- Criar o dataframe dfCantores a partir da planilha nacional 
   do arquivo votoscantores.xlsx 

Exibir
'''

print('1-Dataframe dos votos no concurso de cantores')
dfCantores = pd.read_excel('votoscantores.xlsx',sheet_name='nacional',index_col=0,
                           header=0 )
print(dfCantores)
print('\n2- Exibir indices')



print('\n3 - Exibir colunas:')



print('\n4 - Exibir valores:')


print('\n5 - Exibir shape: linhas X colunas :')



print('\n6 -Votos no SONECA:')


print('\n7 -Votos em MILORDE e em KANKAN')


'''
8 - Criar uma copia dfCop1 com linhas com NaN eliminadas
'''
print( '\n8- Copia sem linhas com NaN')


'''
9- Criar uma copia dfCop2  com colunas com NaN eliminadas
'''
print( '\n9- Copia sem colunas com NaN')



print('\nDF Original')
print(dfCantores)

'''
10- Substituir NaN por 0
'''
print( '\n10- Trocando NaN por 0')


print('\n11-Votos do NORDESTE em NANINHA :')

print('\n12-Criando srSudeste so com votos do SUDESTE')


print('\n13- Exibindo so votos do SUDESTE e do SUL')



print('\n14-Exibindo o total de votos (por regiao)')


print('\n15-Exibindo o total de votos por CANTOR')




print('\n16- Visualizacao (separada) por Regiao ')


print('\n17- Visualizacao por Regiao (Juntas)')


print('\n18- Transposta')



print('\n19- Quantidade total de votos')



print('\n20-Qual o vencedor do concurso? Quantos votos ele teve?')


print('\n21- Cantores que no SUL tiveram mais votos do que no SUDESTE (DataFrame)')



print('\n22- Cantores (DataFrame) que tiveram mais do que 10000 votos no total' )


"""
INCLUSÃO DE NOVOS ELEMENTOS
"""
'''
Acrescentando o queridinho eliminado que retornou com 100 votos por região --> linha
'''
print('\n23- Incluindo a linha "QUERIDINHO"' )



'''
Acrescentando os votos do EXTERIOR --> coluna
'''
print('\n24- Incluindo a coluna EXTERIOR' )
srExt=pd.read_excel('votoscantores.xlsx',sheet_name='exterior',index_col=0,
                    header=0).squeeze().copy()


'''
Alteração de célula
Como o QUERIDINHO não recebeu votos do exterior, atualizar este valor para 0
'''
print('\n25- Alteração da célula na linha "QUERIDINHO", coluna "EXTERIOR"' )













