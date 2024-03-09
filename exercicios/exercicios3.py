##############################################################################################
##                                     1 / 3                                                ##
##############################################################################################

# def classificar_numero(numero):
#   if numero > 0:
#     return True
#   else:
#     return False
    
# def main():
  
#   positivos = 0
#   negativos = 0
    
#   while True:
#     numero = int(input())
    
#     if numero == 0:
#       break  # Encerra o loop se o usuário digitar 0.
    
#     # Chama a função classificar_numero para imprimir a classificação do número
#     resultado = classificar_numero(numero)
    
#     # TODO: Faça a verificação para saber quantos números positivos e negativos foram inseridos
#     if resultado == True:
#       positivos += 1
#       print("positivo!")
#     else:
#       negativos += 1
#       print("negativo!")
  
#   # Imprime a quantidade de números positivos e negativos inseridos
#   print(f"{positivos} números positivos, {negativos} números negativos")

# if __name__ == "__main__":
#   main()

##############################################################################################
##                                     2 / 3                                                ##
##############################################################################################

def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
# TODO: Desenvolva a Função para prever a classe da fruta
    if peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    if peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    if peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é um morango!"
    else:
        return "Não foi possível classificar a fruta."
        

# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)


##############################################################################################
##                                     3 / 3                                                ##
##############################################################################################

# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"

    # Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    if intensidade >= 7 and componente_raro_feitico == "sim" and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais_feiticeiro == "não":
        return "A afinidade elemental do feiticeiro é com o elemento Água!"
    if intensidade >= 7 and componente_raro_feitico == "sim" and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais_feiticeiro == "sim":
        return "A afinidade elemental do feiticeiro é com o elemento Terra!"
    else:
        return "A afinidade elemental do feiticeiro é com o elemento Ar!"
        

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)