from knn.elo import Elo
import joblib

class EloSalvar(Elo):
    def process_request(self, model):

        joblib.dump(model.modelo_knn, 'knn/modelo_knn.pkl')

        return model