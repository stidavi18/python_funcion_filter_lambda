#se usa la funcion rango para crear la lista entre 1 y 100
lista_numeros=list(range(1,101))

def es_un_numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5)+1):
        if numero % i==0:
            return False
    return True
#comprueba si se puede dividir por cualquier numero entre 2 y su raiz cuadrada, si no es divisible por ninguno el numero es primo
#obtiene el numero y validad True si es primo o false si no lo es

numeros_primos = list(filter(es_un_numero_primo,lista_numeros))

print(numeros_primos)


