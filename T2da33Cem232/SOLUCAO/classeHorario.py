# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:09:11 2020

@author: cf
"""
#from datetime import datetime
'''
Horario - Atributos:  hora, min, seg 
           e tempo total(em seg, usado internamente na classe)
Métodos:
construtor:	 este método constrói um objeto Horario, a partir de hora,minuto e segundo,
             com os seguintes default: h=0, m=0, s=0
             Obs: não verifica se h,m,s incorretos
   
apresentação:	 retorna uma string com os valores dos atributos no formato "hh:mm:ss"
-:	 recebe um outro Horario e retorna um novo Horario  equivalente a diferença de tempo entre os horários recebidos
+:	 recebe um outro Horario e retorna um novo Horario  equivalente a soma dos tempos dos horários recebidos
+=:	 recebe um outro Horario e atualiza o Horário com a soma dos tempos dos horários recebidos
	
==:  Recebe  como parâmetro um outro objeto da classe Horário, realizando a operação 
     de comparação equivalente ao operador relacional
!=:	Recebe  como parâmetro um outro objeto da classe Horário, realizando a operação 
     de comparação equivalente ao operador relacional
>:  retorna True se for maior (cronologicamente) do que um horario recebido como parâmetro 
<:	retorna True se for menor (cronologicamente) do que um horario recebido como parâmetro

>=:  retorna True se for maior ou igual (cronologicamente) a um horario recebido como parâmetro 
<=:	retorna True se for menor ou igual (cronologicamente) a um horario recebido como parâmetro
	
getSeg:	   retorna os segundos do horário
getMin:	   retorna os minutos do horário
getHora:   retorna as horas do horário
getTempo:  retorna o tempo total em segundos do horário	
	
clone:	o objeto clona a si próprio, para isto, ele cria um novo objeto da classe Horario com os
	    mesmos valores de atributos e retorna sua referência
        
setSeg:	recebe um valor  e  altera o atributo minuto. Recalcula o tempo 
        decorrido e pode recalcular o valor da hora e do minuto, quando segundos >60
setMin:	recebe um valor  e  altera o atributo minuto. Recalcula o tempo 
        decorrido e pode recalcular o valor da hora, quando minutos >60
setHora: recebe um valor  e  altera o atributo hora. Recalcula o tempo decorrido

totSegundos:  retorna o tempo em s
totMinutos:   retorna o tempo em minutos
totHoras:     retorna o tempo em horas
 
'''
class Horario:
    def __init__(self, h=0,m=0,s=0):
    
        self.hora = h
        self.min = m
        self.seg = s
        self.tempo = self.hora*3600+self.min*60 + self.seg
        return
    
    def __str__(self): 
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)
    def __repr__(self): 
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)
    
    def __add__(self,outro):
        tot=abs(self.tempo+outro.tempo)
        return geraHorario(tot)
    
    def __sub__(self,outro):
        dif=abs(self.tempo-outro.tempo)
        return geraHorario(dif)
    
    def __iadd__(self,outro):
        tot=abs(self.tempo+outro.tempo)
        self.setTempo(tot)
        (self.hora,self.min,self.seg)=transforma(tot)
        return self
    
    def __eq__(self,outro):
        return(self.tempo==outro.tempo)
    def __ne__(self,outro):
        return(self.tempo != outro.tempo)
    def __lt__(self,outro):
        return(self.tempo<outro.tempo)
    def __gt__(self,outro):
        return(self.tempo>outro.tempo)
    def __le__(self,outro):
        return(self.tempo<=outro.tempo)
    def __ge__(self,outro):
        return(self.tempo>=outro.tempo)

    def setSeg(self,s):
        if s <= 60:
            self.seg=s
        else:
            h=s//3600
            s=s%3600
            m=s//60
            s=s%60
        self.hora+=h
        self.min+=m
        self.seg=s
        self.tempo = self.hora*3600+self.min*60 + self.seg
       
    def setMin(self,m):
        if m <= 60:
            self.min=m
        else: 
            self.min=m%60
            self.hora+=m//60
        self.tempo = self.hora*3600+self.min*60 + self.seg
        
    def setHora(self,h):
            self.hora=h
            self.tempo = self.hora*3600+self.min*60 + self.seg
            
    def setTempo(self,tempo):
        if tempo>0:
            self.tempo=tempo
            (self.hora,self.min,self.seg)=transforma(tempo)

    

    def getSeg(self):
        return self.seg
    def getMin(self):
        return self.min
    def getHora(self):
        return self.hora
    def getTempo(self):
        return self.tempo
    
    def totSegundos(self):
        return self.tempo
    def totMinutos(self):
        return self.tempo/60
    def totHoras(self):
        return self.tempo/3600

    def copia(self):
        return Horario(self.hora,self.min,self.seg)
    # funções auxiliares

def transforma(tempo):
    h=tempo//3600
    m=tempo%3600//60
    s=tempo%3600%60
    return (h,m,s)

def geraHorario(tempo):
    (h,m,s)=transforma(tempo)
    return Horario(h,m,s)
