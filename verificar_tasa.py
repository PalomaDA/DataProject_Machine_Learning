import pandas as pd

df = pd.read_csv(r'files\input\dataset_estudiantes.csv')
df.columns = df.columns.str.upper()

print('VERIFICACIÓN DE TASA_ASISTENCIA')
print('=' * 50)
print(f'Rango real: [{df["TASA_ASISTENCIA"].min():.2f}, {df["TASA_ASISTENCIA"].max():.2f}]')
print(f'Valores > 100: {(df["TASA_ASISTENCIA"] > 100).sum()}')
print(f'Valores < 0: {(df["TASA_ASISTENCIA"] < 0).sum()}')

Q1 = df['TASA_ASISTENCIA'].quantile(0.25)
Q3 = df['TASA_ASISTENCIA'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f'\nAnálisis IQR:')
print(f'Q1 (25%): {Q1:.2f}')
print(f'Q3 (75%): {Q3:.2f}')
print(f'IQR: {IQR:.2f}')
print(f'Límite inferior calculado: {lower_bound:.2f}')
print(f'Límite superior calculado: {upper_bound:.2f}')

outliers_below = df[df['TASA_ASISTENCIA'] < lower_bound]
print(f'\nOutliers por debajo de {lower_bound:.2f}: {len(outliers_below)}')
if len(outliers_below) > 0:
    print(f'Valores: {sorted(outliers_below["TASA_ASISTENCIA"].values)}')
