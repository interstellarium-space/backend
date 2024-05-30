# -*- coding: utf-8 -*-

from typing import Optional

from datetime import date
from pydantic import BaseModel


class Chief(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Group(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Contract(BaseModel):
    id: int
    name: Optional[str] = None
    start_date: Optional[date] = None
    finish_date: Optional[date] = None
    chief: Chief
    group: Group


class ContractFilters(BaseModel):
    name: Optional[str] = None
    start_date: Optional[date] = None
    finish_date: Optional[date] = None


class CreateContractRequest(BaseModel):
    name: str
    start_date: Optional[date] = None
    finish_date: Optional[date] = None


class CreateContractResponse(BaseModel):
    id: int