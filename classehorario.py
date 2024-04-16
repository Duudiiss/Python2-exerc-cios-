from datetime import datetime
'''
Horario - Atributos: hora, min, seg
e tempo total(em seg, usado internamente na classe)
Métodos:
construtor: este método constrói um objeto Horario, a partir de hora,minuto e segundo,
com os seguintes default: h=0, m=0, s=0
Obs: não verifica se h,m,s incorretos

apresentação: retorna uma string com os valores dos atributos no formato "hh:mm:ss"
-: recebe um outro Horario e retorna um novo Horario equivalente a diferença de tempo entre os horários recebidos
+: recebe um outro Horario e retorna um novo Horario equivalente a soma dos tempos dos horários recebidos
+=: recebe um outro Horario e atualiza o Horário com a soma dos tempos dos horários recebidos

==: Recebe como parâmetro um outro objeto da classe Horário, realizando a operação
de comparação equivalente ao operador relacional
!=: Recebe como parâmetro um outro objeto da classe Horário, realizando a operação
de comparação equivalente ao operador relacional
>: retorna True se for maior (cronologicamente) do que um horario recebido como parâmetro
=: retorna True se for maior ou igual (cronologicamente) a um horario recebido como parâmetro
60
setMin: recebe um valor e altera o atributo minuto. Recalcula o tempo
decorrido e pode recalcular o valor da hora, quando minutos >60
setHora: recebe um valor e altera o atributo hora. Recalcula o tempo decorrido
totSegundos: retorna o tempo em s
totMinutos: retorna o tempo em minutos
totHoras: retorna o tempo em horas

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
        return tot

    def __sub__(self,outro):
        dif=abs(self.tempo-outro.tempo)
        return dif

    def __iadd__(self,outro):
        tot=abs(self.tempo+outro.tempo)
        self.setTempo(tot)
        (self.hora,self.min,self.seg)==transforma(tot)
        return self

    def __eq__(self,outro):
        return(self.tempo==outro.tempo)
    def __ne__(self,outro):
        return(self.tempo != outro.tempo)
    def __lt__(self,outro):
        return(self.tempooutro.tempo)
    def __le__(self,outro):
        return(self.tempo=outro.tempo)
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
