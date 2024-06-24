# texto = 'Python'

# i = 0

# while i < len(texto):
#     print(texto[i])

#     i += 1

for irAte in range(10):

    if irAte == 2:
        print("Não mostrar o 2")
        continue

    if irAte == 8:
        print("Terminar o laço")
        break

    for j in range(1, 3):
        print(j, irAte)

else:
    print('For completo com sucesso.')