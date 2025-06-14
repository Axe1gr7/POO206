from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "1310041310004"
app.config['MYSQL_DB'] = "DB_flask"

mysql = MySQL(app)

#ruta para checar la conexion a la bd 
@app.route('/db_check')
def db_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.excute('select 1')
        return jsonify({'status':'ok','message':'conexion exitosa'}),200        
    except MySQLdb.MySQLError as e: jsonify({'status':'error','message':str(e)}),500
     
 


#ruta simple 
@app.route('/')
def home():
    return 'Hola mundo FLASK'

#ruta con parametros 
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola,'+nombre+'¡¡¡'

#RUTA TRY-CATCH PARA ERRORES
@app.errorhandler(404)
def PagNoE(e): 
    return 'CUIDADO: ERROR DE CAPA 8 ¡¡¡'

#ruta doble 
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'mismo servidor'

#ruta post
@app.route('/formulario' ,methods=['POST'])
def formulario():
    return 'soy un formulario'


if __name__ == '__main__':
    app.run(port=3000,debug=True)
    