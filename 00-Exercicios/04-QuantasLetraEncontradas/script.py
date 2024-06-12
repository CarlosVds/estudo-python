frase = 'O Python é uma linguagem de programação'\
        'multiparadigma'\
        'Python foi criado por Van Rossum'

i = 0
qtdApareceuMaisVezes = 0
qtdLetraAparceuMaisVezes = ' '


while i < len(frase):
    letraAtual = frase[i]

    if letraAtual == ' ':
        i += 1
        continue

    qtdLetraApareceuAtual = frase.count(letraAtual)

    if qtdApareceuMaisVezes < qtdLetraApareceuAtual:
        qtdApareceuMaisVezes = qtdLetraApareceuAtual
        qtdLetraAparceuMaisVezes = letraAtual 

    i += 1


print(f'A letra que apareceu mais vezes foi "{qtdLetraAparceuMaisVezes}" = {qtdApareceuMaisVezes}X')    