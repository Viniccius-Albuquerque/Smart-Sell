from datetime import datetime
from core.validadores import *
from modules.funcoes_ui import *
from modules.dados import salvar_vendas, salvar_estoque
from core.config import VERDE, VERMELHO, AMARELO, RESET, LARANJA, VERDE_CLARO

def realizar_venda(estoque, registro_vendas, perfil):
    """Realiza uma nova venda"""
    from core.models import PERMISSOES
    
    if "vendas" not in PERMISSOES.get(perfil, []):
        print("\nAcesso negado! Você não pode realizar vendas.")
        pausar()
        return estoque, registro_vendas
    
    if not estoque:
        print("\nEstoque vazio! Não é possível realizar vendas.")
        pausar()
        return estoque, registro_vendas
    
    limpar_tela()
    print(LARANJA + """
      ___          _ _              __   __           _      
     | _ \___ __ _| (_)_____ _ _ _  \ \ / /__ _ _  __| |__ _ 
     |   / -_) _` | | |_ / _` | '_|  \ V / -_) ' \/ _` / _` |
     |_|_\___\__,_|_|_/__\__,_|_|     \_/\___|_||_\__,_\__,_|
    """ + RESET)
    print("\n" + "="*50)
    
    produto = input("Produto: ").strip().lower()
    
    if produto not in estoque:
        print(f"Produto '{produto}' não encontrado!")
        pausar()
        return estoque, registro_vendas
    
    if estoque[produto]["quantidade"] <= 0:
        print(f"Produto '{produto}' sem estoque!")
        pausar()
        return estoque, registro_vendas
    
    valor_aparelho = estoque[produto]["preco"]
    print(f"Preço do produto: R$ {valor_aparelho:.2f}")
    
    # Entrada
    entrada_input = input("Valor de entrada (0 se não houver): R$ ")
    valor_entrada, erro = validar_numero_positivo(entrada_input, "float")
    
    if erro:
        print(f"{erro}")
        pausar()
        return estoque, registro_vendas
    
    # Desconto
    desconto_input = input("Desconto (0-100%): ")
    desconto, erro = validar_desconto(desconto_input)
    
    if erro:
        print(f"{erro}")
        pausar()
        return estoque, registro_vendas
    
    # Cálculos
    desconto_valor = desconto / 100
    valor_com_desconto = valor_aparelho * (1 - desconto_valor)
    valor_final = valor_com_desconto - valor_entrada
    
    if valor_final < 0:
        valor_final = 0
    
    print(f"\n{'='*50}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
    print(f"{'='*50}")
    
    # Pagamento
    valor_pago_input = input("\nValor pago: R$ ")
    valor_pago, erro = validar_numero_positivo(valor_pago_input, "float")
    
    if erro:
        print(f"{erro}")
        pausar()
        return estoque, registro_vendas
    
    troco = valor_pago - valor_final
    
    if troco < 0:
        print(f"Valor insuficiente! Faltam R$ {abs(troco):.2f}")
        pausar()
        return estoque, registro_vendas
    
    # Processar venda
    estoque[produto]["quantidade"] -= 1
    salvar_estoque(estoque)
    
    venda = {
        "produto": produto,
        "valor_aparelho": valor_aparelho,
        "entrada": valor_entrada,
        "desconto": desconto,
        "valor_final": valor_final,
        "troco": troco,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "vendedor": perfil
    }
    
    registro_vendas.append(venda)
    salvar_vendas(registro_vendas)
    
    # Exibir comprovante
    print(f"\n{VERDE}{'='*50}")
    print(f"VENDA REALIZADA COM SUCESSO!")
    print(f"{'='*50}")
    print(f"Produto: {produto}")
    print(f"Valor original: R$ {valor_aparelho:.2f}")
    if desconto > 0:
        print(f"Desconto: {desconto:.0f}%")
        print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
    if valor_entrada > 0:
        print(f"Entrada: R$ {valor_entrada:.2f}")
    print(f"{'='*50}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Valor pago: R$ {valor_pago:.2f}")
    print(f"Troco: R$ {troco:.2f}")
    print(f"Data: {venda['data']}")
    print(f"{'='*50}{RESET}")
    
    if estoque[produto]["quantidade"] <= 2:
        print(f"\n{AMARELO}ATENÇÃO: '{produto}' está acabando! (Estoque: {estoque[produto]['quantidade']}){RESET}")
    
    pausar("\nPressione Enter para continuar...")
    return estoque, registro_vendas

def exibir_registro_vendas(registro_vendas, perfil):
    """Exibe o registro de vendas"""
    from core.models import PERMISSOES
    
    if "registro" not in PERMISSOES.get(perfil, []):
        print("\nAcesso negado! Você não pode ver o registro de vendas.")
        pausar()
        return
    
    limpar_tela()
    print(VERDE_CLARO + "REGISTRO DE VENDAS" + RESET)
    print("="*70)
    
    if not registro_vendas:
        print("\nNenhuma venda realizada ainda.")
    else:
        total_geral = 0
        for i, venda in enumerate(registro_vendas, 1):
            print(f"\n{'='*70}")
            print(f"VENDA #{i}")
            print(f"{'='*70}")
            print(f"Produto: {venda['produto']}")
            print(f"Data: {venda.get('data', '---')}")
            print(f"Vendedor: {venda.get('vendedor', '---')}")
            print(f"Valor original: R$ {venda['valor_aparelho']:.2f}")
            if venda.get('desconto', 0) > 0:
                print(f"Desconto: {venda['desconto']:.0f}%")
            if venda.get('entrada', 0) > 0:
                print(f"Entrada: R$ {venda['entrada']:.2f}")
            print(f"{'-'*70}")
            print(f"Valor final: R$ {venda['valor_final']:.2f}")
            print(f"Troco: R$ {venda.get('troco', 0):.2f}")
            total_geral += venda['valor_final']
        
        print(f"\n{'='*70}")
        print(f"TOTAL GERAL DE VENDAS: R$ {total_geral:.2f}")
        print(f"{'='*70}")
    
    pausar("\nPressione Enter para continuar...")