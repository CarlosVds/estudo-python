lista = ['Carlos','Marcella','Enzo','Cleide','Alcino']

del lista[4]

lista.append('Carla')

lista.pop()

lista.insert(3, 'Carla')

print(lista)

print("*****************************************************")

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

print(lista_a)

print("*****************************************************")

listas_a = ['Carlos', 'Marcella', 'Enzo']

listas_b = listas_a.copy()

listas_a[0] = 'Mãe Cleide'

print(listas_a)
print(listas_b)

print("*****************************************************")

i = 0
for indice in lista:
    print(f'{i} {indice}')
    i += 1   