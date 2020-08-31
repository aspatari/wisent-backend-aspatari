from typing import Optional, List, Union

from .model import Client
from common.types import ID, empty


class ClientService:
    def __init__(self):
        ...

    async def get_clients(self) -> List[Client]:
        clients = await Client.all()

        return clients

    async def get_client_by_id(self, *, client_id: ID) -> Client:
        client = await Client.get(id=client_id)
        return client

    async def get_client(self, *, client: Union[ID, Client]) -> Client:
        if isinstance(client, Client):
            return client
        client = await self.get_client_by_id(client_id=client)
        return client

    async def create_client(
        self, *, first_name: str, last_name: str, email: str
    ) -> Client:
        client = Client(first_name=first_name, last_name=last_name, email=email)
        await client.save()
        return client

    async def edit_client(
        self,
        *,
        client: Union[ID, Client],
        first_name: Optional[str] = empty,
        last_name: Optional[str] = empty,
        email: Optional[str] = empty
    ) -> Client:
        client = await self.get_client(client=client)
        if first_name is not empty:
            client.first_name = first_name
        if last_name is not empty:
            client.last_name = last_name
        if email is not empty:
            client.email = email

        await client.save()
        return client

    async def delete_client(self, *, client: Union[ID, Client]) -> None:
        client = await self.get_client(client=client)
        await client.delete()
        return


client_service = ClientService()
