from server import db
from server.model.processo import Processo

class ProcessoRepository:

    def __init__(self):
        self._session = db.session

    def busca_todos_processos(self):
        return self._session.query(Processo).all()

    def buscar_processo_guid(self, guid):
        return self._session.query(Processo).filter(Processo.guid == guid).first()

    def gravar_processo(self, processo):
        try:
            self._session.add(processo)
            self._session.commit()

        except Exception as e:
            print(e)
            self._session.rollback()

    def excluir_processo(self, processo):
        try:
            self._session.delete(processo)
            self._session.commit()
        except Exception as e:
            print(e)
            self._rollback()
