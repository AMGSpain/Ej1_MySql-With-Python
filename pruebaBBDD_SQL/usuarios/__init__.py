import mysql.connector

def conectar():

    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "master_python",
        #port = 3306
    )
    """
    -Para conocer si ha funcionado la base de datos:
    print(database)
    """


    cursor = database.cursor(buffered=True)
    
    return[database, cursor]