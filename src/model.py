from pymongo import MongoClient
from bson import ObjectId
import joblib
import pandas
from pathlib import Path
from knn.model_knn import ModelKNN

class Model:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.data_base = self.client['volley_classifier']
        self.usuarios = self.data_base.get_collection('usuarios')

        caminho_modelo = Path('knn/modelo_knn.pkl')
        
        if not caminho_modelo.exists():
            self.model_knn = ModelKNN()
            self.model_knn.treinar_modelo()
            
        self.modelo_knn = joblib.load('knn/modelo_knn.pkl')


        

    def classificar_posicao(self, peso, altura, flexibilidade, arremesso, s_horizontal, s_vertical):

        posicao = ['ATACANTE', 'LEVANTADOR', 'LIBERO']

        dados_usuario = pandas.DataFrame([
            {'peso': peso,
             'altura': altura,
             'flexibilidade': flexibilidade,
             'arremesso': arremesso,
             's_horizontal': s_horizontal,
             's_vertical': s_vertical}
        ])

        predicao = self.modelo_knn.predict(dados_usuario)

        return posicao[predicao[0]]

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
    
    def deletar_usuario(self, usuario_id):
        self.usuarios.delete_one({'_id': ObjectId(usuario_id)})

