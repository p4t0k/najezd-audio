# this is our custom mysqldb driver
#

from flask_mysqldb import MySQL
from flask import current_app as app

class MySQLDriver:
    def __init__(self, conf, err):
        #print('[*] inside of constructor')
        self.conf = conf
        self.e = err

    def Connect(self):
        #print('[*] inside of Connect method')
        app.config['MYSQL_USER'] = self.conf['username']
        app.config['MYSQL_PASSWORD'] = self.conf['password']
        app.config['MYSQL_DB'] =  self.conf['database']
        app.config['MYSQL_HOST'] = self.conf['host']
        self.conn = MySQL(app)

    def Run(self, query):
        #print('[*] inside of Run method')
        try:
            cur = self.conn.connection.cursor()
            retval = cur.execute(query)
            output = cur.fetchall()
            return (retval, output)
        except:
            self.e.throwMsg("problem while running DB Query: %s" % str(query), 2)

#    def __exit__(self ,type, value, traceback):
#        if self.mysql:
#            self.mysql.close()
