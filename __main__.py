"""
Projeto-calculadora
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Luiz Kruel
Data: 19/09/2022
Versão: 0.0.5
"""

# importação dos módulos

import entra
import aritmetica
import sai

# Função de boas-vindas

def welcome():
    print("""Bem-vindo(a) à Calculadora!""")

welcome()


# definição das operações

def main():
    lista_numeros = entra.entrada()
    operacao = input("""\nInforme a operação desejada e clique enter:
                 + para adição
                 - para subtração
                 * para multiplicação
                 / para divisão\n""")
    if operacao == "+":
        valor = aritmetica.adicao(lista_numeros[0], lista_numeros[1])
    elif operacao == "-":
        valor = aritmetica.subtracao(lista_numeros[0], lista_numeros[1])
    elif operacao == "*":
        valor = aritmetica.multiplicacao(lista_numeros[0], lista_numeros[1])
    elif operacao == "/":
        valor = aritmetica.divisao(lista_numeros[0], lista_numeros[1])
    else:
        valor = "Esta operação não está definida para esta calculadora."
    sai.saida(valor)


# execução do programa

if __name__ == "__main__":
    main()
