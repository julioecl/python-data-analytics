def exibir_msg(nome):
    print(f"Bem vindo {nome}!")
    
exibir_msg("Julio") # Bem vindo Julio!

# Retornar valor

def somar(numeros):
    return sum(numeros)

retorno_soma = somar([10,15,34])
print(retorno_soma) # 59

# Argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    print(f"Veículo inserido com sucesso! {marca} | {modelo} | {ano} | {placa}")
    
salvar_carro("GM", "Celta", "2015", "CEL-7400")
# Veículo inserido com sucesso! GM | Celta | 2015 | CEL-7400

salvar_carro(marca="Ferrari", modelo="F50", ano="2007", placa="FER-5451")
# Veículo inserido com sucesso! Ferrari | F50 | 2007 | FER-5451

# ARGS (*args) recebe tupla
# KWARGS (**kwargs) recebe dicionário

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mesagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mesagem)
    
exibir_poema("Tuesday February 27, 2024" , "Zen of Python", "Beautiful is better than ugly", autor="Tim Peters", ano=1999)

# AO passar vários argumentos, caso seja obrigatório passar
# posicional sem ser nomeado, utilizamos o /, ou seja os args
# que estiverem antes da /, serão obrigatórios posicionais.
# Caso seja obrigatório nomeado, virão antes do *.

# exibir_poema(data_extenso, / , texto_1, * ) exemplo.

