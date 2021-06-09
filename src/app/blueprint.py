""" blueprint for endpoints """
from typing import Tuple, Any

from http import HTTPStatus
from flask import Blueprint, jsonify

from .search import query_db


blueprint = Blueprint("address search", __name__)


@blueprint.route("/address/<string:address>", methods=["GET"])
def get_address(address: str) -> Tuple[Any, int]:
    """
    Lookup addresses
        - address: address to look for
          description: a string
          required: true
          in: path
    responses:
        200:
          description: Response has returned an address
          schema:
            type: object
            properties:
                lon:
                    type: float
                lat:
                    type: float
                number:
                    type: string
                street:
                    type: string
                city:
                    type: string
                district:
                    type: string
                region:
                    type: string
                postcode:
                    type: string
        404:
          description: address not found
    """
    result = query_db(address)
    if result is None:
        return {"address": "Not found"}, HTTPStatus.NOT_FOUND
    return jsonify(result.dict()), HTTPStatus.OK
