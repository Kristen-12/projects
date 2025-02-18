import pyodbc


try:
    
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=c:\Users\DELL\Documents\student.accdb;'

    conn = pyodbc.connect(con_string)
    c = conn.cursor()
    c.execute("CREATE TABLE stuabout (name text, age integer, gender text, ph integer, hobby text)")
    c.execute("INSERT INTO stuabout VALUES ('Stu 1', 17, 'male',234156,'Football')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 2', 18,'female',231456,'Volleyball')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 3', 19,'male',452786,'Swimming')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 4', 20,'female',123584,'Swimming')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 5', 17,'male',235478,'Reading')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 6', 16,'female',562489,'Listening music')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 7', 15,'male',123045,'Basketball')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 8', 14,'female',123654,'Tennis')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 9', 13,'male',120489,'Hocky')")
    c.execute("INSERT INTO stuabout VALUES ('Stu 10', 18,'female',032457,'Cycling')")
    conn.commit()
    print("Data inserted student")

except pyodbc.Error as e:
    print("Error",e)

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=c:\Users\DELL\Documents\student.accdb;'
    conn = pyodbc.connect(con_string)
    a = conn.cursor()
    a.execute("CREATE TABLE studentdetail (number integer, stuname text, studentid text)")
    a.execute("INSERT INTO studentdetail VALUES (1, 'Jame','log121')")
    a.execute("INSERT INTO studentdetail VALUES (2, 'Helmen','log122')")
    a.execute("INSERT INTO studentdetail VALUES (3, 'Kris','log123')")
    a.execute("INSERT INTO studentdetail VALUES (4, 'Leo','log124')")
    a.execute("INSERT INTO studentdetail VALUES (5,'Hella','log125')")
    a.execute("INSERT INTO studentdetail VALUES (6, 'Jack','log126')")
    a.execute("INSERT INTO studentdetail VALUES (7,'Jasmine','log127')")
    a.execute("INSERT INTO studentdetail VALUES (8,'Octer','log128' )")
    a.execute("INSERT INTO studentdetail VALUES (9,'Jelly','log128')")
    a.execute("INSERT INTO studentdetail VALUES (10,'Lime','log130')")
    conn.commit()
    print("Data inserted into studentdetail")

except pyodbc.Error as e:
    print("Error in insert",e)

