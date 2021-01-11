import os
import pprint

DIA_SEMANA = {
    1: 'Segunda Feira',
    2: 'Terça Feira  ',
    3: 'Quarta Feira ',
    4: 'Quinta Feira ',
    5: 'Sexta Feira  ',
    6: 'Sábado       ',
    7: 'Domingo',
}

def get_dia(data):
    return DIA_SEMANA[data.isoweekday()]

def parse_int(entrada):
    try:
        saida = int(entrada)
    except:
        saida = None
    return saida

def parse_disciplinas(conteudo):
    disciplinas = {}
    disciplina = ''

    for idx, linha in enumerate(conteudo):
        linha = linha.strip()

        if linha.startswith('##'):
            disciplina = linha.replace('##', '')
            contador = conteudo[idx+1]

            cnt = 0 if parse_int(contador) is None else parse_int(contador)
            disciplinas[disciplina] = {
                'cnt': cnt,
                'assuntos': []
            }
        elif linha.startswith('='):
            pass

        elif parse_int(linha) is None and len(linha) != 0:
            disciplinas[disciplina]['assuntos'].append(linha)

    return disciplinas

def read_disciplinas(path):
    file = open(path, 'r')
    conteudo = file.readlines()
    return parse_disciplinas(conteudo)

def parse_ciclos(conteudo):
    planejamento = {}
    superciclo = ''
    ciclo = ''
    disciplina = ''

    for idx, linha in enumerate(conteudo):
        linha = linha.strip()

        if linha.startswith('-'):
            superciclo = linha.replace('-', '')
            planejamento[superciclo] = {}

        elif linha.startswith('##'):
            disciplina = linha.replace('##', '')
            planejamento[superciclo][ciclo]['materias'].append(disciplina)

        elif linha.startswith('#'):
            ciclo = linha.replace('#', '')
            contador = conteudo[idx+1]

            cnt = 0 if parse_int(contador) is None else parse_int(contador)
            planejamento[superciclo][ciclo] = {
                'cnt': cnt,
                'materias': []
            }

    return planejamento


def read_ciclos(path):
    file = open(path, 'r')
    conteudo = file.readlines()
    return parse_ciclos(conteudo)

def write_disciplinas(path, disciplinas):
    with open(path, 'w') as file:
        lista_disciplinas = list(disciplinas.keys())
        for d in lista_disciplinas:
            file.write(f'##{d}\n')
            if len(disciplinas[d]['assuntos']) != 0:
                file.write(str(disciplinas[d]['cnt']) + '\n')
            assuntos = disciplinas[d]['assuntos']
            for a in assuntos:
                file.write(f'{a}\n')

def write_ciclos(path, dados):
    with open(path, 'w') as file:
        superciclos = list(dados.keys())
        for sc in superciclos:
            file.write(f'\n-{sc}\n')
            ciclos = list(dados[sc].keys())
            for ciclo in ciclos:
                file.write(f'\n#{ciclo}\n')
                file.write(str(dados[sc][ciclo]['cnt']) + '\n\n')
                materias = dados[sc][ciclo]['materias']
                for materia in materias:
                    file.write(f'##{materia}\n')

def get_assunto(ciclo, disciplinas):

    materias = ciclo['materias']
    idx = ciclo['cnt'] % len(materias)
    nome_materia = materias[idx]
    materia = disciplinas[nome_materia]

    ciclo['cnt'] += 1
    ciclo['cnt'] %= len(materias)

    if len(materia['assuntos']) == 0:
        return f'{idx} - {nome_materia}'
    else:
        materia_contador = materia['cnt']
        assuntos = materia['assuntos']
        nome_assunto = assuntos[materia_contador % len(assuntos)]

        materia['cnt'] += 1
        materia['cnt'] %= len(assuntos)
        return f'{idx} - {nome_materia}: {nome_assunto}'

def silentremove(filename):
    try:
        os.remove(filename)
    except:
        pass
