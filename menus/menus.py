from core.cores import *
from core.utilitarios import *
from core.dados import estoque


#====================titulos=========================
def titulo_login():
    print(CIANO+"      _           _      ")
    print("     | |___  __ _(_)_ _  ")
    print("     | / _ \/ _` | | ' \)")
    print("     |_\___/\__, |_|_||_|")
    print("            |___/        "+RESET)


def titulo_sistema():
    print(VERDE_CLARO+f'      ___ _    _                       _                       _          ')
    print(f'     / __(_)__| |_ ___ _ __  __ _   __| |___  __ _____ _ _  __| |__ _ ___')
    print(f"     \\__ \\ (_-<  _/ -_) '  \/ _` | / _` / -_) \\ V / -_) ' \/ _` / _` (_-< ")
    print(f'     |___/_/__/\\__\\___|_|_|_\\__,_| \\__,_\\___|  \\_/\\___|_||_\\__,_\\__,_/__/ '+RESET)


def titulo_estoque():
    print(MARROM+"      ___    _                      ")
    print(f"     | __|__| |_ ___  __ _ _  _ ___ ")
    print(f"     | _|(_-<  _/ _ \/ _` | || / -_)")
    print(f"     |___/__/\\__\\___/\\__, |\\_,_\\___|")
    print(f"                        |_|         "+RESET)


def titulo_vendas():
    print(VERDE_CLARO+f"     __   __           _         ")
    print(f"     \\ \\ / /__ _ _  __| |__ _ ___")
    print(f"      \\ V / -_) ' \/ _` / _` (_-<")
    print(f"       \\_/\\___|_||_\\__,_\\__,_/__/"+RESET)


def titulo_realizar_venda():
    print(LARANJA+f"      ___          _ _              __   __           _      ")
    print(f"     | _ \\___ __ _| (_)_____ _ _ _  \\ \\ / /__ _ _  __| |__ _ ")
    print(f"     |   / -_) _` | | |_ / _` | '_|  \\ V / -_) ' \/ _` / _` |")
    print(f"     |_|_\\___\\__,_|_|_/__\\__,_|_|     \\_/\\___|_||_\\__,_\\__,_|"+RESET)


#===================FUNÇÕES MENU=======================
def menu_login():
    limpar_tela()
    mover_topo()
    mostrar_cursor()
    titulo_login()
    espaco()
    espaco()
    esconder_cursor()


def menu_principal(perfil):
    limpar_tela()
    mover_topo()
    mostrar_cursor()
    titulo_sistema()
    espaco()

    print("( 1 ) Estoque")
    espaco()
    print("( 2 ) Vendas")
    espaco()
    print("( 0 ) Sair")

    espaco()
    esconder_cursor()


def menu_estoque():
    limpar_tela()
    mover_topo()
    mostrar_cursor()
    titulo_estoque()
    espaco()
    print('( 1 ) Criar novo produto')
    espaco()
    print('( 2 ) Adicionar Item ao Estoque')
    espaco()
    print('( 3 ) Visualizar Estoque')
    espaco()
    print('( 4 ) Atualizar Preço')
    espaco()
    print('( 0 ) Voltar')
    espaco()
    esconder_cursor()


def menu_edicao_estoque():
    espaco()
    print('( 1 ) Criar novo produto')
    espaco()
    print('( 2 ) Adicionar Item ao Estoque')
    espaco()
    print('( 3 ) Atualizar Preço')
    espaco()
    print('( 0 ) Voltar')
    espaco()


def menu_vendas():
    limpar_tela()
    mover_topo()
    mostrar_cursor()
    titulo_vendas()
    espaco()
    print('( 1 ) Realizar Venda')
    espaco()
    print('( 2 ) Registro de Vendas')
    espaco()
    print('( 0 ) Voltar')
    espaco()
    esconder_cursor()


def menu_realizar_vendas():
    limpar_tela()
    mover_topo()
    mostrar_cursor()
    titulo_realizar_venda()
    espaco()
    esconder_cursor()


def creditos():
    limpar_tela()
    mover_topo()
    mostrar_cursor()
    print("-=-"*15)
    print("Made By:")
    print(VERDE_CLARO+"𝓐  𝓬 𝓱 𝓲 𝓵 𝓵 𝓮 𝓼   𝓢 𝓪 𝓷 𝓽 𝓸 𝓼"+RESET)
    print("-=-Backend Dev-=-")
    print("-=-"*15)
    espaco()


def menu_visualizar_estoque():
    limpar_tela()
    mover_topo()
    titulo_estoque()
    espaco()

    print(f"{'PRODUTO':<30} | {'QTD':<20} | {'PREÇO':<10}")
    print("-" * 60)

    for produto, dados in estoque.items():
        print(f"{produto:<30} | {dados['quantidade']:<20} | R$ {dados['preco']:<10.2f}")
    
    espaco()
    print("-" * 60)