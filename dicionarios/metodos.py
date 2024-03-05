pessoa = {
    "nome": "Julio",
    "idade": 34
}

# COPY 

pessoa_copia = pessoa.copy()
print(pessoa_copia)
# {'nome': 'Julio', 'idade': 34}

# CLEAR

pessoa_copia.clear()
print(pessoa_copia) # {}

# FROMKEYS - Adiciona novas chaves, com ou sem valores.

pessoa_copia.fromkeys(["name", "age"])
print(pessoa_copia)

# GET - buscar chave

print(pessoa.get("nome")) # Julio
print(pessoa.get("telefone", "Não encontrado")) # Não encontrado

# ITEMS - Retorna tupla de chave e valor

print(pessoa.items()) 
# dict_items([('nome', 'Julio'), ('idade', 34)])

# KEYS - retorna só as chaves dict.keys()
# VALUES - retorna só os valores dict.values()

# POP - Retira e retorna esse valor

retirado = pessoa.pop("idade")
print(retirado)
retirado_endereco = pessoa.pop("endereço", "Não encontrado")
print(retirado_endereco)

# SETDEFAULT - Caso não  tenha no dicionário, adiciona com o
# valor setado.

pessoa.setdefault("nome", "Giovanna")
print(pessoa) # {'nome': 'Julio'}
pessoa.setdefault("idade", 34)
print(pessoa) # {'nome': 'Julio', 'idade': 34}

# UPDATE 

pessoa.update({"nome": "Giovanna"}) 
print(pessoa) # {'nome': 'Giovanna', 'idade': 34}
pessoa.update({"telefone": "2555-1223"})
print(pessoa) 
# {'nome': 'Giovanna', 'idade': 34, 'telefone': '2555-1223'}

# IN - verifica se existe ou não no dicionário

resultado = "nome" in pessoa
print(resultado) # True

# DEL 

del(pessoa["nome"])

print(pessoa)