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


@app.route('/')
def home():
     try:
          cursor=mysql.connection.cursor()
          cursor.execute('SELECT * FROM tb_albums')
          consultaTodo= cursor.fetchall()
          return render_template('formulario.html', errores={},albums=consultaTodo)
     
     except Exception as e:
          print('error al consultar todo: ' +e)
          return render_template('formulario.html', errores={},albums=[])
     
     finally: 
          cursor.close()
          

@app.route('/detalle/<int:id>')
def detalle(id):
     try:
          cursor=mysql.connection.cursor()
          cursor.execute('SELECT * FROM tb_albums WHERE id=%s',(id,))
          consultaid= cursor.fetchone()
          return render_template('consulta.html' ,album=consultaid)
     
     except Exception as e:
          print('error al consultar por ID: ' +e)
          return redirect(url_for('home'))
     
     finally: 
          cursor.close()

@app.route('/editar/<int:id>')
def editar_album(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_albums WHERE id = %s', (id,))
        album = cursor.fetchone()
        cursor.close()

        if album:
            return render_template('formUpdate.html', album=album, errores={})
        else:
            flash('Álbum no encontrado')
            return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error al cargar álbum: {str(e)}')
        return redirect(url_for('home'))

          


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
             cursor.execute('insert into tb_albums(titulo,artista,anio) values (%s,%s,%s)',(vtitulo,vartista,vanio))
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


#########

@app.route('/actuali/<int:id>', methods=['POST'])
def actuali(id):
    errores = {}

    vtitulo = request.form.get('txt_titulo', '').strip()
    vartista = request.form.get('txt_artista', '').strip()
    vanio = request.form.get('txt_anio', '').strip()

    # Validaciones
    if not vtitulo:
        errores['txt_titulo'] = 'El título es obligatorio'
    if not vartista:
        errores['txt_artista'] = 'El artista es obligatorio'
    if not vanio:
        errores['txt_anio'] = 'El año es obligatorio'
    elif not vanio.isdigit() or int(vanio) < 1800 or int(vanio) > 2077:
        errores['txt_anio'] = 'Ingresa un año válido'

    if errores:
        # Volver a mostrar formulario con errores y valores ingresados
        album = (id, vtitulo, vartista, vanio)
        return render_template('formUpdate.html', album=album, errores=errores)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE tb_albums
            SET titulo = %s, artista = %s, anio = %s
            WHERE id = %s
        """, (vtitulo, vartista, vanio, id))
        mysql.connection.commit()
        cursor.close()

        flash('Álbum actualizado correctamente')
        return redirect(url_for('detalle', id=id))

    except Exception as e:
        mysql.connection.rollback()
        flash('Error al actualizar álbum: ' + str(e))
         #retorna el formalirio al validar los errores 
        return render_template('forUpdate.html',errores= errores)



if __name__ == '__main__':
    app.run(port=3000,debug=True)
     
