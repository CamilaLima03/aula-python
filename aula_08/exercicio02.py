#validaçãotelefone
#criar programa que recebe 11digitos
#tornar invalido se repetir 3x
#se for válido formatar padrão
#imprimir o numero formatado ou mensagem de erro

numeros = input("Digite o número de telefone com 11 dígitos: ")


if len(numeros) != 11:
    print("numero com tamanho incorreto.")
elif not numeros.isdigit():
    print("não é possível gerar um número de telefone com esses valores")
else:
    valido = True
    for c in numeros:
        cont = 0
        for d in numeros:
            if d == c:
                cont += 1
        if cont >= 3:
            valido = False
            break

    if not valido:
        print("não é possível gerar um número de telefone com esses valores")
    else:
        print(
            "("
            + numeros[0]
            + numeros[1]
            + ") "
            + numeros[2]
            + numeros[3]
            + numeros[4]
            + numeros[5]
            + numeros[6]
            + "-"
            + numeros[7]
            + numeros[8]
            + numeros[9]
            + numeros[10]
        )