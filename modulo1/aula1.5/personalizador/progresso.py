"""Módulo para exibir barras de progresso com rich."""
from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def barra_simples(texto: str, isArquivo: bool):
    """
    Exibe uma barra de progresso simples antes de mostrar o texto.
    """
    with Progress() as progress:
        tarefa = progress.add_task("Carregando...", total=100)
        for _ in range(10):
            time.sleep(0.1)
            progress.update(tarefa, advance=10)

    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(texto)

def barra_completa(texto: str, isArquivo: bool):
    """
    Exibe uma barra de progresso mais elaborada.
    """
    with Progress() as progress:
        tarefa = progress.add_task("Processando...", total=5)
        for _ in range(5):
            time.sleep(0.2)
            progress.update(tarefa, advance=1)

    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            texto = f.read()
    console.print(texto)
