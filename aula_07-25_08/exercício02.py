#adivinhar o número
#1-definir num sercreto
#2 - limite de 5 tentativas
#3- cada tentativa informar se núm maior ou menor
#4- parabéns se acertar
#5-passou das 5 info game over

numero = 9

for i in range(5):
    palpite = int(input("Digite um número: "))
    if palpite > numero:
        print ("Número muito alto")
    elif palpite < numero:
        print("Número muito baixo")
    elif palpite == numero:
        print ("Parabéns")
    else:
        print("Game Over")
