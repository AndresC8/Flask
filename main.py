from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect('/show'))
    response.set_cookie('userIP', user_ip_information)
    return response

@app.route("/show")
def show():
    user_ip = request.cookies.get("userIP")
    return f"ip {user_ip}"

app.run(host='0.0.0.0', port=8000, debug=False)