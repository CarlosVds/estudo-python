palavraSecreta = 'Enzo'
letraAcertada = ''
numeroTentativa = 0

while True:

    letraDigitada = input('Digite uma letra: ')

    numeroTentativa += 1

    if len(letraDigitada) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letraDigitada in palavraSecreta:
        letraAcertada += letraDigitada

    palavraFormada = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in letraAcertada:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'

    print('Palavra formada: ', palavraFormada)

    if palavraFormada == palavraSecreta:
        print('VOCÊ GANHOU, PARABÉNS....')
        print('Número tentativa: ', numeroTentativa)
        letraAcertada = ''
        numeroTentativa = 0
        
        sair = input('Deseja continuar? S[im]').lower().startswith('s')    

        if sair == True:
            continue
        else:
            break
    