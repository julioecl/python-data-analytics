frutas = ['Laranja', 'Maçã', 'Limão']
upper_frutas = []

for fruta in frutas:
    upper_frutas.append(fruta.upper())

print(upper_frutas) # ['LARANJA', 'MAÇÃ', 'LIMÃO']

lower_frutas = [fruta.lower() for fruta in frutas]
#               retorno        for 

print(lower_frutas) # ['laranja', 'maçã', 'limão']

numeros = [1, 5, 7, 15, 6, 25, 50, 510, 513]
divisivel_5 = [numero for numero in numeros if numero % 5 == 0]
#               retorno        for            condição
print(divisivel_5) # [5, 15, 25, 50, 510]

elevar_2 = [numero**2 for numero in numeros]
print(elevar_2) # [1, 25, 49, 225, 36, 625, 2500, 260100, 263169]