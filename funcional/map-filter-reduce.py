from functools import reduce

numeros = [1,2,3,4,5,6,7,8,10]

# map, filter, reduce

numeros_pares = list(filter(lambda x : x % 2 == 0, numeros))

numeros_pares_dobrados = list(map(lambda x: x * 2, numeros_pares))

soma_numeros_pares_dobrados = reduce(lambda x, y: x + y, numeros_pares_dobrados)

print(soma_numeros_pares_dobrados)


# teste = reduce(lambda x, y: x + y, list(map(lambda x: x * 2, list(filter(lambda x : x % 2 == 0, numeros)))))

# print(teste)