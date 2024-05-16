#FUNÇÕES

# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero    
#     return total


# print(soma(1,2,3))

def multiplos(*args):
    total = 1
    for soma in args:
        total *= soma
    return total    

print(multiplos(1,2,3,4,5))

def parImpar(a):
    result = a
    if result % 2 == 0:
        return f'{result} é PAR'
    return f'{result} é ÍMPAR'

print(parImpar(34))