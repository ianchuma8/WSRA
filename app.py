from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    risk = None
    sms = None

    if request.method == "POST":

        name = request.form.get("name")
        phone = request.form.get("phone")
        missed = int(request.form.get("missed"))

        if missed == 0:
            risk = "LOW RISK"
            sms = "Habari! Kumbusho: Malipo yako yako karibu."

        elif missed == 1:
            risk = "MEDIUM RISK"
            sms = "Habari! Unaweza kulipa kidogo kidogo."

        else:
            risk = "HIGH RISK"
            sms = "TAHADHARI! Simu yako imefungwa."

    return render_template("index.html", risk=risk, sms=sms)

if __name__ == "__main__":
    app.run(debug=True)