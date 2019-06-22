# Biometrical-server
Сервер собирает получает данные с биометрических браслетов и записывает их в базу данных. Возможна интеграция сервера 
с Android девайсом для удобного представления данных. Данные отправляются клиентами в определённую директорию при установлении
соединения с сервером. При подключении производится идентификация клиента. Для каждого нового клиента создается таблица и 
делается запись в таблице учёта клиентов. Сервер получает данные и записывает их в соответствующую таблицу. Сервер подсчитывает 
количество строк в таблице и удаляет старые записи. Текущее ограничение на количество строк в таблице - 1000. При превышении 
лимита удаляется 100 строк. Сервер выдерживает 20 одновременно подключённых пользователей при частоте отправки данных - 5 секунд.

Клиент является имитацией биометрического браслета. Считывает данные из подготовленного файла и отправляет их на сервер 
раз в секунду. При отсутствии сервера пытается подключиться каждые 5 секунд. Частота попыток подключения и отправки данных 
настраивается в функциях clientConnectionFailed и clientConnectionLost класса Twist_Factory соответственно. 

Client-maker и File_gen - скрипты для тестирования сервера. Первый создаёт необходимое количество клиентов, второй -
необходимое количество файлов с данными. Файл с данными имеет имя соответствующее имени пациента- носителя биометрического
браслета и первую строчку с этим же именем. Остальные строки (по умолчанию - 100) -  дата, время и биометрические данные.



The server collects data from biometrical bracelets and records it to database. There is possible an integration server with Android-device for convinient presentation of data. Data is sent by clients to certain directory when a connection with the server was established. Identification of a client is made when it connect with the server. A table is created for each new client and a record is created in table of client's registration. The server gets data and writes it to an according table. The server counts a number of rows in the table and remove old records. A current limit for a number of rows in the table is 1000. 100 lines are deleted when the limit is exceeded. The server maintains 20 simultaneously connected users with a data sending frequency of 5 seconds.

Client is an imitation of a biometrical bracelet. It reads data from a prepared file and send it to the server one time in second. It try to connect every 5 second when the server is unavailable. A frequency of tries to connect and a sending of data configure in functions "clientConnectionFailed" and "clientConnectionLost" of class "Twist_Factory" accordingly.

"Client-maker" and "File_gen" are scripts for testing of the server. The first one create a required amount of clients, the second one create a requered amount of files with data. File with data have a name in accordance with name of patient, who wears the biometrical bracelet, and first row with the same name. Other rows (100 by default) have date, time and biometrical data.
