from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    twiml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="female" language="he-IL">שלום, כאן שירי. איך אפשר לעזור?</Say>
</Response>"""
    return Response(twiml, mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
