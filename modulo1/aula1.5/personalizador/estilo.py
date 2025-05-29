"""Módulo que aplica estilos visuais ao texto com rich."""
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def negrito_vermelho(texto: str, isArquivo: bool):
    """
    Mostra o texto em negrito e vermelho.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(f"[bold red]{texto}[/bold red]")

def markdown_exemplo(texto: str, isArquivo: bool):
    """
    Interpreta o texto como Markdown.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(Markdown(texto))
