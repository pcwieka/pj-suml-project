from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
model_dir = '/model'

@app.route('/<path:filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory(model_dir, filename)
    except Exception as e:
        return str(e), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(model_dir, 'champion_model.pkl'))
    return 'Model uploaded', 200

@app.route('/upload_metrics', methods=['POST'])
def upload_metrics():
    file = request.files['file']
    file.save(os.path.join(model_dir, 'champion_metrics.pkl'))
    return 'Metrics uploaded', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
