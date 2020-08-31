import json

from marshmallow import ValidationError

from common.handler import BaseJsonRequestHandler
from .. import serializers
from ..service import client_service
from common.exception import TornadoValidationError


class ClientList(BaseJsonRequestHandler):
    route = "/v1/clients"

    async def get(self):
        clients = await client_service.get_clients()
        schema = serializers.ClientListSchema(many=True)
        result = schema.dump(clients)
        self.success(result)

    async def post(self):
        try:

            schema = serializers.ClientCreateSchema()
            client_data = schema.loads(self.request.body)

            client = await client_service.create_client(**client_data)

            response_data = serializers.ClientDetailSchema().dump(client)
            self.success(response_data, status=201)

        except ValidationError as err:
            messages = err.messages
            print(messages)
            self.error(TornadoValidationError(status_code=400, log_message=messages))
