import pandas as pd

# Cargar v1
df = pd.read_csv('data/dataset_v1.csv')

# Modificaciones para v2
df_v2 = df.copy()
df_v2 = df_v2.dropna()  # Eliminar nulos
df_v2 = df_v2.drop_duplicates()  # Eliminar duplicados

# Guardar v2
df_v2.to_csv('data/dataset_v2.csv', index=False)
print(f"Dataset v2 creado: {df_v2.shape}")