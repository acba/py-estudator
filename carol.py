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
        'cnt': 21,
        'materias': [
            'Português',
            'Auditoria Governamental',
            'Direito Administrativo',

            'Controle Externo',
            'Contabilidade Pública',
            'AFO',

            'Português',
            'Direito Constitucional',
            'Contabilidade Geral',

            'Direito Administrativo',
            'Auditoria Governamental',
            'Português',

            'Controle Externo',
            'AFO',
            'Direito Constitucional',
        ]
    }
}

exercicio = {
    'cb': {
        'cnt': 26,
        'materias': [
            'Português',
            'AFO',
            'Auditoria Governamental',
            'Direito Administrativo',

            'Controle Externo',
            'Português',
            'Contabilidade Pública',
            'AFO',

            'Direito Constitucional',
            'Contabilidade Geral',
            'Português',
            'Auditoria Governamental',

            'Direito Administrativo',
            'AFO',
            'Controle Externo',
            'Português',

            'Contabilidade Pública',
            'Direito Constitucional',
            'Contabilidade Geral'
        ]
    },
}


def get(tipo, ciclo):
    fonte = estudo if tipo == 'estudo' else exercicio
    tempo = '40min' if tipo == 'estudo' else '15min'
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
    get('estudo', 'cb')

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')

    print()
    print()

def dia_mais_leve(atual):
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

    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')

    print()
    print()


def soexercicio(atual):
    print(''.center(80, '='))
    print(f'{dias[atual.isoweekday()]}  -  {atual}'.center(80, '='))
    print(''.center(80, '='))

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'pf')
    get('exercicio', 'pf')
    get('exercicio', 'pf')
    get('exercicio', 'standby')
    get('exercicio', 'standbyce')

    print()
    print()


atual = date.today()
atual = date(2021, 6, 15)


# DIA_SEMANA = {
#     1: 'Segunda Feira',
#     2: 'Terça Feira  ',
#     3: 'Quarta Feira ',
#     4: 'Quinta Feira ',
#     5: 'Sexta Feira  ',
#     6: 'Sábado       ',
#     7: 'Domingo',
# }

while atual.isoweekday() < 7:

    if atual.isoweekday() == 4:
        dia_mais_leve(atual)
    else:
        calcula_dia_cb(atual)
    atual = atual + timedelta(days=1)


print()
print('###### VARS ######')
print(f"Estudo - CB: {estudo['cb']['cnt']}")
print(f"Exercicio - CB: {exercicio['cb']['cnt']}")
print()