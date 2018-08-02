# this is our custom mysqldb driver
#

from flask_mysqldb import MySQL
from flask import current_app as app

class MySQLDriver:
    def __init__(self, conf, err):
        self.conf = conf
        self.e = err

    def Connect(self):
        app.config['MYSQL_USER'] = self.conf['username']
        app.config['MYSQL_PASSWORD'] = self.conf['password']
        app.config['MYSQL_DB'] =  self.conf['database']
        app.config['MYSQL_HOST'] = self.conf['host']
        mysql = MySQL()
        mysql.init_app(app)
        Cursor = mysql.connection.cursor()
        return Cursor

    def Run(self, query, cur):
        # next two lines are temporarily here
        exec = cur.execute(query)
        return exec.fetchall()
#        try:
#            exec = self.Cursor.execute(query)
#            return exec.fetchall()
#        except:
#            self.e.throwMsg("problem while running DB Query: %s" % str(query), 2)

    def __exit__(self ,type, value, traceback):
        if self.mysql:
            self.mysql.close()
