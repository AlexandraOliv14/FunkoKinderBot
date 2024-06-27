import mysql.connector as mariadb
from mysql.connector import errorcode
from config import HOST, DATABASE, PASSWORD, PUERTO, USER


def connection():
    try:
        mariadb_connection = mariadb.connect(
            host=HOST, 
            port=PUERTO,
            user=USER, 
            password=PASSWORD, 
            database=DATABASE
            )
    except mariadb.Error as err:
        handlerErrorConnection(err)
        closeConnection(mariadb_connection)

    return mariadb_connection


def closeConnection(mariadb_connection):
    mariadb_connection.close()


def handlerErrorConnection(err):
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

def getCall(query, valor):
    mariadb_connection = connection()
    try:
        cursor = mariadb_connection.cursor()
        
        cursor.execute(query, valor)
        
        myresult = cursor.fetchall()
        closeConnection(mariadb_connection)
        return myresult

    except mariadb.Error as e:
        print(f"Error: {e}")
        closeConnection(mariadb_connection)

def getUniqueCall(query):
    mariadb_connection = connection()
    try:
        cursor = mariadb_connection.cursor()
        
        cursor.execute(query)
        
        myresult = cursor.fetchall()
        closeConnection(mariadb_connection)
        return myresult

    except mariadb.Error as e:
        print(f"Error: {e}")
        closeConnection(mariadb_connection)

