from operacoes import *

menu1 = 1
hist = []

while menu1 == 1:
    menu2 = input("Selecione: 1-calcular , 2-histórico, 3-finalizar: ").strip()

    while menu2 not in ["1","2","3"]:
        menu2 = input("Menu incorreto, digite novamente: ").strip()
        
    if menu2 == "1":
        op = input("Operador (+, -, *, /, %, raiz, ^2, C): ").strip().lower()

        while op not in ["+", "-", "*", "/", "%", "raiz", "^2", "c"]:
            op = input("Operador inválido, digite novamente: ").strip().lower()

        if op == "c":
            print("Cálculo limpo")
            continue

        if op == "raiz":
            n1 = float(input("Número: "))
            n2 = "-"
            result = raiz(n1)

        elif op == "^2":
            n1 = float(input("Número: "))
            n2 = "-"
            result = quadrado(n1)

        else:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

            if op == "+":
                result = soma(n1, n2)
            elif op == "-":
                result = subtracao(n1, n2)
            elif op == "*":
                result = multiplicacao(n1, n2)
            elif op == "/":
                result = divisao(n1, n2)
            elif op == "%":
                result = porcentagem(n1, n2)

        print("Resultado", result)
        hist.append([n1, op, n2, "=", result])

    elif menu2 == "2":
        print("\n===HISTÓRICO===")
        for linha in hist:
            print(linha)

    elif menu2 == "3":
        menu1 = 0