import pandas
from knn.elo import Elo

class EloCarregarDados(Elo):
    def process_request(self, model):

        model.dataset = pandas.read_csv('knn/dataset.csv', decimal=',', sep=';')

        return model