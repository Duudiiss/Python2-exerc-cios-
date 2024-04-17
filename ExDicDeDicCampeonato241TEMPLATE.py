# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:24:59 2024

@author: JOISA
"""

# Considere um dicionário que representa um campeonato de lutas, 
# em que a chave principal é a modalidade da luta e o valor é um 
# dicionário com inscritos e seus respectivos pesos para o 
# campeonato em 2025, pesos mínimo e máximo para a modalidade, 
# e anos anteriores e respectivos vencedores.


# A) Escreva uma funcao, denominada vencedorNoAno, que
# - receba um dicionário como o descrito, uma modalidade de luta 
# e um ano, e
# - exiba o vencedor no ano nessa modalidade. Caso não exista a modalidade 
# exiba uma msg apropriada. Caso não exista o ano exiba a msg apropriada



# B) Escreva uma função, denominada incluiCompetidor, que receba 
# um dic como o descrito, a modalidade, o nome e peso do competidor 
# e faça a inclusão do competidor nos inscritos da modalidade, 
# somente se o peso atender aos requisitos. Exiba as msgs
# apropriadas para cada caso.


    
# C) Escreva uma funcao criaDicPorAno que receba um dicionário como 
#     o descritoe e construa e retorne um dicionário com
#     CHAVE: ANO
#     VALOR: dicionário com categoria e vencedor da categoria naquele ano

# Para o dicionario fornecido no bloco principal, o dic retornado seria:
# {2016: {'Leve': 'Xan', 'Regular': 'Kal'}, 
#  2018: {'Leve': 'Vik', 'Regular': 'Tif', 'Pesado': 'Lin'}, 
#  2022: {'Leve': 'Ted'}, 2023: {'Regular': 'Muy', 'Pesado': 'Bill'}, 
#  2017: {'Pesado': 'Pip'}}    


    


#BLOCO PRINCIPAL
dicMod= {'Leve' :  {'inscritos': {'Rud':68.4,'Lip':63.7,'Teo':66.3},
                    'pesos': { 'minimo': 61.2, 'maximo': 68.9},
                    'ano': {2016:'Xan', 2018:'Vik', 2022:'Ted'}
                   },
         'Regular':{'inscritos': {'Bob':70.4,'Ruy':78.3,'Lee':76.3},
                    'pesos': { 'minimo': 67.5, 'maximo': 84.9},
                    'ano': {2016:'Kal', 2018:'Tif', 2023:'Muy'}
                   },
         
         'Pesado': {'inscritos': {'Ken':84.4,'Zao':91.3,'Zak':86.3,'Ned':84.7},
                    'pesos': { 'minimo': 82.5, 'maximo': 98.9},
                    'ano': {2017:'Pip', 2018:'Lin', 2023:'Bill'}
                   }
         
         }

print('====== Testes da vencedorNoAno ======')
# vencedorNoAno(dicMod,'Pesado',2018)
# vencedorNoAno(dicMod,'Pesado',2020)
# vencedorNoAno(dicMod,'SuperPesado',2020)

print('\n====== Testes da incluiCompetidor ======')
# incluiCompetidor(dicMod,'Regular', 'Soo',65 )
# incluiCompetidor(dicMod,'Regular', 'Zuk',71 )
# incluiCompetidor(dicMod,'SuperPesado', 'Liu',71 )
# print('\n Dic atualizado:')
# print(dicMod)

print('\n====== Testes da criaDicPorAno ======')

# dicPorAno = criaDicPorAno(dicMod)
# print(dicPorAno)


# SAIDA ESPERADA:
    
# ====== Testes da vencedorNoAno ======
# Mod:Pesado - Ano 2018 - Lin
# Mod:Pesado - Ano 2020 - ano inexistente
# SuperPesado não é modalidade no campeonato

# ====== Testes da incluiCompetidor ======
# Peso do competidor incompatível com a modalidade
# Inclusão feita com sucesso
# SuperPesado não é modalidade no campeonato

#  Dic atualizado:
# {'Leve': {'inscritos': {'Rud': 68.4, 'Lip': 63.7, 'Teo': 66.3}, 
#           'pesos': {'minimo': 61.2, 'maximo': 68.9}, 
#           'ano': {2016: 'Xan', 2018: 'Vik', 2022: 'Ted'}}, 
#  'Regular': {'inscritos': {'Bob': 70.4, 'Ruy': 78.3, 'Lee': 76.3, 'Zuk': 71}, 
#              'pesos': {'minimo': 67.5, 'maximo': 84.9}, 
#              'ano': {2016: 'Kal', 2018: 'Tif', 2023: 'Muy'}}, 
#  'Pesado': {'inscritos': {'Ken': 84.4, 'Zao': 91.3, 'Zak': 86.3, 'Ned': 84.7}, 
#             'pesos': {'minimo': 82.5, 'maximo': 98.9}, 
#             'ano': {2017: 'Pip', 2018: 'Lin', 2023: 'Bill'}}}

# ====== Testes da criaDicPorAno ======
# {2016: {'Leve': 'Xan', 'Regular': 'Kal'}, 
#  2018: {'Leve': 'Vik', 'Regular': 'Tif', 'Pesado': 'Lin'}, 
#  2022: {'Leve': 'Ted'}, 2023: {'Regular': 'Muy', 'Pesado': 'Bill'}, 
#  2017: {'Pesado': 'Pip'}}




