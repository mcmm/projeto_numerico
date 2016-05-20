from math import*
#######################################################
##                                                   ##
##  MAP-3121 - Terceira tarefa computacional - 2016  ##
##                                                   ##
##                        Alunos:                    ##
##          Bruno da Costa Braga (8993480)           ##
##           Maria Carla Machado (8993584)           ##
##                                                   ##
##                       Turma 03                    ##
##                                                   ##
#######################################################

######### Funções
  
def trapz(a, b, t, i):
    hi = (b-a)/(2**i)
    somatoria = 0
    for j in range (1, (2**(i-1))+1):
        f1 = funcao1(a+(2*j - 1)*hi)
        somatoria += f1
    t = t/2 + (hi)*somatoria
    return t

def romb(a, b, n, eps, itmax):
    T = []
    h = (b-a)
    
    T00 = h*(funcao1(a)+funcao1(b))/2
    T_aux = [T00]
    T.append(T_aux)
    t = T00 
    iteracoes = 1
    
    for i in range (1, n+1):
        T_aux = []           
        for k in range (0, i+1):
            if k==0:
                t = trapz(a,b,t,i)  
                T_aux.append(t)
            else:
                Tik = (T_aux[k-1] + (T_aux[k-1] - T[i-1][k-1])/((4**k)-1))
                T_aux.append(Tik)
        T.append(T_aux)
        

        
    while (iteracoes <= itmax):
        iteracoes += 1
        if (abs(T[n][n]-T[n][n-1]) <= eps*T[n][n]):
            print("O método convergiu pela diferença. Foram necessárias {} iterações".format(iteracoes-1))
            print("Precisão:", abs(T[n][n]-T[n][n-1]))
            break
        else:
            for i in range(0, n):
                for j in range(0, i+1):
                    T[i][j] = T[i+1][j]

            
            for k in range (0, n+1):
                if k==0:
                    t = trapz(a,b,T[n-1][0],n+iteracoes-1)  
                    T[n][k]=t
                else:
                    Tik = (T_aux[k-1] + (T_aux[k-1] - T[n-1][k-1])/((4**k)-1))
                    T[n][k] = Tik  
    integral = T[n][n]
    if iteracoes==itmax:
        print("O método atingiu o número máximo de iterações")
    

    return integral

################

################ Programa Principal
sair=0
while sair==0:
    escolha= int(input("\nEscolha uma das funções a seguir para calcular a integral:\n\
    1. x^4ln(x+sqrt(x^2+1))\n\
    2. 1/(1-x)\n\
    3. 1/pi(cos(sen(x))\n\
    4. sqrt(x)cos(x)\n\
    5. Perímetro da Elipse de eixo de comprimento 2 e 3\n\
    6. Sair\n"))

    if escolha==6:
        break

    print("Defina os intervalos da integração:")
    a = float(input("Digite o valor de a:\n"))
    b = float(input("Digite o valor de b:\n"))

    mudar_erro = int(input("A precisão é de 10^(-6), deseja mudá-la?\n0. Não\n1. Sim\n"))
    if mudar_erro==0:
        eps = 0.000001
    else:
        eps=float(input("Digite o valor da precisão:\n"))

    mudar_n = int(input("O número de colunas padrão é 4, deseja mudá-lo?\n0. Não\n1. Sim\n"))
    if mudar_n==0:
        n = 4
    else:
        n=int(input("Digite o valor de n:\n"))

    mudar_itmax = int(input("O número máximo de iterações é 20, deseja mudá-lo?\n0. Não\n1. Sim\n"))
    if mudar_itmax==0:
        itmax = 20
    else:
        itmax=float(input("Digite o valor máximo de iterações:\n"))

    if escolha ==1:
        def funcao1 (x):
            f1 = (x**4)*log(x+sqrt(x**2+1),e)
            return f1
    elif escolha ==2:
        def funcao1 (x):
            f1 = 1/(1-x)
            return f1
    elif escolha ==3:
        def funcao1 (x):
            f1 = cos(sin(x))
            return f1
    elif escolha ==4:
        def funcao1 (x):
            f1 = sqrt(x)*cos(x)
            return f1
    elif escolha ==5:
        def funcao1 (x):
            f1 = sqrt(((1.5*cos(x))**2)+(sin(x)**2))
            return f1
    if escolha==3:
        integral =((1/pi)* romb(a, b, n, eps, itmax))
        print("O valor da integral para a precisão escolhida é de: ", integral)
    else:
        integral = romb(a, b, n, eps, itmax)
        print("O valor da integral para a precisão escolhida é de: ", integral)






                
            
        


