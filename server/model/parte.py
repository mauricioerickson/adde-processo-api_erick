from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship

from server import db, ma
from server.enumerated.tipo_parte_enum import TipoParte
from server.model.pessoa import PessoaSchema


class Parte(db.Model):

    __tablename__ = "tb_parte"
    guid = Column(String, primary_key=True)
    pessoa_guid = Column(Integer, ForeignKey("tb_pessoa.guid"), index=True)
    pessoa = relationship("pessoa", foreign_keys=[pessoa_guid])

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String)


class ParteSchema(ma.ModelSchema):
    pessoa = fields.Nested(PessoaSchema)

    class Meta:
        fields = (
            "guid",
            "pessoa",
        )
