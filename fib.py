# Ejercicio 1 de la tarea 1 de matematicas 4
def fib_recursivo(k):
    '''
    Regresa el numero Fk(el k-esimo numero de Fibonacci)
    k: el numero de Fibonacci que queremos que nos regrese el programa
    returns: el k-esimo numero de Fibonacci
    '''
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib_recursivo(k - 1) + fib_recursivo(k - 2)

def lucas_recursivo(k):
    '''
    Regresa el numero Lk(el k-esimo numero de Lucas)
    k: el numero de Lucas que queremos que nos regrese el programa
    returns: el k-esimo numero de Lucas
    '''
    if k == 0:
        return 2
    if k == 1:
        return 1
    return lucas_recursivo(k - 1) + lucas_recursivo(k - 2)
 
def fib_rapido(k):
    '''
    Regresa el numero Fk(el k-esimo numero de Fibonacci)
    k: el numero de Fibonacci que queremos que nos regrese el programa
    returns: el k-esimo numero de Fibonacci
    '''
    return pow(0.2, 0.5) * (pow(((1 + pow(5, 0.5))/2), k) - pow(((1 - pow(5, 0.5)) / 2), k))


print("Fibonacci recursivo")
for i in range(26):
    print("Fib" + str(i) + " = " + str(fib_recursivo(i)))

print("Lucas recursivo")
for i in range(26):
    print("Luc" + str(i) + " = " + str(lucas_recursivo(i)))

print("Fibonacci rapido")
for i in range(26):
    print("Fib" + str(i) + " = " + str(fib_rapido(i)))
