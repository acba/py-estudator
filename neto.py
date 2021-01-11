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
        'cnt': 205,
        'materias': [
            'Português',
            'Direito Constitucional',
            'Direito Penal',
            'Contabilidade',
            'Direito Administrativo',
            'RLM',
            'Direito Processual Penal',
            'Contabilidade',
            'Estatística',
        ]
    }
}

exercicio = {
    'cb': {
        'cnt': 264,
        'materias': [
            'Português',
            'Direito Constitucional',
            'Direito Penal',
            'Direito Administrativo',
            'RLM',
            'Direito Processual Penal',
            'Contabilidade',
            'Estatística',
        ]
    }
}


def get(tipo, ciclo):
    fonte = estudo if tipo == 'estudo' else exercicio
    tempo = '1h20' if tipo == 'estudo' else '15min'
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
    print('===================================================')
    print('=                                                 =')
    print('=        ', dias[atual.isoweekday()], '  -  ',  atual, '         =')
    print('=                                                 =')
    print('===================================================')

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
    get('exercicio', 'cb')

    print()
    print()

def babyday(atual):
    print('===================================================')
    print('=                                                 =')
    print('=        ', dias[atual.isoweekday()], '  -  ',  atual, '         =')
    print('=                                                 =')
    print('===================================================')

    print()
    print('* ESTUDO')
    print()

    get('estudo', 'cb')
    get('estudo', 'cb')
    # get('estudo', 'cb')

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')

    print()
    print()


# atual = date(2020, 12, 21)
atual = date.today()

while atual.isoweekday() < 7:

    calcula_dia_cb(atual)
    atual = atual + timedelta(days=1)


print()
print('###### VARS ######')
print(f"Estudo - CB: {estudo['cb']['cnt']}")
print(f"Exercicio - CB: {exercicio['cb']['cnt']}")
print()