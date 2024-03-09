n = int(input())
lines = []

# Coletar as transações
for _ in range(n):
    lines.append(input())

# Separar cada linha em transações individuais e adicionar à lista de transações
transactions = []

for transaction_input in lines:
    parts = transaction_input.split(',')
    transaction = (parts[0], int(parts[1]), int(parts[2]))
    transactions.append(transaction)

# Definir uma função para detectar transações fraudulentas
def detect_frauds(transactions):
    suspicious_transactions = []

    # Iterar sobre cada transação
    for transaction in transactions:
        # Desempacotar a transação em seus componentes: id, valor, e limite de fraude
        transaction_id, value, fraud_threshold = transaction
        # Verificar se o valor da transação excede o limite de fraude
        if value > fraud_threshold:
            suspicious_transactions.append(transaction_id)

    return '\n'.join(suspicious_transactions)

# Imprimir a lista de transações suspeitas
print(detect_frauds(transactions))
