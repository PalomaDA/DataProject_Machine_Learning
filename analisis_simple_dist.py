import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv(r'files\input\dataset_estudiantes.csv')
df.columns = df.columns.str.upper()

numeric_cols = ['HORAS_ESTUDIO_SEMANAL', 'NOTA_ANTERIOR', 'TASA_ASISTENCIA', 'HORAS_SUENO', 'EDAD']

print("ANÁLISIS RESUMIDO PARA ESCALADO")
print("=" * 80)

results = []
for col in numeric_cols:
    sample_data = df[col].dropna().sample(n=min(1000, len(df[col].dropna())), random_state=42)
    _, p_value = stats.shapiro(sample_data)
    skewness = df[col].skew()
    
    normal = "✅ Sí" if p_value > 0.05 else "❌ No"
    asimetria = "Simétrica" if abs(skewness) < 0.5 else ("Positiva" if skewness > 0 else "Negativa")
    
    results.append({
        'Variable': col,
        'Media': df[col].mean(),
        'Std': df[col].std(),
        'Min': df[col].min(),
        'Max': df[col].max(),
        'Rango': df[col].max() - df[col].min(),
        'Normal': normal,
        'p-value': p_value,
        'Skewness': skewness,
        'Asim': asimetria
    })

df_results = pd.DataFrame(results)
print(df_results.to_string(index=False))

print("\n" + "=" * 80)
print("RECOMENDACIONES:")
print("=" * 80)
for result in results:
    col = result['Variable']
    print(f"\n{col}:")
    if result['p-value'] > 0.05 and abs(result['Skewness']) < 0.5:
        print("  ✅ StandardScaler (distribución normal)")
    elif abs(result['Skewness']) > 1:
        print("  ⚠️ RobustScaler (alta asimetría)")
    else:
        print("  🔹 StandardScaler o MinMaxScaler (casi normal)")
