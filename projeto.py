from funcoes_projeto import*
#######################################################
##                                                   ##
##  MAP-3121 - Projeto Computacional - 2016          ##
##                                                   ##
##                        Alunos:                    ##
##          Bruno da Costa Braga (8993480)           ##
##           Maria Carla Machado (8993584)           ##
##                                                   ##
##                       Turma 03                    ##
##                                                   ##
#######################################################


############ Programa Principal

# Definição de constantes
eps = 0.000001
n = int(input("Digite o valor de n:"))
h = 1/(n+1)
x_i = []
#y_i = []
u_barra=[]
d = [] # coluna com o lado direito do sistema
phi_linha_primeiro_intervalo = 1/h #Primeiro intervalo: [Xi-1, X]
phi_linha_segundo_intervalo = (-1)/h #Segundo intervalo: [X, Xi+1]

#Preenchendo o vetor x
for i in range(n+2):
    x_i.append(i*h)

#Montagem do vetor d
for i in range(1,n+1):
    #como a função de phi varia de acordo com a posição do intervalo, definimos  uma para cada parte dele
    funcao_primeiro_intervalo = lambda x: (((x-x_i[i-1])/h))*(12*x*(1-x)-2) #mudar dps para funcao do calor
    funcao_segundo_intervalo = lambda x: (((x_i[i+1]-x)/h))*(12*x*(1-x)-2) #mudar dps para funcao do calor
    # como a função de phi varia de acordo com a posição do intervalo, precisamos de uma integral para cada intervalo
    integral_primeiro_intervalo = romb(x_i[i-1],x_i[i],4,eps,15,funcao_primeiro_intervalo) #depois explicar os valores de n e itmax
    integral_segundo_intervalo = romb(x_i[i],x_i[i+1],4,eps,15,funcao_segundo_intervalo) #depois explicar os valores de n e itmax
    # somamos o valor obtido da integral de cada intervalo, assim temos o valor da integral total
    integral_d = integral_primeiro_intervalo + integral_segundo_intervalo
    d.append(integral_d)
    
    
#Montagem da matriz A
escolha = int(input("O que você deseja fazer em relação ao material?\n1. Usar material constante (k=1)\n2. Usar material variável(k variável)\n"))
if escolha==1:
    k=1
    a = criar_diagonal_inferior(n, (-1)/h)#diagonal inferior
    b = criar_vetor(n, 2/h) #diagonal principal
    c = criar_diagonal_superior(n, (-1)/h) #diagonal superior

    # Para resolver o sistema, é necessário fazer a decomposição LU
    matriz_decomposta = decomposicao_LU(n, a, b, c)

    #resolvendo o sistema
    alphas = resolver_sistema(d, matriz_decomposta[1], matriz_decomposta[2], c)

    for contador in range(0, n):
        print("alpha[{}] = {}".format(contador, alphas[contador]))

elif escolha==2:
    k=2

#Definindo o vetor y_i
#for i in range(1,n+1):
#    y=i/(10*n)
#    y_i.append(y)
##for contador in range(0, n):
##    print("y[{}] = {}".format(contador, y_i[contador]))
for contador in range(0, n):
    print("x[{}] = {}".format(contador, x_i[contador]))

#Calculando u_barra
for i in range(0, 10*n): #para o y
    elemento = 0
    y=i/(10*n)
    print("y = {}".format(y))
    for j in range(1,n+1): #para o alpha
        if (y>=x_i[j-1]) and (y<=x_i[j]):
            phi = lambda x:(((x-x_i[j-1])/h))
            elemento += alphas[j-1]*phi(y)
        elif (y>=x_i[j]) and (y<=x_i[j+1]):
            phi = lambda x:(((x-x_i[j-1])/h))
            elemento += alphas[j-1]*phi(y)
##        else:
##            elemento +=0
    u_barra.append(elemento)

for contador in range(0, 10*n+1):
    print("u_barra[{}] = {}".format(contador, u_barra[contador]))


