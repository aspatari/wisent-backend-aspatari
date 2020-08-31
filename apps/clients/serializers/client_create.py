from marshmallow import Schema, fields


class ClientCreateSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
