from flask_app import app 

#importar controlador

from flask_app.controllers import productos_controller, users_controller


















if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)