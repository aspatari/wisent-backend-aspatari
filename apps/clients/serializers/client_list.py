from marshmallow import Schema, fields


class ClientListSchema(Schema):
    id = fields.UUID(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
