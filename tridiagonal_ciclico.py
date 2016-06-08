# -*- coding: utf-8 -*-

# Imports
from metodos_solucao_sistema import*

#### Novos métodos necessários

def criar_vetor_menor(vetor):
    ''' Metodo para copiar os elementos de um vetor, menos seu último, em um novo.
        Parâmetros de entrada:
        vetor: vetor, de tamanho n, a ser copiado;

        Parâmetros de saída:
        novo_vetor: vetor de tamanho n-1, igual ao de entrada mas sem o último elemento'''
    tamanho = len(vetor)-1
    novo_vetor = []
    for contador in range(0, tamanho):
        novo_vetor.append(vetor[contador])
    return novo_vetor

#### Resolvendo um sistema tridiagonal cíclico

def resolver_sistema_tridiagonal_ciclico(a, b, c, d, x, primeiro_elemento, ultimo_elemento):
    print("Agora é só aguardar enquanto a mágica acontece!")

    n = len(a)-1 #pelo fato do indice comecar no 0 e não no 1

    #criando a matriz T:
    T_superior = criar_vetor_menor(c)
    T_principal = criar_vetor_menor(b)
    T_inferior = criar_vetor_menor(a)

    #criando vetor d_til
    d_til = criar_vetor_menor(d)

    #criando vetor x_til
    x_til = criar_vetor_menor(x)
    
    #criando o vetor v:
    v = [0]*n
    v[0] = ultimo_elemento
    v[n-1] = c[n-2]
    
    #criando o vetor w:
    w = [0]*n
    w[0] = primeiro_elemento
    w[n-1] = a[n-1]

    #### decompondo T:
    T_decomposto = decomposicao_LU(n, T_inferior, T_principal, T_superior)

    #### resolvendo T.y_til = d_til
    y_til = resolver_sistema(d_til, T_decomposto[1], T_decomposto[2], T_superior)

    #### resolvendo T.y_til = d_til
    z_til = resolver_sistema(v, T_decomposto[1], T_decomposto[2], T_superior)

    #### encontrando x_til
           
    numerador = d[n] - (c[n]*y_til[0]) - (a[n]*y_til[n-1])
    denominador = b[n] - (c[n]*z_til[0]) - (a[n-1]*z_til[n-1])
    x_n = numerador/denominador
    x_til = [0]*(n+1)
    x_til[n] = x_n
             
    for contador in range(0, n):
             x_til[contador] = y_til[contador] - (x_n*z_til[contador])
             
    
    for contador in range(0,n+1):
             print("x[{}] = {}".format(contador, x_til[contador]))

    
    return 0
