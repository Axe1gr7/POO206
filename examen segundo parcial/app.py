from flask import Flask,jsonify,render_template,request,flash,redirect,url_for
from flask_mysqldb import MySQL
import MySQLdb

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="131004131004"
app.config['MYSQL_DB']="contactos"
app.secret_key='mysecretkey'

mysql= MySQL(app)


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
          cursor.execute('SELECT * FROM contac WHERE status = TRUE')
          consultaTodo= cursor.fetchall()
          return render_template('ex.html', errores={},contactos=consultaTodo)
     
     except Exception as e:
          print('error al consultar todo: ' +e)
          return render_template('ex.html', errores={},contactos=[])
     
     finally: 
          cursor.close()
        
        
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/detall/<int:id>')
def detalle(id):
     try:
          cursor=mysql.connection.cursor()
          cursor.execute('SELECT * FROM contact WHERE id=%s',(id,))
          consultid= cursor.fetchone()
          return render_template('consulta.html' ,contacto=consultid)
     
     except Exception as e:
          print('error al consultar por ID: ' +e)
          return redirect(url_for('home'))
     
     finally: 
          cursor.close()

@app.route('/editar/<int:id>')
def editar_album(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM contac WHERE id = %s', (id,))
        contactos = cursor.fetchone()
        cursor.close()

        if contactos:
            return render_template('ex_edit.html', contactos=contactos, errores={})
        else:
            flash( 'conatcto no encontrado')
            return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error al cargar contacto: {str(e)}')
        return redirect(url_for('home'))

          





@app.route('/guardar', methods = ['POST'])
def guardar():

     errores={}
     vnombre = request.form.get('nombre','').strip()
     vcorreo = request.form.get('correo','').strip()
     vtelefono=request.form.get('telefono','').strip()
     vedad=request.form.get('edad','').strip()

     if not vnombre:
        errores['nombre']='El nombre del contacto debe ser Oblogatorio'

     elif not vcorreo:
         errores['correo']='correo obligatorio'

     elif not vtelefono.isdigit():
         errores['telefono']='telefono no valido'
         
     elif not vedad.isdigit() or int(vedad) < 1 or int(vedad) > 105:
         errores['edad']='Ingresa una edad valida'
          
     if not errores:
        try:
             cursor=mysql.connection.cursor()
             cursor.execute('insert into contac(nombre,correo,telefono,edad) values (%s,%s,%s,%s)',(vnombre,vcorreo,vtelefono,vedad))
             mysql.connection.commit()
             flash('contacto guardado en la bd')
             return redirect(url_for('home'))
    
        except Exception as e:
                mysql.connection.rollback()
                flash('algo fallo' + str(e)) 
                return redirect(url_for('home'))
    
        finally:
            cursor.close()
     return render_template('ex.html',errores= errores)


#########

@app.route('/actuali/<int:id>', methods=['POST'])
def actuali(id):
    errores = {}
    vnombre = request.form.get('nombre','').strip()
    vcorreo = request.form.get('correo','').strip()
    vtelefono=request.form.get('telefono','').strip()
    vedad=request.form.get('edad','').strip()

    if not vnombre:
        errores['nombre']='El nombre del contacto debe ser Oblogatorio'

    elif not vcorreo:
         errores['correo']='correo obligatorio'

    elif not vtelefono.isdigit() or int(vtelefono) < 10:
         errores['telefono']='telefono no valido'
         
    elif not vedad.isdigit() or int(vedad) < 1 or int(vedad) > 105:
         errores['edad']='Ingresa una edad valida'
          
    if errores:
        
        contacto = (id,vnombre,vcorreo,vtelefono,vedad )
        return render_template('ex_edit.html', contacto=contacto, errores=errores)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE contactos
            SET nombre = %s, correo = %s, telefono = %s, edad = %s
            WHERE id = %s
        """, (vnombre,vcorreo,vtelefono,vedad))
        mysql.connection.commit()
        cursor.close()

        flash('contacto actualizado correctamente')
        return redirect(url_for('detall', id=id))

    except Exception as e:
        mysql.connection.rollback()
        flash('Error al actualizar contacto: ' + str(e))
        return render_template('ex_edit.html',errores= errores)


@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def elimina(id):
    if request.method == 'POST':
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE contac SET status = FALSE WHERE id = %s', (id,))
            mysql.connection.commit()
            cursor.close()
            flash('contacto desactivado correctamente')
        except Exception as e:
            mysql.connection.rollback()
            flash('Error al desactivar el contacto: ' + str(e))
        return redirect(url_for('home'))  

    else:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM contac WHERE id = %s", (id,))
        contacto = cursor.fetchone()
        cursor.close()
        if contacto:
            return render_template('ex_el.html', contacto=contacto)
        else:
            flash('contacto no encontrado')
            return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=3000,debug=True)
     
