from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'dinskid'
app.config['MYSQL_DATABASE_PASSWORD'] = '123@Ugofree'
app.config['MYSQL_DATABASE_DB'] = 'lbp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
con = mysql.connect()
cursor = con.cursor()
