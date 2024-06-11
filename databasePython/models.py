from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    numero = Column(String, unique=True)
    saldo = Column(Float)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="contas")
