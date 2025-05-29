"""Módulo de painel: exibe o texto dentro de um painel decorativo."""
from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto: str, isArquivo: bool):
    """
    Mostra o texto dentro de um painel básico.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Panel(texto))

def painel_com_titulo(texto: str, isArquivo: bool):
    """
    Mostra o texto em um painel com título.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Panel(texto, title="Título do Painel"))
