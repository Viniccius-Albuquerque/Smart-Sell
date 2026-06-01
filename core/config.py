import os

# Cores ANSI
RESET = "\033[0m"
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
ROSA = "\033[95m" 
CIANO = "\033[96m"
CINZA = "\033[90m"
VERDE_CLARO = "\033[92m"
ROXO = "\033[94m" 
MARROM = "\033[38;5;94m"
LARANJA = "\033[38;5;208m"
ROSA_CLARO = "\033[38;5;205m"
VERMELHO_CLARO = "\033[91m"

CSI = "\033["

# Obtém o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "dados")

# Garante que a pasta dados existe
os.makedirs(DATA_DIR, exist_ok=True)

# Arquivos de dados (agora na pasta dados)
ARQUIVO_ESTOQUE = os.path.join(DATA_DIR, "estoque.json")
ARQUIVO_VENDAS = os.path.join(DATA_DIR, "vendas.json")
ARQUIVO_FINANCEIRO = os.path.join(DATA_DIR, "financeiro.json")