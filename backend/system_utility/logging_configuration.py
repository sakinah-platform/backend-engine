import structlog
from os import environ

ERROR_LOGGING_FILE = environ.get("ERROR_LOGGING_FILE", "./sakinah_error_log.log")
INFO_LOGGING_FILE = environ.get("INFO_LOGGING_FILE", "./sakinah_info_log.log")
DEBUG_LOGGING_FILE = environ.get("DEBUG_LOGGING_FILE", "./sakinah_debug_log.log")
LOG_SOCKET_RECEIVER_PORT = environ.get('LOG_SOCKET_RECEIVER_PORT', '9020')
LOG_SOCKET_RECEIVER_HOST = environ.get('LOG_SOCKET_RECEIVER_HOST', 'localhost')

LOCAL_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(),
        },
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.KeyValueRenderer(key_order=['timestamp', 'level', 'event', 'logger']),
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console",
        },
        "error_json_file": {
            "class": "logging.handlers.WatchedFileHandler",
            "filename": ERROR_LOGGING_FILE,
            "formatter": "json_formatter",
        },
        "info_json_file": {
            "class": "logging.handlers.WatchedFileHandler",
            "filename": INFO_LOGGING_FILE,
            "formatter": "json_formatter",
        },
        "debug_json_file": {
            "class": "logging.handlers.WatchedFileHandler",
            "filename": DEBUG_LOGGING_FILE,
            "formatter": "json_formatter",
        },
    },
    "loggers": {
        "info_logger": {
            "handlers": ["console", "info_json_file"],
            "level": "INFO",
        },
        # Make sure to replace the following logger's name for yours
        "error_logger": {
            "handlers": ["console", "error_json_file"],
            "level": "ERROR",
        },
    }
}

PRODUCTION_LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {message}",
            "style": "{",
        }
    },
    "handlers": {
        "stream": {
            "class": "logging.StreamHandler"
        },
        "error_socket": {
            "class": "logging.handlers.SocketHandler",
            "host": LOG_SOCKET_RECEIVER_HOST,
            "port": LOG_SOCKET_RECEIVER_PORT,
        }
    },
    "loggers": {
        "ErrorLogger": {
            "level": "ERROR",
            "handlers": ["error_socket", "stream"]
        },
    }
}

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)
