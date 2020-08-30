from tornado.web import Application


class App(Application):
    def __init__(self):
        settings = {"debug": True}
        handlers = [

        ]
        super(App, self).__init__(
            handlers=handlers,
            **settings
        )
