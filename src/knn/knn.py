import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

class KNN:
    def __init__(self):
        self.dataset = None
        self.modelo_knn = KNeighborsClassifier(n_neighbors=3)


        self.encoder_posicao = LabelEncoder()

        self.features_train = None
        self.features_test = None

        self.targets_train = None
        self.targets_test = None


    def carrega_dataset(self):
        # carrega os dados para o treinamento de uma planilha
        self.dataset = pandas.read_csv('dataset.csv', decimal=',', sep=';')

    def converter_numeros(self):
        # os atributos que são palavras são convertidos em numeros
        self.dataset['posicao'] = self.encoder_posicao.fit_transform(self.dataset['posicao'])

    def dividir_dataset(self):
        # separa os dados de entrada e saida
        features = self.dataset.iloc[:, :-1]
        targets = self.dataset.iloc[:, -1]

        # divide os dados de treinamento entre 80% de treino e 20% de teste
        self.features_train, self.features_test, self.targets_train, self.targets_test = train_test_split(features, targets, test_size=0.2, random_state=42)

    def treinamento_modelo(self):
        # treina o modelo
        self.modelo_knn.fit(self.features_train, self.targets_train)
    
    def teste_modelo(self):

        # usa os dados de teste para fazer previsões com o modelo
        targets_predicted = self.modelo_knn.predict(self.features_test)

        # calcula a acuraria do modelo (porcentagem de acerto)
        accuracy = accuracy_score(self.targets_test, targets_predicted)
        print("Acurácia do modelo KNN:", accuracy)


        report = classification_report(self.targets_test, targets_predicted)
        print("Relatório de classificação:")
        print(report)
    
        matrix = confusion_matrix(self.targets_test, targets_predicted)
        print("Matriz de confusão:")
        print(matrix)

    def salvar_modelo(self):
        # salva o modelo
        joblib.dump(self.modelo_knn, 'modelo_knn.pkl')



    def treinar_modelo(self):
        self.carrega_dataset()
        self.converter_numeros()
        self.dividir_dataset()
        self.treinamento_modelo()

knn = KNN()

knn.treinar_modelo()
knn.teste_modelo()
knn.salvar_modelo()
