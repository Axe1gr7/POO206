from flask import Flask,jsonify,render_template,request,flash,redirect,url_for
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="131004131004"
app.config['MYSQL_DB']="DB_flask"
app.secret_key='mysecretkey'

mysql= MySQL(app)

#ruta para probar conexion a mysql
@app.route('/DBCheck')
def DB_check():
     try:
          cursor= mysql.connection.cursor()
          cursor.execute('select 1')
          return jsonify( {'status':'ok','message':'Conectado con exito'} ),200     
     except MySQLdb.MySQLError as e:return jsonify( {'status':'error','message':str(e)} ),500 
     
     
#RUTA TRY-CATCH PARA ERRORES
@app.errorhandler(404)
def PagNoE(e): 
    return 'CUIDADO: ERROR DE CAPA 8 ¡¡¡'


@app.route('/formulario')
def home():
    return render_template('formulario.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/guardar', methods = ['POST'])
def guardar():
#listas  o diccionario 
#lista de errores 
     errores={}
#obtener los datos del formulario
     vtitulo = request.form.get('txt_titulo','').strip()
     vartista = request.form.get('txt_artista','').strip()
     vanio =request.form.get('txt_anio','').strip()
#lista de errores al estar vacios
     if not vtitulo:
        errores['txt_titulo']='El nombre del album Oblogatorio'
     if not vtitulo:
        errores['txt_artista']='El nombre del Artista Oblogatorio'
     if not vtitulo:
        errores['txt_anio']='El año es Oblogatorio'
     elif not vanio.isdigit() or int(vanio) < 1800 or int(vanio) > 2077:
         errores['txt_anio']='Ingresa un año valido'
         
     if not errores:
        try:
             cursor=mysql.connection.cursor()
             cursor.execute('insert into new_table(titulo,artista,anio) values (%s,%s,%s)',(vtitulo,vartista,vanio))
             mysql.connection.commit()
             flash('album guardado en la bd')
             return redirect(url_for('home'))
    
        except Exception as e:
                mysql.connection.rollback()
                flash('algo fallo' + str(e)) 
                return redirect(url_for('home'))
    
        finally:
            cursor.close()
    #retorna el formalirio al validar los errores 
     return render_template('formulario.html',errores= errores)
if __name__ == '__main__':
    app.run(port=3000,debug=True)
     
