from flask import Flask, render_template, request

app = Flask(__name__)

message_history = []

# ---------------- SMS MESSAGES ----------------

LOW_RISK_SMS = "Habari! Kumbusho kutoka Watu: Malipo yako ya KES 83 yanakaribia tarehe ya mwisho. Tafadhali jiandae kulipa kwa wakati ili uendelee kufurahia huduma bila kukatizwa. Asante!"

MEDIUM_RISK_SMS = "Habari! Leo ni siku ya malipo ya KES 83. Ikiwa huwezi kulipa yote leo, unaweza kuanza na kiasi kidogo kidogo. Tuko hapa kukusaidia."

HIGH_RISK_SMS = "TAHADHARI: Simu yako imefungwa kutokana na kuchelewa kwa malipo. Lipa angalau sehemu ya KES 83 leo ili urejeshe huduma ya simu yako."

# ---------------- SMS SIMULATION ----------------

def send_sms(phone, message):
    print("📩 Sending SMS to:", phone)
    print("MESSAGE:", message)

# ---------------- MAIN APP ----------------

@app.route("/", methods=["GET", "POST"])
def home():

    risk = None
    sms = None

    if request.method == "POST":

        phone = request.form.get("phone")
        missed = int(request.form.get("missed"))

        if missed == 0:
            risk = "LOW RISK"
            sms = LOW_RISK_SMS

        elif missed == 1:
            risk = "MEDIUM RISK"
            sms = MEDIUM_RISK_SMS

        else:
            risk = "HIGH RISK"
            sms = HIGH_RISK_SMS

        send_sms(phone, sms)

        message_history.append({
            "phone": phone,
            "risk": risk,
            "sms": sms
        })

    return render_template(
        "index.html",
        risk=risk,
        sms=sms,
        history=message_history
    )

# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)