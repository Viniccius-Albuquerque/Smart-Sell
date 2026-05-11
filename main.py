from core.models import USUARIOS
from modules.dados import carregar_estoque, carregar_vendas, carregar_financeiro
from modules.funcoes_ui import limpar_tela, pausar, exibir_cabecalho
from ui.menus import menu_principal, menu_estoque, menu_vendas, exibir_estoque
from modules.funcoes_estoque import criar_produto, adicionar_estoque, atualizar_preco, buscar_produto
from modules.funcoes_vendas import realizar_venda, exibir_registro_vendas
from core.config import VERMELHO, RESET

def login():
    """Sistema de login do usuário"""
    while True:
        limpar_tela()
        from ui.menus import titulo_login
        titulo_login()
        print("\n" + "="*50)
        
        user = input("Usuário: ").strip().lower()
        senha = input("Senha: ").strip()
        
        if user in USUARIOS and USUARIOS[user]["senha"] == senha:
            print(f"\nBem-vindo, {user}!")
            pausar()
            return USUARIOS[user]["perfil"]
        else:
            print(f"\nLogin inválido! Tente novamente.")
            pausar()

def processar_estoque(estoque, perfil):
    """Processa o menu de estoque"""
    while True:
        menu_estoque()
        
        if perfil == "vendedor":
            print(f"\nModo visualização (sem permissão para editar)")#aaaaaaaaaaa
        
        try:
            escolha = int(input("\nSelecione ação: "))
        except ValueError:
            print("Digite um número válido!")
            pausar()
            continue
        
        if escolha == 1:
            estoque = criar_produto(estoque, perfil)
        elif escolha == 2:
            estoque = adicionar_estoque(estoque, perfil)
        elif escolha == 3:
            exibir_estoque(estoque)
            pausar()
        elif escolha == 4:
            estoque = atualizar_preco(estoque, perfil)
        elif escolha == 5:
            buscar_produto(estoque)
        elif escolha == 0:
            break
        else:
            print("Opção inválida!")
            pausar()
    
    return estoque

def processar_vendas(estoque, registro_vendas, perfil):
    """Processa o menu de vendas"""
    while True:
        menu_vendas()
        
        try:
            escolha = int(input("\nSelecione ação: "))
        except ValueError:
            print("Digite um número válido!")
            pausar()
            continue
        
        if escolha == 1:
            estoque, registro_vendas = realizar_venda(estoque, registro_vendas, perfil)
        elif escolha == 2:
            exibir_registro_vendas(registro_vendas, perfil)
        elif escolha == 0:
            break
        else:
            print("Opção inválida!")
            pausar()
    
    return estoque, registro_vendas

def creditos():
    """Exibe os créditos do sistema"""
    limpar_tela()
    from core.config import VERDE_CLARO
    print("-=-"*20)
    print(VERDE_CLARO + "𝓐 𝓬 𝓱 𝓲 𝓵 𝓵 𝓮 𝓼   𝓢 𝓪 𝓷 𝓽 𝓸 𝓼" + RESET)
    print(VERDE_CLARO + "\n𝑽 𝒊 𝒏 𝒊́ 𝒄 𝒊 𝒖 𝒔   𝑨 𝒍 𝒃 𝒖 𝒒 𝒖 𝒆 𝒓 𝒒 𝒖 𝒆" + RESET)
    print("-=- Backend Dev's -=-")
    print("-=-"*20)
    print("\nObrigado por usar o sistema!")
    pausar()

def main():
    """Função principal do sistema"""
    # Carregar dados
    estoque = carregar_estoque()
    registro_vendas = carregar_vendas()
    financeiro = carregar_financeiro()
    
    # Login
    perfil = login()
    
    # Loop principal
    while True:
        menu_principal(perfil)
        
        try:
            escolha = int(input("\nSelecione ação: "))
        except ValueError:
            print("Digite um número válido!")
            pausar()
            continue
        
        if escolha == 1:
            estoque = processar_estoque(estoque, perfil)
        elif escolha == 2:
            estoque, registro_vendas = processar_vendas(estoque, registro_vendas, perfil)
        elif escolha == 3 and perfil == "gerente":
            exibir_cabecalho("📊 FINANCEIRO", "CIANO")
            print(f"Total de vendas: {len(registro_vendas)}")
            print(f"aturamento total: R$ {sum(v['valor_final'] for v in registro_vendas):.2f}")
            pausar()
        elif escolha == 0:
            creditos()
            break
        else:
            print("Opção inválida!")
            pausar()

if __name__ == "__main__":
    main()