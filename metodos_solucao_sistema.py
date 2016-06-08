# -*- coding: utf-8 -*-

# Imports
from math import *

#### Para criar os vetores da matriz tridiagonal
def criar_vetor(dimensao):
	vetor=[]
	for contador in range(0, dimensao):
                elemento = float(input("Digite o próximo elemento:"))
                vetor.append(elemento)

	return vetor

def criar_diagonal_superior(dimensao):
        diagonal_secundaria=[]
        for contador in range(0, dimensao-1):
                elemento = float(input("Digite o elemento {}{} da diagonal superior:" .format(contador, contador+1)))
                diagonal_secundaria.append(elemento)

        diagonal_secundaria.append(0)
        return diagonal_secundaria

def criar_diagonal_inferior(dimensao):
        diagonal_secundaria=[]
        diagonal_secundaria.append(0)
        for contador in range(1, dimensao):
                elemento = float(input("Digite o elemento {}{} da diagonal inferior:" .format(contador, contador+1)))
                diagonal_secundaria.append(elemento)
        return diagonal_secundaria
####

#### Para fazer a decomposição LU
def decomposicao_LU(dimensao, a, b, c):
    ''' Metodo para fazer a decomposição LU de uma Matriz Tridiagonal A dada.
        Parâmetros de entrada:
        dimensao: dimensão da matriz A (vulgo 'n');
        a: vetor com elementos da diagonal abaixo da principal (diagonal inferior)
        b: vetor com elementos da diagonal principal;
        c: vetor com elementos da diagonal acima da principal (diagonal superior)

        Parâmetros de saída:
        decomposta: matriz que contém L e U:
        decomposta[0] == vetor com diagonal principal de L
        decomposta[1] == vetor com elementos Li+1,i
        decomposta[2] == vetor com diagonal principal de U
        decomposta[3] == vetor com elementos Ui, i+1  '''

    decomposta = [] 

    #Criação das matrizes U e L:
    U_principal = b[:] #copiando a diagonal principal para a diagonal principal de U
    U_superior = [0]*dimensao #outro vetor para armazenar os elementos de U que não são nulos
                                          # não estão na diagonal principal
    L_principal = [1]*dimensao #sabemos que a diagonal principal de L é formada apenas por 1s
    L_inferior = [0]*dimensao
    #Calculando os multiplicadores para criar a matriz L e escalonando para criar
    # a diagonal principal da U
    for contador in range(1, dimensao): 
            L_inferior[contador] = a[contador]/U_principal[contador-1]
            U_principal[contador] = b[contador] - (L_inferior[contador]*c[contador-1])

    #atribuindo valores para a diagonal superior de U
    for elemento in range(0, dimensao):
            U_superior[elemento]=c[elemento]
    
    decomposta.append(L_principal)
    decomposta.append(L_inferior)
    decomposta.append(U_principal)
    decomposta.append(U_superior)

    return decomposta

def resolver_sistema(d, L, U, c):
    ''' Metodo para solucionar um sistema do tipo A.x = d.
        Supõe-se que a decomposição A = LU já tenha sido feita
        Parâmetros de entrada:
        d: dimensão da matriz A (vulgo 'n');
        L: vetor com elementos Li+1,i
        U: vetor com elementos Ui, i+1 
        c: vetor com elementos da diagonal acima da principal (diagonal superior) de A

        Parâmetros de saída:
        x = vetor com a solução do sistema '''
    
    dimensao = len(d) #para não ter que pegar a dimensao nos parâmetros
    n = dimensao-1 #como o índice começa no 0, vai até dimensão - 1
    y = [0]*dimensao #criando o vetor y, de L.y = d

    #calculando y
    y[0] = d[0]

    for contador in range(1, dimensao):
        y[contador] = d[contador] - (L[contador]*y[contador-1])

    x = [0]*dimensao #criando o vetor x, de U. x = y, x é a solução do sistema!

    #calculando x
    x[n] = y[n]/U[n]

    contador = n-1

    while contador != -1:
        x[contador] = (y[contador]-(c[contador]*x[contador+1]))/U[contador]
        contador -= 1

    return x


    



