import tornado.options as options

options.parse_command_line()

if __name__ == "__main__":
    from core.server import run_server

    run_server()
