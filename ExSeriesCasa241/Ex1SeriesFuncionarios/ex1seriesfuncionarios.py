# -*- coding: utf-8 -*-
"""

@author: JOISA

Trabalhando com 2 series diferentes  (FUNCIONARIOS)

Escreva o codigo para responder as perguntas apresentadas
"""

import pandas as pd
import matplotlib.pyplot as plt

lfunc=['LALA','BUBA','NENA','VAVA','TATA', 'PEPE','DUDU','KAKA']
lsalario = [4000, 5600, 8900, 6200, 2300, 7500, 4300, 2900]
lestciv = ['CASADO','SOLTEIRO','SOLTEIRO','CASADO',
           'OUTROS','DIVORCIADO','SOLTEIRO','SOLTEIRO']

#Series1: funcionarios e seus salarios (a partir de listas)
srFuncSalarios= pd.Series(lsalario, index=lfunc)
print('\n--Series funcionarios e salarios--')
print(srFuncSalarios)


'''
Conhecendo a series criada: tamanho, 3 primeiros, 3 ultimos,
quem sao os indices, quem sao os valores, etc
'''

'''
Perguntas sobre as salarios:
    Quantos funcionarios?
    Qual o salario do TATA?
    Qual eh o maior salario?
    De quem?
    Qual a media dos salarios?
    Exibir a series ordenada por funcionario.
    Exibir a series ordenada decrescentemente por salario.
    Quantos ganham acima de 5000 ?
    Considerando as 3 faixas salariais (0,5000], (5000,7000] e acima de 7000, 
    exibir a faixa salarial de cada funcionario.
    Quantos funcionarios ha em cada faixa salarial? (Tabela de Freq. de fx sal)
    Outras...
    
'''

#Series2: funcionarios e seus estados civis (a partir de listas)
srFuncEstCiv= pd.Series(lestciv,index=lfunc)
print('\n--Series funcionarios e estado civil--')
print(srFuncEstCiv)

'''
Series2: 
Conhecendo as series criadas: tamanho, 3 primeiros, 3 ultimos,
quem sao os indices, quem sao os valores, etc
'''

'''
Perguntas sobre estado civil
    Qual o estado civil da NENA?
    Quantos funcionarios  por estado civil? (Tabela de Freq do Estado Civil)
    Qual estado civil predominante? ?
    Quem sao os funcionarios solteiros?
    Apresente a tabela de frequencia do estado civil (numericamente)
    Apresente a tabela de frequencia do estado civil (graficamente)
    Apresente a tabela de frequencia PERCENTUAL do estado civil (numericamente)
    Apresente a tabela de frequencia PERCENTUAL do estado civil (graficamente)
    
'''


'''
Perguntas sobre salarios e estado civil (mais adiante [DEPOIS...])
    Qual a media de salarios por estado civil?
'''




    

