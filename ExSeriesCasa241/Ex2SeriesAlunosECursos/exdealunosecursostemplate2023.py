# -*- coding: utf-8 -*-
"""
Exercicio de Series: alunos e cursos  - JOISA
Como sempre, antes de exibir a resposta na tela, deve ser 
exibida uma mensagem identificando o que sera´ exibido
"""

import pandas as pd
import matplotlib.pyplot as plt


'''
CRIAR a series srAleCurso, lendo dados do arquivo alunosecursos.xlsx
'''



print('******************************************************')
print('Exibindo  a series construida')
'''
EXIBIR a series criada
'''



'''
EXIBIR as 4 primeiras linhas da srAleCurso: usar head()
'''


'''
EXIBIR as 3 ultimas linhas da srAleCurso: usar tail()
'''



print('***********************************************************')
print('Indices, Valores, Numero de Linhas, Numero de Linhas Validas')
'''
EXIBIR os indices  da srAleCurso:  index
'''


'''
EXIBIR os valores  da srAleCurso:  values
'''


'''
EXIBIR tamanho (numero de linhas) da series:  size
'''


'''
EXIBIR numero de linhas VALIDAS da series:  count()
'''



print('******************************************************')
'''
EXIBIR srAleCurso  ALUNO: bla - CURSO: bla : usar iteritems()
'''



'''
EXIBIR o curso do aluno de nome LINO :  loc
'''


'''
EXIBIR o curso do aluno de nome PEPA :  loc
'''


print('***********************************************************')
print('Usando drop(),copy(),dropna()')
'''
ELIMINAR de srAleCurso linhas com curso nao preenchido: dropna()
'''


'''
EXIBIR srAleCurso atualizada
'''


'''
CRIAR uma series copia: copy()
'''


'''
ELIMINAR da copia os alunos VAVA, LUNA, DEDE: drop()
'''


'''
EXIBIR a copia depois das eliminacoes
'''


'''
EXIBIR o tamanho da copia depois das eliminacoes
'''





print('***********************************************************')
'''
EXIBIR srAleCurso original novamente, continuaremos com ela
'''

'''
Quantos sao os cursos distintos?
'''

'''
Quais sao os cursos distintos?
'''


print('***********************************************************')
print('ORDENANDO...')

'''
ORDENAR por indices: sort_index(), exibir
'''



'''
ORDENAR por valor: sort_values(), exibir
'''



print('***********************************************************')
print('Valores e quantidade de ocorrencias, ou seja, ')
print('CURSOS e quantidade de ocorrencias (que significa numero de alunos do curso)')
'''
CONSTRUINDO a TABELA DE FREQUENCIA DE VALORES (no caso CURSOS):
CRIAR a partir da srAleCurso uma nova series (srCursos) onde os indices sao 
nomes de CURSO (uma vez cada)  e os valores a quantidade  de vezes que cada 
curso ocorreu  na srAleCurso:  usar  value_counts()
'''


'''
EXIBIR a series srCursos (que corresponde a tabela de frequencia)
'''



print('VISUALIZANDO...')
'''
VISUALIZANDO srCursos como grafico de barras: plot.bar(title='CURSOS')
'''

#plt.show()

'''
VISUALIZANDO srCursos como grafico pizza:  plot.pie(title="CURSOS")
'''

#plt.show()








