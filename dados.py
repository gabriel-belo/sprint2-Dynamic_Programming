import random
from datetime import datetime, timedelta

def gerar_consumo_diario():
    # Simulando 15 dias de consumo
    insumos = ['Reagente A', 'Reagente B', 'Descartável X', 'Descartável Y']
    consumo_diario = []

    for i in range(15):
        data = (datetime.today() - timedelta(days=14 - i)).strftime('%Y-%m-%d')
        consumo = {
            'data': data,
            'insumo': random.choice(insumos),
            'quantidade': random.randint(5, 50),
            'validade': (datetime.today() + timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d')
        }
        consumo_diario.append(consumo)

    return consumo_diario
