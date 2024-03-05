# OLD
nome = "Julio"
idade = 34
cidade = "Indaial"

print("Olá, meu nome é %s. Tenho %d anos de idade e moro em %s." % (nome, idade, cidade))

# FORMAT

nome = "Alexandre"
idade = 39
cidade = "Timbó"

print("Olá, meu nome é {}. Tenho {} anos de idade e moro em {}.".format(nome, idade, cidade))

print("Olá, meu nome é {0}. Tenho {1} anos de idade e moro em {2}.".format(nome, idade, cidade))

print("Olá, meu nome é {nome}. Tenho {idade} anos de idade e moro em {cidade}.".format(nome="João", idade=25, cidade="Blumenau"))

# Formated String

print(f'Olá, meu nome é {nome}. Tenho {idade} anos de idade e moro em {cidade}.')

numero = 3.15658456
print(f'Valor de numero: {numero:.2f}') # 2 casa decimais