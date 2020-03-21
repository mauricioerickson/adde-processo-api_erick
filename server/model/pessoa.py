from datetime import datetime

from sqlalchemy import Column, String, DateTime

from server import db, ma


class Pessoa(db.Model):

    __tablename__ = "tb_pessoa"
    guid = Column(String, primary_key=True)
    nome = Column(String)
    documento = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String)


class PessoaSchema(ma.ModelSchema):

    class Meta:
        model = Pessoa

        fields = (
            "guid",
            "nome",
            "documento",
        )
