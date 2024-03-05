preco = 10
print(preco/2) # retorno float
print(preco//2) # retorno inteiro
print(preco, type(preco)) # int
preco = str(preco)
print(preco, type(preco)) # string

idade = "25"
print(idade, type(idade))  # str
idade = int(idade) 
print(idade, type(idade)) # int

valor = 10.5
print(valor, type(valor)) #float
valor = int(valor)
print(valor, type(valor)) # int (perda de dados)
valor = float(valor)
print(valor, type(valor))