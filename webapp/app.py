

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
        return make_response("Can not read image", 200)

    data = mrz.to_dict()
    os.remove(file_name)
    return make_response(jsonify(data), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
