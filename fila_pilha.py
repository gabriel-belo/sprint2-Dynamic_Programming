from collections import deque

# Função para registrar o consumo na fila (FIFO)
def registrar_na_fila(consumo_diario):
    fila_consumo = deque()
    for registro in consumo_diario:
        fila_consumo.append(registro)
    return fila_consumo

# Função para registrar o consumo na pilha (LIFO)
def registrar_na_pilha(consumo_diario):
    pilha_consumo = []
    for registro in consumo_diario:
        pilha_consumo.append(registro)
    return pilha_consumo
