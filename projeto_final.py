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
eps = 0.000001
sigma = 1
teta = sigma

escolha_principal=int(input("Olá! Escolha umas das opções:\n1. Teste de Ordem de \
convergência\n2. Modelagem do sistema de resfriamento do chip\n"))

if escolha_principal==1:
    print("Esta escolha executará o teste para os seguintes valores de n: 7, 15,\
31, 63, 127 e 255! Então, vá fazer um café e volte daqui alguns minutos, até que o programa \
termine de rodar")
    k=1
    L=1
    a = 0
    b = 0

    n_vetor = [7,15,31,63,127,255]
    for n in n_vetor:
        inferior = []
        superior = []
        principal = []
        solucao = [] # coluna com o lado direito do sistema
        alphas = []
        x_i = []
        y_i = []
        u_barra=[]
        erro_maximo = 0
        print("Calculando alphas para n = {}".format(n))
        h = L/(n+1)
        for i in range(n+2):
            x_i.append(i*h)
            
        #Montagem do vetor d
        for i in range(1,n+1):
            #como a função de phi varia de acordo com a posição do intervalo, definimos  uma para cada parte dele
            funcao_primeiro_intervalo = lambda x: (((x-x_i[i-1])/h))*(12*x*(1-x)-2)
            funcao_segundo_intervalo = lambda x: (((x_i[i+1]-x)/h))*(12*x*(1-x)-2)
            # como a função de phi varia de acordo com a posição do intervalo, precisamos de uma integral para cada intervalo
            integral_primeiro_intervalo = romb(x_i[i-1],x_i[i],4,eps,15,funcao_primeiro_intervalo) #depois explicar os valores de n e itmax
            integral_segundo_intervalo = romb(x_i[i],x_i[i+1],4,eps,15,funcao_segundo_intervalo) #depois explicar os valores de n e itmax
            # somamos o valor obtido da integral de cada intervalo, assim temos o valor da integral total
            integral_solucao = integral_primeiro_intervalo + integral_segundo_intervalo
            solucao.append(integral_solucao)
            
        ## Criar diagonais da matriz A para resolver o sistema e encontrar os alphas
        for i in range(0,n):
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
            
        #Teste de convergencia
        u = lambda x: (x**2)*((x-1)**2)
        for i in range(10*n+1):
            if abs(u_barra[i]-u(y_i[i]))>erro_maximo:
                erro_maximo = u_barra[i]-u(y_i[i])
        print("Erro com n = {} : {}".format(n, erro_maximo))      
        
        
    
elif escolha_principal==2:
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
    L = 0.02
    h = L/(n+1)
    x_i = []
    #Preenchendo o vetor x
    for i in range(n+2):
        x_i.append(i*h)

    inferior = []
    superior = []
    principal = []
    solucao = [] # coluna com o lado direito do sistema
    alphas = []
    y_i = []
    u_barra=[]
    temperatura=[]
    escolha_k = int(input("O que você deseja fazer em relação ao material?\n1. Usar material constante: Silício com k=148\n2. Usar material variável: k variável\n"))
    if escolha_k==1:
        k = 148
        ## Criar diagonais da matriz A para resolver o sistema e encontrar os alphas
        for i in range(0, n):
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
        d = float(input("Escolha a distancia d (em m) de onde o material periferico, a partir do centro, comeca:  "))
        escolha_k_ncte = int(input("Você gostaria de:\n1. Usar os valores para um chip de Silício e Alumínio (Ks = 148 e Ka = 237)\
\n2. Escolher outros valores\n"))
        if escolha_k_ncte==1:
            k_interno = 148
            k_bordas = 237
        elif escolha_k_ncte==2:
            k_interno = float(input("Digite o k do material interno:"))
            k_bordas = float(input("Digite o k do material das bordas:"))
        else:
            print("Escolha Inválida!")
        ## Criar diagonais da matriz A para resolver o sistema e encontrar os alphas
        for i in range(0, n):
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

    else:
        print("Escolha inválida!")
        
    print("Digite os valores das fronteiras do chip, em Celsius (ºC):")
    a = 273 + float(input("Dê o valor de a:"))
    b = 273 + float(input("Dê o valor de b:"))

    escolha_q = int(input("O que você deseja fazer em relação ao Q+ e ao Q-?\n1. Q+ e Q- constantes\
\n2. Q+ constante e Q- gaussiano\n3. Q+ gaussiano e Q- constante\n4. Q+ e Q- gaussianos\n"))
    if escolha_q==1:
        q_mais = float(input("Digite o valor de Q+: "))
        q_menos = float(input("Digite o valor de Q-: "))
        #Montagem do vetor d
        for i in range(1,n+1):
            #como a função de phi varia de acordo com a posição do intervalo, definimos  uma para cada parte dele
            funcao_primeiro_intervalo = lambda x: (((x-x_i[i-1])/h))*(q_mais-q_menos)
            funcao_segundo_intervalo = lambda x: (((x_i[i+1]-x)/h))*(q_mais-q_menos)
            # como a função de phi varia de acordo com a posição do intervalo, precisamos de uma integral para cada intervalo
            integral_primeiro_intervalo = romb(x_i[i-1],x_i[i],4,eps,15,funcao_primeiro_intervalo) #depois explicar os valores de n e itmax
            integral_segundo_intervalo = romb(x_i[i],x_i[i+1],4,eps,15,funcao_segundo_intervalo) #depois explicar os valores de n e itmax
            # somamos o valor obtido da integral de cada intervalo, assim temos o valor da integral total
            integral_solucao = integral_primeiro_intervalo + integral_segundo_intervalo
            solucao.append(integral_solucao)
    elif escolha_q==2:
        q_mais = float(input("Digite o valor de Q+: "))
        q0_menos = float(input("Digite o valor de Q0-: "))
        #Montagem do vetor d
        for i in range(1,n+1):
            #como a função de phi varia de acordo com a posição do intervalo, definimos  uma para cada parte dele
            funcao_primeiro_intervalo = lambda x: (((x-x_i[i-1])/h))*(q_mais - q0_menos*(e**(((-1)*(x**2))/(teta**2))-(e**(((-1)*(x-L)**2)/(sigma**2)))))
            funcao_segundo_intervalo = lambda x: (((x_i[i+1]-x)/h))*(q_mais - q0_menos*(e**(((-1)*(x**2))/(teta**2))-(e**(((-1)*(x-L)**2)/(sigma**2)))))
            # como a função de phi varia de acordo com a posição do intervalo, precisamos de uma integral para cada intervalo
            integral_primeiro_intervalo = romb(x_i[i-1],x_i[i],4,eps,15,funcao_primeiro_intervalo) #depois explicar os valores de n e itmax
            integral_segundo_intervalo = romb(x_i[i],x_i[i+1],4,eps,15,funcao_segundo_intervalo) #depois explicar os valores de n e itmax
            # somamos o valor obtido da integral de cada intervalo, assim temos o valor da integral total
            integral_solucao = integral_primeiro_intervalo + integral_segundo_intervalo
            solucao.append(integral_solucao)
    elif escolha_q==3:
        q0_mais = float(input("Digite o valor de Q0+: "))
        q_menos = float(input("Digite o valor de Q-: "))
        #Montagem do vetor d
        for i in range(1,n+1):
            #como a função de phi varia de acordo com a posição do intervalo, definimos  uma para cada parte dele
            funcao_primeiro_intervalo = lambda x: (((x-x_i[i-1])/h))*(q0_mais*(e**(((-1)*(x-(L/2))**2)/(sigma**2))) - q_menos)
            funcao_segundo_intervalo = lambda x: (((x_i[i+1]-x)/h))*(q0_mais*(e**(((-1)*(x-(L/2))**2)/(sigma**2))) - q_menos)
            # como a função de phi varia de acordo com a posição do intervalo, precisamos de uma integral para cada intervalo
            integral_primeiro_intervalo = romb(x_i[i-1],x_i[i],4,eps,15,funcao_primeiro_intervalo) #depois explicar os valores de n e itmax
            integral_segundo_intervalo = romb(x_i[i],x_i[i+1],4,eps,15,funcao_segundo_intervalo) #depois explicar os valores de n e itmax
            # somamos o valor obtido da integral de cada intervalo, assim temos o valor da integral total
            integral_solucao = integral_primeiro_intervalo + integral_segundo_intervalo
            solucao.append(integral_solucao)
    elif escolha_q==4:
        q0_mais = float(input("Digite o valor de Q0+: "))
        q0_menos = float(input("Digite o valor de Q0-: "))
        #Montagem do vetor d
        for i in range(1,n+1):
            #como a função de phi varia de acordo com a posição do intervalo, definimos  uma para cada parte dele
            funcao_primeiro_intervalo = lambda x: (((x-x_i[i-1])/h))*(q0_mais*(e**(((-1)*(x-(L/2))**2)/(sigma**2))) - q0_menos*(e**(((-1)*(x**2))/(teta**2))-(e**(((-1)*(x-L)**2)/(sigma**2)))))
            funcao_segundo_intervalo = lambda x: (((x_i[i+1]-x)/h))*(q0_mais*(e**(((-1)*(x-(L/2))**2)/(sigma**2))) - q0_menos*(e**(((-1)*(x**2))/(teta**2))-(e**(((-1)*(x-L)**2)/(sigma**2)))))
            # como a função de phi varia de acordo com a posição do intervalo, precisamos de uma integral para cada intervalo
            integral_primeiro_intervalo = romb(x_i[i-1],x_i[i],4,eps,15,funcao_primeiro_intervalo) #depois explicar os valores de n e itmax
            integral_segundo_intervalo = romb(x_i[i],x_i[i+1],4,eps,15,funcao_segundo_intervalo) #depois explicar os valores de n e itmax
            # somamos o valor obtido da integral de cada intervalo, assim temos o valor da integral total
            integral_solucao = integral_primeiro_intervalo + integral_segundo_intervalo
            solucao.append(integral_solucao)
    else:
        print("Escolha inválida")

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
        
    for i in range(10*n+1):
        temperatura.append((u_barra[i] + a + (b-a)*(y_i[i]/L))-273 )
        
    print("\n -------- Temperatura em Cº em função de 'x' -------- ")
    for contador in range(0, 10*n+1):
        print("T({}) = {}".format(y_i[contador], temperatura[contador]))


