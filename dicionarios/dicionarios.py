# Chave e valor

pessoa = {
    "nome": "Julio",
    "idade": 34
}

pessoa["telefone"] = "1230-2221"

print(pessoa) 
# {'nome': 'Julio', 'idade': 34, 'telefone': '1230-2221'}

# Acessar o registro

print(pessoa["nome"]) # Julio

# Substituir valores

pessoa["telefone"] = "1230-5555"

print(pessoa) 
# {'nome': 'Julio', 'idade': 34, 'telefone': '1230-5555'}