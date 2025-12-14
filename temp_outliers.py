import pandas as pd
import numpy as np
from scipy.stats import zscore

# Cargar datos
df = pd.read_csv(r'files\input\dataset_estudiantes.csv')
df.columns = df.columns.str.upper()

print('=' * 80)
print('ANÁLISIS DE OUTLIERS - MÉTODO IQR')
print('=' * 80)

numeric_cols = ['HORAS_ESTUDIO_SEMANAL', 'NOTA_ANTERIOR', 'TASA_ASISTENCIA', 'HORAS_SUENO', 'EDAD', 'NOTA_FINAL']

for col in numeric_cols:
    print(f'\n{col}:')
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers_count = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
    pct = (outliers_count / len(df)) * 100
    
    print(f'  Rango válido: [{lower_bound:.2f}, {upper_bound:.2f}]')
    print(f'  Outliers: {outliers_count} ({pct:.2f}%)')
    
    if outliers_count > 0:
        below = (df[col] < lower_bound).sum()
        above = (df[col] > upper_bound).sum()
        print(f'  - Por debajo: {below}')
        print(f'  - Por encima: {above}')
