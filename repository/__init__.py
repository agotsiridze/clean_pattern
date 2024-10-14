from sqlalchemy.orm import Session
from models.region import Region
from schemas.region_schema import RegionInput, RegionOutput
from typing import List, Optional, Type
from pydantic import UUID4
