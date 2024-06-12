def lista_primos(n):
    lista_numeros = list(range(2, n+1))
    lista_primos = []
  
    while len(lista_numeros) > 0:
        p = lista_numeros[0]
        lista_primos.append(p)
        lista_numeros = [x for x in lista_numeros if x % p != 0]
  
    return lista_primos

# Testando a função
print(lista_primos(100))

