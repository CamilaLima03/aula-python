#menu de comando para robôs
#1-robô em posição inicial
#2- avançar-recuar-status-desligar
#3- pedir escolha comando
#4- conf escolha execute avançar(adicionar posição), recuar(subtratir pos), status(mostrar pos) e desligar (encerra)
#5- o menu continua aparecendo até desligar
#6- dig comando errado = erro


posicao = 0

while True:
    opcao = input( "Escolha uma ação\n" \
                  "1 - Avançar.\n" \
                  "2 - Recuar.\n" \
                  "3 - Status. \n" \
                  "4 - Desligar. \n")
    if opcao == "1":
        posicao += 1
    elif opcao == "2": 
        posicao - 1
    elif opcao == "3":
        print (f"Local robõ é {posicao}")   
    elif opcao == "6":
        print (" Programa encerrado. ")
        break
    else:
        print("Opção incorreta.")           
          
