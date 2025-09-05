numero = float(input("Digite o preço do produto:"))

if numero >= 100.00:
    print(f"O valor a pagar é R$ {numero - numero * 0.10}.")
else:
    print(f"O valor a pagar é R$ {numero}.")                         
