#filtrando primos
#entrada: lista num inteiros
#saída: num primos encontrados

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
primos = []

for num in numeros:
    eh_primo = True
    if numero < 2:
        eh_primo = false
    else: 
        for i in range(2, numero):
            if numero % i == 0:
                eh_primo = False
                break    
        


        