""" utility functions """

from typing import Optional, List
import pandas as pd

from pydantic import BaseModel


class Address(BaseModel):
    """ schema for address objects """
    lon: float
    lat: float
    number: Optional[str]
    street: str
    city: str
    district: str
    region: str
    postcode: str


def address_text(address: Address) -> str:
    """ a concat repr of the whole address for easy match """
    return f"{address.street} {address.number} {address.postcode} {address.district} {address.city} {address.region}"


def csv2json(path: str, sample: Optional[float] = 0.1) -> List[Address]:
    df = pd.read_csv(path)
    df.rename({col: col.lower() for col in df.columns}, axis=1, inplace=True)
    if sample is not None:
        df = df.sample(frac=sample)
    return df.to_json(orient="index")
