import sqlite3
conn = sqlite3.connect('examples.db')
c= conn.cursor()
#carprice = float(input("Enter the price:"))
#c.execute('''CREATE TABLE stockitems
         #( trans text, date text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('BUY','2006-01-05','RHAT',100,35.14)")

'''stocks = (('BUY','2006-01-05','RHAT',100,35.14),
         ('BUY','2006-01-05','RHAT',90,14.3),
         ('BUY','2006-01-05','RHAT',150,3.14),
         ('BUY','2006-01-05','RHAT',10,5.14),
         ('BUY','2006-01-05','RHAT',110,35.15),
         )
c.executemany('INSERT INTO stockitems VALUES (?,?,?,?,?)',stocks)'''
c.execute("SELECT * from stockitems where qty>100 ")
conn.commit()
for row in c:
    print(row)
#conn.close()



import tkinter 