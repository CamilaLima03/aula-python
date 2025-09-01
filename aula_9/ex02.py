#comparar duas listas e criar uma terceira apenas com  itens em comum
#entrada duas listas
#saída uma nova lista

#ex: 
#lista 01: [vermelho,azul,verde, amarelo]
#lista02: [verde, roxo, azul, preto]

lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
listarepetidos = []

for item in lista1:
    if item in lista2 and item not in listarepetidos:
        listarepetidos.append(item)

print(listarepetidos)        
