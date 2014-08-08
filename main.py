#! /usr/bin/env python
# coding: utf-8

# main file

from bottle import run, route, post, get, request, redirect, static_file

import datetime
import html
# ---for test code---------------------------
"""
    通知登録DBに登録されているものを返すとする
    時間を元に通知すべき（時間が過ぎているかつ、未通知の）番組名を返す

    date: 時刻

    return: 通知すべきもの / None
"""
def easy_db_get(date):
    html = ""
    f = open("mydb.txt", "r")
    text = f.readline()
    if text:
        return text
    else:
        return None

def easy_db_status(date):
    f = open("mydb.txt", "r")
    text = f.readline()
    f.close()
    if text:
        return True
    else:
        return False

def easy_db_post(text):
    f = open("mydb.txt", "a")
    f.write(text + "\n")
    f.close()

def easy_db_check(res):
    return res

# ------------------------------

F_LOG = "chat_log.txt"

"""
    テキストの時間をdatetimeに直す
"""
def parse_time(stringtime):
        year = stringtime[0:4]
        month =  stringtime[4:6]
        day = stringtime[6:8]
        minute = stringtime[8:10]
        sec = stringtime[10:12]
        print year, month, day, minute, sec
        return datetime.datetime(int(year), int(month), int(day), int(minute), int(sec))

"""
    datetimeをテキストに直す
"""
def datetime_to_string(dat):
    return dat.strftime("%Y%m%d%H%M")

# name属性
N_TEXT = "text"
N_SEND_BUTTON = "send"

# Page URL
P_INDEX = "index"
P_ADD = "add"
P_PUSH = "push"

# html
H_INDEX = ""

"""
    for static file
"""
@route("/image/<filename>")
def static(filename):
    return static_file(filename, root="./image")

"""
    生のトップ画面
    今の時間を指定してトーク画面にいく
"""
@route("/%s" % P_INDEX)
def index():
    redirect("/%s/%s" % (P_INDEX, datetime_to_string(datetime.datetime.now())))

"""
    時間を指定したトーク画面
"""
@route("/%s/<specified:int>" % P_INDEX)
def index(specified=""):
    if specified:
        time = parse_time(str(specified))
        if easy_db_status(time):
            redirect("/%s/%s" % (P_PUSH, specified))

        src = html.get_head()
        src += html.get_tail()
        

        return src
    else:
        index()

"""
    プッシュ通知画面
"""
@route("/%s/<specified>" % P_PUSH)
def push(specified=""):
    if specified:
        text = easy_db_get(parse_time(specified))
        # 通知済みフラグを立てる

        # 
        return """
        <p>プッシュ画面</p>
        <p>もうすぐ[ %s ]が始まります</p>
        <br />
        my_db.txtを空にして、フラグを立てたこととする<br />
        <p><a href="/%s">戻る</a>
        """ % (text, P_INDEX)
    else:
        redirect("/%s"  % (P_INDEX))

"""
    yu-za-karanomesse-jiwosyori
"""
@post("/message")
def post_message():
    mess = request.forms.get(N_TEXT)
     # bangumimeiwo eru
    if mess:
        # fairuni touroku
        write_message_user(mess, F_LOG)
        reg_watch_program(mess)
        redirect("/index")

"""
    視聴番組通知登録
"""
def reg_watch_program(title):

    # 視聴予約データベースに登録する
    #
    

    redirect("/%s/%s" % (P_INDEX, datetime_to_string(datetime.datetime.now())))

run(host="localhost", port=8080)

