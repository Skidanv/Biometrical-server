# -*- coding: utf-8 -*-

from twisted.internet import protocol, reactor
from twisted.internet.protocol import ClientFactory, Protocol
import time

host = 'localhost'
port = 8123

class Twist_client(protocol.Protocol):
    #Отправка сообщения с проверкой
            
    def connectionMade(self):
        print "Connectios success"
	f = open ('/home/vitaliy/Desktop/Сервак/Data/pat0.txt')
	for data in f: #отправка данных построчно
	    print data
            self.transport.write(data)
	self.transport.loseConnection()
        
class Twist_Factory(protocol.ClientFactory):
    protocol = Twist_client
    
    def clientConnectionFailed(self, connector, reason):
        print 'connection failed:', reason.getErrorMessage()
        time.sleep(5)
        connector.connect()

    def clientConnectionLost(self, connector, reason):
        print 'connection lost:', reason.getErrorMessage()
        time.sleep(1)
        connector.connect()
        #reactor.stop()
    
factory = Twist_Factory()
reactor.connectTCP(host, port, factory)
reactor.run()


