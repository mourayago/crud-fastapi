from typing import Optional
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)
print("Conexão com SQLite estabelecida.")


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))
    


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # Estabelece a relação entre Produto e Fornecedor
    fornecedor = relationship("Fornecedor")


Session = sessionmaker(bind=engine)

with Session() as session:
    Base.metadata.create_all(engine)

    fornecedores = [
        Fornecedor(nome="Fornecedor A", telefone="12345678", email="contato@a.com", endereco="Endereço A"),
        Fornecedor(nome="Fornecedor B", telefone="87654321", email="contato@b.com", endereco="Endereço B"),
        Fornecedor(nome="Fornecedor C", telefone="12348765", email="contato@c.com", endereco="Endereço C"),
        Fornecedor(nome="Fornecedor D", telefone="56781234", email="contato@d.com", endereco="Endereço D"),
        Fornecedor(nome="Fornecedor E", telefone="43217865", email="contato@e.com", endereco="Endereço E")
    ]

    produtos = [
    Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
    Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
    Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2)
    ]
    session.add_all(produtos)
    session.add_all(fornecedores)
    session.commit()