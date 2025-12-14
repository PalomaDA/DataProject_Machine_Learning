import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cargar datos
df = pd.read_csv(r'files\input\dataset_estudiantes.csv')
df.columns = df.columns.str.upper()

# Variables numéricas (excluyendo la variable objetivo)
numeric_cols = ['HORAS_ESTUDIO_SEMANAL', 'NOTA_ANTERIOR', 'TASA_ASISTENCIA', 
                'HORAS_SUENO', 'EDAD']

print("=" * 80)
print("ANÁLISIS DE DISTRIBUCIONES - VARIABLES NUMÉRICAS")
print("=" * 80)

for col in numeric_cols:
    print(f"\n{'=' * 80}")
    print(f"{col}")
    print(f"{'=' * 80}")
    
    # Estadísticas descriptivas
    print("\n📊 Estadísticas:")
    print(f"  Media: {df[col].mean():.2f}")
    print(f"  Mediana: {df[col].median():.2f}")
    print(f"  Desv. Std: {df[col].std():.2f}")
    print(f"  Min: {df[col].min():.2f}")
    print(f"  Max: {df[col].max():.2f}")
    print(f"  Rango: {df[col].max() - df[col].min():.2f}")
    
    # Test de normalidad (Shapiro-Wilk) - máximo 5000 muestras
    if len(df[col].dropna()) > 0:
        sample_size = min(5000, len(df[col].dropna()))
        sample_data = df[col].dropna().sample(n=sample_size, random_state=42)
        statistic, p_value = stats.shapiro(sample_data)
        print(f"\n📈 Test de Normalidad (Shapiro-Wilk):")
        print(f"  p-value: {p_value:.6f}")
        if p_value > 0.05:
            print(f"  ✅ Distribución normal (p > 0.05)")
        else:
            print(f"  ❌ NO es distribución normal (p <= 0.05)")
    
    # Asimetría y curtosis
    skewness = df[col].skew()
    kurtosis = df[col].kurtosis()
    print(f"\n📐 Forma de la distribución:")
    print(f"  Asimetría (Skewness): {skewness:.3f}")
    if abs(skewness) < 0.5:
        print(f"    → Distribución simétrica")
    elif skewness > 0:
        print(f"    → Asimétrica positiva (cola derecha)")
    else:
        print(f"    → Asimétrica negativa (cola izquierda)")
    
    print(f"  Curtosis: {kurtosis:.3f}")
    if abs(kurtosis) < 0.5:
        print(f"    → Distribución normal (mesocúrtica)")
    elif kurtosis > 0:
        print(f"    → Colas pesadas (leptocúrtica)")
    else:
        print(f"    → Colas ligeras (platicúrtica)")

# Crear visualizaciones
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('DISTRIBUCIONES DE VARIABLES NUMÉRICAS', fontsize=16, fontweight='bold')

for idx, col in enumerate(numeric_cols):
    row = idx // 3
    col_idx = idx % 3
    
    # Histograma con KDE
    axes[row, col_idx].hist(df[col].dropna(), bins=30, edgecolor='black', alpha=0.7, color='#809671')
    axes[row, col_idx].set_title(f'{col}', fontweight='bold')
    axes[row, col_idx].set_xlabel('Valores')
    axes[row, col_idx].set_ylabel('Frecuencia')
    axes[row, col_idx].grid(True, alpha=0.3)
    
    # Añadir línea de media
    mean_val = df[col].mean()
    axes[row, col_idx].axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Media: {mean_val:.2f}')
    axes[row, col_idx].legend()

# Eliminar el último subplot vacío
fig.delaxes(axes[1, 2])

plt.tight_layout()
plt.savefig(r'C:\Users\Usuario\.gemini\antigravity\brain\767b1282-36e1-4320-85f7-d8a426613d13\distribuciones_numericas.png', 
            dpi=150, bbox_inches='tight')
print("\n✅ Gráficos guardados")

print("\n" + "=" * 80)
print("ANÁLISIS COMPLETADO")
print("=" * 80)
