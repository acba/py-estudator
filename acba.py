import os
from datetime import date, timedelta
import utils

def calcula_dia(ciclos, disciplinas, atual, path):
    with open(path, 'a') as f:
        print(''.center(80, '='), file=f)
        print(f'{utils.get_dia(atual)}  -  {atual}'.center(80, '='), file=f)
        print(''.center(80, '='), file=f)

        print('\n* ESTUDO\n', file=f)
        print(utils.get_assunto(ciclos['estudo']['cb'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['estudo']['ce'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['estudo']['cb'], disciplinas), file=f)

        print('\n* EXERCICIO\n', file=f)

        print(utils.get_assunto(ciclos['exercicio']['reforco'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['exercicio']['cb'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['exercicio']['ce'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['exercicio']['cb'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['exercicio']['ce'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['exercicio']['cb'], disciplinas), file=f)
        print(utils.get_assunto(ciclos['exercicio']['ce'], disciplinas), file=f)

        print('\n', file=f)

disciplinas  = utils.read_disciplinas('dados/acba.disciplinas')
ciclos       = utils.read_ciclos('dados/acba.ciclos')

utils.silentremove('dados/acba.planilha')

atual = date.today()
atual = date(2021, 1, 4)

while atual.isoweekday() < 7:
    calcula_dia(ciclos, disciplinas, atual, 'dados/acba.planilha')
    atual = atual + timedelta(days=1)

utils.write_ciclos('dados/acba.ciclos.out', ciclos)
utils.write_disciplinas('dados/acba.disciplinas.out', disciplinas)