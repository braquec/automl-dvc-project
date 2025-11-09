import json
import yaml
import pandas as pd
from datetime import datetime

def generate_report():
    # Cargar métricas
    with open('metrics.json', 'r') as f:
        metrics = json.load(f)
    
    # Cargar parámetros
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    
    # Encontrar el mejor modelo
    best_model_name = metrics.get('best_model', {}).get('name', 'N/A')
    best_r2 = metrics.get('best_model', {}).get('r2', 0)
    
    # Crear reporte markdown
    report_content = f"""# Reporte Final - Laboratorio AutoML con DVC

## Información del Experimento
- **Fecha**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Dataset**: {params['data']['file']} (v{params['data']['version']})
- **Variable objetivo**: {params['preprocess']['target']}

## Mejor Modelo
- **Modelo ganador**: {best_model_name}
- **R² score**: {best_r2:.4f}

## Métricas de Todos los Modelos
"""

    # Agregar métricas de cada modelo
    for model_name, model_metrics in metrics.items():
        if model_name != 'best_model' and isinstance(model_metrics, dict):
            report_content += f"""
### {model_name}
- **MSE**: {model_metrics.get('mse', 'N/A'):.4f}
- **R²**: {model_metrics.get('r2', 'N/A'):.4f}
- **MAE**: {model_metrics.get('mae', 'N/A'):.4f}
"""

    # Agregar parámetros finales
    report_content += f"{model_name}"
