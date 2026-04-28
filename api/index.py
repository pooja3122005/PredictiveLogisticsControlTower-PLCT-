from __future__ import annotations

from asgi2wsgi import ASGI2Wsgi

from app.main import app as fastapi_app

app = ASGI2Wsgi(fastapi_app)
