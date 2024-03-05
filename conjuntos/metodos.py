# Métodos

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 2, 1}
conjunto_c = {0, 7}

# ADD

conjunto_c.add(9)
print(conjunto_c) # {0, 9, 7}

# CLEAR

conjunto_c.clear()
print(conjunto_c) # {}

# COPY

conjunto_d = conjunto_b.copy()
print(conjunto_d) # {3, 4, 2, 1}

# DISCARD

conjunto_d.discard(2)
print(conjunto_d) # {1, 3, 4}

# POP -> Retira do início para o final, ao contrário das listas.

conjunto_d.pop() 
print(conjunto_d) # {3, 4}

# REMOVE -> semelhante ao DISCARD, mas caso não tenha o 
# valor solicitado, é lançado um erro: KeyError: 2

# conjunto_d.remove(2)
# print(conjunto_d) # KeyError: 2

conjunto_d.remove(3)
print(conjunto_d) # {4}

# LEN

print(len(conjunto_b)) # 4

# IN está contido

print(1 in conjunto_b) #True