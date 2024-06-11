from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Cliente, Conta

engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

# Recuperando dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}, Email: {cliente.email}")
    for conta in cliente.contas:
        print(f"Conta Número: {conta.numero}, Saldo: {conta.saldo}")

session.close()
