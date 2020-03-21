from server import db


class Conversor:

    @staticmethod
    def converter_para_json(schema, data):
        return schema(many=True if type(data) == list else False).dump(data)

    @staticmethod
    def converter_para_objeto(schema, data):
        return schema(many=True if type(data) == list else False).load(data, session=db.session)
