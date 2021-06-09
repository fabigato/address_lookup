""" example search module. Probably something for elastic search """
import re
from collections import Counter
from typing import Optional

from unidecode import unidecode

from .util import Address, address_text
from .db import DB


def query_db(addres: str) -> Optional[Address]:
    """ simple address match functionality. Tokenizes the query and checks matches per token against all addresses """
    pieces = re.split(r'[\s,\.]', re.sub(r'\s+', ' ', unidecode(addres)))
    matches = []
    for piece in pieces:
        matches += [idx for idx, a in enumerate(DB) if piece.lower() in unidecode(address_text(a).lower())]
    if len(matches) > 0:
        winner = Counter(matches).most_common()[0][0]
        return DB[winner]
    else:
        return None
