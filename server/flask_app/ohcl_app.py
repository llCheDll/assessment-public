import json
import os
import pandas as pd

from flask import Flask, request, jsonify, abort
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './upload_files'
ALLOWED_EXTENSIONS = set(['csv',])

app = Flask(__name__)
app.secret_key = 'secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_ohlc(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    df = pd.DataFrame.from_csv(file_path)
    ohlc_df = df['price'].resample('1Min').ohlc()

    jsonfiles = json.loads(ohlc_df.to_json(orient='index'))

    return jsonfiles


@app.route('/api/v1/candle', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        resp = {"response": 'Success!'}
        return jsonify(resp)
        
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return jsonify(get_ohlc(filename))
                
        return abort(400)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')