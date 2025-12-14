import pandas as pd

df = pd.read_csv(r'files\input\dataset_estudiantes.csv')
df.columns = df.columns.str.upper()

# Obtener variables categóricas
cat_cols = df.select_dtypes(include='object').columns.tolist()

print('VARIABLES CATEGÓRICAS DEL DATASET')
print('=' * 60)

for col in cat_cols:
    print(f'\n{col}:')
    print(f'  Categorías: {df[col].nunique()} únicas')
    print(f'  Valores: {sorted(df[col].dropna().unique())}')
    print(f'  Distribución:')
    print(df[col].value_counts().to_string())
    print(f'  Nulos: {df[col].isnull().sum()}')
