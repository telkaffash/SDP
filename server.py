from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/ping")
def ping():
    return jsonify({"status":"connected"})

@app.post("/api/command")
def command():
    data=request.get_json()
    cmd=data.get("command","")

    if cmd=="takeoff":
        return jsonify({"reply":"Taking off"})
    elif cmd=="land":
        return jsonify({"reply":"Landing"})
    else:
        return jsonify({"reply":"Received: "+cmd})

app.run(host="0.0.0.0",port=5000)