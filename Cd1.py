# Definindo as operações
def opr(n1, n2, operacoes):
    if operacoes == '+':
        return f'{n1} + {n2} = {n1+n2}' 
    if operacoes == '-':
     return f'{n1} - {n2} = {n1-n2}'
    if operacoes == '/':
     return f'{n1} / {n2} = {n1/n2}'
    if operacoes == '*':
       return f'{n1} x {n2} = {n1*n2}'
    if operacoes not in '+-/*':
       return 'operação invalida'
    
# Definindo a lista de historico
def historico(hist):
   for lista in hist:
      print(lista)

# Principal
def main():
    operacoes= []
    while True:
        escolha = input('Calcular/Historico/Sair: ').capitalize()
        if escolha == 'Calcular':
            n1= float(input('Primeiro numero:'))
            n2= float(input('Segundo numero: '))
            op= input('operação: ')
            resultado= opr(n1=n1,n2=n2,operacoes=op)
        if escolha == 'Sair':
            break

        # Registrando o historico
        operacoes.append(resultado)
        if escolha == 'Historico':
            historico(hist=operacoes)
    
        print(resultado)

main()
