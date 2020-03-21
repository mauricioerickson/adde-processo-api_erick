from server import db
from server.model.pessoa import Pessoa


class PessoaRepository:

    def __init__(self):
        self._session = db.session

    def busca_todas_pessoas(self):
        return self._session.query(Pessoa).all()

    def busca_pessoa_por_guid(self, guid):
        return self._session.query(Pessoa).filter(Pessoa.guid == guid).first()

    def gravar_pessoa(self, pessoa):
        try:
            self._session.add(pessoa)
            self._session.commit()
        except Exception as e:
            print(e)
            self._session.rollback()

    def excluir_pessoa(self, pessoa):
        try:
            self._session.delete(pessoa)
            self._session.commit()
        except Exception as e:
            print(e)
            self._session.rollback()


