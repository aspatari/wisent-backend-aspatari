from common.handler import BaseJsonRequestHandler
from common.types import ID
from .. import serializers, service


class ClientCreateEditDelete(BaseJsonRequestHandler):
    route = '/v1/clients/(?P<client_id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'

    async def get(self, client_id: ID):
        client = await service.client_service.get_client(client=client_id)
        schema = serializers.ClientDetailSchema()
        result = schema.dump(client)
        self.success(result)

    def patch(self, client_id: ID):
        self.finish({"method": "patch"})

    def delete(self, client_id: ID):
        self.finish({"method": "delete"})
