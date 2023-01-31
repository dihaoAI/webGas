import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def save_file():
    data = request.files
    print(data)
    file = data['file']
    file.save(file.filename+'.csv')

    return 'okok'


if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0', port=1234)


