from sqlmodel import SQLModel

from . import models  # noqa: F401
from .db import engine

SQLModel.metadata.create_all(engine)
