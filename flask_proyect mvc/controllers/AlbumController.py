from flask import Blueprint,render_template,request,redirect,url_for,flash
from models.AlbumModel import * 

albumsBP = Blueprint('albums', __name__)

#ruta inicio 
@albumsBP.route('/')
def home():
     try:
         consultaTodo = getall()
         cursor=mysql.connection.cursor()
         cursor.execute('SELECT * FROM tb_albums WHERE status = TRUE')
         consultaTodo= cursor.fetchall()
         return render_template('formulario.html', errores={},albums=consultaTodo)
     
     except Exception as e:
          print('error al consultar todo: ' +e)
          return render_template('formulario.html', errores={},albums=[])

     
#ruta guardar
@albumsBP.route('/guardar', methods = ['POST'])
def guardar():
     errores={}
     vtitulo = request.form.get('txt_titulo','').strip()
     vartista = request.form.get('txt_artista','').strip()
     vanio =request.form.get('txt_anio','').strip()

     if not vtitulo:
        errores['txt_titulo']='El nombre del album es Obligatorio'
     if not vartista:
        errores['txt_artista']='El nombre del Artista es Obligatorio'
     if not vanio:
        errores['txt_anio']='El año es Obligatorio'
     elif not vanio.isdigit() or int(vanio) < 1800 or int(vanio) > 2077:
         errores['txt_anio']='Ingresa un año valido'
         
     if not errores:
        if InsertarAlbum(vtitulo,vartista,vanio):
             flash('Algo falló al guardar el álbum.')
             return redirect(url_for('albums.home'))
        else:
             flash('Álbum guardado en la base de datos.')
             return redirect(url_for('albums.home'))
     
     return render_template('formulario.html',errores= errores)
 

#editar
@albumsBP.route('/editar/<int:id>')
def editar_album(id):
    try:
        consultais = getByid(id)
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_albums WHERE id = %s', (id,))
        album = cursor.fetchone()
        cursor.close()

        if album:
            return render_template('formUpdate.html', album=album, errores={})
        else:
            flash('Álbum no encontrado')
            return redirect(url_for('albums.home'))
    except Exception as e:
        flash(f'Error al cargar álbum: {str(e)}')
        return redirect(url_for('albums.home'))


#detalles
@albumsBP.route('/detalle/<int:id>')
def detalle(id):
     try:
          getByid (id)
          cursor=mysql.connection.cursor()
          cursor.execute('SELECT * FROM tb_albums WHERE id=%s',(id,))
          consultaid= cursor.fetchone()
          return render_template('consulta.html' ,album=consultaid)
     
     except Exception as e:
          print('error al consultar por ID: ' +e)
          return redirect(url_for('albums.home'))
     cursor.close()



#eliminar
@albumsBP.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def elimina(id):
    if request.method == 'POST':
        try:
            softDelete (id)
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE tb_albums SET status = FALSE WHERE id = %s', (id,))
            mysql.connection.commit()
            cursor.close()
            flash('Álbum desactivado correctamente')
        except Exception as e:
            mysql.connection.rollback()
            flash('Error al desactivar el álbum: ' + str(e))
        return redirect(url_for('albums.home')) 

    else:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tb_albums WHERE id = %s", (id,))
        album = cursor.fetchone()
        cursor.close()
        if album:
            return render_template('eliminar.html', album=album)
        else:
            flash('Álbum no encontrado')
            return redirect(url_for('albums.home'))  
        

        
#update
@albumsBP.route('/actuali/<int:id>', methods=['POST'])
def actuali(id):
    errores = {}

    vtitulo = request.form.get('txt_titulo', '').strip()
    vartista = request.form.get('txt_artista', '').strip()
    vanio = request.form.get('txt_anio', '').strip()

    if not vtitulo:
        errores['txt_titulo'] = 'El título es obligatorio'
    if not vartista:
        errores['txt_artista'] = 'El artista es obligatorio'
    if not vanio:
        errores['txt_anio'] = 'El año es obligatorio'
    elif not vanio.isdigit() or int(vanio) < 1800 or int(vanio) > 2077:
        errores['txt_anio'] = 'Ingresa un año válido'

    if errores:
        album = (id, vtitulo, vartista, vanio)
        return render_template('formUpdate.html', album=album, errores=errores)

    try: 
        UpdateAlbum(vtitulo, vartista, vanio, id)
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE tb_albums
            SET titulo = %s, artista = %s, anio = %s
            WHERE id = %s
        """, (vtitulo, vartista, vanio, id))
        mysql.connection.commit()
        cursor.close()

        flash('Álbum actualizado correctamente')
        return redirect(url_for('albums.detalle', id=id))

    except Exception as e:
        mysql.connection.rollback()
        flash('Error al actualizar álbum: ' + str(e))
        return render_template('forUpdate.html',errores= errores)


@albumsBP. route('/confirmaDel/<int:id>')
def confirma (id):
    try:
        consultald= getByid (id)
        return render_template( 'confirmbel.html',album=consultald)
    except Exception as e:
        print('Error al consultar por-id: '+str(e))
        return redirect (url_for( 'albums.home'))