def criar_saudacao(saudacao):
    def saudar(nome):
         return f'{saudacao}, {nome}'
    return saudar

falarBomDia = criar_saudacao('Bom dia')
falarBoaNoite = criar_saudacao('Bom noite')

for nome in ['Carlos','Marcella','Enzo']:
     print(falarBomDia(nome))
     print(falarBoaNoite(nome))
     
     