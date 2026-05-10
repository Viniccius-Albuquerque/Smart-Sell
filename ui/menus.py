from core.config import *
from modules.funcoes_ui import *

def titulo_login():
    print(CIANO + """
      _           _      
     | |___  __ _(_)_ _  
     | / _ \/ _` | | ' \ 
     |_\___/\__, |_|_||_|
            |___/        """ + RESET)

def titulo_sistema():
    print(VERDE_CLARO + """
      ___ _    _                       _                       _          
     / __(_)__| |_ ___ _ __  __ _   __| |___  __ _____ _ _  __| |__ _ ___
     \__ \ (_-<  _/ -_) '  \/ _` | / _` / -_) \ V / -_) ' \/ _` / _` (_-< 
     |___/_/__/\__\___|_|_|_\__,_| \__,_\___|  \_/\___|_||_\__,_\__,_/__/ 
    """ + RESET)

def titulo_estoque():
    print(MARROM + """
      ___    _                      
     | __|__| |_ ___  __ _ _  _ ___ 
     | _|(_-<  _/ _ \/ _` | || / -_)
     |___/__/\__\___/\__, |\_,_\___|
                        |_|         
    """ + RESET)

def menu_principal(perfil):
    limpar_tela()
    mover_topo()
    titulo_sistema()
    print(f"\n{'='*50}")
    print(f"Bem-vindo, {perfil.upper()}!")
    print(f"{'='*50}\n")
    print(" (1) Estoque")
    print(" (2) Vendas")
    if perfil == "gerente":
        print(" (3) Financeiro")
    print(" (0) Sair")
    print("\n" + "="*50)

def menu_estoque():
    limpar_tela()
    mover_topo()
    titulo_estoque()
    print("\n" + "="*50)
    print("1. Criar novo produto")
    print("2. Adicionar ao estoque")
    print("3. Visualizar estoque")
    print("4. Atualizar preço")
    print("5. Buscar produto")
    print("0. Voltar")
    print("="*50)

def menu_vendas():
    limpar_tela()
    mover_topo()
    print(VERDE_CLARO + """
     __   __           _         
     \ \ / /__ _ _  __| |__ _ ___
      \ V / -_) ' \/ _` / _` (_-<
       \_/\___|_||_\__,_\__,_/__/
    """ + RESET)
    print("\n" + "="*50)
    print("1. Realizar venda")
    print("2. Registro de vendas")
    print("0. Voltar")
    print("="*50)

def exibir_estoque(estoque):
    """Exibe o estoque formatado"""
    limpar_tela()
    mover_topo()
    titulo_estoque()
    
    if not estoque:
        print("\nEstoque vazio!\n")
        return
    
    print(f"\n{'PRODUTO':<30} | {'QTD':<10} | {'PREÇO':<12}")
    print("-" * 55)
    
    for produto, dados in estoque.items():
        status = "ATENÇÃO" if dados["quantidade"] <= 2 else "OK"
        print(f"{produto:<30} | {dados['quantidade']:<10} | R$ {dados['preco']:<10.2f} {status}")
    
    print("\n" + "="*55)
    print("Legenda: Estoque OK | Estoque baixo (≤2 unidades)")
    print("="*55)