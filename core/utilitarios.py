import sys
from core.cores import CSI


def espaco():
    print()


def esconder_cursor():
    sys.stdout.write(CSI + "?25l")
    sys.stdout.flush()


def mostrar_cursor():
    sys.stdout.write(CSI + "?25h")
    sys.stdout.flush()


def limpar_tela():
    sys.stdout.write(CSI + "2J")
    sys.stdout.write(CSI + "H")
    sys.stdout.flush()


def mover_topo():
    sys.stdout.write(CSI + "H")
    sys.stdout.flush()