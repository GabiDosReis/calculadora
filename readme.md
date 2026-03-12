Aqui está um **README.md** simples e organizado para o seu código:

```markdown
# Calculadora em Python com Histórico

Este é um programa simples de **calculadora em Python** executado no terminal.  
Ele permite realizar operações matemáticas básicas e armazenar o **histórico de cálculos** feitos durante a execução.

## Funcionalidades

- Realizar operações matemáticas:
  - Adição (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)
- Visualizar o histórico de cálculos realizados
- Encerrar o programa pelo menu

## Como funciona

Ao executar o programa, o usuário verá um menu com três opções:

Selecione a ação que deseja realizar:
1 - Calcular
2 - Histórico
3 - Finalizar

### 1 - Calcular
O usuário deve informar:

- Primeiro número
- Operador matemático
- Segundo número

Exemplo:

Insira o primeiro número: 5
Insira o operador: +
Insira o segundo número: 3


Resultado exibido:

8.0

### 2 - Histórico

Mostra todos os cálculos realizados durante a execução do programa.

Exemplo:

[5.0, '+', 3.0, '=', 8.0, '||', 10.0, '*', 2.0, '=', 20.0, '||']

### 3 - Finalizar

Encerra o programa.

## Estrutura do Código

- `menu1`: controla o loop principal do programa.
- `hist`: lista que armazena o histórico das operações.
- `while`: mantém o programa rodando até o usuário escolher sair.
- `match`: usado para selecionar a opção do menu e o operador matemático.

## Requisitos

- Python **3.10 ou superior** (necessário para usar `match case`).

## Como executar

1. Salve o arquivo como `calculadora.py`
2. Execute no terminal:

```bash
python calculadora.py
``

## Possíveis melhorias

* Melhorar a formatação do histórico
* Tratar erro de divisão por zero
* Validar entradas do usuário
* Permitir limpar o histórico
* Criar interface gráfica
