# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:15:31 2022

@author: Mario
"""


import pyodbc as conn
from decouple import config
import mysql.connector as c


def get_points(username, password, hostname, database, port):
    try:
        db = c.connect(user="{0}".format(username), password="{0}".format(password),
                       host="{0}".format(hostname), database="{0}".format(database), port="{0}".format(port))
        return db
    except Exception as ex:
        return "Error to connect to MySQL: {0}".format(ex)


def get_connectionMySQL():
    try:
        return get_points(
            config('USER_NAME'),
            config('PASSWORD'),
            config('HOSTNAME'),
            config('DATABASE'),
            config('PORT')
        )
    except Exception as ex:
        raise ex


def connect_sqlserver(hostname, dbname, username, password):
    try:
        conexion = conn.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                hostname + ';DATABASE=' + dbname + ';UID=' + username + ';PWD=' + password, autocommit=True)
        print("Database connect successfully to SQL Server")
        return conexion
    except Exception as e:
        # Atrapar error
        print("Error to connect to SQL Server: ", e)
        
def get_connection():
    try:
        return connect_sqlserver(
            config('HOST'),
            config('DB'),
            config('USER'),
            config('PASS')
        )
    except Exception as ex:
        raise ex