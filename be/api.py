from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/crew', methods=['POST'])
def run_crew(): 
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=3001)