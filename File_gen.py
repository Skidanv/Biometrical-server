# -*- coding: utf-8 -*-
import random
import re

#скрипт для создания файлов с данными

def stringGen(): #генерация строки-среза данных с биометрического браслета
    data_pat=("2017",random.randint(1, 12), random.randint(1, 30), random.randint(0, 23), 
              random.randint(0, 59), random.randint(0, 59), round(random.uniform (36, 39), 1), random.randint(100, 300),
              random.randint(50, 170), round(random.uniform (36, 39), 2))
    new_file.write(data_pat[0]+"-"+str(data_pat[1])+"-"+str(data_pat[2])+" "+str(data_pat[3])+":"+str(data_pat[4])
                   +":"+str(data_pat[5])+" "+str(data_pat[6])+" "+str(data_pat[7])+" "+str(data_pat[8])+" "+str(data_pat[9])+"\n")
    
print("Количество создаваемых файлов: ")
file_count = input()
i = 0
while i<file_count: #создание файлов с заголовком-именем и 100 строк данных
    new_file = open("/home/vitaliy/Desktop/Сервак/Data/pat"+str(i)+".txt", "w")
    title_file = re.sub('.txt', '', new_file.name)
    new_file.write(title_file+"\n")
    j=0
    while j<100:
        stringGen()
        j=j+1
    new_file.close()
    i=i+1
