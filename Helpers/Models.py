from typing import List, Optional

from pydantic import BaseModel, Field


class Entry(BaseModel):
    entry_id: int = Field(alias="id")
    title: str
    verified: bool


class Entries(BaseModel):
    entity: List[Entry]


class Pattern(BaseModel):
    addition: Optional[dict[str, str or int]]
    important_numbers: Optional[list[int]]
    title: str
    verified: bool
