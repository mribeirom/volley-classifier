from knn.elo import Elo
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class EloTeste(Elo):
    def process_request(self, model):

        targets_predicted = model.modelo_knn.predict(model.features_test)
        
        accuracy = accuracy_score(model.targets_test, targets_predicted)
        print(f'\tAcurácia: {accuracy:.2%}')
        
        report = classification_report(model.targets_test, targets_predicted)
        print('\n\tRelatório de classificação:')
        print(report)
        
        matrix = confusion_matrix(model.targets_test, targets_predicted)
        print('\tMatriz de confusão:')
        print(matrix)
        
        return model