from pymongo import MongoClient
from bson import ObjectId

class Model:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.data_base = self.client['volley_classifier']
        self.usuarios = self.data_base.get_collection('usuarios')


    def registrar_usuario(self, nome, peso, altura, flexibilidade, arremesso, s_horizontal, s_vertical, posicao):
        self.usuarios.insert_one({"nome": nome,
                                  "peso": peso,
                                  "altura": altura,
                                  "flexibilidade": flexibilidade,
                                  "arremesso": arremesso,
                                  "s_horizontal": s_horizontal,
                                  "s_vertical": s_vertical,
                                  "posicao": posicao
                                  })
    
    def listar_usuarios(self):
        return self.usuarios.find()
    
    def get_usuario(self, usuario_id):
        return self.usuarios.find_one({'_id': ObjectId(usuario_id)})

