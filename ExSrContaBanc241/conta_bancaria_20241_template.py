# -*- coding: utf-8 -*-
"""
NOME:
MATRICULA:
TURMA:
PROFESSOR:

"""

import pandas as pd
import matplotlib.pyplot as plt

print('\n------------------------------------------')

'''
Questao1: Trabalhe com Series

O arquivo dadosbancarios.xlsx possui informacoes sobre as contas bancarias 
de um determinado banco.

Uma conta bancaria eh identificada por dois digitos que representam a 
agencia, um tracinho (sinal de menos) e o numero da conta propriamente 
dito. Exemplo: 44-1234  => agencia 44, numero da conta 1234

A planilha saldo tem o saldo inicial no mês das contas.

A planilha tipo tem a informacao sobre o tipo da conta: se basica, regular
ou  especial (classy).

Na planilha natureza ha a informação se a conta eh de uma pessoa fisica ou 
de uma empresa

A planilha operacoes tem a relacao de varias operacoes (creditos e/ou debitos) 
dessas contas bancarias durante um determinado periodo. Na planilha operacoes 
um valor positivo corresponde a uma operacao de credito 
em conta, enquanto valor negativo corresponde a uma operacao de debito em conta

'''

print('\n******************************************')
print('********** Questao 1: Series *************')
print('******************************************')

# Criacao das series
srSaldo= pd.read_excel('dadosbancarios20241.xlsx',sheet_name='saldo',
                     index_col=0, header=0).squeeze() 

srTipoDaConta = pd.read_excel('dadosbancarios20241.xlsx',sheet_name='tipodeconta',
                     index_col=0, header=0).squeeze() 

srNat = pd.read_excel('dadosbancarios20241.xlsx',sheet_name='natureza',
                     index_col=0, header=0).squeeze() 

srOperacoes= pd.read_excel('dadosbancarios20241.xlsx',sheet_name='operacoes',
                     index_col=0, header=0).squeeze() 
print('\n------------------------------------------')
print('Conhecendo as series')
print('\n0.1- Exiba a srSaldo ordenada por valor')

print('\n0.2- Exiba a srTipoDaConta ordenada por indice')

print('\n0.3- Exiba quantas são e quais são naturezas distintas das contas ')

print('\n0.4- Exiba as 5 contas de maior valor absoluto da srOperacoes')

print('\n------------------------------------------')

print('\n1.1.A-Na srSaldo: Qual o valor do maior saldo inicial?  E exiba uma conta com o maior saldo inicial.')

print('\n------------------------------------------')
print('\n1.1.B- Na srSaldo: Exiba os elementos com saldo acima de 500 e abaixo de 2300.')

print('\n------------------------------------------')
print('\n1.1.C- Considerando a srOperacoes, exibir todas as operações da conta 11-456.')


print('\n------------------------------------------')
print('\n1.1.D- Considerando a srTipoDaConta, exibir as contas do tipo classy.')


print('\n------------------------------------------')
print('\n1.1.E- Considerando a srSaldo e srTipoDaConta, exibir os saldos das contas do tipo classy.')


print('\n------------------------------------------')
print('\n1.1.F- Quantas são as contas do tipo regular?')


print('\n------------------------------------------')
print('\n1.1.G- Apresente uma visualização gráfica da srSaldo (barras)')


print('\n------------------------------------------')
print('\n1.1.H- Apresente a tabela de frequencia percentual dos tipos da contas')


print('\n------------------------------------------')
print('\n1.1.I- Apresente a visualização gráfica apropriada da tabela anterior')


print('\n--Trabalhando com a srOperacoes, responda--')
#Trabalhando com a srOperacoes, responda:
print('\n1.2.A- Qual o valor total das operações de CREDITO?')

print('\n1.2.B- Qual percentual de operações de DÉBITO ?')


print('\n------------------------------------------')
print('\n1.3.A -Por CONTA: qual a quantidade de operacoes de CREDITO:')
#Forma1: value_counts() no index


#Forma2: agrupar pelo indice e contar




print('\n------------------------------------------')
print('\n1.3.B-Quais as contas com a maior quantidade de operacoes de CREDITO?')


print('\n------------------------------------------')
print('\n1.4.A-Agrupe a srOperacoes por AGENCIA. Exiba os elementos da agencia 22.')


print('\n------------------------------------------')
print('\n1.4.B- E qual a quantidade de operacoes por AGENCIA:')


print('\n------------------------------------------')
print('\n1.5-Exiba o maior valor ABSOLUTO de uma operacao POR AGENCIA\
 e uma conta da operacao de maior valor absoluto POR AGENCIA.')


print('\n--Considere tambem srSaldo e srTipoDaConta--')
#Considerando tambem as series srSaldo e srTipoDaConta
print('\n1.6.A-Qual o saldo inicial medio POR TipoDaConta?')


print('\n1.6.B-POR TipoDaConta: quant de contas, saldo maximo, saldo minimo, saldo medio, saldo mediano')


print('\n------------------------------------------')
print('\n1.7-Considere o saldo inicial e as operacoes realizadas nas diferentes contas')
print('Exiba o saldo atualizado (final) das contas:')


print('\n------------------------------------------')
# Crie 4 faixas de saldo final: 
#      até 1000 reais(inc) -> BAIXO
#      de 1000 a 5000(inc) -> NORMAL
#      de 5000 a 10000(inc)-> BOM
#      acima de 1000       -> ALTO

print('\n1.8- Exiba a Tab de Freq das faixas de saldo final')


# Um novo imposto emergencial foi criado e sera aplicado sobre os 
# saldos finais das contas. Se a conta for de natureza PESSOAL o 
# desconto sera´ de 5%. Se for de natureza EMPRESARIAL o desconto 
# sera´ de 10%. 

# Deve ser criada uma função calcula_imposto a ser aplicada 
# aos grupos com transform.
# A função deve testar o name da series (nome do grupo)

print('\n1.9- Nova series com imposto a ser pago por conta')

#Função calcula_imposto


#Aplicar funcao no grupo com transform


print('\n1.10.A- Quantidade de contas no cruzamento TipoDaConta X Natureza')
#Use crosstab


print('\n1.10.B- Maior saldo final de uma conta por (no cruzamento) TipoDaConta X Natureza')
#Use crosstab


print('\n--------------------FIM-------------------')
print('------------------------------------------')
