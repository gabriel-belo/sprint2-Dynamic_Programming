from dados import gerar_consumo_diario
from fila_pilha import registrar_na_fila, registrar_na_pilha
from busca import busca_sequencial, busca_binaria
from ordenacao import merge_sort, quick_sort

# Gerar os dados simulados de consumo diário
consumo_diario = gerar_consumo_diario()

# Fila e Pilha
fila_consumo = registrar_na_fila(consumo_diario)
pilha_consumo = registrar_na_pilha(consumo_diario)

# Exibindo a fila (ordem cronológica)
print("\n[FILA] Consumo em ordem cronológica:")
for item in fila_consumo:
    print(item)

# Exibindo a pilha (últimos consumos primeiro)
print("\n[PILHA] Últimos consumos primeiro:")
while pilha_consumo:
    print(pilha_consumo.pop())

# Busca Sequencial
print("\nBusca Sequencial por 'Reagente A':")
print(busca_sequencial(consumo_diario, 'Reagente A'))

# Ordenação por Quantidade usando Merge Sort
ordenado_por_quantidade = merge_sort(consumo_diario, 'quantidade')
print("\nOrdenado por quantidade (Merge Sort):")
for item in ordenado_por_quantidade:
    print(item)

# Ordenação por Validade usando Quick Sort
ordenado_por_validade = quick_sort(consumo_diario, 'validade')
print("\nOrdenado por validade (Quick Sort):")
for item in ordenado_por_validade:
    print(item)

# Busca Binária (é necessário que os dados estejam ordenados por nome de insumo)
consumo_diario_ordenado = sorted(consumo_diario, key=lambda x: x['insumo'])
print("\nBusca Binária por 'Descartável X':")
print(busca_binaria(consumo_diario_ordenado, 'Descartável X'))
