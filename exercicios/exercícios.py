#Desafios de Código SQUADIO - Iniciante

# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

if quantidade_passos > 0:
  for passo in range(quantidade_passos):
    if passo == 0:
      print(f"Explorador: {passo+1} passo")
    else:
      print(f"Explorador: {passo+1} passos")
else:
  print("Nenhum passo dado na floresta.")
  

# Lista para armazenar os itens

itens = []

for item in range(3):
  item = input()
  itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")

# Armazenamento de Dados é Vida!
  
capacidade_atual, aumento_percentual = map(int, input().split())
resultado = capacidade_atual * (1 + (aumento_percentual/100))

print(f'{resultado:.0f}')