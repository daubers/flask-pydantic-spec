from typing import Literal, Optional

from pydantic import BaseModel, Field


class SecurityScheme(BaseModel):
    type: Literal["http", "apiKey"]
    scheme: Optional[Literal["Basic", "Bearer"]] = None
    found_in: Optional[Literal["header", "query", "cookie"]] = Field(default=None, serialization_alias="in")
    bearerFormat: Optional[str] = None
    name: str
    description: Optional[str] = None

