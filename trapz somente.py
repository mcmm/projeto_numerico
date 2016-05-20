from math import*
def funcao1 (x):
    f1 = (x**4)*log(x+sqrt(x**2+1),e)
    return f1

        
def trapz(a, b, t, i):
    hi = (b-a)/(2**i)
    somatoria = 0
    for j in range (1, (2**(i-1))+1):
        f1 = funcao1(a+(2*j - 1)*hi)
        somatoria += f1
    t = t/2 + (hi)*somatoria
    return t

loop = 0
a = 0
b = 2
h = (b-a)    
t = h*(funcao1(a)+funcao1(b))/2
i = 1
iteracoes = 1

while loop == 0:
    t_aux = t
    t = trapz(a, b, t, i)
    i += 1    
    if (abs(t_aux - t) <= 0.000001*t):
        break
    iteracoes +=1

print("Valor integral:", t)
print("Iteracoes:", iteracoes)
    
    
