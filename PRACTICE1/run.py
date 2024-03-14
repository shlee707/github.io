from flask import Flask
from view import main

app = Flask(__name__, static_url_path='/static')

app.register_blueprint(main.main_bp)
app.secret_key = 'seunghee'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8080',debug=True)