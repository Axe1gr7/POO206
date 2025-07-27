from flask import Flask
from flask_mysqldb import MySQL

from config import config

mysql = MySQL() 


def create_app():
    #configuracion para bd
    app=Flask(__name__)
    app.config.from_object(config)
    mysql.init_app(app)
    #configuracion para controlador 
    from controllers.AlbumController import albumsBP
    from controllers.controller import internoBP
    app.register_blueprint(albumsBP)
    return app 





if __name__ == '__main__':
    app= create_app()
    app.run(port=3000,debug=True)
     
