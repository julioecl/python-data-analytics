curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso) 
# True pois tem o mesmo valor 
# ocupam a mesma região de memória

print( saldo is limite) 
# True pois tem o mesmo valor 
# ocupam a mesma região de memória

saldo += 15

print( saldo is limite) 
# False pois não tem o mesmo valor
# Não ocupam a mesma região de memória