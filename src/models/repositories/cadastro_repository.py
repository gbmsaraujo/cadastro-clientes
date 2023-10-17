from src.models.configs.connection import DBConnectionHandler
from src.models.entities.pessoas import PessoaEntity
from src.models.repositories.interface.Icadastro_repo import ICadastroRepo
from src.models.types.cadastro_type import CadastroType


class CadastroRepository(ICadastroRepo):
    def get_clients(self):
        with DBConnectionHandler() as db:
            data = db.session.query(PessoaEntity).all()
            pessoas = [pessoa.__dict__ for pessoa in data] if data else None
            return pessoas

    def insert_client(self, info_client):
        with DBConnectionHandler() as db:
            pessoa = PessoaEntity(
                nome=info_client["nome"].lower(),
                idade=int(info_client["idade"]),
                bairro=info_client["bairro"].lower(),
                profissao=info_client["profissao"].lower(),
            )
            db.session.add(pessoa)
            db.session.commit()
            return True

    def search_client_by_name(self, name):
        with DBConnectionHandler() as db:
            pessoa = (
                db.session.query(PessoaEntity)
                .filter_by(nome = name.lower())
                .first()
            )

            return pessoa if pessoa else None

    def delete_client_by_name(self, name):
        with DBConnectionHandler() as db:
            pessoa = (
                db.session.query(PessoaEntity)
                .filter_by(nome = name.lower())
                .first()
            )

            if not pessoa:
                return

            db.session.delete(pessoa)
            db.session.commit()
            return True

    def update_info_person(self, info_client: CadastroType):
        with DBConnectionHandler() as db:
            pessoa_db = self.search_client_by_name(info_client['nome'])

            print(pessoa_db.__dict__)
            print(info_client)

            if not pessoa_db:
                return
            
            pessoa_db.nome = info_client['nome']
            pessoa_db.idade = info_client["idade"]
            pessoa_db.profissao = info_client["profissao"].lower()
            pessoa_db.bairro = info_client["bairro"].lower()
            db.session.commit()
            return True
