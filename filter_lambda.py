lista_numeros=list(range(1,101))

op_primos = lambda x: all(x % i !=0 

for i in range(2, int(x ** 0.5)+1))and x >1

numeros_primos=list(filter(op_primos, lista_numeros))

print(numeros_primos)