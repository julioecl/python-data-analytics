MAIOR_IDADE = 18
IDADE_ESPECIAL = 60
idade = 17

# if / elif / else

def verifica_habilitacao():
    idade = int(input("Digite sua idade: "))    
    if idade >= IDADE_ESPECIAL:
        print("Você é apto para tirar sua habilitação, mas precisa renovar dentro de 5 anos!")
    elif idade >= MAIOR_IDADE:
        print("Você é apto para tirar sua habilitação!")
    else:
        print("Você não ainda não pode tirar sua habilitação!")

verifica_habilitacao()