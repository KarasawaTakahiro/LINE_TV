#! /usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime

class Database():
    def __init__(self):
        self.connector = MySQLdb.connect(host="localhost", db="hoge", user="root", passwd="38CJADSDv49Dy7X7K2XdsgpavySzN7G6H6x", charset="utf8")
        self.cursor = self.connector.cursor()

    def get_tvprogramid_from_tvtitle(self, title):
        sql = "select id from tvprogram where program_name = '%s'" % title
        self.cursor.execute(sql)
        return int(self.cursor.fetchone()[0])

    def insert_tvprogramid_into_notification(self, tvid):
        sql = "insert into notification_reservations (tvprogram_id, status) values (%d, 0);" % tvid
        self.cursor.execute(sql)
        self.connector.commit()

    def get_all_tvprogramid_from_notification(self, date):
        """
            YYYY-MM-DD HH:MM:SS
        """
        sql = "SELECT id FROM notification_reservations INNER JOIN tvprogram ON notification_reservations.id = tvprogram.id WHERE status = 0 and start_time > %s;" % (date - datetime.datetime(0, 0, 0, 0, 15)).strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.connector.commit()
        self.cursor.close()
        self.connector.close()


