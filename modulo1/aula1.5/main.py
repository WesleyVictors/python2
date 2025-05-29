"""
Script principal que oferece uma interface de linha de comando para o pacote 'personalizador'.
"""

import argparse
from personalizador import layout, painel, progresso, estilo

# Dicionário para mapear nomes dos módulos aos próprios módulos
modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

# Dicionário que mapeia nomes de módulos para suas funções disponíveis
funcoes = {
    "layout": ["centralizar_texto", "alinhar_direita"],
    "painel": ["painel_simples", "painel_com_titulo"],
    "progresso": ["barra_simples", "barra_completa"],
    "estilo": ["negrito_vermelho", "markdown_exemplo"]
}

# Configura o argparse
parser = argparse.ArgumentParser(description="Personalizador de Texto com Rich")

parser.add_argument("texto", help="Texto ou caminho para arquivo a ser formatado")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um caminho para um arquivo de texto")
parser.add_argument("-m", "--modulo", required=True, choices=modulos.keys(),
                    help="Módulo a ser usado: layout, painel, progresso, estilo")
parser.add_argument("-f", "--funcao", required=True,
                    help="Função a ser executada no módulo escolhido."
                         "layout: centralizar_texto, alinhar_direita"
                         "painel: painel_simples, painel_com_titulo"
                         "progresso: barra_simples, barra_completa"
                         "estilo: negrito_vermelho, markdown_exemplo")

args = parser.parse_args()

# Obtém o módulo e executa a função escolhida
modulo = modulos[args.modulo]

# Valida se a função escolhida está disponível
if args.funcao not in funcoes[args.modulo]:
    print(f"Função inválida para o módulo {args.modulo}.")
    print("Funções disponíveis:", ", ".join(funcoes[args.modulo]))
else:
    # Executa a função com os argumentos fornecidos
    getattr(modulo, args.funcao)(args.texto, args.arquivo)
