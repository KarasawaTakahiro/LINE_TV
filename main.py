#! /usr/bin/env python
# coding: utf-8

# main file

from bottle import run, route, post, get, request, redirect, static_file

import datetime
import html 
import os.path

# ---for test code---------------------------

IKARI_START = datetime.timedelta(2014, 8, 8, 15, 40)


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

def check_push(date):
    """
    dated = datetime.timedelta(date.year, date.month, date.day, date.hour, date.minute, date.second)
    nowt = datetime.now()
    nowd = datetime.timedelta(nowt.year, nowt.month, nowt.day, nowt.hour, nowt.minute, mow.second)
    if (dated > (IKARI_START - datetime.timedelta(minutes=15))) and (nowd < IKARI_START):
        return True
    else:
        False
    """
    return False

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

def write_message_user(mess,filename):
    f = open(filename,"a")
    f.write("0," + mess + "\n")
    f.close()

def wirte_message_partner(mess,filename):
    f = open(filename,"a")
    f.write("1," + mess + "\n")
    f.close()

def read_messages(filename):
    f = open(filename, "r")
    li = []
    text = f.readline()
    while text:
        li.append(text)
        text = f.readline()
    return li

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
        time = parse_time(str(specified))  # 時間を変換
        if check_push(time):
            redirect("/%s/%s" % (P_PUSH, specified))
        src = html.get_head()
        if(os.path.exists(F_LOG)):  # ログファイルがあるか
            for li in read_messages(F_LOG):
                status, mess = li.split(",")
                if(status == 1):
                    src += html.get_say_self(mess)
                else:
                    src += html.get_say_partner(mess)
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
        # 通知済みフラグを立てる

        # 
        return """
        <p>プッシュ画面</p>
        <p>もうすぐ番組が始まります</p>
        <br />
        <p><a href="/%s">戻る</a>
        """ % (P_INDEX)
    else:
        redirect("/%s"  % (P_INDEX))

"""
    ユーザからのメッセージを処理
"""
@post("/message")
def post_message():
    mess = request.forms.get(N_TEXT)
     # bangumimeiwo eru
    if mess:
        # fairuni touroku
        write_message_user(mess, F_LOG)
        reg_watch_program(mess)

"""
    視聴番組通知登録
"""
def reg_watch_program(title):

    # 視聴予約データベースに登録する
    #
    
    redirect("/%s" % (P_INDEX))

run(host="localhost", port=8080)

