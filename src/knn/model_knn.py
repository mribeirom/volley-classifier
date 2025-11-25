
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

from knn.elo_carregar_dados import EloCarregarDados
from knn.elo_converter_numeros import EloConverterNumeros
from knn.elo_dividir_dados import EloDividirDados
from knn.elo_treinamento import EloTreinamento
from knn.elo_teste import EloTeste
from knn.elo_salvar import EloSalvar

class ModelKNN:
    def __init__(self):

        self.dataset = None
        self.modelo_knn = KNeighborsClassifier(n_neighbors=3)
        self.encoder_posicao = LabelEncoder()
        self.features_train = None
        self.features_test = None
        self.targets_train = None
        self.targets_test = None
        
        #Cria os elos
        self.elo_carregar = EloCarregarDados()
        self.elo_converter = EloConverterNumeros()
        self.elo_dividir = EloDividirDados()
        self.elo_treinar = EloTreinamento()
        self.elo_testar = EloTeste()
        self.elo_salvar = EloSalvar()
        
        #Monta a cadeia
        self.elo_carregar.set_next(self.elo_converter)
        self.elo_converter.set_next(self.elo_dividir)
        self.elo_dividir.set_next(self.elo_treinar)
        self.elo_treinar.set_next(self.elo_testar)
        self.elo_testar.set_next(self.elo_salvar)

    def treinar_modelo(self):

        return self.elo_carregar.run(self)
    
if __name__ == "__main__":
    model = ModelKNN()
    model.treinar_modelo()