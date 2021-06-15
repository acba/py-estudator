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
        'cnt': 82,
        'materias': [
            # 'Direito Constitucional',
            # 'Direito Penal',
            # 'Direito Processual Penal',
            'Contabilidade',
            'Português',
            'TI - Dados (Aulas 18 a 23)',
            'Direito Administrativo',
            'Contabilidade',
            'Estatística',
            'TI - Redes (Aulas 00 a 05)',
            'RLM',
            'Contabilidade',
            'TI - Dados (Aulas 18 a 23)',
        ]
    }
}

exercicio = {
    'cb': {
        'cnt': 692,
        'materias': [
            'Português',
            'TI - Redes (Aulas 00 a 05)',
            'Contabilidade',
            'RLM',
            'Direito Constitucional',
            'Estatística',
            'TI - Dados (Aulas 18 a 23)',
            'Contabilidade',
            'Direito Penal',
            'TI - Redes (Aulas 00 a 05)',
            'Direito Administrativo',
            'RLM',
            'Português',
            'TI - Dados (Aulas 18 a 23)',
            'Estatística',
            'Contabilidade',
            'TI - Redes (Aulas 00 a 05)',
            'RLM',
            'Direito Processual Penal',
            'TI - Dados (Aulas 18 a 23)',
            'Contabilidade',
            'Estatística',
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
    # get('exercicio', 'cb')

    print()
    print()

def discursiva(atual):
    print('===================================================')
    print('=                                                 =')
    print('=        ', dias[atual.isoweekday()], '  -  ',  atual, '         =')
    print('=                                                 =')
    print('===================================================')

    print()
    print('* DISCURSIVA')
    print()

    print()
    print()

def reta_final(atual):
    print('===================================================')
    print('=                                                 =')
    print('=        ', dias[atual.isoweekday()], '  -  ',  atual, '         =')
    print('=                                                 =')
    print('===================================================')

    print()
    print('* EXERCICIO')
    print()

    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')
    get('exercicio', 'cb')

    print()

    get('exercicio', 'cb')
    get('exercicio', 'cb')


    print()
    print('* REVISÃO')
    print()

    print()
    print()

def sabado(atual):
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
    # get('exercicio', 'cb')
    # get('exercicio', 'cb')

    print()
    print()


atual = date.today()
atual = date(2021, 5, 17)

while atual.isoweekday() < 7:

    if atual.isoweekday() == 6:
        reta_final(atual)
    else:
        reta_final(atual)
    atual = atual + timedelta(days=1)


print()
print('###### VARS ######')
print(f"Estudo - CB: {estudo['cb']['cnt']}")
print(f"Exercicio - CB: {exercicio['cb']['cnt']}")
print()