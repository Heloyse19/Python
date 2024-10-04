# Definindo as operações
def opr(n1, n2, operacoes): 
    if operacoes == '+':
        resultado= n1 + n2
        return resultado
    if operacoes == '-':
     resultado= n1-n2
     return resultado
    if operacoes == '/':
     resultado= n1/n2
     return resultado
    if operacoes == '*':
       resultado= n1*n2
       return resultado
    if operacoes not in '+-/*':
       return 'operação invalida'
    
# Lista do historico
def historico(hist):
   for lista in hist:
      print(lista)

# Calcular historico
def opr_historico(hist):
    numeros_hist = hist
    hist
   
# Principal
def main():
    checar = []
    operacoes= []
    while True:
        escolha = input('Calcular/Historico/Calcular historico/Sair: ').capitalize()
        
        if escolha == 'Calcular': # checar se as variaveis n1, n2 receberam numeros
            n1= float(input('Primeiro numero:'))
            n2= float(input('Segundo numero: '))
            op= input('operação: ')
            checar.append(n1, n2, op)
            if checar:
                resultado= opr(n1=n1,n2=n2,operacoes=op)
                checar.append(resultado)
                operacoes.append(resultado)
            else:
               print('Sem valor digitado')
        if escolha == 'Sair':
            break
        
        # Exibir historico
        if escolha == 'Historico':
            historico(hist=operacoes)
    
        print(resultado)

main()
