from ap import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "1235"
app.config['MYSQL_DATABASE_DB'] = "usa_house"
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1:3307'

mysql.init_app(app)

