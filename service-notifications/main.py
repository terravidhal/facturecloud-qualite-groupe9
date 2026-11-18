import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/sante")
def sante():
    return jsonify(statut="ok"), 200


@app.get("/tva")
def route_tva():
    try:
        montant = int(request.args.get("montant", ""))
        return jsonify(montant_ht=montant, tva=(montant * 0.2, 2)), 200
    except ValueError:
        return jsonify(error="MONTANT_INVALIDE"), 400
   


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8082)))


