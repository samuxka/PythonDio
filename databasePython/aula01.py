import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect

base = declarative_base()

class User(base):
    __tablename__ = "user_account"
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullName = Column(String)
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullName={self.fullName})"
    
class Address(base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    emailAddress = Column(String(50), nullable=False)
    userId = Column(Integer, ForeignKey("user_account.id"))
    user = relationship("User", back_populates="address")
    def __repr__(self):
        return f"Address(id={self.id}, email={self.emailAddress})"
    
    
print(User.__tablename__)
print(Address.__tablename__)

# CONECTAR AO BANCO DE DADOS

engine = create_engine("sqlite://")

base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user"))
