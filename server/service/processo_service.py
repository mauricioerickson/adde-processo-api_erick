import uuid
from server.repository.processo_repository import ProcessoRepository

class ProcessoService:

    def __init__(self):
        self._repository = ProcessoRepository()

    def busca_processo(self, guid=None):
        if guid is None:
            processo = self._repository.busca_todos_processos()
        else:
            processo = self._repository.buscar_processo_guid(guid)

        return processo

    def inserir_processo(self, processo):
        try:
            processo.guid = str(uuid.uuid4())
            self._repository.gravar_processo(processo)
            return processo
        except Exception as e:
            print(e)

        return None

    def atualizar_processo(self, guid, processo):
        processo_db = self._repository.buscar_processo_guid(guid)

        if processo_db is None:
            raise Exception(f'Processo com guid {guid} não encontrado')

        try:
            processo_db.numero = processo.numero
            processo_db.data = processo.data
            processo_db.valor = processo.valor
            self._repository.gravar_processo(processo_db)
            return processo_db
        except Exception as e:
            print(e)

        return None

    def excluir_processo(self, guid):
        processo_db = self._repository.buscar_processo_guid(guid)
        if processo_db is None:
            raise Exception(f'Processo com guid {guid} nao encontrado')

        try:
            self._repository.excluir_processo(processo_db)
            return True
        except Exception as e:
            print(e)

        return False
