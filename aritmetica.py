"""
Projeto-calculadora
Descrição: módulo que realiza as 4 operações matemáticas.
Autor: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.5
"""

# processamento de dados

def adicao(x: float, y: float) -> float:
    #soma dois números.
    return x + y


def subtracao(x: float, y: float) -> float:
   #subtrai um número x de um número y.
   return x - y

def multiplicacao(x: float, y: float) -> float:
    #multiplica os dois números.
    return x*y


def divisao(x: float, y: float) -> float:
    #divide x por y sendo y diferente de zero
    if y == 0:
        return "Não se pode dividir por zero."
    return x/y
