# operador E (and)
a = 3
b = 4
c = 5
d = 6

# True, ambas precisam ser verdadeiras
print(a < b and c < d) 

# operador OU (or)
# True, uma das duas precisa ser verdadeira para ser verdadeira
print(b > c or c > a)

# operador negação (not)
print(not ((a < b and c < d))) # not True = False
print(not ((a > b or c > d))) # not False = True