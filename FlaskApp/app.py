from flask import Flask, redirect, render_template, request, jsonify
from pymodule import scheduler_run
app = Flask(__name__)

@app.route('/start_scheduler', methods=['POST'])
def schedule_start(): 
    if request.method == 'POST':    
        data = request.get_json()
        scheduler_run(data)
    return jsonify({'result' : 'Success', 'data': data})

if __name__=="__main__":
    app.run(debug=True, port=8000)




