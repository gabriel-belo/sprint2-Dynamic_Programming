# Função de Busca Sequencial
def busca_sequencial(lista, nome_insumo):
    for item in lista:
        if item['insumo'] == nome_insumo:
            return item
    return None

# Função de Busca Binária (Requer lista ordenada)
def busca_binaria(lista, nome_insumo):
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid]['insumo'] == nome_insumo:
            return lista[mid]
        elif lista[mid]['insumo'] < nome_insumo:
            low = mid + 1
        else:
            high = mid - 1
    return None
