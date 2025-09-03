#crie um programa que conte quantas vezes um num aparece
#entrada: uma lista de num a ser procurado
#saida: quantas vezes o num aparece


numeros = [1, 5, 2, 8 , 5, 3, 5]
numero_procurado = 5
contador = 0

for numero in numeros:
    if numero == numero_procurado:
        contador += 1

print(f"O número {numero_procurado} aparece {contador} vezes na lista.")