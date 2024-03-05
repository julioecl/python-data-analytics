lista = [ 20, 30, 50]

# adicionar elemento após o último elemento
lista.append(15)
# copiar a lista
lista_copy = lista.copy()

# adicionar lista a uma lista
linguagens = ["python", "ruby"]

linguagens.extend(["c", "js", "Java"])

print(linguagens) # ['python', 'ruby', 'c', 'js', 'Java']

# pop() retira o último elemento ou qual for indicado nos parenteses
retirado = linguagens.pop()

print(retirado) # Java
print(linguagens) # ['python', 'ruby', 'c', 'js']

retirado = linguagens.pop(2)

print(retirado) # c
print(linguagens) # ['python', 'ruby', 'js']

# remove() retira o elemento que for passado de parametro
linguagens.remove('js')
print(linguagens) # ['python', 'ruby']

# reverse() retorna ao contrário
linguagens.reverse() 
print(linguagens) # ['ruby', 'python']

# sort() ordena a lista 
linguagens.sort()
print(linguagens) # ['python', 'ruby']

# len() tamanho da lista
print(len(linguagens)) # 2