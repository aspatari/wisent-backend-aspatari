from marshmallow import ValidationError

from common.exception import TornadoDoseNotExist, TornadoValidationError
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

    async def patch(self, client_id: ID):
        try:

            schema = serializers.ClientEditSchema()
            client_data = schema.loads(self.request.body)

            client = await service.client_service.edit_client(client=client_id, **client_data)

            response_data = serializers.ClientDetailSchema().dump(client)
            self.success(response_data, status=200)

        except ValidationError as err:
            messages = err.messages
            self.error(TornadoValidationError(status_code=400, log_message=messages))
        except DoesNotExist as e:
            self.error(TornadoDoseNotExist(id=client_id))


async def delete(self, client_id: ID):
    try:
        client = await service.client_service.delete_client(client=client_id)
        self.success({}, status=204)

    except DoesNotExist as e:
        self.error(TornadoDoseNotExist(id=client_id))
