class Elo:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next

    def process_request(self, model):
        return model

    def run(self, model):
        model = self.process_request(model)
        if self.next:
            self.next.run(model)