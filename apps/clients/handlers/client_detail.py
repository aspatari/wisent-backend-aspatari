from common.exception import TornadoDoseNotExist
from common.handler import BaseJsonRequestHandler
from common.types import ID
from .. import serializers, service
from tortoise.exceptions import DoesNotExist


class ClientCreateEditDelete(BaseJsonRequestHandler):
    route = '/v1/clients/(?P<client_id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'

    async def get(self, client_id: ID):
        try:
            client = await service.client_service.get_client(client=client_id)
            schema = serializers.ClientDetailSchema()
            result = schema.dump(client)
            self.success(result)
        except DoesNotExist as e:
            self.error(TornadoDoseNotExist(id=client_id))

    def patch(self, client_id: ID):
        self.finish({"method": "patch"})

    async def delete(self, client_id: ID):
        try:
            client = await service.client_service.delete_client(client=client_id)
            self.success({}, status=204)

        except DoesNotExist as e:
            self.error(TornadoDoseNotExist(id=client_id))
