import sys
from core.config import CSI, RESET

def limpar_tela():
    """Limpa a tela do terminal"""
    sys.stdout.write(CSI + "2J")
    sys.stdout.write(CSI + "H")
    sys.stdout.flush()

def mover_topo():
    """Move o cursor para o topo"""
    sys.stdout.write(CSI + "H")
    sys.stdout.flush()

def esconder_cursor():
    """Esconde o cursor do terminal"""
    sys.stdout.write(CSI + "?25l")
    sys.stdout.flush()

def mostrar_cursor():
    """Mostra o cursor do terminal"""
    sys.stdout.write(CSI + "?25h")
    sys.stdout.flush()

def pausar(mensagem="Pressione Enter para continuar..."):
    """Pausa a execução até o usuário pressionar Enter"""
    input(mensagem)

def mostrar_loading(segundos=1):
    """Mostra animação de loading"""
    import time
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(segundos/3)
    print()

def exibir_cabecalho(titulo, cor):
    """Exibe um cabeçalho formatado"""
    limpar_tela()
    mover_topo()
    # Obtém a cor da string (ex: "CIANO" -> valor real)
    cor_valor = getattr(__import__('core.config', fromlist=[cor]), cor, "")
    print(cor_valor + titulo)
    print("=" * 50 + RESET)