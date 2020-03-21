
from server.converter.conversor import Conversor
from server.model.processo import ProcessoSchema
from server.service.processo_service import ProcessoService

# /processos
def get_todos_processos():
    service = ProcessoService()
    processos = service.busca_processo()
    return Conversor.converter_para_json(ProcessoSchema, processos), 200


def post_criar_processo(body):
    processo = Conversor.converter_para_objeto(ProcessoSchema, body)

    service = ProcessoService()
    processo = service.inserir_processo(processo)
    return Conversor.converter_para_json(ProcessoSchema, processo), 200


# /processos/{guid}
def get_processo_por_guid(processo_guid):
    service = ProcessoService()
    processo = service.busca_processo(processo_guid)
    return Conversor.converter_para_json(ProcessoSchema, processo), 200


def put_atualizar_processo(processo_guid, body):
    processo = Conversor.converter_para_objeto(ProcessoSchema, body)

    service = ProcessoService()
    processo = service.atualizar_processo(processo_guid, processo)
    return Conversor.converter_para_json(ProcessoSchema, processo), 200


def delete_processo(processo_guid):
    service = ProcessoService()
    service.excluir_processo(processo_guid)
    return "Ok", 200
