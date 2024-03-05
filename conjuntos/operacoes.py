# operações com conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 2}

# UNION

print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 4}

# INTERSECTION

print(conjunto_a.intersection(conjunto_b)) # {2, 3}

# DIFFERENCE

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}
print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

# ISSUBSET - subconjunto

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 2, 1}
conjunto_c = {0, 7}

print(conjunto_a.issubset(conjunto_b)) # True
print(conjunto_b.issubset(conjunto_a)) # False

# ISSUPERSET - contém o subconjunto

print(conjunto_a.issuperset(conjunto_b)) # False 
print(conjunto_b.issuperset(conjunto_a)) # True

# ISDISJOINT - não contem elementos

print(conjunto_c.isdisjoint(conjunto_b)) # True
print(conjunto_b.isdisjoint(conjunto_a)) # False 