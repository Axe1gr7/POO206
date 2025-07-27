from app import mysql 

#metoso para obtener albums activos 
def getall():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_albums WHERE status = TRUE')
    consultaTodo= cursor.fetchall()
    cursor.close()
    return consultaTodo

#obtener album por id 
def getByid(id):
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_albums WHERE id=%s',(id,))
    consultaid= cursor.fetchone()
    cursor.close()
    return consultaid

#insertar 
def InsertarAlbum(vtitulo,vartista,vanio): 
    cursor=mysql.connection.cursor()
    cursor.execute('insert into tb_albums(titulo,artista,anio) values (%s,%s,%s)',(vtitulo,vartista,vanio))
    mysql.connection.commit() 
    cursor.close()
    
#update
def UpdateAlbum(vtitulo, vartista, vanio, id):
    cursor = mysql.connection.cursor()
    cursor.execute("""UPDATE tb_albums SET titulo = %s, artista = %s, anio = %s WHERE id = %s""", (vtitulo, vartista, vanio, id))
    mysql.connection.commit()
    cursor.close()
    
    
#eliminar
def softDelete(id):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE tb_albums SET status = FALSE WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()