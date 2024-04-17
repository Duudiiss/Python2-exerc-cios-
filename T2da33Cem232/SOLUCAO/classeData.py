# -*- coding: utf-8 -*-
from datetime import date
'''
Constrói um objeto Data, a partir do dia, mês e ano
Data
Atributos: dia, mês e ano
Métodos:
construtor:	 recebe dia,mes,ano de uma data. Caso os 3 valores não sejam fornecidos
             a data é criada como a data de HOJE (parâmetro default).
             Obs:  se dia,mes,ano fornecidos não especifiquem uma data correta,
             é criada a data  01/01/0001
apresentação:	 retorna uma string com os valores dos atributos
-:	 recebe uma outra data e retorna a quantidade de dias entre as datas (valor absoluto)
+:	Recebe um número de dias e retorna a data após/antes este intervalo de dias
+=:	Recebe um nº de dias e altera o objeto para a data após/antes este intervalo de dias
	
==:	Recebe  como parâmetro um outro objeto da classe Data, realizando a operação de comparação equivalente ao operador relacional
!=:	
>:  retorna True se  for mais recente do que uma data recebida como parâmetro
<:  retorna True se  for mais antiga do que uma data recebida como parâmetro 
	
getDia:	retorna o dia da data	
getMes:	retorna o mês da data
getMesExtenso:	retorna o mês da data corrente por extenso
getAno:	retorna o ano da data
diaDaSemana:	Retorna o dia da semana da data

setDia:	recebe um dia e o altera se for válido
setMes:	recebe um mês e o altera se for válido
setAno:	recebe um mês e o altera se for válido

isMesValido	Retorna True se é um valor de mês válido ou False caso contrário'
isDiaValido	Retorna True se é um dia válido para o mês ou False caso contrário
isBissexto	retorna verdadeiro se o ano da data corrente for bissexto e falso caso contrário (múltiplo de 4 e (não múltiplo de 100 ou múltiplo de 400))

copia:	o objeto clona a si próprio, para isto, ele cria um novo objeto da classe Data com os
	mesmos valores de atributos e retorna sua referência pelo método


'''
class Data:
    def __init__(self, dia=date.today().day,mes=date.today().month,ano=date.today().year):
        '''recebe um valor de dia, mes e ano, todos inteiros, e cria um objeto. 
           Default: : data atual
           Caso os valores fornecidos estejam incorretos, cria a data 1/1/1'''
        self.ano = ano
        self.mes = mes
        self.dia = dia
        if not self.isMesValido(mes) or not self.isDiaValido(dia):
            self.ano = 1
            self.mes = 1
            self.dia = 1
        self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)

    def __str__(self): 
        '''retorna uma string da data no format dd/mm/aaaa'''
        return "{:0>2d}/{:0>2d}/{:0>4d}".format(self.dia, self.mes,self.ano)
    
    def __repr__(self): 
        '''retorna uma string da data no format dd/mm/aaaa'''
        return "{:0>2d}/{:0>2d}/{:0>4d}".format(self.dia, self.mes,self.ano)

    def __sub__(self, outra): # dias entre duas datas
        '''recebe  uma  Data e retorna a quantidade de dias entre elas'''
        djnovo=abs(self.djul-outra.djul)
        return (djnovo)
    
    def __add__(self,x=20): # data após/antes x dias
        '''Recebe um número de dias e retorna a data após/antes este intervalo de dias'''
        djnovo=self.djul+x
        (d,m,a)=convDiaJulianoData(djnovo)
        return Data(d,m,a)    

    def __iadd__(self,x=20): # data após/antes x dias
        '''Recebe um número de dias e altera o objeto para a data após/antes este intervalo de dias'''
        djnovo=self.djul+x
        (d,m,a)=convDiaJulianoData(djnovo)
        self.ano = a
        self.mes = m
        self.dia = d
        return self  

    def __eq__(self,outra):
        '''recebe  uma  Data e retorna True se tiver os mesmos valores de atributo 
        e False caso contrário.'''
        return(self.djul==outra.djul)
    def __neq__(self,outra):
        '''recebe  uma  Data e retorna True se não tiver os mesmos valores de atributo 
        e False caso contrário.'''
        return(self.djul!=outra.djul)
    def __lt__(self,outra):
        '''recebe  uma  Data e retorna True se for mais antiga que a Data recebida  
            e False caso contrário.'''
        return(self.djul <outra.djul)
    def __gt__(self,outra):
        '''recebe  uma  Data e retorna True se for mais recente que a Data recebida  
            e False caso contrário.'''
        return(self.djul> outra.djul)


    def isBissexto(self):
        '''Retorna True se é ano bissexto ou False caso contrário'''
        ano=self.ano
        return ano%4==0 and (ano%100!=0 or ano%400==0)

    def copia(self):
        '''Retorna uma cópia da Data'''
        return Data(self.dia,self.mes,self.ano)

    def getMes(self):
        '''Retorna o número do mês'''
        return self.mes
    def getAno(self):
        '''Retorna o ano'''
        return self.ano
    def getDia(self):
        '''Retorna o dia'''
        return self.dia
    def getMesExtenso(self):
        '''Retorna uma string com o mês por extenso'''
        tMeses=('Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez')
        return tMeses(self.getMes()-1)
    
    def setMes(self, m):
        '''Recebe um valor e atualiza o atributo mês, se correto para o dia'''
        mes = self.mes
        if self.isMesValido(m):
            self.mes=m
            if not self.isDiaValido(self.dia): # mes tornou o dia invalido
                self.mes=mes
            else:
                self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)
        return
    
    def setAno(self,a):
        '''Recebe um valor e atualiza o atributo ano'''
        self.ano=a
        self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)
        return
    
    def setDia(self,d):
        '''Recebe um valor e atualiza o atributo dia, se correto para o mês'''
        if self.isDiaValido(d):
            self.dia=d
            self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)
        return 
    
    def diaDaSemana(self):
        '''Retorna o dia da semana'''
        tDia=('SAB','DOM','SEG','TER','QUA','QUI','SEX')
        a = (12 - self.getMes())// 10
        b = self.getAno() - a 
        c = self.getMes() + 12*a  
        d = b//100
        e=  d//4
        f = 2-d+e
        g = int(365.25*b)
        h=  int ( 30.6001 * (c + 1))
        i = f + g + h + self.getDia() + 5
        return(tDia[ i%7])

       
    def isMesValido(self,mes):
        '''Retorna True se é um valor de mês válido ou False caso contrário'''
        return mes>0 and mes<13

    def isDiaValido(self,dia):
        '''Retorna True se é um dia válido para o mês ou False caso contrário'''
        tDias=(31,28,31,30,31,30,31,31,30,31,30,31)
        mes= self.getMes()
        if mes==2:
            if self.isBissexto():
                maior=28
            else:
                maior=29
        else:
            maior = tDias[mes-1]
        return dia>0 and dia<=maior
#AUXILARES
def convDataDiaJuliano(dia,mes,ano):
    if mes < 3:
        ano=ano-1
        mes=mes+12
    A=int(ano/100)
    B=int(A/4)
    C=2-A+B
    D = int(365.25 * (ano + 4716))
    E = int(30.6001 * (mes + 1))
    F = D + E + dia + 0.5 + C - 1524.5
    return int(F)

def convDiaJulianoData(juliano):
    A = juliano
    if A > 2299160:
        B =int((A - 1867216.25) / 36524.25)
        C = A + 1 + B - int(B / 4)
    else:
        C = A
    D = C + 1524
    E = int((D - 122.1) / 365.25)
    F = int(E * 365.25)
    G = int((D - F) / 30.6001)
    H = D - F - int(G * 30.6001)
    if G < 14:
        I = G - 1
    else:
        I = G - 13
    if I > 2:
        J = E - 4716
    else:
        J = E - 4715
    if J > 0:
        K = J
    else:
        K = abs(J + 1)
    return(H,I,K)
 
