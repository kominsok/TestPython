import sqlite3
def Create_Table():
    db=sqlite3.connect('mysql.db')
    cursor=db.cursor()
    cursor.execute("create table test_table(code,name)")
    cursor.close()
    db.close()

def Insert_M():
    connector=sqlite3.connect('mysql.db')
    sql="insert into test_table values('1','java')"
    connector.execute(sql)
    sql="insert into test_table values('2','python')"
    connector.execute(sql)
    sql="insert into test_table values('3','c++')"
    connector.execute(sql)
    connector.commit()
    connector.close()

def Select_M():
    connector=sqlite3.connect("mysql.db")
    cursor=connector.cursor()
    cursor.execute("select * from test_table")
    result=cursor.fetchall()

    for row in result:
        print("code:"+row[0]+" name:"+row[1])
    cursor.close()
    connector.close()
    
if __name__=="__main__":
    Create_Table()
    Insert_M()
    Select_M()
