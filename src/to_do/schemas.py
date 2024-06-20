from datetime import datetime
from typing import List

from pydantic import BaseModel


class GroupCreate(BaseModel):
    name: str
    description: str
