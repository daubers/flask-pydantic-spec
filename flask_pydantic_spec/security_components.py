from typing import Literal, Optional

from pydantic import BaseModel


class SecurityScheme(BaseModel):
    type: Literal["http", "apiKey"]
    scheme: Literal["Basic", "Bearer"]
    _in: Literal["header", "query", "cookie"]
    bearerFormat: Optional[str]
    name: str
    description: Optional[str]

