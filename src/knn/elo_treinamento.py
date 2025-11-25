from knn.elo import Elo

class EloTreinamento(Elo):
    def process_request(self, model):

        model.modelo_knn.fit(model.features_train, model.targets_train)

        return model