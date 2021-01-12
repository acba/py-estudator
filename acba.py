from datetime import date, timedelta
import utils

disciplinas  = utils.read_disciplinas('dados/acba.disciplinas')
ciclos       = utils.read_ciclos('dados/acba.ciclos')
alocacao     = utils.read_alocacao('dados/acba.alocacao')

utils.silentremove('dados/acba.planilha.out')

atual = date.today()

while atual.isoweekday() < 7:
    utils.calcula_dia(ciclos, disciplinas, alocacao, atual, 'dados/acba.planilha.out')
    atual = atual + timedelta(days=1)

utils.write_ciclos('dados/acba.ciclos.out', ciclos)
utils.write_disciplinas('dados/acba.disciplinas.out', disciplinas)