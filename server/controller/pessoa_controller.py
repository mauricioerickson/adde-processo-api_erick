
from server.converter.conversor import Conversor
from server.model.pessoa import PessoaSchema
from server.service.pessoa_service import PessoaService


# /pessoas
def get_todas_pessoas():
    service = PessoaService()
    pessoas = service.busca_pessoa()
    return Conversor.converter_para_json(PessoaSchema, pessoas), 200


def post_criar_pessoa(body):
    pessoa = Conversor.converter_para_objeto(PessoaSchema, body)

    service = PessoaService()
    pessoa = service.inserir_pessoa(pessoa)
    return Conversor.converter_para_json(PessoaSchema, pessoa), 200


# /pessoas/{guid}
def get_pessoa_por_guid(guid):
    service = PessoaService()
    pessoa = service.busca_pessoa(guid)
    return Conversor.converter_para_json(PessoaSchema, pessoa), 200


def put_atualizar_pessoa(pessoa_guid, body):
    pessoa = Conversor.converter_para_objeto(PessoaSchema, body)

    service = PessoaService()
    pessoa = service.atualizar_pessoa(pessoa_guid, pessoa)
    return Conversor.converter_para_json(PessoaSchema, pessoa), 200


def delete_pessoa(pessoa_guid):
    service = PessoaService()
    service.excluir_pessoa(pessoa_guid)
    return "Ok", 200
