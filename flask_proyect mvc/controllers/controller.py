from flask import Blueprint,jsonify
from app import mysql 
import MySQLdb

internoBP = Blueprint('albums', __name__)


#ruta para probar conexion a mysql
@internoBP.route('/DBCheck')
def DB_check():
     try:
          cursor= mysql.connection.cursor()
          cursor.execute('select 1')
          return jsonify( {'status':'ok','message':'Conectado con exito'} ),200     
     except MySQLdb.MySQLError as e:return jsonify( {'status':'error','message':str(e)} ),500 


     
#RUTA TRY-CATCH PARA ERRORES
@internoBP.errorhandler(404)
def PagNoE(e): 
    return 'CUIDADO: ERROR DE CAPA 8 ¡¡¡'