import psycopg2

conn = psycopg2.connect(dbname="Blunder",
                host="127.0.0.1",
                user="postgres",
                password="20120711",
                port="5432")

cursor = conn.cursor()

query = 'insert into preference (title) values (\'Плавание\'),(\'Хоккей\');'
cursor.execute(query)
