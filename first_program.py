#Ejemplo de problema sin optimizar

def fibonacci_recursivo(n):
    if n==0 or n==1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) 

if __name__ == '__main__':
    n = int(input('Escribe tu n: '))
    r = fibonacci_recursivo(n)
    print(r)       


 # Programación dinámica 

 # Subestructura optima: Una solución global óptima se puede encontrar al combinar soluciones óptimas
 # de subproblemas locales. 
 
 # Problemas empalmados: Resolver el mismo problema varias veces optimamente. 

 # MEMORIZATION: Técnica para guardar computos previos y evitar realizarlos nuevamente.
 # Intercambia tiempo por espacio 