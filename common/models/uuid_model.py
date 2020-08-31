from tortoise import fields
from tortoise.models import Model
from uuid import uuid4


class UUIDPkModel(Model):
    id = fields.UUIDField(pk=True, default=uuid4)

    class Meta:
        abstract = True
