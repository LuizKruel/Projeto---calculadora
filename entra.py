"""
Projeto-calculadora
Descrição: módulo de um programa python que permite a entrada de dois numeros.
Autor: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.5
"""

#Entrada de dados

def entrada() -> list:
    #Entra os dados de número em uma lista
    x = float(input("\nDigite o primeiro número e clique enter: "))
    y = float(input("\nDigite o segundo número e clique enter: "))
    return [x, y]
