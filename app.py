import werkzeug
from flask.scaffold import _endpoint_from_view_func
from werkzeug.utils import cached_property

import flask

flask.helpers._endpoint_from_view_func = _endpoint_from_view_func

werkzeug.cached_property = cached_property

from flask import Flask, make_response, jsonify, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api()
api.init_app(app)


@api.route('/test')
class test_get(Resource):
    def get(self):
        resp = make_response(jsonify({'mensagem': 'APPLICATION UP.'}), 200)
        return resp

user_fields = api.model('Usuario', {
    'id': fields.String,
    'nome': fields.String,
    'email': fields.String,
    'rua': fields.String,
    'bairro': fields.String,
    'cep': fields.String,
    'cidadeId': fields.String,
    'estadoId': fields.String,
    'sexoId': fields.String,
    'telefone': fields.String,
    'foto': fields.String,
})

@api.route('/usuario')
@api.doc(model='Usuario')
class create_user(Resource):
    def post(self):
        return {}

@api.route('/usuarios')
@api.doc(model='Usuario')
class get_all_users(Resource):
    def get(self):
        return {}

@api.route('/usuario/<iduser>')
@api.doc(params={'iduser': 'An User ID'})
class get_user_by_id(Resource):
    def get(self, iduser):
        return {}

@api.route('/usuario/<iduser>')
@api.doc(params={'iduser': 'An User ID'})
class update_user(Resource):
    def put(self, iduser):
        return {}

@api.route('/usuario/<iduser>')
@api.doc(params={'iduser': 'An User ID'})
class delete_user(Resource):
    def delete(self, iduser):
        return {}

user_auth = api.model('user_auth', {
    'nome': fields.String,
    'senha': fields.String,
})

@api.route('/autenticarUsuario')
class auth_user(Resource):
    @api.expect(user_auth)
    def post(self):
        return {}

@api.route('/deslogarUsuario')
class logout_user(Resource):
    def post(self):
        return {}

@api.route('/racas')
class get_all_breed(Resource):
    def get(self):
        return {}

@api.route('/raca/<idbreed>')
@api.doc(params={'idbreed': 'An Breed ID'})
class get_breed_by_id(Resource):
    def get(self, idbreed):
        return {}

@api.route('/racas/<sizeId>')
@api.doc(params={'sizeId': 'An size ID'})
class get_breed_by_size(Resource):
    def get(self, sizeId):
        return {}

@api.route('/portes')
class get_all_size(Resource):
    def get(self):
        return {}

@api.route('/cachorro')
class create_dog(Resource):
    def post(self):
        return {}

@api.route('/cachorro')
class update_dog(Resource):
    def put(self):
        return {}

@api.route('/cachorro/<iddog>')
@api.doc(params={'iddog': 'An dog ID'})
class delete_dog(Resource):
    def delete(self, iddog):
        return {}

@api.route('/cachorro/<iddog>')
@api.doc(params={'iddog': 'An dog ID'})
class get_dog_by_id(Resource):
    def get(self, iddog):
        return {}

@api.route('/usuarioCachorros/<iduser>')
@api.doc(params={'iduser': 'An user ID'})
class get_dogs_by_user(Resource):
    def get(self, iduser):
        return {}

@api.route('/cachorros')
class get_all_dogs(Resource):
    def get(self):
        return {}

@api.route('/informacoes')
class get_info(Resource):
    def get(self):
        return {}

@api.route('/fotoPerfil')
class upload_profile_photo(Resource):
    def post(self):
        return {}

@api.route('/fotoPerfil/<iduser>')
@api.doc(params={'iduser': 'An user ID'})
class get_profile_photo(Resource):
    def get(self, iduser):
        return {}

@api.route('/fotoPerfil/<iduser>')
@api.doc(params={'iduser': 'An user ID'})
class delete_profile_photo(Resource):
    def delete(self, iduser):
        return {}

@api.route('/fotoCachorro')
class upload_dog_photo(Resource):
    def post(self):
        return {}

@api.route('/fotoCachorro/<iddog>')
@api.doc(params={'iddog': 'An dog ID'})
class get_dog_photo(Resource):
    def get(self, iddog):
        return {}

@api.route('/fotoCachorro/<iddog>')
@api.doc(params={'iddog': 'An dog ID'})
class delete_dog_photo(Resource):
    def delete(self, iddog):
        return {}


#######################################################
# Execucao da Aplicacao
if __name__ == '__main__':
    app.run()
