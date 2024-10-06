# Definindo as operações
def opr(n1, n2, operacoes): 
    # Realiza a operação de acordo com o operador fornecido
    if operacoes == '+':
        resultado = n1 + n2  # Adição
        return resultado
    if operacoes == '-':
        resultado = n1 - n2  # Subtração
        return resultado
    if operacoes == '/':
        resultado = n1 / n2  # Divisão
        return resultado
    if operacoes in '*Xx':
        resultado = n1 * n2  # Multiplicação
        return resultado
    # Se a operação não for válida, retorna uma mensagem de erro
    if operacoes not in '+-/*':
        return 'operação invalida'

# Lista do historico
def historico(hist):
    count = 1  # Contador para a numeração do histórico
    for lista in hist:
        print('-' * 80)  # Linha separadora
        print(f'{count}. {lista}')  # Exibe a operação no histórico
        count += 1  # Incrementa o contador

# Calcular historico
def opr_historico(results):
    # Soma todos os resultados e imprime
    print(f'A soma do historico: {sum(results)}')

# Função Principal
def main():
    resultados = []  # Lista para armazenar os resultados das operações
    operacoes = []  # Lista para armazenar as operações realizadas
    while True:
        # Solicita a escolha do usuário
        escolha = input('Calcular/Historico/Soma Historico/Sair: ').capitalize()
        try:
            if escolha == 'Calcular':  # Checar se a opção é calcular
                n1 = float(input('Primeiro numero:'))  # Primeiro número
                n2 = float(input('Segundo numero: '))  # Segundo número
                op = input('operação: ')  # Operação desejada

                resultado = opr(n1=n1, n2=n2, operacoes=op)  # Chama a função de operação
                operacoes.append(f'{n1} {op} {n2} = {resultado}')  # Armazena a operação no histórico
                resultados.append(resultado)  # Armazena o resultado
                print(f'{n1} {op} {n2} = {resultado}')  # Imprime o resultado
        except ValueError:
            print('Valor invalido, por favor insira algum valor')  # Mensagem de erro para entrada inválida
        if escolha == 'Sair':
            break  # Encerra o loop se o usuário escolher sair

        # Exibir histórico
        if escolha == 'Historico':
            historico(hist=operacoes)  # Exibe o histórico de operações
        if escolha == 'Soma historico':
            opr_historico(results=resultados)  # Soma e exibe o total dos resultados

# Inicia o programa
main()
