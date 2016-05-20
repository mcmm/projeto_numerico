from math import*


def funcao1 (x):
    f1 = sqrt(x)*cos(x)
    return f1
    
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
    print("T2:", T)
        

        
    while (iteracoes <= itmax):
        iteracoes += 1
        if (abs(T[n][n]-T[n][n-1]) <= eps*T[n][n]):
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
    print("itmax:", itmax)   
    integral = T[n][n]
    print("eps:", eps*T[n][n])
    print("diferença:", abs(T[n][n]-T[n][n-1]))
    print("iteracoes:", iteracoes-1)

    return integral


integral = romb(0, pi/2, 4, 0.000001, 10)
print(integral)
                
            
        


