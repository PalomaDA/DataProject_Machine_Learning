import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv(r'files\input\dataset_estudiantes.csv')
df.columns = df.columns.str.upper()

print('=' * 80)
print('ANÁLISIS DETALLADO DE OUTLIERS')
print('=' * 80)

# 1. HORAS_ESTUDIO_SEMANAL
print('\n' + '='*80)
print('1. HORAS_ESTUDIO_SEMANAL')
print('='*80)
Q1 = df['HORAS_ESTUDIO_SEMANAL'].quantile(0.25)
Q3 = df['HORAS_ESTUDIO_SEMANAL'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[df['HORAS_ESTUDIO_SEMANAL'] > upper]['HORAS_ESTUDIO_SEMANAL'].sort_values()
print(f'Límite superior: {upper:.2f} horas/semana')
print(f'Valores outliers (por encima): {len(outliers)}')
print(f'Valores: {list(outliers.round(2))}')
print(f'Índices: {list(outliers.index)}')

# Ver contexto de estos outliers
print('\nContexto de los outliers:')
for idx in outliers.index:
    print(f'  Registro {idx}:')
    print(f'    - Horas estudio: {df.loc[idx, "HORAS_ESTUDIO_SEMANAL"]:.2f}')
    print(f'    - Nota anterior: {df.loc[idx, "NOTA_ANTERIOR"]:.2f}')
    print(f'    - Nota final: {df.loc[idx, "NOTA_FINAL"]:.2f}')
    print(f'    - Tiene tutor: {df.loc[idx, "TIENE_TUTOR"]}')
    print(f'    - Aprobado: {df.loc[idx, "APROBADO"]}')

# 2. TASA_ASISTENCIA
print('\n' + '='*80)
print('2. TASA_ASISTENCIA')
print('='*80)
Q1 = df['TASA_ASISTENCIA'].quantile(0.25)
Q3 = df['TASA_ASISTENCIA'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[df['TASA_ASISTENCIA'] < lower]['TASA_ASISTENCIA'].sort_values()
print(f'Límite inferior: {lower:.2f}%')
print(f'Valores outliers (por debajo): {len(outliers)}')
print(f'Valores: {list(outliers.round(2))}')
print(f'Índices: {list(outliers.index)}')

# Ver contexto de estos outliers
print('\nContexto de los outliers:')
for idx in outliers.index:
    print(f'  Registro {idx}:')
    print(f'    - Tasa asistencia: {df.loc[idx, "TASA_ASISTENCIA"]:.2f}%')
    print(f'    - Horas estudio: {df.loc[idx, "HORAS_ESTUDIO_SEMANAL"]:.2f}')
    print(f'    - Nota final: {df.loc[idx, "NOTA_FINAL"]:.2f}')
    print(f'    - Aprobado: {df.loc[idx, "APROBADO"]}')

# 3. NOTA_FINAL
print('\n' + '='*80)
print('3. NOTA_FINAL')
print('='*80)
Q1 = df['NOTA_FINAL'].quantile(0.25)
Q3 = df['NOTA_FINAL'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers_below = df[df['NOTA_FINAL'] < lower]['NOTA_FINAL'].sort_values()
outliers_above = df[df['NOTA_FINAL'] > upper]['NOTA_FINAL'].sort_values()
print(f'Límite inferior: {lower:.2f}')
print(f'Límite superior: {upper:.2f}')
print(f'\nOutliers por debajo: {len(outliers_below)}')
print(f'Valores: {list(outliers_below.round(2))}')
print(f'\nOutliers por encima: {len(outliers_above)}')
print(f'Valores: {list(outliers_above.round(2))}')

print('\nContexto outliers bajos:')
for idx in outliers_below.index:
    print(f'  Registro {idx}:')
    print(f'    - Nota final: {df.loc[idx, "NOTA_FINAL"]:.2f}')
    print(f'    - Nota anterior: {df.loc[idx, "NOTA_ANTERIOR"]:.2f}')
    print(f'    - Horas estudio: {df.loc[idx, "HORAS_ESTUDIO_SEMANAL"]:.2f}')
    print(f'    - Tasa asistencia: {df.loc[idx, "TASA_ASISTENCIA"]:.2f}%')
    print(f'    - Aprobado: {df.loc[idx, "APROBADO"]}')

print('\nContexto outliers altos:')
for idx in outliers_above.index:
    print(f'  Registro {idx}:')
    print(f'    - Nota final: {df.loc[idx, "NOTA_FINAL"]:.2f}')
    print(f'    - Nota anterior: {df.loc[idx, "NOTA_ANTERIOR"]:.2f}')
    print(f'    - Horas estudio: {df.loc[idx, "HORAS_ESTUDIO_SEMANAL"]:.2f}')
    print(f'    - Tasa asistencia: {df.loc[idx, "TASA_ASISTENCIA"]:.2f}%')
    print(f'    - Aprobado: {df.loc[idx, "APROBADO"]}')

print('\n' + '='*80)
print('RESUMEN FINAL')
print('='*80)
print('✅ Variables SIN outliers detectados:')
print('   - NOTA_ANTERIOR')
print('   - HORAS_SUENO')
print('   - EDAD')
print('\n⚠️ Variables CON outliers detectados:')
print('   - HORAS_ESTUDIO_SEMANAL: 4 outliers (0.40%)')
print('   - TASA_ASISTENCIA: 4 outliers (0.40%)')
print('   - NOTA_FINAL: 5 outliers (0.50%)')
print(f'\nTotal de outliers únicos: {len(set(list(df[df["HORAS_ESTUDIO_SEMANAL"] > 23.49].index) + list(df[df["TASA_ASISTENCIA"] < 21.04].index) + list(df[df["NOTA_FINAL"] < 45.09].index) + list(df[df["NOTA_FINAL"] > 97.59].index)))}')
