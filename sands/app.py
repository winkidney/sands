from flask import Flask

from sands import settings

__all__ = (
    "app",
)

app = Flask(
    "sands",
    static_folder=settings.STATIC_FOLDER,
    template_folder=settings.TEMPLATE_FOLDER,
)

if hasattr(settings, "SECRET_KEY"):
    app.config["SECRET_KEY"] = settings.SECRET_KEY