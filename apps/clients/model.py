from tortoise import fields

from common.models import BaseModel


class Client(BaseModel):
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
