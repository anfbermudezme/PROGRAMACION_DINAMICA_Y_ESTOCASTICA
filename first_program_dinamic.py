#Ejemplo de problema optimizado

import sys

def fibonacci_dinamico(n, memo = {}):
    if n==0 or n==1:
        return 1 
    try:
        return memo[n]
    except KeyError: 
        sys.setrecursionlimit(1000000002)
        r =  fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo) 
        memo[n]= r

        return r          

if __name__ == '__main__':
    n = int(input('Escribe tu n: '))
    r = fibonacci_dinamico(n)
    print(r)  