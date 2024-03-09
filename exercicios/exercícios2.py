##############################################################################################
##                                     1 / 3                                                ##
##############################################################################################

valor = float(input())

if valor > 0:
  print('Deposito realizado com sucesso!')
  print(f'Saldo atual: R$ {valor:.2f}')
elif valor < 0:
  print('Valor invalido! Digite um valor maior que zero.')
else:
  print('Encerrando o programa...')

##############################################################################################
##                                     2 / 3                                                ##
##############################################################################################
  
ativos = []
quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

ativos.sort()
 
print(ativos[0])
print(ativos[1])
print(ativos[2])

##############################################################################################
##                                     3 / 3                                                ##
##############################################################################################

senha = "010203jupiter*"
# senha = "010203Jupiter"

comprimento_minimo = 8
tem_letra_maiuscula = False
tem_letra_minuscula = False
tem_numero = False
tem_caractere_especial = False

if len(senha) < comprimento_minimo:
  print(f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres.")  

for i in range(len(senha)):
  if (senha[i].islower()):
    tem_letra_minuscula = True
  if (senha[i].isupper()):
    tem_letra_maiuscula = True
  if (not senha[i].isalnum()):
    tem_caractere_especial = True
  if (senha[i].isnumeric()):
    tem_numero = True 
    
# Verificando se a senha contém sequências comuns
sequencias_comuns = ["123456", "abcdef"]
for sequencia in sequencias_comuns:
  if sequencia in senha:
    print("Sua senha contem uma sequencia comum. Tente uma senha mais complexa.")

# Verificando se a senha contém palavras comuns
palavras_comuns = ["password", "123456", "qwerty"]
if senha in palavras_comuns:
  print("Sua senha e muito comum. Tente uma senha mais complexa.")


if comprimento_minimo >=8: # essa linha não é necessária na função do exercício, pois caso seja menor, já tem o return na hora de verificar o comprimento.
  if tem_letra_maiuscula:
    print(tem_letra_maiuscula, "Letra maiuscula")
    if tem_letra_minuscula:
      print(tem_letra_minuscula, "Letra minuscula")
      if tem_numero:
        print(tem_numero, "tem_numero")
        if tem_caractere_especial:
          print(tem_caractere_especial, "tem_caractere_especial")
          print("Sua senha atende aos requisitos de seguranca. Parabens!")
        else:
          print("Sua senha nao atende aos requisitos de seguranca.")
      else:
        print("Sua senha nao atende aos requisitos de seguranca.")    
    else:
      print("Sua senha nao atende aos requisitos de seguranca.")
  else:
    print("Sua senha nao atende aos requisitos de seguranca.")