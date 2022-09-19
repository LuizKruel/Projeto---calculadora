"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.8
"""

import entra
import aritmetica
import sai

#main (escrever o módulo principal)
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


#Execução do programa
if __name__ == "__main__":
    main()
