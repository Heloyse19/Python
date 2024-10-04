def opr(n1, n2, operacoes):
    if operacoes == '+':
        return n1+n2 
    if operacoes == '-':
     return n1-n2
    if operacoes == '/':
     return n1/n2
    if operacoes == '*':
       return n1*n2

def main():
    while True:
     n1= float(input('Primeiro numero:'))
     n2= float(input('Segundo numero: '))
     op= input('operação: ')
     if op == '//':
        break
     operacoes= []
     resultado= opr(n1=n1,n2=n2,operacoes=op)
     print(resultado)

main()
