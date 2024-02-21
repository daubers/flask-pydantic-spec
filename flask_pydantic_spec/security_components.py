from typing import Literal, Optional

from pydantic import BaseModel


class SecurityScheme(BaseModel):
    type: Literal["http", "apiKey"]
    scheme: Optional[Literal["Basic", "Bearer"]]
    _in: Optional[Literal["header", "query", "cookie"]]
    bearerFormat: Optional[str]
    name: str
    description: Optional[str]

