nome = "Julio"

for letra in nome:
    print(letra)

texto = "Lorem Ipsum is simply dummy text of the printing"
vogais = "AEIOU"

for letra in texto:    
    if letra.upper() in vogais:
        print(letra, end=" ")
    
print()
        
for numero in range(10):
    print(numero, end=" ")