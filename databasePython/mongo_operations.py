from pymongo import MongoClient

# Substitua <username>, <password> e <cluster-url> pelas suas credenciais e URL do MongoDB
client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority")
db = client.bank

# Inserindo dados
cliente_data = {
    "nome": "João Silva",
    "email": "joao.silva@example.com",
    "contas": [
        {
            "numero": "1234-5",
            "saldo": 1000.0
        }
    ]
}

db.clientes.insert_one(cliente_data)

# Recuperando dados
clientes = db.clientes.find()
for cliente in clientes:
    print(f"Cliente: {cliente['nome']}, Email: {cliente['email']}")
    for conta in cliente['contas']:
        print(f"Conta Número: {conta['numero']}, Saldo: {conta['saldo']}")
