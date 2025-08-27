#validaçãotelefone
#criar programa que recebe 11digitos
#tornar invalido se repetir 3x
#se for válido formatar padrão
#imprimir o numero formatado ou mensagem de erro

numero = input("Digite seu telefone com DDD: ")
valido = True

for c in numero:
    contador_repetidos = 0
    for d in numero:
        print (f"num c {c} num {d} são iguais? {c==d}")
        if c==d:
            contador_repetidos+=1
        if contador_repetidos >=3:
            print("Número inválido!")
            valido = False
            break               