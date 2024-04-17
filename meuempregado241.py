# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:34:59 2024

@author: PC-PROF
"""

from classeData import Data

# • Um empregado tem:
# o número, nome, salário e data de admissão (dtAdm). 
# Esta última é do tipo Data.
# • Um empregado é criado no sistema sendo para isso fornecidos: 
#     um número, um nome, um salário e dia, mês e ano de sua admissão.
# • O print de um empregado deve exibir todos os seus dados. 
# Esse método deve obrigatoriamente usar método(s) da classe Data.
# • Um empregado pode receber um aumento, devendo para isso ser 
# fornecido o valor desse aumento => método aumento
# • Um empregado deve informar se foi admitido depois de uma certa 
# data (Data) recebida => método admDepoisDe. Esse método deve 
# obrigatoriamente usar método(s) da classe Data.
# • Um empregado deve calcular e retornar seu bônus, considerando 
# a data de hoje. O bônus de um empregado é calculado como 
# 3% do salario * número de anos completos (plenos) do  empregado na empresa 
# => método calculaBonus. Esse método deve obrigatoriamente usar método(s) da classe Data.
# • Um empregado é maior do que o outro se ele está há mais 
# tempo na empresa.


class Empregado:
    
    def __init__(self,num,nome,sal, dia,mes,ano):
        self.numero = num
        self.nome= nome
        self.salario = sal
        self.dtAdm = Data(dia,mes,ano)
        
    def __str__(self): 
        s='Num:{}-Nome:{}-Sal:{:.2f}-Adm:{}'.format(self.numero,
            self.nome, self.salario, self.dtAdm)
        return s
    
    def __repr__(self): 
        s='Num:{}-Nome:{}-Sal:{:.2f}-Adm:{}'.format(self.numero,
            self.nome, self.salario, self.dtAdm)
        return s
    
    def __gt__(self, outroEmp):
        return self.dtAdm < outroEmp.dtAdm
    
    def aumento(self, acresc):
        self.salario += acresc
    
    def admDepoisDe( self, dtInteresse):
        if self.dtAdm > dtInteresse:
            print('{} admitido depois de {}'.format(self.nome,self.dtAdm))
        else:
            print('{} não foi admitido depois de {}'.format(self.nome,self.dtAdm))

    def calculaBonus(self):
        dtHoje= Data()
        totDias = dtHoje - self.dtAdm
        qtdAnosPlenos = totDias//365
        return 0.03*self.salario*qtdAnosPlenos

##################
e1= Empregado (111,'zeus',3000.50, 22,8,2013)
print(e1)
e1.admDepoisDe(Data(20,3,2013))
e1.admDepoisDe(Data(13,4,2015))
e1.aumento(1000)
print(e1)
print('Bonus:',e1.calculaBonus())
print('------------------')
e2= Empregado (999,'hera',3000.50, 21,5,1998)
print(e2)
print('------------------')
if e1>e2:
    print('Mais antigo na empresa:',e1)
else:
    print('Mais antigo na empresa:',e2)

