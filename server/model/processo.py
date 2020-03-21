from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, Table
from sqlalchemy.orm import relationship

from server import db, ma
# from server.enumerated.tipo_parte_enum import TipoParte
# from server.model.parte import ParteSchema

# processo_parte = Table(
#     'tb_relacao_processo_parte', db.metadata,
#     Column('processo_guid', String, ForeignKey('tb_processo.guid')),
#     Column('parte_guid', String, ForeignKey('tb_parte.guid')),
#     Column('tipo_parte', Enum(TipoParte)),
# )


class Processo(db.Model):

    __tablename__ = "tb_processo"
    guid = Column(String, primary_key=True)
    numero = Column(String)
    data = Column(DateTime)
    valor = Column(DateTime)
    # partes = relationship("Partes", secondary=processo_parte)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String)


class ProcessoSchema(ma.ModelSchema):
    # partes = fields.Nested(ParteSchema, many=True)

    class Meta:
        model = Processo

        fields = (
            "guid",
            # "tipo_parte",
            "numero",
            "data",
            "valor",
            # "partes"
        )
