import json
from core.dados import estoque, registro_vendas, financeiro


#======salvar estoque===
def salvar_estoque():
    with open("data/estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)


#======carregar estoque======
def carregar_estoque():
    global estoque

    try:
        with open("data/estoque.json", "r") as arquivo:
            dados_carregados = json.load(arquivo)
            estoque.clear()
            estoque.update(dados_carregados)
    except FileNotFoundError:
        pass
    except Exception:
        pass


#=======SALVAR VENDAS=======
def salvar_vendas():
    with open("data/vendas.json", "w") as arquivo:
        json.dump(registro_vendas, arquivo, indent=4)


#=======CARREGAR VENDAS=======
def carregar_vendas():
    global registro_vendas

    try:
        with open("data/vendas.json", "r") as arquivo:
            dados_carregados = json.load(arquivo)
            registro_vendas.clear()
            registro_vendas.extend(dados_carregados)
    except FileNotFoundError:
        pass
    except Exception:
        pass


#=======SALVAR FINANCEIRO=======
def salvar_financeiro():
    with open("data/financeiro.json", "w") as arquivo:
        json.dump(financeiro, arquivo, indent=4)


#=======CARREGAR FINANCEIRO=======
def carregar_financeiro():
    global financeiro

    try:
        with open("data/financeiro.json", "r") as arquivo:
            dados_carregados = json.load(arquivo)
            financeiro.clear()
            financeiro.update(dados_carregados)
    except FileNotFoundError:
        pass
    except Exception:
        pass