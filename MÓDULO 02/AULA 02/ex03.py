#inventário cada tupla representa uma lista (nome_do_produto,id)
#estoque_principal:produtos dispóniveis loja
#estoque online: produtos no site

#imprimir conjuntos
#1-disponiveis em ambos 
#2-disp loja
#3- dispo online

estoque_principal = [("Camiseta", 101),
                     ("Calça", 102),
                     ("Boné", 103),
                     ("Tênis", 104)
]
estoque_online = [("Boné", 103),
                  ("Camisa Polo", 105),
                  ("Calça", 102),
                  ("Chinelo", 106)
]

set_principal = set(estoque_principal)
set_online =set(estoque_online)

disponivelnaloja = set_principal.difference(set_online)
disponivelnosite = set_online.difference(set_principal)
disponivelemambos = set_principal.intersection(set_online)

print(disponivelnosite)
print(disponivelnaloja)






