# Considere um dicionário com as atividades da academia com professores e seus respectivos
# horários oferecidas por uma academia, em que cada elemento do dicionário é:
# ATIVIDADE: dicionário interno com professor e lista dos horários
# em que o professor dá aula da atividade.
# Nesse exercício o horário é representado como uma tupla com (DIA, HORA).
# (ver dicionário no bloco principal)

# Observações:
# - não existem duas aulas da mesma atividade em um mesmo horário
# - obviamente um professor não pode dar duas aulas em um mesmo horário
# - as aulas têm duração de 50 minutos


# Escreva uma função, denominada criaDic, que receba um dicionário
# como o descrito acima e, considerando apenas as aulas iniciadas
# ANTES das 18h, crie e retorne um novo dicionario com
# CHAVE: professor
# VALOR: dicionario interno com:
# CHAVE: ATIVIDADE
# VALOR: quantidade de aulas dessa atividade dadas pelo professor
# com inicio antes das 18

# Teste sua função chamando-a com o dicionário fornecido no bloco
# principal e exibindo a resposta retornada
# OBS1: Não pode criar o dic por enumeração


#Escreva a seguir sua função:

def criaDic(dAtiv):
    dicProfAtividade = dict()
    for atividade, dicProf in dAtiv.items():
        for prof, aulas in dicProf.items():
            for aula in aulas:
                if aula[1]<18:
                    dicProfAtividade[prof] = {atividade:aula}
    return dicProfAtividade


    

#BLOCO PRINCIPAL

dAtiv = {'MuayThai': { 'BOB': [('SEG',17), ('SEG',21),('QUA',21)],
'TED':[('QUA',19),('SEX',21)] },
'Boxe': { 'TED': [('SEG',20), ('QUI',20)]},
'JiuJitsu': { 'BOB': [('TER',17), ('QUI',17)],
'LIU': [('SEG',18), ('QUA',18)] },
'Judo': { 'LIU': [('TER',18),('TER',20), ('QUI',17), ('QUI',20)] },
'ZumbaFit': { 'LUK':[('SEX',22)] },
'Aerobica': { 'LUK':[('SEG',18),('SEG',19),('QUA',19)],
'RIK':[('TER',18), ('QUI',18), ('SEX',18)],
'LEO':[('SEG',10),('QUA',10)] },
'Spinning': { 'LEO':[('TER',10),('QUI',10),('SEX',10)],
'RIK':[('TER',17), ('QUI',17)]},
'Yoga': { 'IDA': [('SEG',10), ('QUA',10), ('QUI',15)],
'MIA':[('TER',16), ('QUI',16)] },
'Pilates': { 'MIA':[('SEG',16), ('QUA',16)],
'EVA':[('SEG',14),('TER',17),('SEX',17)],
'VIK':[('QUI',10)] },
'Alongamento': { 'VIK':[('SEG',11), ('TER',11), ('QUI',11)] }
}

print(criaDic(dAtiv))