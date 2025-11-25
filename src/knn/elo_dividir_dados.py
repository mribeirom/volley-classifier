from knn.elo import Elo
from sklearn.model_selection import train_test_split

class EloDividirDados(Elo):
    def process_request(self, model):

        features = model.dataset.iloc[:, :-1]
        targets = model.dataset.iloc[:, -1]
        
        model.features_train, model.features_test, model.targets_train, model.targets_test = train_test_split(features, targets, test_size=0.2, random_state=42)

        return model