

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check_fraud", methods=["POST"])
def check_fraud():
    data = request.get_json()

    amount = float(data.get("amount", 0))
    receiver = data.get("receiver", "")
    unfamiliar = data.get("unfamiliar", "no")

    risk_score = 0
    reasons = []

    # Rule 1: High transaction amount
    if amount >= 25000:
        risk_score += 50
        reasons.append("High transaction amount")

    # Rule 2: Unfamiliar receiver
    if unfamiliar == "yes":
        risk_score += 50
        reasons.append("Unfamiliar receiver")

    if risk_score >= 50:
        status = "Suspicious"
    else:
        status = "Low Risk"

    return jsonify({
        "status": status,
        "risk_score": risk_score,
        "reasons": reasons,
        "receiver": receiver
    })


if __name__ == "__main__":
    app.run(debug=True)
