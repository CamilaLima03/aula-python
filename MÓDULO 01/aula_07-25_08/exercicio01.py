#simulação de pedido de uma lanchonete

valor_hamburguer = 20.00
cupom_deesconto = "123"

while True:
    lanche = input("Qual lanche deseja? ")
    if lanche == "hamburguer" :
       print ("Pedido confirmado")
       break
    else: 
        print ("produto não cadastrado. ")

cupom = input ("Digite o cupom: ")
if cupom == cupom_deesconto:
    print(f"Seu lanche custou {valor_hamburguer * 0.9}")
else:
    print(f"Seu lanche custou {valor_hamburguer}")            
    





    