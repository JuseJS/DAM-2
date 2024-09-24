import copy

lista = [1,2,3,4,5]

def duplicar_valores(lista):
    lista_modifica = copy.deepcopy(lista)
    for i in range(len(lista_modifica)):
        lista_modifica[i] = lista_modifica[i] * 2
    return lista_modifica

lista_modifica = duplicar_valores(lista)
print(lista)            # Output: [1, 2, 3, 4, 5]
print(lista_modifica)   # Output: [2, 4, 6, 8, 10]
