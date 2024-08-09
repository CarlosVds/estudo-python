frase = 'Olha só que,       coisa interessante     '

listaFraseNormal = frase.split(',')

listaVazia = []

for i, frase in enumerate(listaFraseNormal):
    listaVazia.append(listaFraseNormal[i].strip())
    

print(listaVazia)
