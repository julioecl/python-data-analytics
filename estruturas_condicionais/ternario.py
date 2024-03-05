# ternário True or False

saque = 400
limite = 300

def realiza_saque():
    if saque < limite:
        return True
    else:
        return False

if realiza_saque():
    print("Saque realizado!")
else:
    print("Saque não realizado!")