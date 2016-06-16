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

# Definição de variaveis
eps = 0.000001
sigma = 1
teta = sigma
x_i = []
y_i = []
u_barra=[]
u_barra_fronteira=[]
erro_maximo = 0
erro_maximo_fronteira = 0
solucao = [] # coluna com o lado direito do sistema
inferior = []
superior = []
principal = []
L = 0.02
h = L/(n+1)
q_mais = 37500000
q_menos = 20000000

#Preenchendo o vetor x
for i in range(n+2):
    x_i.append(i*h)
print("xi", x_i)

#Montagem do vetor d
for i in range(1,n+1):
    #como a função de phi varia de acordo com a posição do intervalo, definimos  uma para cada parte dele
    funcao_primeiro_intervalo = lambda x: (((x-x_i[i-1])/h))*(q_mais*(e**(((-1)*(x-(L/2))**2)/(sigma**2))) - q_menos*(e**(((-1)*(x**2))/(teta**2))-(e**(((-1)*(x-L)**2)/(sigma**2)))))
    funcao_segundo_intervalo = lambda x: (((x_i[i+1]-x)/h))*(q_mais*(e**(((-1)*(x-(L/2))**2)/(sigma**2))) - q_menos*(e**(((-1)*(x**2))/(teta**2))-(e**(((-1)*(x-L)**2)/(sigma**2)))))
    # como a função de phi varia de acordo com a posição do intervalo, precisamos de uma integral para cada intervalo
    integral_primeiro_intervalo = romb(x_i[i-1],x_i[i],4,eps,15,funcao_primeiro_intervalo) #depois explicar os valores de n e itmax
    integral_segundo_intervalo = romb(x_i[i],x_i[i+1],4,eps,15,funcao_segundo_intervalo) #depois explicar os valores de n e itmax
    # somamos o valor obtido da integral de cada intervalo, assim temos o valor da integral total
    integral_solucao = integral_primeiro_intervalo + integral_segundo_intervalo
    solucao.append(integral_solucao)

print("solucao", solucao)
    

escolha_k = int(input("O que você deseja fazer em relação ao material?\n1. Usar material constante\n2. Usar material variável(k variável)\n"))
if escolha_k==1:
    escolha_k_cte = int(input("Qual valor de k você gostaria de usar?\n1. k=1\n2. k=3.6\n3.Outro k constante\n"))
    if escolha_k_cte==1:
        k =1
    elif escolha_k_cte==2:
        k = 3.6
    elif escolha_k_cte==3:
        k = float(input("Digite o valor de k:"))
    else:
        print("Escolha Inválida!")

## Criar diagonais da matriz A para resolver o sistema e encontrar os alphas
    for i in range(1, n+1):
        if i ==0:
            inferior.append(0)
            principal.append((2*k)/h)
            superior.append(((-1)*k)/h)
        elif  i ==n:
            inferior.append(((-1)*k)/h)
            principal.append((2*k)/h)
            superior.append(0)
        else:
            inferior.append(((-1)*k)/h)
            principal.append((2*k)/h)
            superior.append(((-1)*k)/h)


elif escolha_k==2:
    d = float(input("Escolha a distancia d (em mm) de onde o material periferico, a partir do centro, comeca:  "))
    escolha_k_ncte = int(input("Você gostaria de:\n1. Usar os valores para um chip de Silício e Alumínio (Ks = 3.6 e Ka = 60)\
\n2. Escolher outros valores\n"))
    if escolha_k_ncte==1:
        k_interno = 3.6
        k_bordas = 60
    elif escolha_k_ncte==2:
        k_interno = float(input("Digite o k do material interno:"))
        k_bordas = float(input("Digite o k do material das bordas:"))
    else:
        print("Escolha Inválida!")
## Criar diagonais da matriz A para resolver o sistema e encontrar os alphas                         
    for i in range(1, n+1):
        if ((x_i[i] >= (L/2)-d) and x_i[i]<=((L/2)+d)):
            k = k_interno
        else:
            k = k_bordas
        if i ==0:
            inferior.append(0)
            principal.append((2*k)/h)
            superior.append(((-1)*k)/h)
        elif  i ==n:
            inferior.append(((-1)*k)/h)
            principal.append((2*k)/h)
            superior.append(0)
        else:
            inferior.append(((-1)*k)/h)
            principal.append((2*k)/h)
            superior.append(((-1)*k)/h)

# Para resolver o sistema, é necessário fazer a decomposição LU
matriz_decomposta = decomposicao_LU(n, inferior, principal, superior)

#resolvendo o sistema
alphas = resolver_sistema(solucao, matriz_decomposta[1], matriz_decomposta[2], superior)

for contador in range(0, n):
    print("alpha[{}] = {}".format(contador, alphas[contador]))


#Calculando u_barra
for i in range(10*n+1): #para o y
    elemento = 0
    y=(L*i)/(10*n)
    y_i.append(y)
    for j in range(1,n+1): #para o alpha
        if (y>=x_i[j-1]) and (y<x_i[j]):
            phi = lambda x:(((x-x_i[j-1])/h))
            elemento += alphas[j-1]*phi(y)
        elif (y>=x_i[j]) and (y<=x_i[j+1]):
            phi = lambda x:(((x_i[j+1]-x)/h))
            elemento += alphas[j-1]*phi(y)
    u_barra.append(elemento)
print("y:", y)
print("u_barra:", u_barra)

###Teste de convergencia
##u = lambda x: (x**2)*((x-1)**2)
##for i in range(10*n+1):
##    if abs(u_barra[i]-u(y_i[i]))>erro_maximo:
##        erro_maximo = u_barra[i]-u(y_i[i])
##print("Erro:", erro_maximo)


###Teste de fronteira não homogênea
##L = 1
a=293
b=293
for i in range(10*n+1):
    u_barra_fronteira.append((u_barra[i] + a + (b-a)*(y_i[i]/L))-273 )
##    if abs(u_barra_fronteira[i]-u(y_i[i]))>erro_maximo_fronteira:
##        erro_maximo_fronteira = u_barra_fronteira[i]-u(y_i[i])
print("U Fronteira:", u_barra_fronteira)

