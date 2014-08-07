#! /usr/bin/env python
# coding: utf-8

# main file

from bottle import run, route, post, get, request, redirect

# name属性
N_TEXT = "text"
N_SEND_BUTTON = "send"

# Page URL
P_INDEX = "index"
P_ADD = "add"

# html
H_INDEX = ""

@route("/%s"%P_INDEX)
def index():
    return '''
    <p>TopPage</p>
    %s
    <br />
    <form action="/%s" method="post">
        <input name="%s" type="text" />
        <input type="submit" value="送る">
    </form>
    ''' % ("データベースを参照してトーク履歴からHTMLを作って表示", P_ADD, N_TEXT)

@post("/%s" % P_ADD)
def do_send():
    text = request.forms.get(N_TEXT)
    print "get: " + text

    # データベースに登録する

    redirect("/%s"%P_INDEX)


run(host="localhost", port=8080)

