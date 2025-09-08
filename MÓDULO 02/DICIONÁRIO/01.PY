#AGENDA DE CONTATOS: CRIE UM SISTEMA SIMPLES DE AGENDA QUE USE UM DICIONÁRIO. USE UM LOOP WHILE PARA MOSTRAR UM MENU COM  OPÇÕES DE ADICIONAR CONTATO, BUSCAR, SAIR:

contatos_na_agenda = {}

while True:
    print("\n--AGENDA--:")
    print("1 - Adicionar contato.")
    print("2 - Buscar contato")
    print("3 - Sair")

    try:
     escolha = input("Digite sua escolha: ")
     escolha = int(escolha)
    except ValueError:
        print("Entrada inválida. Digite um número de 1 a 3.")
        continue
    if escolha == 1:
       print("\n--- Adicionar---")
       nome = input("Nome: ")
       telefone = int(input("Número: "))
       contatos_na_agenda[nome] = {"contato": nome, "telefone": telefone}

    if escolha == 2:
       print("\n--- Buscar Contato---")
       