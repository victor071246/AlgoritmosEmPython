def buscaMenor(arr):
    menor = arr[0] 
    menor_indice = 0 
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
        return menor_indice

