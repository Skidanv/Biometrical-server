# -*- coding: utf-8 -*-
from twisted.internet import protocol, reactor
from worksql import WorkSQL
import re
import sqlite3
import sys
reload (sys)
sys.setdefaultencoding('utf8')
pname = ''
i=0
def data_counter():
    global i
    i+=1
    print i

class Twist(protocol.Protocol):
    

    #установление соединения с БД
    def connectionMade(self):
	dbname = 'my.db'
	global db
	db = WorkSQL(dbname)
    	print 'connection success!'

    #получение данных
    def dataReceived(self, data):
        print type(data)
        data1 = data.split("\n")
        data1.remove('')
        j=0
        for line in data1: #первая линия - имя пациента, остальные - срез данных с датчиков
            if j == 0:
                j=1
                global pname
                pname = line
                print pname
                try:
                    if db.find_pat(pname) == pname:
                        continue
                    else:
                        db.new_patient(pname) #добавление нового пациента, если его нет в БД
                except TypeError:
                    db.new_patient(pname)
            else:
                biodata = line.split(" ")
                db.new_data(pname, biodata)
        r_count = db.rec_count(pname)
        if r_count > 1000:
            r_count -= 1000
            db.del_old_data(pname, r_count) #удаление старых данных, если больше 1000 записей
        print db.rec_count(pname)
        #db.del_data(pname)
        #db.del_pat(pname)
        data_counter()

    #разрыв соединения
    def connectionLost(self, reason): 
        print 'Connection lost!'
	db.close()


factory = protocol.Factory()
factory.protocol = Twist
print 'wait...'
reactor.listenTCP(8123, factory)
reactor.run()


