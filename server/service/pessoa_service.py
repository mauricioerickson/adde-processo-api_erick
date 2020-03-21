import uuid

from server.repository.pessoa_repository import PessoaRepository


class PessoaService:

    def __init__(self):
        self._repository = PessoaRepository()

    def busca_pessoa(self, guid=None):
        if guid is None:
            pessoa = self._repository.busca_todas_pessoas()
        else:
            pessoa = self._repository.busca_pessoa_por_guid(guid)

        return pessoa

    def inserir_pessoa(self, pessoa):
        try:
            pessoa.guid = str(uuid.uuid4())
            self._repository.gravar_pessoa(pessoa)
            return pessoa
        except Exception as e:
            print(e)

        return None

    def atualizar_pessoa(self, guid, pessoa):
        pessoa_db = self._repository.busca_pessoa_por_guid(guid)
        if pessoa_db is None:
            raise Exception(f'Pessoa com guid {guid} nao encontrada')

        try:
            pessoa_db.nome = pessoa.nome
            pessoa_db.documento = pessoa.documento
            self._repository.gravar_pessoa(pessoa_db)
            return pessoa_db
        except Exception as e:
            print(e)

        return None

    def excluir_pessoa(self, guid):
        pessoa_db = self._repository.busca_pessoa_por_guid(guid)
        if pessoa_db is None:
            raise Exception(f'Pessoa com guid {guid} nao encontrada')

        try:
            self._repository.excluir_pessoa(pessoa_db)
            return True
        except Exception as e:
            print(e)

        return False
