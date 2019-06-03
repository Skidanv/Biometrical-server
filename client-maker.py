# -*- coding: utf-8 -*-
import os, subprocess
import time
import shutil
import os

#скрипт создания клиентов для тестирования

print "Сколько клиентов?y/n"
q = input()
q = int(q)
i = 1
while (i<q):
    shutil.copy2(r'/home/vitaliy/Desktop/Сервак/Clients/Client0.py', r'/home/vitaliy/Desktop/Сервак/Clients/Client'+str(i)+'.py') #копирование образца
    with open('/home/vitaliy/Desktop/Сервак/Clients/Client'+str(i)+'.py') as file_in:
        text = file_in.read() #копирование содержания в буфер
    text = text.replace("pat0", "pat"+str(i)) #замена имени пациента
    file_in.close()
    os.remove('/home/vitaliy/Desktop/Сервак/Clients/Client'+str(i)+'.py') #удаление файла
    with open('/home/vitaliy/Desktop/Сервак/Clients/Client'+str(i)+'.py', "w") as file_in:
        file_in.write(text) #создание и запись файла с новым именем пациента
    file_in.close()
    i+=1

print "Запустить клиентов?y/n"
yesno = raw_input()

if yesno == 'y':
    i = 0
    while (i<q):
        subprocess.Popen('python /home/vitaliy/Desktop/Сервак/Clients/Client'+str(i)+'.py', shell=True) #исполнение клиентов
        time.sleep(1)
else:
    print "Запуск клиентов отменён"
