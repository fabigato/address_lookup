""" main script """
from http import HTTPStatus
from typing import Tuple, Any

from flask import Flask, jsonify

from search import query_db

app = Flask(__name__)


@app.route("/address/<string:address>", methods=["GET"])
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=False, processes=4)
