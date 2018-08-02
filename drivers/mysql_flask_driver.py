# this is our custom mysqldb driver
#

class MySQLDriver:
    def __init__(self, app, conf):
        self.app = app
        self.conf = conf

    def Connect(self):
        self.app.config['MYSQL_DATABASE_USER'] = self.conf['username']
        self.app.config['MYSQL_DATABASE_PASSWORD'] = self.conf['password']
        self.app.config['MYSQL_DATABASE_DB'] =  self.conf['database']
        self.app.config['MYSQL_DATABASE_HOST'] = self.conf['host']
        mysql = MySQL(self.app)
        self.Cursor = mysql.connection.cursor()
    def Run(self, query):
        try:
            exec = self.Cursor.execute(query)
            return exec.fetchall()
        except:
            e.throwMsg("Error while running DB Query: %s" % str(query), 2)
