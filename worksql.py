import sqlite3

class WorkSQL:


    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname) #открытие соединения с БД
        self.c = self.conn.cursor() #установка курсора
    
    #создание нового пациента
    def new_patient(self, pname):
        #добавление имени в таблицу пациентов 
        self.c.execute("INSERT INTO patients (name) VALUES ('%s')"% (pname))
	# получение присвоенного пациенту уникального id 
        self.c.execute("SELECT id FROM patients WHERE rowid=last_insert_rowid()")
	#создание личной таблицы пациента с биометрией
        self.c.execute('''CREATE TABLE %s (id int, date text, 
                                        temp real, hum real,
                                        pulse int, kard int,
                                        FOREIGN KEY(id) REFERENCES patients(id))'''%(pname))
        
        #self.conn.commit()

    #добавление среза данных в таблицу пациента
    def new_data(self, pname, biodata):
        self.c.execute("INSERT INTO %s VALUES (?, ?, ?, ?, ?, ?)"% (pname), biodata)
    
    #количество записей (срезов данных) в таблице пациента
    def rec_count(self, pname):
        self.c.execute("SELECT COUNT(*) FROM %s"%(pname))
        return self.c.fetchone()[0]

    #вывод всех данных из таблицы пациента
    def sel_pat(self, pname):
        self.c.execute("SELECT * FROM %s"%(pname))
        return self.c.fetchall()

    #наличие пациента в БД
    def find_pat(self, pname):
        self.c.execute("SELECT name FROM patients WHERE name='%s'"%(pname))
        return self.c.fetchone()[0]

    #удаление старых данных
    def del_old_data(self, pname, r_count):
        self.c.execute("DELETE FROM %s WHERE ROWID IN (SELECT ROWID FROM %s ORDER BY ROWID ASC LIMIT %s)"% (pname, pname, r_count))
        #self.conn.commit()

    #удаление всех данных
    def del_data(self, pname):
        self.c.execute("DELETE FROM %s"% (pname))
        #self.conn.commit()

    #удаление пациента из БД
    def del_pat(self, pname):
        self.c.execute("DROP TABLE %s"% (pname))
        self.c.execute("DELETE FROM patients WHERE name = '%s'"% (pname))
        #self.conn.commit()

    #закрытие соединения с БД
    def close(self):
        self.conn.commit()
        self.c.close()
        self.conn.close()
