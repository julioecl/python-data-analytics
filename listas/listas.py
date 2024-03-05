frutas = ['Laranja', 'Maçã', 'Limão']

letras = list('julio')
print(letras)

numeros = list(range(10))
print(numeros)

# Acesso direto
print(frutas[1])
# Índice negativo
print(frutas[-1]) #último elemento

# Matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [3, 6, 9]
]
print(matriz[0]) # linha inteira [1, 2, 3]
print(matriz[0][0]) # elemento específico 1

# Fatiamento | igual a string
print(frutas[::-1]) 

# Percorrer a lista com for
for fruta in frutas:
    print(fruta)

# Enumerate
for i, fruta in enumerate(frutas):
    print(f'{i}: {fruta}') 
    
