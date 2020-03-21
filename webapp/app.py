

"""
    Passport Reader
    ~~~~~~~~~~~~~~~

    A simple backend API to extract informations from a passport image file.

    :copyright: (c) 2019 by Patrick RANDRIA.
    :license: MIT, see LICENSE_FILE for more details.
"""

from flask import Flask, request, make_response, jsonify
from passporteye import read_mrz
import os
import tempfile

UPLOAD_FOLDER = '/uploads'
EDIT_FOLDER = '/edit'

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome ! The endpoint is at <b>/process</b>'

@app.route('/process', methods=['POST'])
def process():

    imagefile = request.files.get('imagefile', None)
    js = request.get_json()
    # print ("---------------------------")
    # print(request.data)
    # print ("---------------------------")

    if not imagefile:
        return make_response("Missing file parameter", 400)

    file_name = '%s.bmp' %tempfile.NamedTemporaryFile(prefix="tess_").name
    imagefile.save(file_name)
    mrz = read_mrz(file_name)
    if mrz is None:
        os.remove(file_name)
        return make_response("Can not read image", 404)

    data = mrz.to_dict()
    os.remove(file_name)
    result = {}

    result["country"] = data["country"]
    result["date_of_birth"] = data["date_of_birth"]
    result["expiration_date"] = data["expiration_date"]
    result["mrz_type"] = data["mrz_type"]
    result["names"] = data["names"]
    result["nationality"] = data["nationality"]
    result["number"] = data["number"]
    result["personal_number"] = data["personal_number"]
    result["sex"] = data["sex"]
    result["surname"] = data["surname"]
    result["type"] = data["type"]
    result["valid_composite"] = data["valid_composite"]
    result["valid_date_of_birth"] = data["valid_date_of_birth"]
    result["valid_expiration_date"] = data["valid_expiration_date"]
    result["valid_number"] = data["valid_number"]
    result["valid_personal_number"] = data["valid_personal_number"]
    result["valid_score"] = data["valid_score"]
    return make_response(jsonify(result), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
