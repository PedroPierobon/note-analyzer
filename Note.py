import pandas as pd
import numpy as np


df = pd.read_csv('notas_alunos.csv')
df['media'] = (df['nota_1'] + df['nota_2']) / 2
df['situacao'] = np.where(df['media'] >= 7.0, 'Aprovado', 'Reprovado')
df.to_json('notas_finais.json', orient='records')
print(df['situacao'])