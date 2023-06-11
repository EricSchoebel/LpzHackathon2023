from flask import Flask
from flask_cors import CORS
from api_controller import api_controller

app = Flask(__name__) #initialize application
app.config.from_object(__name__)

#Important against Cross-Origin-Error:

#like that everything is allowed (insecure)
#CORS(app, resources={r"/*":{'origins': "*"}})

#like that only from localhost:8080 it is allowed
CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers": "Acces-Control-Allow-Origin"}})

app.register_blueprint(api_controller, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

