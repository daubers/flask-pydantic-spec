from typing import Literal, Optional

from pydantic import BaseModel, Field


class SecurityScheme(BaseModel):
    type: Literal["http", "apiKey"]
    scheme: Optional[Literal["Basic", "Bearer"]]
    found_in: Optional[Literal["header", "query", "cookie"]] = Field(serialization_alias="in")
    bearerFormat: Optional[str]
    name: str
    description: Optional[str]

