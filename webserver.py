from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

toggle = False


@app.route('/')
def home():
    return render_template("index.html", toggle=toggle)

@app.route('/status')
def status():
    status = { "toggle": toggle }
    return status

@app.route('/status/off')
def status_off():
    toggle = False
    status = { "toggle": toggle, "response": 200 }
    return status

@app.route('/status/on')
def status_on():
    toggle = True
    status = { "toggle": toggle, "response": 200 }
    return status


@app.route("/send", methods=["POST"])
def send():
    global toggle
    form = request.form
    try:
        if form["switch"] == "on":
            toggle = True
        else:
            toggle = False
    except:
        toggle = False
    print(toggle)
    return redirect("/")

def run():
    app.run(host='0.0.0.0', port='8000')
