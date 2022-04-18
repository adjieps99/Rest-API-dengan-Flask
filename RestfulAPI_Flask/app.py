# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

#identitas
identitas = {} #global variabel

#resource
class ContohResource(Resource):
    def get(self):
        #response = {"msg": "Hallo Adjie ini API pertamamu"}
        #return response
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg":"Data berhasil dimasukan"}
        return response

api.add_resource(ContohResource, "/api", methods = ["GET", "POST"])

if __name__=="__main__":
    app.run(debug=True)