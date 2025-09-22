DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# mapa caractere -> valor (ex: 'A' -> 10)
DIGITOS_PARA_VALOR = {ch: i for i, ch in enumerate(DIGITOS)}


def para_decimal_fracionario(fracao, base_inicial):
    # converte a parte após a fracionaria (string) para um número decimal
    soma = 0
    pot = base_inicial  # denominador inicial = base^1
    for d in fracao:
        soma += DIGITOS_PARA_VALOR[d] / pot
        pot *= base_inicial
    return soma


def para_decimal_inteiro(numero, base_inicial):
    # converte a parte inteira (string) para um inteiro decimal
    soma = 0
    n = len(numero)
    i = 1
    for d in numero:
        soma += DIGITOS_PARA_VALOR[d] * (base_inicial ** (n - i))
        i += 1
    return soma


def decimal_base_fracionario(fracao, base_final):
    # converte uma fração decimal (0 <= fracao < 1) para a base desejada
    # limita a 8 dígitos para não ficar em loop eterno
    resultado = ""
    while fracao > 0 and len(resultado) < 8:
        fracao *= base_final
        resultado += DIGITOS[int(fracao)]
        fracao -= int(fracao)
    return resultado


def decimal_base_inteiro(numero, base_final):
    # converte um inteiro decimal para a base desejada (recursivo)
    resto = numero % base_final
    quociente = numero // base_final
    if quociente >= base_final:
        return decimal_base_inteiro(quociente, base_final) + DIGITOS[resto]
    else:
        if quociente == 0:
            return DIGITOS[resto]
        return DIGITOS[quociente] + DIGITOS[resto]


def base_para_base(numero, base_inicial, base_final):
    # converte uma string 'numero' de base_inicial para base_final
    # aceita sinal '-' e separador '.' ou ','
    if numero == "0":
        return "0"

    complemento = ""
    if numero[0] == '-':
        numero = numero[1:]
        if int(numero) != 0:
            complemento = '-'

    if '.' in numero:
        inteiro, frac = numero.split(".")
    elif ',' in numero:
        inteiro, frac = numero.split(",")
    else:
        inteiro, frac = numero, ""

    inteiro_decimal = para_decimal_inteiro(inteiro, base_inicial)
    inteiro_final = decimal_base_inteiro(inteiro_decimal, base_final)
    if frac:
        frac_decimal = para_decimal_fracionario(frac, base_inicial)
        frac_final = decimal_base_fracionario(frac_decimal, base_final)
        if frac_final:
            return complemento + str(inteiro_final) + '.' + str(frac_final)

    return complemento + str(inteiro_final)


def main():
    is_running = True
    while is_running:
        print("*****************************************************")
        print("Bem vindo ao sistema de conversão de bases numéricas!")
        print("*****************************************************")

        numero = input("Digite o numero que deseja converter: ")
        try:
            base_inicial = int(input("Digite a base do numero inserido (2-62): "))
            if base_inicial < 2 or base_inicial > 62:
                print("Base inválida! Tente novamente.\n")
                continue

            # valida dígitos (simples)
            for c in numero:
                if c != '-' and c != '.' and c != ',' and DIGITOS_PARA_VALOR[c] >= int(base_inicial):
                    raise ValueError("O numero não é valido para a base escolhida")

            base_final = int(input("Digite a base para qual deseja converter (2-62): "))
            if base_final < 2 or base_final > 62:
                print("Base inválida! Tente novamente.\n")
                continue

            print(f"Resultado: {base_para_base(numero, base_inicial, base_final)}")

            print("\nDeseja realizar outra conversão?")
            continuar = input("Digite 's' para sim ou qualquer outra tecla para sair: ").lower()
            if continuar != 's':
                is_running = False
            print("\n")
        except ValueError:
            print("Valor incompatível! Tente novamente.\n")

    print("Obrigado por usar o conversor de bases numéricas!")


main()
