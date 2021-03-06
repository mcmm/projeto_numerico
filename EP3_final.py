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
            print("\n   O método convergiu pela diferença. Foram necessárias {} iterações".format(iteracoes-1))
            print("   Precisão:", abs(T[n][n]-T[n][n-1]))
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
        print("\n   O método atingiu o número máximo de iterações")

    return integral

################

################ Programa Principal

sair = 0
eps = 0.000001
n = 4
itmax = 20 

while sair==0:

    print("\n\nAs variáveis padrões atuais são: n =",n,", Epslon =",eps,", ITMAX =",itmax)
    print("\n   1. Alterar as variáveis padrões (n, epslon, ITMAX)")
    print("   2. Integrar x^4ln(x+sqrt(x^2+1))")
    print("   3. Integrar 1/(1-x)")
    print("   4. Integrar 1/pi(cos(sen(x))")
    print("   5. Integrar sqrt(x)cos(x)")
    print("   6. Perímetro da Elipse de eixos de comprimento 2 e 3")
    print("   7. Sair")
    escolha = int(input("\n   Escolha uma das opções acima:"))          
                     
       
    if escolha ==1:
        print("\n   Escolha qual variável você deseja alterar:")
        print("   1. Alterar 'n'")
        print("   2. Alterar 'Epslon'")
        print("   3. Alterar 'ITMAX'\n")
        mudar = int(input())

        if mudar == 1:
            n=int(input("Digite o valor de n:\n"))
        elif mudar == 2:
            eps=float(input("Digite o valor da precisão:\n"))
        elif mudar == 3:
            itmax=float(input("Digite o valor máximo de iterações:\n"))

    elif escolha ==2:
        def funcao1 (x):
            f1 = (x**4)*log(x+sqrt(x**2+1),e)
            return f1
        print("\n   Escolha uma das opções:")
        print("   1. Integrar usando o intervalo padrão: a = 0, b = 2")
        print("   2. Integrar usando outro intervalo")
        escolha2 = int(input())
        if escolha2 == 1:
            a = 0
            b = 2
        else:
            print("\n   Defina os intervalos da integração:")
            a = float(input("   Digite o valor de a:"))
            b = float(input("   Digite o valor de b:"))
        integral = romb(a, b, n, eps, itmax)
        print("   O valor da integral para a precisão escolhida é de: ", integral)

    elif escolha ==3:
        def funcao1 (x):
            f1 = 1/(1-x)
            return f1
        print("\n   Escolha uma das opções:")
        print("   1. Integrar usando o intervalo padrão: a = 0, b = 0.995")
        print("   2. Integrar usando outro intervalo")
        escolha2 = int(input())
        if escolha2 == 1:
            a = 0
            b = 0.995
        else:
            print("\n   Defina os intervalos da integração:")
            a = float(input("   Digite o valor de a:"))
            b = float(input("   Digite o valor de b:"))
        integral = romb(a, b, n, eps, itmax)
        print("   O valor da integral para a precisão escolhida é de: ", integral)

    elif escolha ==4:
        def funcao1 (x):
            f1 = cos(sin(x))
            return f1
        print("\n   Escolha uma das opções:")
        print("   1. Integrar usando o intervalo padrão: a = 0, b = pi")
        print("   2. Integrar usando outro intervalo")
        escolha2 = int(input())
        if escolha2 == 1:
            a = 0
            b = pi
        else:
            print("\n   Defina os intervalos da integração:")
            a = float(input("   Digite o valor de a:"))
            b = float(input("   Digite o valor de b:"))
        integral =((1/pi)* romb(a, b, n, eps, itmax))
        print("   O valor da integral para a precisão escolhida é de: ", integral)

    elif escolha ==5:
        print("\n   Escolha uma das opções:")
        print("   1. Integrar usando a função padrão")
        print("   2. Integrar usando a função após a troca de variável x=y^2")
        escolha2 = int(input())
        if escolha2 == 1:
            def funcao1 (x):
                f1 = sqrt(x)*cos(x)
                return f1
            print("\n   Escolha uma das opções:")
            print("   1. Integrar usando o intervalo padrão: a = 0, b = pi/2")
            print("   2. Integrar usando outro intervalo")
            escolha3 = int(input())
            if escolha3 == 1:
                a = 0
                b = pi/2
            else:
                print("\n   Defina os intervalos da integração:")
                a = float(input("   Digite o valor de a:"))
                b = float(input("   Digite o valor de b:"))
            
        else:
            def funcao1 (x):
                f1 = 2*(x**2)*cos((x**2)) ##função após a mudança de variável x=y^2
                return f1
            print("\n   Escolha uma das opções:")
            print("   1. Integrar usando o intervalo padrão: a = 0, b = sqrt(pi/2)")
            print("   2. Integrar usando outro intervalo")
            escolha2 = int(input())
            if escolha3 == 1:
                a = 0
                b = sqrt(pi/2)
            else:
                print("\n   Defina os intervalos da integração:")
                a = float(input("   Digite o valor de a:"))
                b = float(input("   Digite o valor de b:"))
        integral = romb(a, b, n, eps, itmax)
        print("   O valor da integral para a precisão escolhida é de: ", integral)

    elif escolha ==6:
        def funcao1 (x):            
            f1 = sqrt(((1.5*cos(x))**2)+(sin(x)**2))            
            return f1
        a=0
        b=2*pi
        integral = romb(a, b, n, eps, itmax)
        print("   O Perímetro da Elipse em questão é: ", integral)
  
    elif escolha==7:
        break

    



                
            
        


