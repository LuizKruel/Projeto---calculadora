"""
Projeto-calculadora
Descrição: módulo que permite a entrada de dois numeros.
Autor: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.5
"""

# entrada de dados

def entrada() -> list:
    x = float(input("\nDigite o primeiro número e clique enter: "))
    y = float(input("\nDigite o segundo número e clique enter: "))
    return [x, y]
