#criar lista de vendas onde toda venda é uma tupla(nome_do_produti, valor,qt)
#1-criar lista nova chamado lucradas contendo apenas valor*qt maior 100
#crie conj produtos  nomes únicos com a lista original

vendas = [("Teclado",50,2),
          ("Mouse", 25.50,4),
          ("Monitor", 300, 1),
          ("Fone", 45, 1),
          ("Webcam", 75.20, 2)
]
lucradas = list()
produtos_unico = set()

for produto, valor, quantidade in vendas:
    valor_total = valor*quantidade
    if valor_total >= 100:
        lucradas.append((produto,valor,quantidade))

    produtos_unico.add(produto)   
    
print(lucradas)
print(produtos_unico)








