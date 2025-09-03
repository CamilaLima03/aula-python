#TUPLAS DE ACESSO(USUARIO, STATUS_LOGIN)
#USANDO LAÇOS DE REPETIÇÃO E CONDICIONAIS IDENT E IMP:
#1- NOME USU COM LOGIN OK
#2- NOME USER COM LOGIN FALHA

acessos = [("Pedro", "sucesso"),
           ("Ana", "falha"),
           ("Maria", "sucesso"),
           ("Pedro", "falha"),
           ("Ana", "falha")
]

login = set(acessos)
loginok = set()
loginfalha = set()

for usuario, status_login in login:
    if status_login == "falha":
       loginfalha.add(usuario)
    elif status_login == "sucesso":
        loginok.add(usuario)   

somente_falha = loginfalha.difference(loginok)           
        

print(f"Os usuários {loginok} obtiveram login com sucesso pelo menos 1x.")
print(f"Os usuários {somente_falha} obtiveram  erro no login todas às vezes.")
