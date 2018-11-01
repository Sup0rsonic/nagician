import _mysql as mysql
import re
import os
import sys
import json

host = ''
port = 3306
user = ''
password = ''
database = ''

debug = True

if debug:
    host = 'localhost'
    port = 3306
    user = 'test'
    password = 'test'

class conn():
    global host,port,user,password,database
    def connect(self):
        try:
            dbconn = mysql.connect(host=host,port=port,user=user,password=password)
        except Exception,e:
            print '[!]Error:Unable to connect to database'


class dbLoader():
    def check(self,conn):
        sess = conn.cursor()
        sess.execute('select 1 from information_schema.schemata where schema_name = ' + database)
        res = sess.fetchall()
        if len(res) == 0:
            return True
        else:
            return False

    def genDB(self,conn):
        sess = conn.cursor()
        try:
            if raw_input('[*]No database detected. Do you want build database now?\n(Y/N)').upper() == 'Y':
                print '[*]Generating database %s' %database
            else:
                print '[!]Database not found.Quitting.'
            sess.execute('CREATE DATABASE' + database)
            print '[+]Generate database success,spawning tables.'
            sess.execute('USE %s' % database)
            sess.execute('CREATE TABLE hosts (ip varchar(255),port int(5),key varchar(255))')
            sess.execute('CREATE TABLE modules (name varchar(255),description varchar(65535),path varchar(65535),parameter varchar(255))')
            sess.execute('CREATE TABLE payloads (name varchar(255),description varchar(65535),path varchar(65535),parameter varchar(255))')
            sess.execute('CREATE TABLE sessions (ip varchar(255),port int(5),type varchar(50),key varchar(255))')
            sess.execute('CREATE TABLE exploit (name varchar(255),description varchar(65535),path varchar(65535),parameter varchar(255)), arch varchar(50)')
            sess.execute('CREATE TABLE botnet (id int,name varchar(255),route varchar(65535),bots varchar(65535))')
            print '[+]Database generated.'
            return 0
        except Exception,e:
            print '[!]Failed to generate database.'
            if debug == True:
                print str(e)
            return

    def insert(self,conn,query):
        sess = conn.cursor()
        try:
            sess.execute(query)
        except Exception,e:
            print '[*]Insert failed.'
            if debug == True:
                print e

    def select(self,conn,query):
        sess = conn.cursor
        try:
            sess.execute(query)
            return sess.fetchall()
        except Exception,e:
            print '[*]Select failed.'
            if debug == True:
                print e
                return []

class updateLoader():
    def update(self,conn,mode):
        sys.path.add('../modules')
        f= open('resource.json','r')
        raw = f.read()
        db = json.loads(str(raw))
        payload = db['PAYLOAD']
        stager = db['STAGER']
        exploit = db['EXPLOIT']
        count = 0
        for i in payload:
            query = 'INSERT INTO payloads values(%s,%s,%s,%s)' % (i['NAME'],i['DESCRIPTION'],i['PATH'],i['PARAMETER'])
            try:
                conn.execute(query)
                count += 1
            except Exception,e:
                print '[!]Error Updating data'
                print e
        for i in stager:
            query = '' # query
            try:
                conn.execute(query)
                count += 1
            except Exception, e:
                print '[!]Error Updating data'
                print e
        for i in exploit:
            query = 'INSERT INTO payloads values(%s,%s,%s,%s,%s)' % (i['NAME'], i['DESCRIPTION'], i['PATH'], i['PARAMETER'],i['ARCH'])
            try:
                conn.execute(query)
                count += 1
            except Exception, e:
                print '[!]Error Updating data'
                print e
        print '[+]Database update complete, %s rows affected.' % str(count)
