# Sistema Bancário Simples

Este projeto é um sistema bancário simples em Python que permite realizar operações de saque, depósito e exibir extrato bancário. O sistema possui restrições para saques diários e exibe todas as movimentações financeiras realizadas na conta.

## Funcionalidades

- **Depósito**: Permite realizar depósitos de valores positivos na conta.
- **Saque**: Permite realizar saques com um limite diário de 3 saques e um valor máximo de R$ 500,00 por saque.
- **Extrato**: Exibe todas as movimentações realizadas (saques e depósitos) e o saldo atual da conta.

## Regras do Sistema

1. **Limite de Saques**: Apenas 3 saques diários são permitidos.
2. **Valor Máximo de Saque**: O valor máximo permitido para cada saque é de R$ 500,00.
3. **Saldo Insuficiente**: Caso o saldo seja insuficiente para realizar o saque, uma mensagem será exibida.
4. **Formato de Valores**: Todos os valores exibidos seguem o formato `R$ xxx.xx`.

## Como Usar

1. Clone este repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/MatheusDSantossi/simple_banking_system.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd simple_banking_system
    ```
3. Execute o script:
    ```bash
    python main.py
    ```
Desenvolvido por [Matheus D. Santos](https://github.com/MatheusDSantossi)

Para mais informações e acesso ao código completo, visite o repositório no GitHub: [Simple Banking System](https://github.com/MatheusDSantossi/simple_banking_system).