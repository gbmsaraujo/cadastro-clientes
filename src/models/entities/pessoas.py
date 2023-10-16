from src.models.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class PessoaEntity(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    bairro = Column(String(200), nullable=False)
    profissao = Column(String(200), nullable=False)
