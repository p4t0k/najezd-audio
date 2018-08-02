#!/usr/bin/env python3

from flask import Flask, request, render_template
import configparser, os, sys, strings

# configuration parsing
cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), "najezd-audio.conf"))
cfgvar = {}
# TODO: load configuration in loop
cfgvar['audio-dir'] = cfg.get('global', 'audio-dir')
cfgvar['driver'] = cfg.get('database', 'driver')
cfgvar['host'] = cfg.get('database', 'host')
cfgvar['username'] = cfg.get('database', 'username')
cfgvar['password'] = cfg.get('database', 'password')
cfgvar['database'] = cfg.get('database', 'database')

# internal logic functions and classes

class ErrorHandling:
    def __init__(self):
        # msg severity: 0 = NOTICE, 1 = WARNING, 2 = ERROR, 3 = FATAL ERROR
        self.severity = ('NOTICE', 'WARNING', 'ERROR', 'FATAL ERROR')

    def throwMsg(self, msg, level, exit_code=0):
        msg = self.severity[level] + ': ' + msg
        print(msg)
        # it will exit if it's error or fatal error and non-zero exit code is defined
        if level in [2,3] and exit_code != 0:
            sys.exit(exit_code)

def genTickets(num=1):
    chars = string.ascii_letters + string.digits
    pw_arr = []
    for i in range(num):
        password = "".join(choice(chars) for x in range(10))
        pw_arr += [password]
    return pw_arr

#bcrypt.hashpw('test'.encode('utf-8'), bcrypt.gensalt( 12 ))
#bcrypt.checkpw('tcest'.encode('utf-8'), b'[b(2$wFuhUv.b0cULfhGNBzHn6.cCWXPtvLjimqV59sUksc../K25Aqf4S'))]

# Flask logic

app = Flask(__name__)

## instantiation of our classes

# notifications
e = ErrorHandling()

# database drivers
if cfgvar['driver'] == 'mysql':
    sys.path.insert(0, os.path.join('drivers', 'mysql_flask_driver.py'))
    import MySQLDriver from mysql_flask_driver as DBDriver

else:
    e.throwMsg("Driver %s not found!" % cfgvar['driver'], 3, 129)

db = DBDriver()
db.Connect()

@app.route('/get-album/')
@app.route('/get-album/<code>')
def get_album(code=None):
    ticketid = db.Run('''SELECT id FROM tickets WHERE ticket = "oVnKoO4wwc"''')
    return render_template('najezd-audio.html', code=code)

# run app
if __name__ == "__main__":
    app.run()
