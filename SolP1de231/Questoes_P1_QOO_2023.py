# -*- coding: utf-8 -*-

'''
Questão 2 
Teste as classes construídas por você, executando o código que se encontra 
comentado na área de testes 

'''
from dataP1 import Data
#Escreva aqui a classe Arquivo


class Arquivo:
    
    def __init__(self,nome,autor,dtCriação,texto=''):
        self.nome=nome
        self.autor=autor
        self.dtCriação=dtCriação
        self.texto=texto
        self.dtModificação=dtCriação
        return

    def __str__(self):
        s = 'Arquivo: {}.txt - Autor: {}.\nCriado em {} com {} bytes.'.format(self.nome,self.autor,self.dtCriação,self.tamanho())
        return s
    
    def __repr_(self):
        s = 'Arquivo: {}.txt - Autor: {}.\nCriado em {} com {} bytes.'.format(self.nome,self.autor,self.dtCriação,self.tamanho())
        return s
    
    def __add__(self,outroArq):
        novoArq = Arquivo (self.nome + outroArq.nome, 'sistema', Data(), '{}\n{}'.format(self.texto,outroArq.texto))
        return novoArq
    
    def tamanho(self):
        return len(self.texto)
    
    def substituiTexto(self,novoTexto,novaDt):
        self.texto = novoTexto
        self.dtModificação = novaDt
        return
    
    def adicionaTexto(self,novoTexto,novaDt):
        self.texto += novoTexto
        self.dtModificação = novaDt
        return
    
    def exibeTexto(self):
        print(self.texto)
        return
    
    def ultimaAlteracaoNaData(self,dt):
        return self.dtModificação==dt
    

#Escreva aqui a classe Pasta


class Pasta:
    
    def __init__(self,nome):
        self.nome=nome
        self.lArq=[]
        return
    
    def __str__(self):
        s = 'PASTA: {}   Quantidade de arquivos: {}'.format(self.nome,len(self.lArq))
        return s
    
    def _repr__(self):
        s = 'PASTA: {}   Quantidade de arquivos: {}'.format(self.nome,len(self.lArq))
        return s
    
    def incluiArquivo(self,arqCriado):
        self.lArq.append(arqCriado)
        return
    
    def exibeArquivos(self):
        if len(self.lArq)==0:
            print('PASTA VAZIA')
        else:
            for arquivo in self.lArq:
                print (arquivo)
        return
    
    def alteradosNaData(self,dt):
        for arquivo in self.lArq:
            if arquivo.ultimaAlteracaoNaData(dt):
                print (arquivo)
        return
            
    
        

#-------- Área de teste da questao 2 --------
print('\n------ Teste da Q2 ------')
'''Retire # das linhas abaixo'''
print("\n=====================================")
print("ARQUIVOS CRIADOS")
print("=====================================")

arq1=Arquivo('comprasFrutas','fifi',Data(12,4,2023),'abacate,pera,abacaxi,manga')
print(arq1)
print("Texto do arquivo: ")
arq1.exibeTexto()

'''Adicionando texto'''
dtAlteracao=Data(19,4,2023)
arq1.adicionaTexto(',banana,laranja',dtAlteracao)
print("\n")
print(arq1)
print("Texto do arquivo: ")
arq1.exibeTexto()

'''Teste da data da última alteração'''
if arq1.ultimaAlteracaoNaData(dtAlteracao):
    print("\n\n-->A última alteração do arquivo FOI em {}".format(dtAlteracao))
else:
    print("\n\n-->A última alteração do arquivo NÃO foi em {}".format(dtAlteracao))

print("--------------------------------")
print("--------------------------------")

arq2=Arquivo('comprasBebidas','guga',Data(10,4,2023))
print(arq2)
print("Texto do arquivo: ")
arq2.exibeTexto()

'''Substituindo texto'''
arq2.substituiTexto('suco,água',Data(21,4,2023))
print("\n")
print(arq2)
print("Texto do arquivo: ")
arq2.exibeTexto()

print("--------------------------------")
print("--------------------------------")

'''Juntando dois arquivos'''
arq3=arq1+arq2
print(arq3)
print("Texto do arquivo: ")
arq3.exibeTexto()

'''Teste da data da última alteração'''
hoje=Data()
if arq2.ultimaAlteracaoNaData(hoje):
    print("\n\n-->A última alteração do arquivo FOI em {}".format(hoje))
else:
    print("\n\n-->A última alteração do arquivo NÃO foi em {}".format(hoje))



print("--------------------------------")
print("--------------------------------")

arq4=Arquivo('convBibi','bibi',Data(1,4,2023),'juca,keko,kaka,lilo,mano,mimi,dora,zeze')
print(arq4)
print("Texto do arquivo: ")
arq4.exibeTexto()

print("--------------------------------")
print("--------------------------------")

print("\n======================================")
print("PASTA CRIADA")
print("======================================")
pasta1=Pasta('festaNiver')
print(pasta1)
print("--------------------------------")
print("Arquivos da pasta")
pasta1.exibeArquivos()


print("\n======================================")
print("ARQUIVOS INCLUIDOS NAS PASTAS")
print("======================================")

'''Incluindo arquivos na pasta '''
pasta1.incluiArquivo(arq1)
pasta1.incluiArquivo(arq2)
pasta1.incluiArquivo(arq3)
pasta1.incluiArquivo(arq4)

'''Exibindo pasta atualizada'''
print(pasta1)
print("Arquivos da pasta")
pasta1.exibeArquivos()
print("--------------------------------")

'''Exibindo arquivos modificados em determinada data'''
print("Arquivos alterado hoje na pasta {}\n".format(pasta1))
pasta1.alteradosNaData(Data())


print('\n---- Fim do Teste da Q3 ----')             
