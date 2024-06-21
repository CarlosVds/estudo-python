# contador = 0

# while contador < 100:
#     contador += 1

#     if contador == 6:
#         print('Não vou mostrar o 6')
#         continue

#     print(contador)

#     if contador == 40:
#         break

# texto = 'Python'
# i = 0

# while i < len(texto):
#     print(texto[i])
#     i += 1
#   
senha = '123456'
senha_digitada = ' '
senha_errada = 0

while True: 
    
    senha_digitada = input("Senha = ")

    senha_errada += 1

    if senha == senha_digitada:
        print('Senha correta')
        print('Sistema liberado')
        break

    if senha_errada >= 3:
        print('Senha bloqueada')
        break

   
    
    