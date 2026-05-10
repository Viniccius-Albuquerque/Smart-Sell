from core.validadores import *
from modules.funcoes_ui import *
from modules.dados import salvar_estoque
from ui.menus import exibir_estoque
from core.config import RESET

def criar_produto(estoque, perfil):
    """Cria um novo produto no estoque"""
    from core.models import PERMISSOES
    
    if "estoque_add" not in PERMISSOES.get(perfil, []):
        print("\nAcesso negado! Você não pode criar produtos.")
        pausar()
        return estoque
    
    produto = input("\nNome do novo produto: ").strip().lower()
    
    if not produto:
        print("Nome do produto não pode estar vazio!")
        pausar()
        return estoque
    
    if produto in estoque:
        print(f"Produto '{produto}' já existe!")
        pausar()
        return estoque
    
    preco_input = input("Preço do produto: R$ ")
    preco, erro = validar_preco(preco_input)
    
    if erro:
        print(f"{erro}")
        pausar()
        return estoque
    
    estoque[produto] = {
        "quantidade": 0,
        "preco": preco
    }
    
    if salvar_estoque(estoque):
        print(f"\nProduto '{produto}' criado com sucesso!")
    else:
        print("\nErro ao salvar produto!")
    
    pausar()
    return estoque

def adicionar_estoque(estoque, perfil):
    """Adiciona quantidade a um produto existente"""
    from core.models import PERMISSOES
    
    if "estoque_add" not in PERMISSOES.get(perfil, []):
        print("\nAcesso negado! Você não pode modificar o estoque.")
        pausar()
        return estoque
    
    if not estoque:
        print("\nNenhum produto cadastrado! Crie um produto primeiro.")
        pausar()
        return estoque
    
    produto = input("\nNome do produto: ").strip().lower()
    
    if produto not in estoque:
        print(f"Produto '{produto}' não encontrado!")
        pausar()
        return estoque
    
    qtd_input = input(f"Quantidade a adicionar em '{produto}': ")
    quantidade, erro = validar_quantidade(qtd_input)
    
    if erro:
        print(f"{erro}")
        pausar()
        return estoque
    
    estoque[produto]["quantidade"] += quantidade
    
    if salvar_estoque(estoque):
        print(f"\n{quantidade} unidade(s) adicionada(s) a '{produto}'")
        print(f"Estoque atual: {estoque[produto]['quantidade']} unidades")
    else:
        print("\nErro ao salvar estoque!")
    
    pausar()
    return estoque

def atualizar_preco(estoque, perfil):
    """Atualiza o preço de um produto"""
    from core.models import PERMISSOES
    
    if "estoque_add" not in PERMISSOES.get(perfil, []):
        print("\nAcesso negado! Você não pode alterar preços.")
        pausar()
        return estoque
    
    if not estoque:
        print("\nNenhum produto cadastrado!")
        pausar()
        return estoque
    
    produto = input("\nNome do produto: ").strip().lower()
    
    if produto not in estoque:
        print(f"Produto '{produto}' não encontrado!")
        pausar()
        return estoque
    
    print(f"Preço atual: R$ {estoque[produto]['preco']:.2f}")
    novo_preco_input = input("Novo preço: R$ ")
    novo_preco, erro = validar_preco(novo_preco_input)
    
    if erro:
        print(f"{erro}")
        pausar()
        return estoque
    
    estoque[produto]["preco"] = novo_preco
    
    if salvar_estoque(estoque):
        print(f"\nPreço de '{produto}' atualizado para R$ {novo_preco:.2f}")
    else:
        print("\nErro ao salvar preço!")
    
    pausar()
    return estoque

def buscar_produto(estoque):
    """Busca produtos pelo nome"""
    if not estoque:
        print("\nEstoque vazio!")
        pausar()
        return
    
    busca = input("\nBuscar produto: ").strip().lower()
    
    if not busca:
        print("Termo de busca vazio!")
        pausar()
        return
    
    resultados = {produto: dados for produto, dados in estoque.items() 
                  if busca in produto}
    
    if resultados:
        print(f"\nResultados para '{busca}':")
        print(f"{'PRODUTO':<30} | {'QTD':<10} | {'PREÇO':<12}")
        print("-" * 55)
        for produto, dados in resultados.items():
            print(f"{produto:<30} | {dados['quantidade']:<10} | R$ {dados['preco']:<10.2f}")
    else:
        print(f"\nNenhum produto encontrado com '{busca}'")
    
    pausar()