def fatorial(i):
     if i == 0 or i == 1:
         return 1
     else:
         return i * fatorial(i-1)

def combinacao(n1, x1):
    comb=fatorial(n1)/(fatorial(x1)*fatorial(n1-x1))
    return comb;

def calculaFormula(p, n, x, q):
    comb_result=combinacao(n,x)
    PX=comb_result*(p**x)*(q**(n-x))
    return PX;



P=float(input("Informe o valor relativo de p (probabilidade de sucesso)= "))
N=float(input("Informe o valor de N (tamanho da amostra)= "))
X=int(input("Informe o valor de X (número de sucessos) =  "))
P = P/100
Q = 1-P


PBI = calculaFormula(P, N, X, Q)
PBIp=PBI*100

PBA=0
for i in range(X+1):
    PB = calculaFormula(P, N, i, Q)
    PBA=PBA+PB

PBAp=PBA*100

    

print('\nValores utilizados na fórmula: ')
print(f"p = {P}\nn = {N}\nx = {X}\n")
print(f"A probabilidade binomial individual: ")
print(f"P(x={X}) = {round(PBIp, 2)}%")
print('')
print(f"A probabilidade binomial acumulada: ")
print(f"P(x<={X}) {round(PBAp, 2)}%")
print('')