# -*- coding: utf-8 -*-

# Imports

from tridiagonal_ciclico import*

#### Resolvendo um sistema

escolha = int(input("Olá! Escolha uma das opções a seguir:\n1. Veja a solução\
do sistema dado no enunciado!\n2. Dê um sistema com dimensão maior que 2\
para eu resolver!"))

if escolha ==1:
    dimensao = 20
    #Criando as diagonais
    a = [0]*dimensao
    b = [0]*dimensao
    c = [0]*dimensao
    d = [0]*dimensao

    for contador in range(dimensao):
        a[contador] = 0.5
        b[contador] = 2
        c[contador] = 0.5
        multiplicador = pi/10
        i = (contador+1)
        d[contador] = cos(i*multiplicador)


elif escolha == 2:
    dimensao = int(input("Vamos resolver um sistema?\nEste programa resolve sistemas do tipo: A.x = d,\
sendo A uma matriz tridiagonal!\nPara começar, preciso de algumas informações a respeito da matriz A:\
\nDê a dimensão de A (ex: Uma matriz 3x3 tem dimensão 3): "))
    a = [0]*dimensao
    b = [0]*dimensao
    c = [0]*dimensao
    d = [0]*dimensao
    #Criando as diagonais

    #Diagonal principal:
    print("Por A ser diagonal, sabemos que seus únicos elementos não nulos são a diagonal principal,\
            e as diagonais acima e abaixo da principal. Para começar, quero que você me diga os elementos da \
            diagonal principal:\n")
    b = criar_vetor(dimensao)

    ##### Só teremos elementos != 0 sem ser na diagonal principal
    # se mod(i-j) >1, ou seja, dim > 2
    if dimensao > 2:
        print("Pela dimensão que você me deu, sei que sua A tem mais alguns elementos não nulos!\
            Então, preciso que você me diga agora os elementos da diagonal acima da principal:\n")
        #Diagonal Superior
        c = criar_diagonal_superior(dimensao)

        #Diagonal Inferior
        print("Bom, agora só me resta saber quais são os elementos da diagonal abaixo da principal!\n")
        a = criar_diagonal_inferior(dimensao)

        print("Por fim, antes que eu consiga resolver esse sistema, preciso saber quais são os elementos\
            que compõe o vetor d!")
        d = criar_vetor(dimensao)


print("Aguarde enquanto o programa resolve o sistema!")
matriz_decomposta = decomposicao_LU(dimensao, a, b, c)

solucao = resolver_sistema(d, matriz_decomposta[1], matriz_decomposta[2], c)

if escolha == 1:
    primeiro_elemento = 0.5
    ultimo_elemento = 0.5
    solucao_tridiagonal = resolver_sistema_tridiagonal_ciclico(a, b, c, d, solucao, primeiro_elemento, ultimo_elemento)

elif escolha == 2:
    ciclico = int(input("o sistema dado é cíclico?\n1. Sim\n2. Não"))
    if ciclico ==1:
        print("Por A ser tridiagonal cíclica, preciso saber de mais algumas informações!:\n")
        ultimo_elemento = float(input("Digite o último elemento da primeira linha: "))  # é o elemento a1
        primeiro_elemento = float(input("Digite o primeiro elemento da última linha: "))  # é o elemento cn
        solucao_tridiagonal = resolver_sistema_tridiagonal_ciclico(a, b, c, d, x, primeiro_elemento, ultimo_elemento)
    elif ciclico==2:
        for contador in range(0, dimensao):
            print("x[{}] = {}".format(contador, solucao[contador]))


