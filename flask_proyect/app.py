
from flask import Flask 

app= Flask (__name__)
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
    