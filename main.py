DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
DIGITOS_PARA_VALOR = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
    'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
    'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
    'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44,
    'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53,
    's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61
}

def para_decimal_fracionario(fracao, base_inicial):
    # converte a parte após a fracionaria (string) para um número decimal
    soma = 0
    pot = base_inicial
    for d in fracao:
        soma += DIGITOS_PARA_VALOR.get(d) / pot
        pot *= base_inicial
    return soma

def para_decimal_inteiro(numero, base_inicial):
    # converte a parte inteira (string) para um inteiro decimal
    soma = 0
    n = len(numero)
    i = 1
    for d in numero:
        soma += DIGITOS_PARA_VALOR.get(d) * (base_inicial ** (n - i))
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
        if numero != "0":
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

        numero = input("Digite o numero que deseja converter: ").strip()

        try:
            base_inicial = int(input("Digite a base do numero inserido (2-62): ").strip())
            if base_inicial < 2 or base_inicial > 62:
                print("Base inválida! Tente novamente.\n")
                continue

            # valida dígitos
            for c in numero:
                if c != '-' and c != '.' and c != ',' and DIGITOS_PARA_VALOR.get(c) >= int(base_inicial):
                    raise ValueError("O numero não é valido para a base escolhida")

            base_final = int(input("Digite a base para qual deseja converter (2-62): ").strip())
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
        except Exception as e:
            print(f"Erro inesperado: {e}")

    print("Obrigado por usar o conversor de bases numéricas!")

main()
