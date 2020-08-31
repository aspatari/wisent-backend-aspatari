from tortoise import fields

from common.models import BaseModel


class Messages(BaseModel):
    message = fields.TextField()
