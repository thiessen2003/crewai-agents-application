from flask import Flask, jsonify, request, abort
import uuid

app = Flask(__name__)

@app.route('/api/crew', methods=['POST'])
def run_crew(): 
    data = request.json
    if not data or 'companies' not in data or 'positions' not in data: 
        abort(400, description="Invalid request with missing data")
   
    job_id = str(uuid())

    return jsonify({"status": "success"}), 200

@app.route('/api/crew/<job_id>', methods=['GET'])
def get_status(job_id):
    return jsonify({"status": f"Getting status for {job_id}"}), 200



if __name__ == '__main__':
    app.run(debug=True, port=3001)