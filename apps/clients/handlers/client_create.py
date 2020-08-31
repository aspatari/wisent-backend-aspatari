from common.handler import BaseJsonRequestHandler



class ClientCreate(BaseJsonRequestHandler):
    route = '/v1/clients'

    def patch(self):
        self.finish({"method": "patch"})
