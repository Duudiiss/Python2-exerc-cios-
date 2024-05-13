# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:36:35 2020

@author: Joisa

crosstab
"""
import pandas as pd

ls=['F','F','F','M','M','F','M','F','M']
lcatalt=['ALTA','BAIXA','ALTA','MEDIA','MEDIA','ALTA','MEDIA','BAIXA','BAIXA']
lidade=[3,4,2,3,3,2,4,1,2]
lnome=['LILA','JUJU','DADA','DEDE','DUDU','BIBI','VAVA','MIMI','TATA']

ss= pd.Series(ls,index=lnome,name='Sexo')
print(ss,'\n')
sc= pd.Series(lcatalt,index=lnome, name='CatAlt')
print(sc,'\n')
si= pd.Series(lidade,index=lnome, name='Idade')
print(si,'\n')

print('\nQuantas criancas de cada idade por sexo?')
ct1= pd.crosstab(index=ss, columns=si)
print(ct1)

print('\nQuantas criancas de cada sexo por categoria de altura, com totais?')
ct2= pd.crosstab(index=sc, columns=ss, margins=True)
print(ct2) 

print('\nQual a maior idade no cruzamento catAlt X sexo')
ct3= pd.crosstab(index=sc, columns=ss, values=si, aggfunc='max')
print(ct3) 
