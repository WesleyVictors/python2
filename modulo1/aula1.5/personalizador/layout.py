"""Módulo de layout usando rich para alinhar textos de forma elegante."""
from rich.console import Console
from rich.align import Align

console = Console()

def centralizar_texto(texto: str, isArquivo: bool):
    """
    Centraliza o texto na tela.
    Se isArquivo for True, lê o conteúdo do arquivo passado.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Align.center(texto))  # Centraliza o texto

def alinhar_direita(texto: str, isArquivo: bool):
    """
    Alinha o texto à direita da tela.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Align.right(texto))  # Alinha à direita
