from core.dados import usuarios


#===============Função Usuario==========
def login():
    while True:
        usuario = input("Usuário: ").lower()
        senha = input("Senha: ")

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            print(f"\nBem-vindo, {usuario}!")
            return usuarios[usuario]["perfil"]
        else:
            print("Login inválido!\n")


#============permição de cada perfil=======
def tem_permissao(perfil, permissao):
    permissoes = {
        "gerente": ["estoque_view", "estoque_add", "vendas", "registro"],
        "vendedor": ["estoque_view", "vendas"]
    }

    return permissao in permissoes.get(perfil, [])