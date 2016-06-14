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


escolha_n = int(input("Escolha um dos ns abaixo, ou então digite\n1. 7\n2. 15\n3. 31\n4. 63\n5. Outro\n"))
if escolha_n==1:
    n = 7
elif escolha_n==2:
    n = 15
elif escolha_n==3:
    n = 31
elif escolha_n==4:
    n = 63
elif escolha_n==5:
    n = int(input("Digite o valor de n:"))

# Definição de constantes
eps = 0.000001
h = 1/(n+1)
x_i = []
y_i = []
u_barra=[]
u_barra_fronteira=[]
erro_maximo = 0
erro_maximo_fronteira = 0
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
escolha_k = int(input("O que você deseja fazer em relação ao material?\n1. Usar material constante (k=1)\n2. Usar material variável(k variável)\n"))
if escolha_k==1:
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
##    for contador in range(0, n):
##        print("Matriz D[{}] = {}".format(contador, d[contador]))

elif escolha_k==2:
    k=2
    ##implementar aqui o k variavel

#Calculando u_barra
for i in range(10*n+1): #para o y
    elemento = 0
    y=i/(10*n)
    y_i.append(y)
    for j in range(1,n+1): #para o alpha
        if (y>=x_i[j-1]) and (y<x_i[j]):
            phi = lambda x:(((x-x_i[j-1])/h))
            elemento += alphas[j-1]*phi(y)
        elif (y>=x_i[j]) and (y<=x_i[j+1]):
            phi = lambda x:(((x_i[j+1]-x)/h))
            elemento += alphas[j-1]*phi(y)
    u_barra.append(elemento)

#Teste de convergencia
u = lambda x: (x**2)*((x-1)**2)
for i in range(10*n+1):
    if abs(u_barra[i]-u(y_i[i]))>erro_maximo:
        erro_maximo = u_barra[i]-u(y_i[i])
print("Erro:", erro_maximo)


#Teste de fronteira não homogênea
L = 1
a=u(0)
b=u(L)
for i in range(10*n+1):
    u_barra_fronteira.append(u_barra[i] + a + (b-a)*(y_i[i]/L) )
    if abs(u_barra_fronteira[i]-u(y_i[i]))>erro_maximo_fronteira:
        erro_maximo_fronteira = u_barra_fronteira[i]-u(y_i[i])
print("Erro Fronteira:", erro_maximo_fronteira)

