"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input('Digite um número inteiro: ')

try:
    entrada_int = int(numero_inteiro)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'

    if par_impar:
        par_impar_texto = 'Par'


    print(f'O número {numero_inteiro} é {par_impar_texto}')
except:
    print('Voce não digitou um número inteiro')
