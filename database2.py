#! /usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

connector = MySQLdb.connect(host="localhost", db="hoge", user="root", passwd="38CJADSDv49Dy7X7K2XdsgpavySzN7G6H6x", charset="utf8")
cursor = connector.cursor()
sql = u"CREATE TABLE test_table(id VARCHAR(10), program_name VARCHAR(10));"
cursor.execute(sql)
sql = u"INSERT INTO test_table(id,program_name) VALUES('1','アメトーーク！');"
cursor.execute(sql)
sql = u"INSERT INTO test_table(id,program_name) VALUES('2','ドラえもん');"
cursor.execute(sql)
sql = u"INSERT INTO test_table(id,program_name) VALUES('3','怒り新党');"
cursor.execute(sql)
sql = u"SELECT * from test_table"

connector.commit()
    
cursor.close()
connector.close()

