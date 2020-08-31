import environ

env = environ.Env()
ROOT_DIR = environ.Path(__file__) - 2

READ_DOT_ENV_FILE = env.bool("READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined
    # as environment variables.
    env_file = str(ROOT_DIR.path(".env"))
    print("Loading : {}".format(env_file))
    env.read_env(env_file)
    print("The .env file has been loaded. See base.py for more information")

DATABASE_URL = env.str("DATABASE_URL")
PORT = env.int("PORT", 8000)
ADDRESS = env.str("SERVER_ADDRESS", '0.0.0.0')
DEBUG = env.bool("DEBUG", True)

APP_SETTINGS = {"debug": DEBUG}

LOG_LVL = "DEBUG" if DEBUG else "INFO"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                + "pathname=%(pathname)s lineno=%(lineno)s "
                + "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(asctime)s [%(levelname)s] %(message)s", "datefmt": "%Y-%m-%d %H:%M:%S", },
        "rich": {"datefmt": "[%X]", "format": "[%(name)s][%(funcName)s] -> %(message)s"},
    },
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "simple", },
        "console-verbose": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose", },
        "terminal": {"class": "rich.logging.RichHandler", "formatter": "rich", "level": "DEBUG", },
    },
    "loggers": {
        "tornado": {"handlers": ["terminal"], "level": LOG_LVL, "propagate": True, },
        "service": {"handlers": ["terminal"], "level": LOG_LVL, "propagate": True, },
    },
}
