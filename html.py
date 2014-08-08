# coding: utf-8

import frame

def get_say_self(mess):
    html = ""
    html += frame.SELF_FRONT
    html += mess
    html += frame.SELF_TAIL
    return html

def get_say_partner(mess):
    html = ""
    html += frame.PARTNER_FRONT
    html += mess
    html += frame.PARTNER_TAIL
    return html

def get_head():
    return frame.HEAD

def get_tail():
    return frame.TAIL

