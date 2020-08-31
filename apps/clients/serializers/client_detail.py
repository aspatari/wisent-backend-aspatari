from marshmallow import Schema, fields


class ClientDetailSchema(Schema):
    id = fields.UUID(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime(dump_only=True)
