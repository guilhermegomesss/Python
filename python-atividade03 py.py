
def soma_elementos_indice_par(lista):
    soma = 0
    for i in range(0, len(lista), 2):
        soma += lista[i]
    return soma


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]


resultado = soma_elementos_indice_par(minha_lista)

print(f"A soma dos elementos de índice par da lista é: {resultado}")