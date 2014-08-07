from bottle import Bottle, route, run, template, get, post, request

@route("/object/<id:int>")
def callback(id):
    assert isinstance(id, int)

@route("/show/<name:re:[a-z]+>")
def callback(name):
    assert name.isalpha()

@route("/static/<path:path>")
def callback(path):
    return static_file(path)

@get("/login")
def login_form():
    return """
<form action="/login" method="post">
UserName: <input name="username" type="text" />
<input value="Login" type="submit" />
"""

@post("/login")
def do_login():
    username = request.forms.get('username')
    return "<p>%s</p>" % username



run(host="localhost", port=8080, debug=True, reloader=True)

