from pymysql import *   
import streamlit as st    

def GetDBdata():
    # create a connection to DB
    conn = connect(host='localhost',
                   port=3306,user='root',
                   password='',
                   database='ksu_database',
                   charset='utf8'
                   )
    # create cursor object
    cursor_data = conn.cursor()
    # send an SQL
    count = cursor_data.execute('SELECT * FROM student')
    
    # the rows selected from the DB table
    print("The number of rows is: %d " % count)

    # close the used objects in Memory
    cursor_data.close()
    conn.close()
    # require all of cursor's data
    result = cursor_data.fetchall()  
    return(result)    

###  
st.success("All of student data from ksu_database.student table is below:\n") 
st.write(GetDBdata())

