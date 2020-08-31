from common.handler import BaseJsonRequestHandler
from .. import serializers
from ..service import client_service


class ClientList(BaseJsonRequestHandler):
    route = "/v1/clients"

    async def get(self):
        clients = await client_service.get_clients()
        schema = serializers.ClientListSchema(many=True)
        result = schema.dump(clients)
        self.success(result)

    async def post(self):
        client = await client_service.create_client(
            first_name="artur", last_name="spatari", email="artur.sptari@gmai.com"
        )

        self.success("{}")
