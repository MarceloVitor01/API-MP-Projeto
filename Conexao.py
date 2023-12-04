import mysql.connector as connector

class ConexaoBD:
    host = 'banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com'
    username = 'doadmin'
    password = 'AVNS_erI8p2wSSm0gckO83UU'
    port = '25060'
    database = 'defaultdb'

    def __init__(self, host, username, password, port, database):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database

    def conecta_bd(self):
        self.conn = connector(
                host = self.host,
                username = self.username,
                password = self.password,
                port = self.port,
                database = self.database
        )