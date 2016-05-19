import math 

def funcao1 (x):
    f1 = x
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
    t = 0
    inicio =0 
    iteracoes = 0
    while (iteracoes <= itmax):    
        for i in range (inicio, n+1):
            T_aux = []
            for k in range (0, i+1):
                if k==0:
                    print("i:", i)
                    t = trapz(a,b,t,i)
                    print("t:", t)
                    T_aux.append(t)
                else:
                    Tik = (T_aux[k-1] + (T_aux[k-1] - T[i-1][k-1])/((4**k)-1))
                    T_aux.append(Tik)
        if (abs(T[n][n]-T[n][n-1] <= eps*T[n][n])):
            break
        else:
            inicio += 1
        iteracoes += 1
    integral = T[n][n]
    return integral


integral = romb(0, 2, 4, 0.000001, 100)
print(integral)
                
            
        

    

teste = trapz(3,10,0,10)
print(teste)
    
