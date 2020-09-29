from starlette.config import Config

config = Config(".env")

# DB
DB_DSN = config("DB_DSN", default='sqlite:///database.db')

# Security
BASIC_AUTH_USERNAME = config("BASIC_AUTH_USERNAME", default="admin")
BASIC_AUTH_PASSWORD = config("BASIC_AUTH_PASSWORD", default="admin")

# General
API_PREFIX = config("API_PREFIX", default="")
PROJECT_NAME = config("PROJECT_NAME", default="Starx Notification Service")
DEBUG = config("DEBUG", cast=bool, default=True)
VERSION = config("VERSION", default="")