MAIOR_IDADE = 18
IDADE_ESPECIAL = 60
idade = 17

# if / else
def verifica_idade():
    idade = int(input("Digite sua idade: "))
    if idade >= MAIOR_IDADE:
        print("Você é apto para tirar sua habilitação!")
    else:
        print("Você não ainda não pode tirar sua habilitação!")


verifica_idade()