from collections import Counter

materias = [
    'Português',
    'Auditoria Governamental',
    'Direito Administrativo',

    'Controle Externo',
    'Contabilidade Pública',
    'Contabilidade Pública',
    'AFO',

    'Português',
    'Direito Constitucional',
    'Contabilidade Geral',
    'Contabilidade Geral',

    'Direito Administrativo',
    'Direito Administrativo',
    'AFO',
    'Auditoria Governamental',
    'Português',
    'Português',

    'Controle Externo',
    'AFO',
    'Direito Constitucional',
]


def spread(items):

    grouped = Counter(items).most_common()
    desalocados = sum([d[1] for d in grouped])
    placements = [None] * desalocados

    for el in grouped:
        tipo = el[0]
        qtd = el[1]

        instance = 0

        blank_count = -1
        for idx in range(len(placements)):
            if placements[idx] is None:
                blank_count += 1

                if blank_count * qtd // desalocados == instance:
                    placements[idx] = tipo
                    instance += 1

        desalocados -= qtd

    return placements


print(spread(materias))

[
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
