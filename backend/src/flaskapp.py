from flask import Flask
from api_controller import api_controller


app = Flask(__name__, template_folder='../templates') #initialize application
app.register_blueprint(api_controller, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

