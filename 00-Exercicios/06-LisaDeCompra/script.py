import os

lista = []

while True:
    select = input('Selecione uma opção\n[i]nserir [a]pagar [l]star: ')

    if select == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif select == 'a':
        indice_str = input('Escolha o índice para apagar: ') 

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar esse índice.')    

    elif select == 'l':
        os.system('cls') 

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
                print(i, valor)
    else:
        print('Escolha uma opção válida.')   