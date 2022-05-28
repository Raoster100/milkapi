from typing import List
from fastapi import APIRouter, Depends, Path
from pydantic import Field

catalogs_router = APIRouter()