from keys import *
import random
import smtplib

from models.entities.Code import Code

class ModelCode():
    @classmethod
    def clearTable(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("TRUNCATE TABLE code")
            connection.commit()
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def addCode(self,connection):
        code = random.randint(1000,10000)
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO code (code_number) VALUES (%s)", (code, ))
            connection.commit()
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def checkCode(self, connection, code):
        try:
            cursor = connection.cursor()
            sql = """SELECT code_number FROM code 
                    WHERE code_number='{}'""".format(code.number)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                code_number = Code(row[0])
                return code_number
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def getCode(self, connection):
        try:
            cursor = connection.cursor()
            sql = "SELECT * FROM code"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                code_number = row[0]
                return code_number
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
