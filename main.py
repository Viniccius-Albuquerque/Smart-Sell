#==================import's=================
import time

from core.cores import *
from core.dados import *
from core.persistencia import *
from core.utilitarios import *

from autenticacao.login import *

from menus.menus import *


#============================LOOP PRINCIPAL================================

menu_login()
perfil = login()
carregar_estoque()
carregar_vendas()
carregar_financeiro()


while True:
    menu_principal(perfil)

    try:
        escolha = int(input(VERDE_CLARO + 'Selecione ação: ' + RESET))
    except ValueError:
        print("Digite um número válido!")
        input("Pressione Enter...")
        continue


    #===================ESTOQUE=======================
    if escolha == 1:
        from autenticacao.login import tem_permissao

        if not tem_permissao(perfil, "estoque_view"):
            print("Acesso negado!")
            input("Pressione Enter...")
            continue


        while True:
            menu_estoque()

            if perfil == "vendedor":
                print(AMARELO + "Modo visualização (sem permissão para editar)" + RESET)

            try:
                escolha_estoque = int(input(AMARELO+'\nSelecione ação: '+RESET))
            except ValueError:
                print("Digite um número válido!")
                continue


            # CRIAR PRODUTO
            if escolha_estoque == 1:
                if not tem_permissao(perfil, "estoque_add"):
                    print("Acesso negado!\n")
                    input("Pressione Enter...")
                    continue

                produto = input("Nome do novo produto: ").strip().lower()

                if produto in estoque:
                    print(VERMELHO+"Esse produto já existe!"+RESET)
                else:
                    try:
                        preco = float(input(VERDE_CLARO+"Preço do produto: R$ "+RESET))

                        if preco <= 0:
                            print("Preço inválido!")
                            input("Pressione Enter...")
                            continue

                        estoque[produto] = {
                            "quantidade": 0,
                            "preco": preco
                        }

                        salvar_estoque()
                        print(VERDE_CLARO + f"\nProduto '{produto}' criado com sucesso!\n" + RESET)

                    except ValueError:
                        print("Preço inválido!")

                input("\nPressione Enter...")


            # ADICIONAR ITEM
            elif escolha_estoque == 2:
                if not tem_permissao(perfil, "estoque_add"):
                    print("\nAcesso negado! Você não pode modificar o estoque.\n")
                    input("Pressione Enter...")
                    continue

                produto = input("Produto: ").strip().lower()

                if produto not in estoque:
                    print("Produto não existe! Crie primeiro.")
                    input("Pressione Enter...")
                    continue

                try:
                    quantidade = int(input("Quantidade a adicionar: "))

                    if quantidade <= 0:
                        print("Digite um número maior que 0!")
                        input("Pressione Enter...")
                        continue

                    estoque[produto]["quantidade"] += quantidade
                    salvar_estoque()

                    print(VERDE+f"\n{produto} agora tem {estoque[produto]['quantidade']} unidades\n")

                except ValueError:
                    print("Quantidade inválida!")

                input("\nPressione Enter...")


            # VER ESTOQUE
            elif escolha_estoque == 3:
                if not tem_permissao(perfil, "estoque_view"):
                    print("Acesso negado!")
                    input("Pressione Enter...")
                    continue

                menu_visualizar_estoque()
                input("\nPressione Enter para continuar...")


            #ATUALIZAR PRECO
            elif escolha_estoque == 4:
                if not tem_permissao(perfil, "estoque_add"):
                    print("Acesso negado!")
                    input("Pressione Enter...")
                    continue

                produto = input("Produto: ").strip().lower()

                if produto not in estoque:
                    print("Produto não existe!")
                    input("Pressione Enter...")
                    continue

                try:
                    novo_preco = float(input("Novo preço: R$ "))

                    if novo_preco <= 0:
                        print("Preço inválido!")
                        input("Pressione Enter...")
                        continue

                    estoque[produto]["preco"] = novo_preco
                    salvar_estoque()

                    print(VERDE_CLARO+f"\nPreço de '{produto}' atualizado para R$ {novo_preco:.2f}"+RESET)

                except ValueError:
                    print("Valor inválido!")

                input("\nPressione Enter...")


            # VOLTAR
            elif escolha_estoque == 0:
                break

            else:
                print("Opção inválida!")
                input("Pressione Enter...")


    #===================VENDAS=======================
    elif escolha == 2:
        from autenticacao.login import tem_permissao

        while True:
            menu_vendas()

            try:
                escolha_vendas = int(input(AMARELO+'\nSelecione ação: '+RESET))
            except ValueError:
                print("Digite um número válido!")
                continue


            # REALIZAR VENDA
            if escolha_vendas == 1:
                if not tem_permissao(perfil, "vendas"):
                    print("Acesso negado!")
                    input("Pressione Enter...")
                    continue

                menu_realizar_vendas()

                entrada = input(VERDE + "Digite o produto: " + RESET).lower()

                if entrada not in estoque:
                    print("Produto não existe!")
                    input("Pressione Enter...")
                    continue

                if estoque[entrada]["quantidade"] <= 0:
                    print(VERMELHO + "Produto sem estoque!" + RESET)
                    input("Pressione Enter para voltar...")
                    continue

                try:
                    valor_aparelho = estoque[entrada]["preco"]
                    print(f"Preço do produto: R$ {valor_aparelho:.2f}")

                    valor_entrada_cliente = float(input("Valor de entrada (0 se não houver): R$ "))

                    if valor_entrada_cliente < 0:
                        print("Valor de entrada inválido!")
                        continue

                    desconto = float(input("Desconto percentual (0 se não houver): "))

                    if desconto < 0 or desconto > 100:
                        print("Desconto inválido!")
                        continue

                    desconto_valor = desconto / 100
                    valor_com_desconto = valor_aparelho * (1 - desconto_valor)
                    valor_final = valor_com_desconto - valor_entrada_cliente

                    #=======imprimir valor com desconto========
                    espaco()
                    print(f"Valor total a pagar: R$ {valor_final:.2f}")
                    espaco()

                    #=======troco======
                    valor_pago = float(input("Valor PAGO: R$ "))

                    troco = valor_pago - valor_final

                    if troco < 0:
                        print("Valor Insuficiente!")
                        input("Pressione Enter...")
                        continue

                    # Se o valor final for negativo (entrada maior que o valor com desconto)
                    if valor_final < 0:
                        print(f"Troco para o cliente: R$ {abs(valor_final):.2f}")
                        valor_final = 0
                        troco = valor_pago

                    #===========venda realizada==========
                    estoque[entrada]["quantidade"] -= 1
                    salvar_estoque()

                    from datetime import datetime
                    
                    venda = {
                        "produto": entrada,
                        "valor_aparelho": valor_aparelho,
                        "entrada": valor_entrada_cliente,
                        "desconto": desconto,
                        "valor_final": valor_final,
                        "troco": troco if troco >= 0 else 0,
                        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                        "cliente": "Não informado",
                        "pagamento": "Dinheiro"
                    }

                    registro_vendas.append(venda)
                    salvar_vendas()

                    print(VERDE + "\nVenda realizada com sucesso!\n" + RESET)
                    print(f"Produto: {entrada}")
                    espaco()
                    print('-'*25)
                    print(f"Valor final: R$ {valor_final:.2f}")
                    print('-'*25)
                    espaco()
                    if troco > 0:
                        print(f"Troco: R$ {troco:.2f}")

                    if estoque[entrada]["quantidade"] <= 2:
                        print(AMARELO + f"ATENÇÃO: {entrada} está acabando!" + RESET)

                except ValueError:
                    print("Erro nos valores digitados!")

                input("\nPressione Enter para continuar...")


            # REGISTRO DE VENDAS
            elif escolha_vendas == 2:
                if not tem_permissao(perfil, "registro"):
                    print("Acesso negado!")
                    input("Pressione Enter...")
                    continue

                print("\n--- REGISTRO DE VENDAS ---")

                if not registro_vendas:
                    print("Nenhuma venda realizada.")
                else:
                    for indice, venda in enumerate(registro_vendas, 1):
                        print(f"\n{'='*40}")
                        print(f"Venda {indice}:")
                        print(f"Produto: {venda['produto']}")
                        print(f"Cliente: {venda.get('cliente', 'Não informado')}")
                        print(f"Data: {venda.get('data', '---')}")
                        print(f"Pagamento: {venda.get('pagamento', '---')}")
                        print(f"Valor aparelho: R$ {venda['valor_aparelho']:.2f}")
                        print(f"Entrada: R$ {venda['entrada']:.2f}")
                        print(f"Desconto: {venda['desconto']:.0f}%")
                        print(f"Valor final: R$ {venda['valor_final']:.2f}")
                        print(f"Troco: R$ {venda.get('troco', 0):.2f}")
                        print('='*40)

                input("\nPressione Enter para continuar...")


            # VOLTAR
            elif escolha_vendas == 0:
                break

            else:
                print("Opção inválida!")
                input("Pressione Enter...")


    elif escolha == 0:
        salvar_estoque()
        salvar_vendas()
        salvar_financeiro()
        creditos()
        break
    
    else:
        print("Opção inválida!")
        input("Pressione Enter...")