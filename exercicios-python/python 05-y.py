# Definir duas listas A e B com 5 elementos cada
lista_A = [1, 2, 3, 4, 5]
lista_B = [6, 7, 8, 9, 10]

# Trocar os elementos entre as listas
temp = lista_A.copy()  # Criar uma cópia temporária de lista_A
lista_A = lista_B.copy()  # Copiar os elementos de lista_B para lista_A
lista_B = temp.copy()  # Copiar os elementos da cópia temporária para lista_B

# Exibir as listas após a troca
print("Lista A após a troca:", lista_A)
print("Lista B após a troca:", lista_B)