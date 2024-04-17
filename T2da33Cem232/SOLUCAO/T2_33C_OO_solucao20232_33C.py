# -*- coding: utf-8 -*-

# NOME COMPLETO:
# MATRICULA:
# TURMA:
# PROFESSOR:


from classeHorario import Horario
from classeData import Data

#Escreva a seguir a classe Pedido


class Pedido:
    
    def __init__(self, numero, cliente, valor, hInicialPedido, dataPedido=Data() ):
        self.numero = numero
        self.cliente= cliente
        self.valor= valor
        self.horario = hInicialPedido
        self.data = dataPedido
        self.horarioDeEntrega = Horario()
        
    def __str__(self):
        s='Num:{}-Cli:{}-Data:{}-Horario:{}-Status:{}'.format(
            self.numero,self.cliente,self.data,self.horario,self.obtemStatus())
        return s
    
    def __repr__(self):
        s='Num:{}-Cli:{}-Data:{}-Horario:{}-Status:{}'.format(
            self.numero,self.cliente,self.data,self.horario,self.obtemStatus())
        return s
    
    def __lt__(self, outroPed):
        if self.data == outroPed.data: 
            return self.horario < outroPed.horario
        return self.data < outroPed.data
    
    def registraHorarioDeEntrega(self, horEntrega):
        self.horarioDeEntrega = horEntrega
        
    def obtemStatus(self):
        if self.horarioDeEntrega == Horario():
            return 'EmAndamento'
        else:
            return 'Entregue'
    
    def calculaTempoDeEspera(self):
        if self.obtemStatus()=='Entregue':
            return self.horarioDeEntrega - self.horario
        else:
            return 'Sem registro de entrega'
    
    def obtemValor(self):
        if self.data.getMes()==9:
            return self.valor*0.9
        else:
            return self.valor
        



#Escreva a seguir a classe Entregador

class Entregador:
    
    def __init__(self,nome, tipoDeTransporte):
        self.nome= nome
        self.tipoDeTransporte = tipoDeTransporte
        self.lPedidos= []
        
        
    def __str__(self):
        s='Nome:{}-ListaDePedidos:{}'.format(self.nome,self.lPedidos)
        return s
    
    def __repr__(self):
        s='Nome:{}-ListaDePedidos:{}'.format(self.nome,self.lPedidos)
        return s
    
    def incluiPedido(self,ped):
        self.lPedidos.append(ped)
     
    def exibeListaDePedidos(self):
        print(self.lPedidos)
    
    
    def exibePagamento(self):
        if self.tipoDeTransporte == 'moto' :
            lim = Horario(1,30)       
        else:
            lim = Horario(2,30)
        tot= 0.0
        
        for ped in self.lPedidos:
            if ped.obtemStatus()=='Entregue':
                if ped.calculaTempoDeEspera() < lim:
                    tot+=7
                else:
                    tot+=5
            else:
                tot-= 0.1*ped.obtemValor()
        print('{}-Pagamento de {:.2f} reais'.format(self.nome, tot))
        
        




##############################################################
# Teste suas classes tirando os #
print('---- Testes da classe Pedido -----')
ped= Pedido(22,'lala',125.50,Horario(14,30), Data(18,9,2023))
print(ped)
print(ped.calculaTempoDeEspera())
ped.registraHorarioDeEntrega(Horario(16,20))
print(ped)
print(ped.calculaTempoDeEspera())
print(ped.obtemValor())
print('---------')
ped2= Pedido(11,'vivi',100,Horario(19,30), Data(25,8,2023))
print(ped2)
print(ped2.obtemValor())
print('---------')
ped3=Pedido(44,'xuxu',130,Horario(16,45), Data(19,9,2023))
ped3.registraHorarioDeEntrega(Horario(21,30))
print(ped3)
print(ped3.calculaTempoDeEspera())
print(ped3.obtemValor())
print('---------')
ped4= Pedido(99,'zizi',180,Horario(14,25), Data(19,9,2023))
print(ped4)
print(ped4<ped)
print(ped4<ped3)
ped4.registraHorarioDeEntrega(Horario(16,20))
print('---------')
ped5= Pedido(66,'kiki',110,Horario(18,15))
print(ped5) #  aqui saira a data de hoje
ped5.registraHorarioDeEntrega(Horario(19,13))
print('---------')
print('---- Testes da classe Entregador -----')
entreg= Entregador('EDY','bike')
print(entreg)
print('---------')
entreg.incluiPedido((ped))
entreg.incluiPedido((ped2))
entreg.incluiPedido((ped3))
entreg.incluiPedido((ped4))
entreg.incluiPedido((ped5))
print(entreg)
print('---------')
entreg.exibePagamento()


################################################
# SAIDA ESPERADA

# ---- Testes da classe Pedido -----
# Num:22-Cli:lala-Data:18/09/2023-Horario:14:30:00-Status:EmAndamento
# Sem registro de entrega
# Num:22-Cli:lala-Data:18/09/2023-Horario:14:30:00-Status:Entregue
# 01:50:00
# 112.95
# ---------
# Num:11-Cli:vivi-Data:25/08/2023-Horario:19:30:00-Status:EmAndamento
# 100
# ---------
# Num:44-Cli:xuxu-Data:19/09/2023-Horario:16:45:00-Status:Entregue
# 04:45:00
# 117.0
# ---------
# Num:99-Cli:zizi-Data:19/09/2023-Horario:14:25:00-Status:EmAndamento
# False
# True
# ---------
# Num:66-Cli:kiki-Data:23/09/2023-Horario:18:15:00-Status:EmAndamento
# ---------
# ---- Testes da classe Entregador -----
# Nome:EDY-ListaDePedidos:[]
# ---------
# Nome:EDY-ListaDePedidos:[Num:22-Cli:lala-Data:18/09/2023-Horario:14:30:00-Status:Entregue,
#                          Num:11-Cli:vivi-Data:25/08/2023-Horario:19:30:00-Status:EmAndamento, 
#                          Num:44-Cli:xuxu-Data:19/09/2023-Horario:16:45:00-Status:Entregue, 
#                          Num:99-Cli:zizi-Data:19/09/2023-Horario:14:25:00-Status:Entregue, 
#                          Num:66-Cli:kiki-Data:23/09/2023-Horario:18:15:00-Status:Entregue]
# ---------
# EDY-Pagamento de 16.00 reais



