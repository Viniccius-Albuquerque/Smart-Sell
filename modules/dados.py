import json
from core.config import ARQUIVO_ESTOQUE, ARQUIVO_VENDAS, ARQUIVO_FINANCEIRO

def salvar_estoque(estoque):
    """Salva o estoque no arquivo JSON"""
    try:
        with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as arquivo:
            json.dump(estoque, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar estoque: {e}")
        return False

def carregar_estoque():
    """Carrega o estoque do arquivo JSON"""
    try:
        with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Erro ao carregar estoque: {e}")
        return {}

def salvar_vendas(registro_vendas):
    """Salva o registro de vendas"""
    try:
        with open(ARQUIVO_VENDAS, "w", encoding="utf-8") as f:
            json.dump(registro_vendas, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar vendas: {e}")
        return False

def carregar_vendas():
    """Carrega o registro de vendas"""
    try:
        with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Erro ao carregar vendas: {e}")
        return []

def salvar_financeiro(financeiro):
    """Salva dados financeiros"""
    try:
        with open(ARQUIVO_FINANCEIRO, "w", encoding="utf-8") as f:
            json.dump(financeiro, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar financeiro: {e}")
        return False

def carregar_financeiro():
    """Carrega dados financeiros"""
    try:
        with open(ARQUIVO_FINANCEIRO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"total_vendas": 0, "historico": []}
    except Exception as e:
        print(f"Erro ao carregar financeiro: {e}")
        return {"total_vendas": 0, "historico": []}