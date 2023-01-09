# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:30:06 2022

@author: user
"""

import pymysql

def connect_with_datbase():
    try:
        connect = pymysql.connect(
                                host="localhost", 
                                user="root", 
                                password="", 
                                database="emood"
                                )

        cur = connect.cursor()
        cur.execute("select * from user")

        # Fetch all the data
        row = cur.fetchall()
        print(row)
        

        # Close the connection
        connect.close()
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # Calling the function
    connect_with_datbase()