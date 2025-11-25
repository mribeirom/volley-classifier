from knn.elo import Elo

class EloConverterNumeros(Elo):
    def process_request(self, model):

        model.dataset['posicao'] = model.encoder_posicao.fit_transform(model.dataset['posicao'])

        return model