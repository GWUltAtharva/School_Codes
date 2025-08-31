 
import mysql.connector as con 
 
db = con.connect( 
    host = 'localhost', 
    user = 'root', 
    password = 'sql@123', 
    database = 'student') 
 
cur = db.cursor() 
 
cur.execute('SELECT * FROM data') 
r = cur.fetchall() 
 
for i in r: 
    for j in i: 
        print(j, end="\t") 
    print() 
     
print() 
 
for r,s,d,m in r: 
    print("%4d|%30s|%12s|%5.2f"%(r,s.ljust(30," "),d,m))
