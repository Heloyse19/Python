# Documentação do Código

## Função `opr(n1, n2, operacoes)`

- **Descrição**: Realiza operações aritméticas básicas (adição, subtração, multiplicação e divisão) entre dois números fornecidos.
  
- **Parâmetros**:
  - `n1` (float): O primeiro número.
  - `n2` (float): O segundo número.
  - `operacoes` (str): O símbolo da operação a ser realizada. Aceita:
    - `'+'` para adição
    - `'-'` para subtração
    - `'/'` para divisão
    - `'*'`, `'X'`, ou `'x'` para multiplicação
  
- **Retorno**: 
  - O resultado da operação se a operação for válida.
  - Uma string `'operação invalida'` se a operação não for reconhecida.

## Função `historico(hist)`

- **Descrição**: Exibe um histórico de operações realizadas, formatando cada entrada com um número sequencial.
  
- **Parâmetros**:
  - `hist` (list): Uma lista contendo strings que representam as operações realizadas.
  
- **Retorno**: Não retorna nenhum valor. Apenas imprime as operações no console.

## Função `opr_historico(results)`

- **Descrição**: Calcula e imprime a soma de todos os resultados armazenados na lista.
  
- **Parâmetros**:
  - `results` (list): Uma lista de números (resultados das operações) a serem somados.
  
- **Retorno**: Não retorna nenhum valor. Apenas imprime a soma no console.

## Função `main()`

- **Descrição**: Controla o fluxo do programa, permitindo ao usuário calcular operações, visualizar o histórico e somar resultados.
  
- **Retorno**: Não retorna nenhum valor. O programa continua em execução até que o usuário escolha sair.

## Exemplo de Uso

1. O usuário pode escolher entre calcular uma nova operação, visualizar o histórico, somar os resultados do histórico ou sair do programa.
2. As operações válidas incluem adição, subtração, multiplicação e divisão.
3. O histórico e a soma dos resultados são apresentados de forma clara e organizada.

## Observações

- O programa trata entradas inválidas, solicitando que o usuário insira valores corretos.
- O histórico é armazenado e pode ser consultado a qualquer momento durante a execução do programa.
