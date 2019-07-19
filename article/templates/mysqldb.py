import mysql.connector
conn = mysql.connector.connect(user ='pnv',
                               password ='password',
                               host = '127.0.0.1',
                               database ='webnews')

cursor = conn.cursor()
query = "select * from article_article"
cursor.execute(query)
for i in cursor:
         print(i) 
cursor.close()
conn.close()