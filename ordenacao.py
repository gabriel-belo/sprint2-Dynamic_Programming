# Função Merge Sort (ordenação por quantidade)
def merge_sort(lista, chave):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    return merge(esquerda, direita, chave)

def merge(esq, dir, chave):
    resultado = []
    while esq and dir:
        if esq[0][chave] <= dir[0][chave]:
            resultado.append(esq.pop(0))
        else:
            resultado.append(dir.pop(0))
    resultado.extend(esq or dir)
    return resultado

# Função Quick Sort (ordenação por validade)
def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    menores = [x for x in lista[1:] if x[chave] <= pivo[chave]]
    maiores = [x for x in lista[1:] if x[chave] > pivo[chave]]

    return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)
