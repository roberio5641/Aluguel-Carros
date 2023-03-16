carros = {
    "Honda-fit" : 1000,
    "Suzuki-Vitara" : 1500,
    "Mini-cooper" : 800
}

alugueis = {}

users = {
    "astrogildo500" : "senhafraca",
    "asclepiades_braz" : "senhamuitofraca"
}

def carstorent(carros):
    print("Lista de carros e seus preços de aluguel abaixo:")
    keys = carros.keys()
    for k in keys:
        print(k + " " + str(carros[k]))
    c = input("Qual carro você quer alugar? ")
    if c in keys:
        print("Carro Alugado")
    else:
        print("Carro não disponível. Escolha outro...")

def login(users):
    user = input("Qual é o seu endereço de e-mail? ")
    senha = input("Qual é a sua senha? ")
    try:
        if users[user] == senha:
            print("Acesso permitido")
            carstorent(carros)
        else:
            print("Acesso bloqueado. Usuário inexistente ou nome de usuário e senha não correspondem...")
    except KeyError:
        print("Acesso bloqueado. Usuário inexistente ou nome de usuário e senha não correspondem...")

def check_integrity(carros):
    keys = list(carros.keys())
    for x in keys:
        if carros[x] > 0:
             print("Não há valores negativos no dicionário.")
             return True
        else:
             print("O dicionário contém valores negativos:", carros[x])
        return False

check_integrity(carros)

login(users)