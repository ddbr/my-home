from flask import Flask, request

app = Flask(__name__)

@app.route("/trigger", methods=["POST"])
def trigger_from_wiser():
    data = request.json
    button_id = data.get("button_id")

    if not button_id:
        return {"error": "Missing button_id"}, 400

    print(f"🔘 Trigger received from Wiser: {button_id}")
    # TODO: Here you could trigger a HomeKit switch or log to DB

    return {"status": "ok"}, 200

def start_flask_server():
    app.run(host="0.0.0.0", port=5000)
