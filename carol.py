import math
from datetime import date, timedelta

dias = {
    1: 'Segunda Feira',
    2: 'Terça Feira  ',
    3: 'Quarta Feira ',
    4: 'Quinta Feira ',
    5: 'Sexta Feira  ',
    6: 'Sábado       ',
    7: 'Domingo',
}

estudo = {
    'cb': {
        'cnt': 304,
        'materias': [
            'Português',
            'RLM',
            'Auditoria Governamental',
            'Controle Externo',
            'Administração Pública',
            'Direito Civil',
            'Finanças Corporativas',
            'Direito Processual Civil',
            'Análise de Dados e Informação',
        ]
    }
}

exercicio = {
    'cb': {
        'cnt': 336,
        'materias': [
            'Português',
            'Direito Administrativo',
            'Direito Constitucional',
            'Auditoria Governamental',
            'Controle Externo',
            'RLM',
            'Estatística',
            # 'Direito Constitucional',
            'Análise de Dados e Informação',
            'Matemática Financeira',
            'Direito Penal',
            'Finanças Corporativas',
            'Direito Civil',
            'Direito Tributário',
            'Direito Processual Civil'
        ]
    },
    'ce': {
        'cnt': 360,
        'materias': [
            'AFO',
            'Contabilidade Geral',
            'Economia',
            'Contabilidade Pública',
            'Contabilidade de Custos',
            'Contabilidade Geral',
            'Contabilidade Pública',
            'AFO',
            'Economia',
            'Contabilidade Geral',
            'Contabilidade Pública',
            {'Licitações, Contratos e Convênios': ['Contratos Administrativos', 'Lei 8.666', 'Pregão - SRP - RDC - Convênios']},
            'Contabilidade Geral',
            'AFO',
            'Contabilidade Pública',
            'Economia',
            'Contabilidade Geral',
            'Contabilidade Pública',
            'AFO',
            'ADC - Análise das Demonstrações Contábeis',
            'Economia',
            'AFO',
            'Contabilidade Geral',
            'Contabilidade Pública',
        ]
    },
    'reforco': {
        'cnt': 5,
        'materias': [
            'Auditoria Governamental',
            'Economia',
            'Controle Externo',
            {'Licitações, Contratos e Convênios': ['Contratos Administrativos', 'Lei 8.666', 'Pregão - SRP - RDC - Convênios']},
            'Análise de Dados e Informação',
        ]
    }
}


def get(tipo, ciclo):
    fonte = estudo if tipo == 'estudo' else exercicio
    tempo = '1h' if tipo == 'estudo' else '15min'
    dado = fonte[ciclo]

    idx = dado['cnt'] % len(dado['materias'])
    materia = dado['materias'][idx]

    if type(materia) == str:
        print(f'{idx} - {materia}: {tempo}')
    elif type(materia) == list:
        itr = math.floor(dado['cnt'] / len(dado['materias']))
        submateria = materia[itr % len(materia)]

        print(f'{idx} - {submateria}: {tempo}')
    elif type(materia) == dict:
        nome_materia = list(materia.keys())[0]

        itr = math.floor(dado['cnt'] / len(dado['materias']))
        submateria = materia[nome_materia][itr % len(materia[nome_materia])]

        print(f'{idx} - {nome_materia}: {submateria}: {tempo}')
    else:
        print(f'Error')

    dado['cnt'] +=1

def calcula_dia_cb(atual):
    print(''.center(80, '='))
    print(f'{dias[atual.isoweekday()]}  -  {atual}'.center(80, '='))
    print(''.center(80, '='))

    print()
    print('* ESTUDO')
    print()

    get('estudo', 'cb')
    get('estudo', 'cb')
    get('estudo', 'cb')

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'reforco')
    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')

    print()
    print()

def calcula_dia_discursiva(atual):
    print(''.center(80, '='))
    print(f'{dias[atual.isoweekday()]}  -  {atual}'.center(80, '='))
    print(''.center(80, '='))

    print()
    print('* DISCURSIVA')
    print()

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'reforco')
    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')

    print()
    print()

def babyday(atual):
    print(''.center(80, '='))
    print(f'{dias[atual.isoweekday()]}  -  {atual}'.center(80, '='))
    print(''.center(80, '='))

    print()
    print('* ESTUDO')
    print()

    get('estudo', 'cb')
    get('estudo', 'cb')
    # get('estudo', 'ce')

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')
    get('exercicio', 'ce')

    print()
    print()

def soexercicio(atual):
    print('===================================================')
    print('=                                                 =')
    print('=        ', dias[atual.isoweekday()], '  -  ',  atual, '         =')
    print('=                                                 =')
    print('===================================================')

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')
    get('exercicio', 'ce')
    get('exercicio', 'cb')
    get('exercicio', 'ce')

    print()
    print()

atual = date.today()


while atual.isoweekday() < 6:

    if atual.isoweekday() == 3:
        calcula_dia_discursiva(atual)
    else:
        calcula_dia_cb(atual)
    atual = atual + timedelta(days=1)


print()
print('###### VARS ######')
print(f"Estudo - CB: {estudo['cb']['cnt']}")
print(f"Exercicio - CB: {exercicio['cb']['cnt']} CE: {exercicio['ce']['cnt']} REF: {exercicio['reforco']['cnt']}")
print()