from flask import Flask, jsonify, request, abort
from uuid import uuid4
from threading import Thread

app = Flask(__name__)

def kickoff_crew(job_id: str, companies: list[str], positions: list[str]):
    print(f"Running crew for {job_id} with companies {companies} and positions {positions}")

    #SETUP THE CREW HERE
    

    #RUN THE CREW HERE

    #LET APP KNOW WE ARE DONE

@app.route('/api/crew', methods=['POST'])
def run_crew(): 
    data = request.json
    if not data or 'companies' not in data or 'positions' not in data: 
        abort(400, description="Invalid request with missing data")
   
    job_id = str(uuid4())
    companies = data['companies']
    positions = data['positions']

    #Run the crew 
    thread = Thread(target=kickoff_crew, args=(job_id, companies, positions))

    thread.start()

    return jsonify({"job_id": job_id}), 200

@app.route('/api/crew/<job_id>', methods=['GET'])
def get_status(job_id):
    return jsonify({"status": f"Getting status for {job_id}"}), 200



if __name__ == '__main__':
    app.run(debug=True, port=3001)