import re
import pandas as pd

with open('tcdf-raw.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    data = re.sub('( \d+ )', ' ', data)

    p = re.compile(r'(\d+),([\s\d\w]+),([\s\d]+.[\s\d]+),([\s\d]+.[\s\d]+),([\s\d]+.[\s\d]+)')
    resultado = p.findall(data)

    df = pd.DataFrame(resultado, columns =['nInscricao', 'Nome', 'P1', 'P2', 'Pfinal'])

    df['P1'] = pd.to_numeric(df['P1'])
    df['P2'] = pd.to_numeric(df['P2'])
    df['Pfinal'] = pd.to_numeric(df['Pfinal'])

    df = df.sort_values(by=['Pfinal'], ascending=False).reset_index()
    df = df.drop(columns=['index'])

    df.to_csv('tcdf.csv', index=False)

